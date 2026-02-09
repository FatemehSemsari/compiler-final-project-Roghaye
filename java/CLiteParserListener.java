// Generated from CLiteParser.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CLiteParser}.
 */
public interface CLiteParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CLiteParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(CLiteParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(CLiteParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#declarations}.
	 * @param ctx the parse tree
	 */
	void enterDeclarations(CLiteParser.DeclarationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#declarations}.
	 * @param ctx the parse tree
	 */
	void exitDeclarations(CLiteParser.DeclarationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(CLiteParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(CLiteParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#typeSpec}.
	 * @param ctx the parse tree
	 */
	void enterTypeSpec(CLiteParser.TypeSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#typeSpec}.
	 * @param ctx the parse tree
	 */
	void exitTypeSpec(CLiteParser.TypeSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#statements}.
	 * @param ctx the parse tree
	 */
	void enterStatements(CLiteParser.StatementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#statements}.
	 * @param ctx the parse tree
	 */
	void exitStatements(CLiteParser.StatementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(CLiteParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(CLiteParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(CLiteParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(CLiteParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(CLiteParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(CLiteParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(CLiteParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(CLiteParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(CLiteParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(CLiteParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(CLiteParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(CLiteParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(CLiteParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(CLiteParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#conjunction}.
	 * @param ctx the parse tree
	 */
	void enterConjunction(CLiteParser.ConjunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#conjunction}.
	 * @param ctx the parse tree
	 */
	void exitConjunction(CLiteParser.ConjunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#equality}.
	 * @param ctx the parse tree
	 */
	void enterEquality(CLiteParser.EqualityContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#equality}.
	 * @param ctx the parse tree
	 */
	void exitEquality(CLiteParser.EqualityContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#relation}.
	 * @param ctx the parse tree
	 */
	void enterRelation(CLiteParser.RelationContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#relation}.
	 * @param ctx the parse tree
	 */
	void exitRelation(CLiteParser.RelationContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#addition}.
	 * @param ctx the parse tree
	 */
	void enterAddition(CLiteParser.AdditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#addition}.
	 * @param ctx the parse tree
	 */
	void exitAddition(CLiteParser.AdditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(CLiteParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(CLiteParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(CLiteParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(CLiteParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CLiteParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(CLiteParser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CLiteParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(CLiteParser.PrimaryContext ctx);
}