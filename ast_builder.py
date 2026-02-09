from generated.CLiteParserVisitor import CLiteParserVisitor
from generated.CLiteParser import CLiteParser

from ast_nodes import (
    Program, Decl, Assign, Return, If, While, Block, Empty,
    BinOp, UnaryOp, Var, IntLit, FloatLit
)

class ASTBuilder(CLiteParserVisitor):

    def visitProgram(self, ctx: CLiteParser.ProgramContext):
        decls = self.visit(ctx.declarations())
        stmts = self.visit(ctx.statements())
        return Program(decls=decls, stmts=stmts)

    def visitDeclarations(self, ctx: CLiteParser.DeclarationsContext):
        return [self.visit(d) for d in ctx.declaration()]

    def visitDeclaration(self, ctx: CLiteParser.DeclarationContext):
        type_name = ctx.typeSpec().getText()
        name = ctx.ID().getText()
        init = self.visit(ctx.expression()) if ctx.expression() else None
        return Decl(type_name=type_name, name=name, init=init)

    def visitStatements(self, ctx: CLiteParser.StatementsContext):
        return [self.visit(s) for s in ctx.statement()]

    def visitStatement(self, ctx: CLiteParser.StatementContext):
        if ctx.SEMI():
            return Empty()
        if ctx.block():
            return self.visit(ctx.block())
        if ctx.assignment():
            return self.visit(ctx.assignment())
        if ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        if ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        if ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        return self.visitChildren(ctx)

    def visitBlock(self, ctx: CLiteParser.BlockContext):
        stmts = self.visit(ctx.statements())
        return Block(stmts=stmts)

    def visitAssignment(self, ctx: CLiteParser.AssignmentContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        return Assign(name=name, value=value)

    def visitReturnStatement(self, ctx: CLiteParser.ReturnStatementContext):
        value = self.visit(ctx.expression()) if ctx.expression() else None
        return Return(value=value)

    def visitIfStatement(self, ctx: CLiteParser.IfStatementContext):
        cond = self.visit(ctx.expression())
        then_branch = self.visit(ctx.statement(0))
        else_branch = self.visit(ctx.statement(1)) if ctx.ELSE() else None
        return If(cond=cond, then_branch=then_branch, else_branch=else_branch)

    def visitWhileStatement(self, ctx: CLiteParser.WhileStatementContext):
        cond = self.visit(ctx.expression())
        body = self.visit(ctx.statement())
        return While(cond=cond, body=body)

    def visitExpression(self, ctx: CLiteParser.ExpressionContext):
        node = self.visit(ctx.conjunction(0))
        for i in range(1, len(ctx.conjunction())):
            right = self.visit(ctx.conjunction(i))
            node = BinOp(op="||", left=node, right=right)
        return node

    def visitConjunction(self, ctx: CLiteParser.ConjunctionContext):
        node = self.visit(ctx.equality(0))
        for i in range(1, len(ctx.equality())):
            right = self.visit(ctx.equality(i))
            node = BinOp(op="&&", left=node, right=right)
        return node

    def visitEquality(self, ctx: CLiteParser.EqualityContext):
        left = self.visit(ctx.relation(0))
        if ctx.relation(1) is None:
            return left
        op = "==" if ctx.EQ() else "!="
        right = self.visit(ctx.relation(1))
        return BinOp(op=op, left=left, right=right)

    def visitRelation(self, ctx: CLiteParser.RelationContext):
        left = self.visit(ctx.addition(0))
        if ctx.addition(1) is None:
            return left
        if ctx.LT(): op = "<"
        elif ctx.LE(): op = "<="
        elif ctx.GT(): op = ">"
        else: op = ">="
        right = self.visit(ctx.addition(1))
        return BinOp(op=op, left=left, right=right)

    def visitAddition(self, ctx: CLiteParser.AdditionContext):
        node = self.visit(ctx.term(0))
        ops = ctx.getChildren()
        # ساده‌تر: از متن بین ترم‌ها می‌گیریم
        for i in range(1, len(ctx.term())):
            op_text = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.term(i))
            node = BinOp(op=op_text, left=node, right=right)
        return node

    def visitTerm(self, ctx: CLiteParser.TermContext):
        node = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op_text = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.factor(i))
            node = BinOp(op=op_text, left=node, right=right)
        return node

    def visitFactor(self, ctx: CLiteParser.FactorContext):
        if ctx.MINUS():
            return UnaryOp(op="-", operand=self.visit(ctx.primary()))
        if ctx.NOT():
            return UnaryOp(op="!", operand=self.visit(ctx.primary()))
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx: CLiteParser.PrimaryContext):
        if ctx.ID():
            return Var(name=ctx.ID().getText())
        if ctx.IntegerLiteral():
            return IntLit(value=int(ctx.IntegerLiteral().getText(), 0))
        if ctx.FloatingLiteral():
            return FloatLit(value=float(ctx.FloatingLiteral().getText()))
        return self.visit(ctx.expression())
