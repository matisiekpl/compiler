from antlr4 import *

from cdbLexer import cdbLexer
from cdbListener import cdbListener
from cdbParser import cdbParser

input_stream = open('main.c').read()
lexer = cdbLexer(InputStream(input_stream))
stream = CommonTokenStream(lexer)
parser = cdbParser(stream)
tree = parser.compilationUnit()

headers = "#include <stdio.h>\n#include <sqlite3.h>\n#include <stddef.h>\n#include <stdlib.h>\n"
callbacks = ""
output = ""


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

    def enterSqlInit(self, ctx: cdbParser.SqlInitContext):
        global output
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

output = headers + callbacks + output

print(f'🤖 Using {callback_counter} callbacks')
print(f'🚀 Transpiling done')

f = open('output.c', 'w')
f.write(output.replace('<EOF>', ''))
f.close()
