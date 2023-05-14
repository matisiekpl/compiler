from cdbLexer import cdbLexer
from cdbListener import cdbListener
from cdbParser import cdbParser
from antlr4 import *

input_stream = open('main.c').read()
print(input_stream)
lexer = cdbLexer(InputStream(input_stream))
stream = CommonTokenStream(lexer)
parser = cdbParser(stream)
tree = parser.compilationUnit()
print(tree)


class HelloPrintListener(cdbListener):
    def enterEveryRule(self, ctx: ParserRuleContext):

        print(ctx.stop.text)

    def enterSqlSelectStatement(self, ctx: cdbParser.SqlSelectStatementContext):
        print('a')


walker = ParseTreeWalker()
walker.walk(HelloPrintListener(), tree)
