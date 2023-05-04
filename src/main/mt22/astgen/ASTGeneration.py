from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.declprime()))

    def visitDeclprime(self, ctx: MT22Parser.DeclprimeContext):
        if ctx.declprime():
            return self.visit(ctx.decl()) + self.visit(ctx.declprime())
        return self.visit(ctx.decl())

    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return [self.visit(ctx.funcdecl())]

    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.multidecl():
            idlist, exprlist, typ = self.visit(ctx.multidecl())
            return list(map(lambda i: VarDecl(idlist[i], typ, exprlist[i]), range(len(idlist))))
        typ = self.visit(ctx.returnabletype())
        return list(map(lambda x: VarDecl(x, typ, None), self.visit(ctx.idprime())))

    def visitMultidecl(self, ctx: MT22Parser.MultideclContext):
        if ctx.multidecl():
            idlist, exprlist, typ = self.visit(ctx.multidecl())
            return [ctx.ID().getText()] + idlist, exprlist + [self.visit(ctx.expr())], typ

        return [ctx.ID().getText()], [self.visit(ctx.expr())], self.visit(ctx.returnabletype())

    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        inherit = None
        if ctx.INHERIT():
            inherit = ctx.ID(1).getText()
        return FuncDecl(ctx.ID(0).getText(), self.visit(ctx.typ()), self.visit(ctx.paramlist()), inherit, self.visit(ctx.blockstmt()))

    # Visit a parse tree produced by MT22Parser#idPrime.
    def visitIdprime(self, ctx: MT22Parser.IdprimeContext):
        if ctx.CM():
            return [ctx.ID().getText()] + self.visit(ctx.idprime())
        return [ctx.ID().getText()]

    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.exprprime():
            return self.visit(ctx.exprprime())
        return []

    # Visit a parse tree produced by MT22Parser#exprprime.
    def visitExprprime(self, ctx: MT22Parser.ExprprimeContext):
        if ctx.CM():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())
        return [self.visit(ctx.expr())]

    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        if ctx.paramprime():
            return self.visit(ctx.paramprime())
        return []

    # Visit a parse tree produced by MT22Parser#paramprime.
    def visitParamprime(self, ctx: MT22Parser.ParamprimeContext):
        if ctx.CM():
            return [self.visit(ctx.paramdecl())] + self.visit(ctx.paramprime())
        return [self.visit(ctx.paramdecl())]

    # Visit a parse tree produced by MT22Parser#paramDecl.
    def visitParamdecl(self, ctx: MT22Parser.ParamdeclContext):
        return ParamDecl(ctx.ID().getText(), self.visit(ctx.returnabletype()), ctx.OUT(), ctx.INHERIT())

    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#assignstmt.
    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.arraycell())

    # Visit a parse tree produWSced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx: MT22Parser.IfstmtContext):
        cond = self.visit(ctx.expr())
        tstmt = self.visit(ctx.stmt())
        fstmt = None
        if ctx.elsestmt():
            fstmt = self.visit(ctx.elsestmt())
        return IfStmt(cond, tstmt, fstmt)

    # Visit a parse tree produced by MT22Parser#elsestmt.
    def visitElsestmt(self, ctx: MT22Parser.ElsestmtContext):
        return self.visit(ctx.stmt())

    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx: MT22Parser.ForstmtContext):
        return ForStmt(AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr(0))), self.visit(ctx.expr(1)), self.visit(ctx.expr(2)), self.visit(ctx.stmt()))

    # Visit a parse tree produced by MT22Parser#whilestmt.
    def visitWhilestmt(self, ctx: MT22Parser.WhilestmtContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))

    # Visit a parse tree produced by MT22Parser#dowhilestmt.
    def visitDowhilestmt(self, ctx: MT22Parser.DowhilestmtContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.blockstmt()))

    # Visit a parse tree produced by MT22Parser#breakstmt.
    def visitBreakstmt(self, ctx: MT22Parser.BreakstmtContext):
        return BreakStmt()

    # Visit a parse tree produced by MT22Parser#continuestmt.
    def visitContinuestmt(self, ctx: MT22Parser.ContinuestmtContext):
        return ContinueStmt()

    # Visit a parse tree produced by MT22Parser#returnstmt.
    def visitReturnstmt(self, ctx: MT22Parser.ReturnstmtContext):
        expr = None
        if ctx.expr():
            expr = self.visit(ctx.expr())
        return ReturnStmt(expr)

    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx: MT22Parser.CallstmtContext):
        return CallStmt(ctx.ID().getText(), self.visit(ctx.exprlist()))

    # Visit a parse tree produced by MT22Parser#blockstmt.
    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        return BlockStmt(self.visit(ctx.stmtlist()))

    # Visit a parse tree produced by MT22Parser#stmtlist.
    def visitStmtlist(self, ctx: MT22Parser.StmtlistContext):
        if ctx.stmtlist():
            if ctx.stmt():
                return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())
            return self.visit(ctx.vardecl()) + self.visit(ctx.stmtlist())
        return []

    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.CONCATE():
            return BinExpr(ctx.CONCATE().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        return self.visit(ctx.expr1(0))

    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.LT():
            return BinExpr(ctx.LT().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.GT():
            return BinExpr(ctx.GT().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.LE():
            return BinExpr(ctx.LE().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.GE():
            return BinExpr(ctx.GE().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.EQUAL():
            return BinExpr(ctx.EQUAL().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.NOT_EQUAL():
            return BinExpr(ctx.NOT_EQUAL().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        return self.visit(ctx.expr2(0))

    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.OR():
            return BinExpr(ctx.OR().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        if ctx.AND():
            return BinExpr(ctx.AND().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        return self.visit(ctx.expr3())

    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.ADD():
            return BinExpr(ctx.ADD().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        if ctx.SUB():
            return BinExpr(ctx.SUB().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        return self.visit(ctx.expr4())

    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.MUL():
            return BinExpr(ctx.MUL().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        if ctx.DIV():
            return BinExpr(ctx.DIV().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        if ctx.MOD():
            return BinExpr(ctx.MOD().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return self.visit(ctx.expr5())

    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.NOT():
            return UnExpr(ctx.NOT().getText(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())

    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.SUB():
            return UnExpr(ctx.SUB().getText(), self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())

    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.arraylit():
            return self.visit(ctx.arraylit())
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            floatlit = ctx.FLOATLIT().getText()
            if floatlit[0:2] == ".e" or floatlit[0:2] == ".E":
                return FloatLit(0.0)
            return FloatLit(float(floatlit))

        if ctx.BOOLEANLIT():
            return BooleanLit(ctx.BOOLEANLIT().getText() == "true")
        if ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        if ctx.funccall():
            return self.visit(ctx.funccall())
        if ctx.arraycell():
            return self.visit(ctx.arraycell())
        if ctx.expr():
            return self.visit(ctx.expr())
        if ctx.ID():
            return Id(ctx.ID().getText())
        return None

    # Visit a parse tree produced by MT22Parser#arrayCell.
    def visitArraycell(self, ctx: MT22Parser.ArraycellContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.exprprime()))

    # Visit a parse tree produced by MT22Parser#funcCall.
    def visitFunccall(self, ctx: MT22Parser.FunccallContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.exprlist()))

    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.VOID():
            return VoidType()
        return self.visit(ctx.returnabletype())

    # Visit a parse tree produced by MT22Parser#returnableType.
    def visitReturnabletype(self, ctx: MT22Parser.ReturnabletypeContext):
        if ctx.array():
            return self.visit(ctx.array())
        if ctx.atomictype():
            return self.visit(ctx.atomictype())
        if ctx.AUTO():
            return AutoType()
        return None

    # Visit a parse tree produced by MT22Parser#array.
    def visitArray(self, ctx: MT22Parser.ArrayContext):
        return ArrayType(self.visit(ctx.intprime()), self.visit(ctx.atomictype()))

    # Visit a parse tree produced by MT22Parser#atomictype.
    def visitAtomictype(self, ctx: MT22Parser.AtomictypeContext):
        if ctx.INTEGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BooleanType()
        if ctx.STRING():
            return StringType()
        return None

    # Visit a parse tree produced by MT22Parser#intprime.
    def visitIntprime(self, ctx: MT22Parser.IntprimeContext):
        if ctx.CM():
            return [int(ctx.INTLIT().getText())] + self.visit(ctx.intprime())
        return [int(ctx.INTLIT().getText())]

    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.exprlist()))
