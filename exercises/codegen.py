from AST import *

class IntType(): pass
class FloatType(): pass
class BoolType(): pass


# Cau 1
def visitIntLiteral(self,ctx,o):
    code = self.emit.emitPUSHICONST(ctx.value,o.frame)
    typ = IntType()
    return code,typ

# Câu 2:
def visitFloatLiteral(self,ctx,o): 
    code = self.emit.emitPUSHFCONST(ctx.value,o.frame)
    typ = FloatType()
    return code,typ

# Câu 3:
def visitBinExpr(self, ast: BinExpr, o: Access):
    ctxt = o
    frame = ctxt.frame
    op = str(ast.op).lower()

    lCode, lType = self.visit(ast.e1, ctxt)         # e1c, e1t
    rCode, rType = self.visit(ast.e2, ctxt)         #e2c, e2t

    if op in ['+', '-']:
        return lCode + rCode + self.emit.emitADDOP(op, IntType(), frame), IntType()
    elif op in ['*', '/']:
        return lCode + rCode + self.emit.emitMULOP(op, IntType(), frame), IntType()
    elif op == '+.':
        return lCode + rCode + self.emit.jvm.emitFADD(), FloatType()
    elif op == '-.':
        return lCode + rCode + self.emit.jvm.emitFSUB(), FloatType()
    elif op == '*.':
        return lCode + rCode + self.emit.jvm.emitFMUL(), FloatType()
    elif op == '/.':
        return lCode + rCode + self.emit.jvm.emitFDIV(), FloatType()

# Câu 4:
def visitId(self, ctx, o):
    sym = list(filter(lambda x: x.name == ctx.name, o.sym))[0]
    if type(sym.value) is Index:
        code = self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame)
    else:
        code = self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, sym.mtype, o.frame)
    return code, sym.mtype

# Câu 5:
def visitBinExpr(self,ctx,o):
    op = ctx.op
    e1c, e1t = self.visit(ctx.e1, o)
    e2c, e2t = self.visit(ctx.e2, o)
    if type(e1t) is FloatType or type(e2t) is FloatType:
        mType = FloatType()
    else:
        mType = IntType()
    if op == '/': mType = FloatType()
    if type(e1t) is IntType and type(mType) != type(e1t): e1c = e1c + self.emit.emitI2F(o.frame)
    if type(e2t) is IntType and type(mType) != type(e2t): e2c = e2c + self.emit.emitI2F(o.frame)
    if op in ['>','<','>=','<=','!=','==']:
        return e1c + e2c + self.emit.emitREOP(op, mType, o.frame), BoolType()
    if op in ['+', '-']:
        return e1c + e2c + self.emit.emitADDOP(op, mType, o.frame), mType
    if op in ['*']:
        return e1c + e2c + self.emit.emitMULOP(op, mType, o.frame), mType
    if op in ['/']:
        return e1c + e2c + self.emit.emitMULOP(op, mType, o.frame), mType



#Câu 1:
def visitVarDecl(self, ctx, o):
    # No frame, this is a static field
    if o.frame is None:
        code = self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False)
        self.emit.printout(code)
        return Symbol(ctx.name, ctx.typ, CName(self.className))
    else:
    # A local variable
        idx = o.frame.getNewIndex()
        code = self.emit.emitVAR(idx, ctx.name, ctx.typ, o.frame.getStartLabel(), o.frame.getEndLabel())
        self.emit.printout(code)
        return Symbol(ctx.name, ctx.typ, Index(idx))

# Câu 2:
def visitId(self, ctx, o):
    if o.isLeft == False:
        sym = list(filter(lambda x: x.name == ctx.name, o.sym))[0]
        if type(sym.value) is Index:
            code = self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame)
        else:
            code = self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, sym.mtype, o.frame)
        return code, sym.mtype
    else:
        sym = list(filter(lambda x: x.name == ctx.name, o.sym))[0]
        if type(sym.value) is Index:
            code = self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame)
        else:
            code = self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name, sym.mtype, o.frame)
        return code, sym.mtype