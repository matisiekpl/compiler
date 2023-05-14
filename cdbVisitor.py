# Generated from .\cdb.antl4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cdbParser import cdbParser
else:
    from cdbParser import cdbParser

# This class defines a complete generic visitor for a parse tree produced by cdbParser.

class cdbVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cdbParser#parse.
    def visitParse(self, ctx:cdbParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:cdbParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#genericSelection.
    def visitGenericSelection(self, ctx:cdbParser.GenericSelectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#genericAssocList.
    def visitGenericAssocList(self, ctx:cdbParser.GenericAssocListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#genericAssociation.
    def visitGenericAssociation(self, ctx:cdbParser.GenericAssociationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#postfixExpression.
    def visitPostfixExpression(self, ctx:cdbParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:cdbParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#unaryExpression.
    def visitUnaryExpression(self, ctx:cdbParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#unaryOperator.
    def visitUnaryOperator(self, ctx:cdbParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#castExpression.
    def visitCastExpression(self, ctx:cdbParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:cdbParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:cdbParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#shiftExpression.
    def visitShiftExpression(self, ctx:cdbParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#relationalExpression.
    def visitRelationalExpression(self, ctx:cdbParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#equalityExpression.
    def visitEqualityExpression(self, ctx:cdbParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#andExpression.
    def visitAndExpression(self, ctx:cdbParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:cdbParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:cdbParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:cdbParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:cdbParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:cdbParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:cdbParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:cdbParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#expression.
    def visitExpression(self, ctx:cdbParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#constantExpression.
    def visitConstantExpression(self, ctx:cdbParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#declaration.
    def visitDeclaration(self, ctx:cdbParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#declarationSpecifiers.
    def visitDeclarationSpecifiers(self, ctx:cdbParser.DeclarationSpecifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#declarationSpecifiers2.
    def visitDeclarationSpecifiers2(self, ctx:cdbParser.DeclarationSpecifiers2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#declarationSpecifier.
    def visitDeclarationSpecifier(self, ctx:cdbParser.DeclarationSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:cdbParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#initDeclarator.
    def visitInitDeclarator(self, ctx:cdbParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#storageClassSpecifier.
    def visitStorageClassSpecifier(self, ctx:cdbParser.StorageClassSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:cdbParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#structOrUnionSpecifier.
    def visitStructOrUnionSpecifier(self, ctx:cdbParser.StructOrUnionSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#structOrUnion.
    def visitStructOrUnion(self, ctx:cdbParser.StructOrUnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#structDeclarationList.
    def visitStructDeclarationList(self, ctx:cdbParser.StructDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#structDeclaration.
    def visitStructDeclaration(self, ctx:cdbParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#specifierQualifierList.
    def visitSpecifierQualifierList(self, ctx:cdbParser.SpecifierQualifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#structDeclaratorList.
    def visitStructDeclaratorList(self, ctx:cdbParser.StructDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#structDeclarator.
    def visitStructDeclarator(self, ctx:cdbParser.StructDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#enumSpecifier.
    def visitEnumSpecifier(self, ctx:cdbParser.EnumSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#enumeratorList.
    def visitEnumeratorList(self, ctx:cdbParser.EnumeratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#enumerator.
    def visitEnumerator(self, ctx:cdbParser.EnumeratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#enumerationConstant.
    def visitEnumerationConstant(self, ctx:cdbParser.EnumerationConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#atomicTypeSpecifier.
    def visitAtomicTypeSpecifier(self, ctx:cdbParser.AtomicTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#typeQualifier.
    def visitTypeQualifier(self, ctx:cdbParser.TypeQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#functionSpecifier.
    def visitFunctionSpecifier(self, ctx:cdbParser.FunctionSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#alignmentSpecifier.
    def visitAlignmentSpecifier(self, ctx:cdbParser.AlignmentSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#declarator.
    def visitDeclarator(self, ctx:cdbParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#directDeclarator.
    def visitDirectDeclarator(self, ctx:cdbParser.DirectDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#vcSpecificModifer.
    def visitVcSpecificModifer(self, ctx:cdbParser.VcSpecificModiferContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#gccDeclaratorExtension.
    def visitGccDeclaratorExtension(self, ctx:cdbParser.GccDeclaratorExtensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#gccAttributeSpecifier.
    def visitGccAttributeSpecifier(self, ctx:cdbParser.GccAttributeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#gccAttributeList.
    def visitGccAttributeList(self, ctx:cdbParser.GccAttributeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#gccAttribute.
    def visitGccAttribute(self, ctx:cdbParser.GccAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#nestedParenthesesBlock.
    def visitNestedParenthesesBlock(self, ctx:cdbParser.NestedParenthesesBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#pointer.
    def visitPointer(self, ctx:cdbParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#typeQualifierList.
    def visitTypeQualifierList(self, ctx:cdbParser.TypeQualifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#parameterTypeList.
    def visitParameterTypeList(self, ctx:cdbParser.ParameterTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#parameterList.
    def visitParameterList(self, ctx:cdbParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:cdbParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#identifierList.
    def visitIdentifierList(self, ctx:cdbParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#typeName.
    def visitTypeName(self, ctx:cdbParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx:cdbParser.AbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#directAbstractDeclarator.
    def visitDirectAbstractDeclarator(self, ctx:cdbParser.DirectAbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#typedefName.
    def visitTypedefName(self, ctx:cdbParser.TypedefNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#initializer.
    def visitInitializer(self, ctx:cdbParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#initializerList.
    def visitInitializerList(self, ctx:cdbParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#designation.
    def visitDesignation(self, ctx:cdbParser.DesignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#designatorList.
    def visitDesignatorList(self, ctx:cdbParser.DesignatorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#designator.
    def visitDesignator(self, ctx:cdbParser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#staticAssertDeclaration.
    def visitStaticAssertDeclaration(self, ctx:cdbParser.StaticAssertDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#sqlSelectStatement.
    def visitSqlSelectStatement(self, ctx:cdbParser.SqlSelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#sqlInsertStatement.
    def visitSqlInsertStatement(self, ctx:cdbParser.SqlInsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#sqlUpdateStatement.
    def visitSqlUpdateStatement(self, ctx:cdbParser.SqlUpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#sqlDeleteStatement.
    def visitSqlDeleteStatement(self, ctx:cdbParser.SqlDeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#fieldList.
    def visitFieldList(self, ctx:cdbParser.FieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#commaSeparatedList.
    def visitCommaSeparatedList(self, ctx:cdbParser.CommaSeparatedListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#spaceSeparatedList.
    def visitSpaceSeparatedList(self, ctx:cdbParser.SpaceSeparatedListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#statement.
    def visitStatement(self, ctx:cdbParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#sqlInit.
    def visitSqlInit(self, ctx:cdbParser.SqlInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#labeledStatement.
    def visitLabeledStatement(self, ctx:cdbParser.LabeledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#compoundStatement.
    def visitCompoundStatement(self, ctx:cdbParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#blockItemList.
    def visitBlockItemList(self, ctx:cdbParser.BlockItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#blockItem.
    def visitBlockItem(self, ctx:cdbParser.BlockItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#expressionStatement.
    def visitExpressionStatement(self, ctx:cdbParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#selectionStatement.
    def visitSelectionStatement(self, ctx:cdbParser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#iterationStatement.
    def visitIterationStatement(self, ctx:cdbParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#forCondition.
    def visitForCondition(self, ctx:cdbParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#forDeclaration.
    def visitForDeclaration(self, ctx:cdbParser.ForDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#forExpression.
    def visitForExpression(self, ctx:cdbParser.ForExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#jumpStatement.
    def visitJumpStatement(self, ctx:cdbParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#compilationUnit.
    def visitCompilationUnit(self, ctx:cdbParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#translationUnit.
    def visitTranslationUnit(self, ctx:cdbParser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#externalDeclaration.
    def visitExternalDeclaration(self, ctx:cdbParser.ExternalDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:cdbParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cdbParser#declarationList.
    def visitDeclarationList(self, ctx:cdbParser.DeclarationListContext):
        return self.visitChildren(ctx)



del cdbParser