from antlr4 import *

from cdbLexer import cdbLexer
from cdbListener import cdbListener
from cdbParser import cdbParser

input_stream = open('main.c').read()
print(input_stream)
lexer = cdbLexer(InputStream(input_stream))
stream = CommonTokenStream(lexer)
parser = cdbParser(stream)
tree = parser.compilationUnit()

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


class Listener(cdbListener):
    def visitTerminal(self, node: cdbParser.SqlSelectStatementContext):
        global output
        for banned_context in banned_contexts:
            if check_for_parent(node, banned_context):
                return
        if node.getChildCount() == 0:
            output += node.getText() + ' '

    def enterSqlSelectStatement(self, ctx: cdbParser.SqlSelectStatementContext):
        global output
        output += "SELECT "

    def enterSqlInit(self, ctx: cdbParser.SqlInitContext):
        global output
        output += """
        sqlite3 *db;
        int rc;
        char *sql;
        rc = sqlite3_open("test.db", &db); // otwarcie bazy danych
        if( rc ) {
            fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
            sqlite3_close(db);
            exit(1);
        }
        """


listener = Listener()
walker = ParseTreeWalker()
walker.walk(listener, tree)
print(output)
