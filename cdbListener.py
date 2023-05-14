# Generated from .\cdb.antl4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cdbParser import cdbParser
else:
    from cdbParser import cdbParser

# This class defines a complete listener for a parse tree produced by cdbParser.
class cdbListener(ParseTreeListener):

    # Enter a parse tree produced by cdbParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:cdbParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:cdbParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#genericSelection.
    def enterGenericSelection(self, ctx:cdbParser.GenericSelectionContext):
        pass

    # Exit a parse tree produced by cdbParser#genericSelection.
    def exitGenericSelection(self, ctx:cdbParser.GenericSelectionContext):
        pass


    # Enter a parse tree produced by cdbParser#genericAssocList.
    def enterGenericAssocList(self, ctx:cdbParser.GenericAssocListContext):
        pass

    # Exit a parse tree produced by cdbParser#genericAssocList.
    def exitGenericAssocList(self, ctx:cdbParser.GenericAssocListContext):
        pass


    # Enter a parse tree produced by cdbParser#genericAssociation.
    def enterGenericAssociation(self, ctx:cdbParser.GenericAssociationContext):
        pass

    # Exit a parse tree produced by cdbParser#genericAssociation.
    def exitGenericAssociation(self, ctx:cdbParser.GenericAssociationContext):
        pass


    # Enter a parse tree produced by cdbParser#postfixExpression.
    def enterPostfixExpression(self, ctx:cdbParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#postfixExpression.
    def exitPostfixExpression(self, ctx:cdbParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:cdbParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by cdbParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:cdbParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by cdbParser#unaryExpression.
    def enterUnaryExpression(self, ctx:cdbParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#unaryExpression.
    def exitUnaryExpression(self, ctx:cdbParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#unaryOperator.
    def enterUnaryOperator(self, ctx:cdbParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by cdbParser#unaryOperator.
    def exitUnaryOperator(self, ctx:cdbParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by cdbParser#castExpression.
    def enterCastExpression(self, ctx:cdbParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#castExpression.
    def exitCastExpression(self, ctx:cdbParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:cdbParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:cdbParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:cdbParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:cdbParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#shiftExpression.
    def enterShiftExpression(self, ctx:cdbParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#shiftExpression.
    def exitShiftExpression(self, ctx:cdbParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#relationalExpression.
    def enterRelationalExpression(self, ctx:cdbParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#relationalExpression.
    def exitRelationalExpression(self, ctx:cdbParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#equalityExpression.
    def enterEqualityExpression(self, ctx:cdbParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#equalityExpression.
    def exitEqualityExpression(self, ctx:cdbParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#andExpression.
    def enterAndExpression(self, ctx:cdbParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#andExpression.
    def exitAndExpression(self, ctx:cdbParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:cdbParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:cdbParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:cdbParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:cdbParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:cdbParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:cdbParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:cdbParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:cdbParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:cdbParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:cdbParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:cdbParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:cdbParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:cdbParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by cdbParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:cdbParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by cdbParser#expression.
    def enterExpression(self, ctx:cdbParser.ExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#expression.
    def exitExpression(self, ctx:cdbParser.ExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#constantExpression.
    def enterConstantExpression(self, ctx:cdbParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#constantExpression.
    def exitConstantExpression(self, ctx:cdbParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#declaration.
    def enterDeclaration(self, ctx:cdbParser.DeclarationContext):
        pass

    # Exit a parse tree produced by cdbParser#declaration.
    def exitDeclaration(self, ctx:cdbParser.DeclarationContext):
        pass


    # Enter a parse tree produced by cdbParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:cdbParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by cdbParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:cdbParser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by cdbParser#declarationSpecifiers2.
    def enterDeclarationSpecifiers2(self, ctx:cdbParser.DeclarationSpecifiers2Context):
        pass

    # Exit a parse tree produced by cdbParser#declarationSpecifiers2.
    def exitDeclarationSpecifiers2(self, ctx:cdbParser.DeclarationSpecifiers2Context):
        pass


    # Enter a parse tree produced by cdbParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:cdbParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by cdbParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:cdbParser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by cdbParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:cdbParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by cdbParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:cdbParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by cdbParser#initDeclarator.
    def enterInitDeclarator(self, ctx:cdbParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by cdbParser#initDeclarator.
    def exitInitDeclarator(self, ctx:cdbParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by cdbParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:cdbParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by cdbParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:cdbParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by cdbParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:cdbParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by cdbParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:cdbParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by cdbParser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx:cdbParser.StructOrUnionSpecifierContext):
        pass

    # Exit a parse tree produced by cdbParser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx:cdbParser.StructOrUnionSpecifierContext):
        pass


    # Enter a parse tree produced by cdbParser#structOrUnion.
    def enterStructOrUnion(self, ctx:cdbParser.StructOrUnionContext):
        pass

    # Exit a parse tree produced by cdbParser#structOrUnion.
    def exitStructOrUnion(self, ctx:cdbParser.StructOrUnionContext):
        pass


    # Enter a parse tree produced by cdbParser#structDeclarationList.
    def enterStructDeclarationList(self, ctx:cdbParser.StructDeclarationListContext):
        pass

    # Exit a parse tree produced by cdbParser#structDeclarationList.
    def exitStructDeclarationList(self, ctx:cdbParser.StructDeclarationListContext):
        pass


    # Enter a parse tree produced by cdbParser#structDeclaration.
    def enterStructDeclaration(self, ctx:cdbParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by cdbParser#structDeclaration.
    def exitStructDeclaration(self, ctx:cdbParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by cdbParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:cdbParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by cdbParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:cdbParser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by cdbParser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx:cdbParser.StructDeclaratorListContext):
        pass

    # Exit a parse tree produced by cdbParser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx:cdbParser.StructDeclaratorListContext):
        pass


    # Enter a parse tree produced by cdbParser#structDeclarator.
    def enterStructDeclarator(self, ctx:cdbParser.StructDeclaratorContext):
        pass

    # Exit a parse tree produced by cdbParser#structDeclarator.
    def exitStructDeclarator(self, ctx:cdbParser.StructDeclaratorContext):
        pass


    # Enter a parse tree produced by cdbParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:cdbParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by cdbParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:cdbParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by cdbParser#enumeratorList.
    def enterEnumeratorList(self, ctx:cdbParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by cdbParser#enumeratorList.
    def exitEnumeratorList(self, ctx:cdbParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by cdbParser#enumerator.
    def enterEnumerator(self, ctx:cdbParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by cdbParser#enumerator.
    def exitEnumerator(self, ctx:cdbParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by cdbParser#enumerationConstant.
    def enterEnumerationConstant(self, ctx:cdbParser.EnumerationConstantContext):
        pass

    # Exit a parse tree produced by cdbParser#enumerationConstant.
    def exitEnumerationConstant(self, ctx:cdbParser.EnumerationConstantContext):
        pass


    # Enter a parse tree produced by cdbParser#atomicTypeSpecifier.
    def enterAtomicTypeSpecifier(self, ctx:cdbParser.AtomicTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cdbParser#atomicTypeSpecifier.
    def exitAtomicTypeSpecifier(self, ctx:cdbParser.AtomicTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cdbParser#typeQualifier.
    def enterTypeQualifier(self, ctx:cdbParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by cdbParser#typeQualifier.
    def exitTypeQualifier(self, ctx:cdbParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by cdbParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:cdbParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by cdbParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:cdbParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by cdbParser#alignmentSpecifier.
    def enterAlignmentSpecifier(self, ctx:cdbParser.AlignmentSpecifierContext):
        pass

    # Exit a parse tree produced by cdbParser#alignmentSpecifier.
    def exitAlignmentSpecifier(self, ctx:cdbParser.AlignmentSpecifierContext):
        pass


    # Enter a parse tree produced by cdbParser#declarator.
    def enterDeclarator(self, ctx:cdbParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by cdbParser#declarator.
    def exitDeclarator(self, ctx:cdbParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by cdbParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:cdbParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by cdbParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:cdbParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by cdbParser#vcSpecificModifer.
    def enterVcSpecificModifer(self, ctx:cdbParser.VcSpecificModiferContext):
        pass

    # Exit a parse tree produced by cdbParser#vcSpecificModifer.
    def exitVcSpecificModifer(self, ctx:cdbParser.VcSpecificModiferContext):
        pass


    # Enter a parse tree produced by cdbParser#gccDeclaratorExtension.
    def enterGccDeclaratorExtension(self, ctx:cdbParser.GccDeclaratorExtensionContext):
        pass

    # Exit a parse tree produced by cdbParser#gccDeclaratorExtension.
    def exitGccDeclaratorExtension(self, ctx:cdbParser.GccDeclaratorExtensionContext):
        pass


    # Enter a parse tree produced by cdbParser#gccAttributeSpecifier.
    def enterGccAttributeSpecifier(self, ctx:cdbParser.GccAttributeSpecifierContext):
        pass

    # Exit a parse tree produced by cdbParser#gccAttributeSpecifier.
    def exitGccAttributeSpecifier(self, ctx:cdbParser.GccAttributeSpecifierContext):
        pass


    # Enter a parse tree produced by cdbParser#gccAttributeList.
    def enterGccAttributeList(self, ctx:cdbParser.GccAttributeListContext):
        pass

    # Exit a parse tree produced by cdbParser#gccAttributeList.
    def exitGccAttributeList(self, ctx:cdbParser.GccAttributeListContext):
        pass


    # Enter a parse tree produced by cdbParser#gccAttribute.
    def enterGccAttribute(self, ctx:cdbParser.GccAttributeContext):
        pass

    # Exit a parse tree produced by cdbParser#gccAttribute.
    def exitGccAttribute(self, ctx:cdbParser.GccAttributeContext):
        pass


    # Enter a parse tree produced by cdbParser#nestedParenthesesBlock.
    def enterNestedParenthesesBlock(self, ctx:cdbParser.NestedParenthesesBlockContext):
        pass

    # Exit a parse tree produced by cdbParser#nestedParenthesesBlock.
    def exitNestedParenthesesBlock(self, ctx:cdbParser.NestedParenthesesBlockContext):
        pass


    # Enter a parse tree produced by cdbParser#pointer.
    def enterPointer(self, ctx:cdbParser.PointerContext):
        pass

    # Exit a parse tree produced by cdbParser#pointer.
    def exitPointer(self, ctx:cdbParser.PointerContext):
        pass


    # Enter a parse tree produced by cdbParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:cdbParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by cdbParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:cdbParser.TypeQualifierListContext):
        pass


    # Enter a parse tree produced by cdbParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:cdbParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by cdbParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:cdbParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by cdbParser#parameterList.
    def enterParameterList(self, ctx:cdbParser.ParameterListContext):
        pass

    # Exit a parse tree produced by cdbParser#parameterList.
    def exitParameterList(self, ctx:cdbParser.ParameterListContext):
        pass


    # Enter a parse tree produced by cdbParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:cdbParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by cdbParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:cdbParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by cdbParser#identifierList.
    def enterIdentifierList(self, ctx:cdbParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by cdbParser#identifierList.
    def exitIdentifierList(self, ctx:cdbParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by cdbParser#typeName.
    def enterTypeName(self, ctx:cdbParser.TypeNameContext):
        pass

    # Exit a parse tree produced by cdbParser#typeName.
    def exitTypeName(self, ctx:cdbParser.TypeNameContext):
        pass


    # Enter a parse tree produced by cdbParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:cdbParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by cdbParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:cdbParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by cdbParser#directAbstractDeclarator.
    def enterDirectAbstractDeclarator(self, ctx:cdbParser.DirectAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by cdbParser#directAbstractDeclarator.
    def exitDirectAbstractDeclarator(self, ctx:cdbParser.DirectAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by cdbParser#typedefName.
    def enterTypedefName(self, ctx:cdbParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by cdbParser#typedefName.
    def exitTypedefName(self, ctx:cdbParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by cdbParser#initializer.
    def enterInitializer(self, ctx:cdbParser.InitializerContext):
        pass

    # Exit a parse tree produced by cdbParser#initializer.
    def exitInitializer(self, ctx:cdbParser.InitializerContext):
        pass


    # Enter a parse tree produced by cdbParser#initializerList.
    def enterInitializerList(self, ctx:cdbParser.InitializerListContext):
        pass

    # Exit a parse tree produced by cdbParser#initializerList.
    def exitInitializerList(self, ctx:cdbParser.InitializerListContext):
        pass


    # Enter a parse tree produced by cdbParser#designation.
    def enterDesignation(self, ctx:cdbParser.DesignationContext):
        pass

    # Exit a parse tree produced by cdbParser#designation.
    def exitDesignation(self, ctx:cdbParser.DesignationContext):
        pass


    # Enter a parse tree produced by cdbParser#designatorList.
    def enterDesignatorList(self, ctx:cdbParser.DesignatorListContext):
        pass

    # Exit a parse tree produced by cdbParser#designatorList.
    def exitDesignatorList(self, ctx:cdbParser.DesignatorListContext):
        pass


    # Enter a parse tree produced by cdbParser#designator.
    def enterDesignator(self, ctx:cdbParser.DesignatorContext):
        pass

    # Exit a parse tree produced by cdbParser#designator.
    def exitDesignator(self, ctx:cdbParser.DesignatorContext):
        pass


    # Enter a parse tree produced by cdbParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:cdbParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by cdbParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:cdbParser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by cdbParser#sqlSelectStatement.
    def enterSqlSelectStatement(self, ctx:cdbParser.SqlSelectStatementContext):
        pass

    # Exit a parse tree produced by cdbParser#sqlSelectStatement.
    def exitSqlSelectStatement(self, ctx:cdbParser.SqlSelectStatementContext):
        pass


    # Enter a parse tree produced by cdbParser#sqlInsertStatement.
    def enterSqlInsertStatement(self, ctx:cdbParser.SqlInsertStatementContext):
        pass

    # Exit a parse tree produced by cdbParser#sqlInsertStatement.
    def exitSqlInsertStatement(self, ctx:cdbParser.SqlInsertStatementContext):
        pass


    # Enter a parse tree produced by cdbParser#sqlUpdateStatement.
    def enterSqlUpdateStatement(self, ctx:cdbParser.SqlUpdateStatementContext):
        pass

    # Exit a parse tree produced by cdbParser#sqlUpdateStatement.
    def exitSqlUpdateStatement(self, ctx:cdbParser.SqlUpdateStatementContext):
        pass


    # Enter a parse tree produced by cdbParser#sqlDeleteStatement.
    def enterSqlDeleteStatement(self, ctx:cdbParser.SqlDeleteStatementContext):
        pass

    # Exit a parse tree produced by cdbParser#sqlDeleteStatement.
    def exitSqlDeleteStatement(self, ctx:cdbParser.SqlDeleteStatementContext):
        pass


    # Enter a parse tree produced by cdbParser#fieldList.
    def enterFieldList(self, ctx:cdbParser.FieldListContext):
        pass

    # Exit a parse tree produced by cdbParser#fieldList.
    def exitFieldList(self, ctx:cdbParser.FieldListContext):
        pass


    # Enter a parse tree produced by cdbParser#commaSeparatedList.
    def enterCommaSeparatedList(self, ctx:cdbParser.CommaSeparatedListContext):
        pass

    # Exit a parse tree produced by cdbParser#commaSeparatedList.
    def exitCommaSeparatedList(self, ctx:cdbParser.CommaSeparatedListContext):
        pass


    # Enter a parse tree produced by cdbParser#spaceSeparatedList.
    def enterSpaceSeparatedList(self, ctx:cdbParser.SpaceSeparatedListContext):
        pass

    # Exit a parse tree produced by cdbParser#spaceSeparatedList.
    def exitSpaceSeparatedList(self, ctx:cdbParser.SpaceSeparatedListContext):
        pass


    # Enter a parse tree produced by cdbParser#statement.
    def enterStatement(self, ctx:cdbParser.StatementContext):
        pass

    # Exit a parse tree produced by cdbParser#statement.
    def exitStatement(self, ctx:cdbParser.StatementContext):
        pass


    # Enter a parse tree produced by cdbParser#labeledStatement.
    def enterLabeledStatement(self, ctx:cdbParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by cdbParser#labeledStatement.
    def exitLabeledStatement(self, ctx:cdbParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by cdbParser#compoundStatement.
    def enterCompoundStatement(self, ctx:cdbParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by cdbParser#compoundStatement.
    def exitCompoundStatement(self, ctx:cdbParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by cdbParser#blockItemList.
    def enterBlockItemList(self, ctx:cdbParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by cdbParser#blockItemList.
    def exitBlockItemList(self, ctx:cdbParser.BlockItemListContext):
        pass


    # Enter a parse tree produced by cdbParser#blockItem.
    def enterBlockItem(self, ctx:cdbParser.BlockItemContext):
        pass

    # Exit a parse tree produced by cdbParser#blockItem.
    def exitBlockItem(self, ctx:cdbParser.BlockItemContext):
        pass


    # Enter a parse tree produced by cdbParser#expressionStatement.
    def enterExpressionStatement(self, ctx:cdbParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by cdbParser#expressionStatement.
    def exitExpressionStatement(self, ctx:cdbParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by cdbParser#selectionStatement.
    def enterSelectionStatement(self, ctx:cdbParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by cdbParser#selectionStatement.
    def exitSelectionStatement(self, ctx:cdbParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by cdbParser#iterationStatement.
    def enterIterationStatement(self, ctx:cdbParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by cdbParser#iterationStatement.
    def exitIterationStatement(self, ctx:cdbParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by cdbParser#forCondition.
    def enterForCondition(self, ctx:cdbParser.ForConditionContext):
        pass

    # Exit a parse tree produced by cdbParser#forCondition.
    def exitForCondition(self, ctx:cdbParser.ForConditionContext):
        pass


    # Enter a parse tree produced by cdbParser#forDeclaration.
    def enterForDeclaration(self, ctx:cdbParser.ForDeclarationContext):
        pass

    # Exit a parse tree produced by cdbParser#forDeclaration.
    def exitForDeclaration(self, ctx:cdbParser.ForDeclarationContext):
        pass


    # Enter a parse tree produced by cdbParser#forExpression.
    def enterForExpression(self, ctx:cdbParser.ForExpressionContext):
        pass

    # Exit a parse tree produced by cdbParser#forExpression.
    def exitForExpression(self, ctx:cdbParser.ForExpressionContext):
        pass


    # Enter a parse tree produced by cdbParser#jumpStatement.
    def enterJumpStatement(self, ctx:cdbParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by cdbParser#jumpStatement.
    def exitJumpStatement(self, ctx:cdbParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by cdbParser#compilationUnit.
    def enterCompilationUnit(self, ctx:cdbParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by cdbParser#compilationUnit.
    def exitCompilationUnit(self, ctx:cdbParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by cdbParser#translationUnit.
    def enterTranslationUnit(self, ctx:cdbParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by cdbParser#translationUnit.
    def exitTranslationUnit(self, ctx:cdbParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by cdbParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:cdbParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by cdbParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:cdbParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by cdbParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:cdbParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by cdbParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:cdbParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by cdbParser#declarationList.
    def enterDeclarationList(self, ctx:cdbParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by cdbParser#declarationList.
    def exitDeclarationList(self, ctx:cdbParser.DeclarationListContext):
        pass


