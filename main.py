from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from cdbLexer import cdbLexer
from cdbListener import cdbListener
from cdbParser import cdbParser

output = ""
callbacks = ""
callback_counter = 0
err = None
sql_init = False


class SyntaxErr:
    def __init__(self, line, column, details):
        self.message = f"Syntax error at line {line}:{column} - {details}"
        self.line = line
        self.column = column


def transpile(input_stream):
    global output, callback_counter, err, callbacks, sql_init
    output = ''
    callbacks = ''
    sql_init = False
    callback_counter = 0
    lexer = cdbLexer(InputStream(input_stream))
    stream = CommonTokenStream(lexer)
    parser = cdbParser(stream)

    err = None

    class Errors(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            global err
            err = SyntaxErr(line, column, msg)
            print(err.message)

    error_listener = Errors()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.compilationUnit()

    headers = ""
    for header in input_stream.split('\n'):
        if header.startswith('#include'):
            headers += header + "\n"
    callbacks = ""

    def check_for_parent(ctx, t):
        if isinstance(ctx, t):
            return True
        else:
            if ctx.parentCtx is not None:
                return check_for_parent(ctx.parentCtx, t)
            return False

    banned_contexts = [
        cdbParser.SqlSelectStatementContext,
        cdbParser.SqlInsertStatementContext,
        cdbParser.SqlUpdateStatementContext,
        cdbParser.SqlDeleteStatementContext,
        cdbParser.SqlInitContext
    ]

    callback_counter = 0

    class Listener(cdbListener):
        def visitTerminal(self, node: cdbParser.SqlSelectStatementContext):
            global output
            for banned_context in banned_contexts:
                if check_for_parent(node, banned_context):
                    return
            if node.getChildCount() == 0:
                output += node.getText() + ' '

        def enterSqlSelectStatement(self, ctx: cdbParser.SqlSelectStatementContext):
            global output, callback_counter, callbacks
            try:
                fields = ctx.children[1].getText()
                table = ctx.children[3].getText()
                callback = ctx.children[5].getText()
                if 'int ' + callback not in input_stream:
                    callback = f"callback{callback_counter}"
                    callbacks += f"""
                                int callback{callback_counter}(void *NotUsed, int argc, char **argv, 
                                            char **azColName) {{
                            NotUsed = 0;
                            for (int i = 0; i < argc; i++) {{
                                printf("%s = %s\\n", azColName[i], argv[i] ? argv[i] : "NULL");
                            }}
                            printf("\\n");return 0;}}\n"""
                    callback_counter += 1
                line = ctx.getText()
                line.split('(')
                output += f"""
                                    sql = sqlite3_mprintf("SELECT {fields} FROM {table};");
                                    rc = sqlite3_exec(db, sql, {callback}, 0, &zErrMsg);
                                    """
            except:
                print()

        def enterSqlInit(self, ctx: cdbParser.SqlInitContext):
            global output, sql_init
            sql_init = True
            output += """
            sqlite3 *db;
            int rc;
            char *sql;
            char *zErrMsg = 0;
            rc = sqlite3_open("test.db", &db); // otwarcie bazy danych
            if( rc ) {
                fprintf(stderr, "Can't open database: %s", sqlite3_errmsg(db));
                sqlite3_close(db);
                exit(1);
            }
            """

        def enterSqlInsertStatement(self, ctx: cdbParser.SqlInsertStatementContext):
            global output
            line = ctx.getText()
            line.split('(')
            table = ctx.children[1]
            fields = ctx.children[3].children[0].getText()
            values = ctx.children[5].children[0].getText()
            output += f"""
            sql = sqlite3_mprintf("INSERT INTO {table} ({fields}) VALUES ({("'%q', " * len(fields.split(',')))[:-2]});", {values});
            rc = sqlite3_exec(db, sql, NULL, 0, &zErrMsg);
            """

        def enterSqlUpdateStatement(self, ctx: cdbParser.SqlUpdateStatementContext):
            global output
            line = ctx.getText()
            line.split('(')
            table = ctx.children[1]
            fields = ctx.children[3].children[0].getText()
            fields = fields.replace('"', '\\"')
            conditions = ctx.children[5].children[0].getText()
            conditions = conditions.replace('"', '\\"')
            output += f"""
            sql = sqlite3_mprintf("UPDATE {table} SET {fields} WHERE {conditions};");
            rc = sqlite3_exec(db, sql, NULL, 0, &zErrMsg);
            """

        def enterSqlDeleteStatement(self, ctx: cdbParser.SqlDeleteStatementContext):
            global output
            line = ctx.getText()
            line.split('(')
            table = ctx.children[1]
            conditions = ctx.children[3].children[0].getText()
            output += f"""
                   sql = sqlite3_mprintf("DELETE FROM {table} WHERE {conditions};");
                   rc = sqlite3_exec(db, sql, NULL, 0, &zErrMsg);
                   """

    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    result = headers + callbacks + output

    if not sql_init:
        err = SyntaxErr(0, 0, 'There is no sqlInit;')
        print(err.message)

    print(f'🤖 Using {callback_counter} callbacks')
    print(f'🚀 Transpiling done')

    return result.replace('<EOF>', ''), err

# out = transpile(open('main.c').read())
#
# f = open('output.c', 'w')
# f.write(out.replace('<EOF>', ''))
# f.close()
