from typing import List
from StaticError import *
from Visitor import Visitor
from AST import *
from abc import ABC


class StmtType: pass
class DeclType: pass

class VarDeclType(DeclType): pass
class FuncDeclType(DeclType): pass
class IllegalType(Type): pass

class LoopStmtType(StmtType): pass
class MustInLoopStmtType(StmtType): pass
class AssignStmtType(StmtType): pass
class IfStmtType(StmtType): pass
class ReturnStmtType(StmtType): pass
class BlockStmtType(StmtType): pass
class CallStmtType(StmtType): pass

class Symbol:
    def __init__(self, name, typ: Type):
        self.name = name
        self.typ = typ
    def __str__(self):
        return "Symbol({}, {})".format(self.name, self.typ)


class VarSym(Symbol):
    def __init__(self, name : str, typ : Type):
        super().__init__(name, typ)
    
    def __str__(self):
        return "VarSym({}, {})".format(self.name, self.typ)


class ParaSym(Symbol):
    def __init__(self, name : str, typ : Type, out: bool = False, inherit: bool = False):
        super().__init__(name, typ)
        self.out = out
        self.inherit = inherit
    def __str__(self):
        return "ParaSym({}, {}{}{})".format(self.name, 
                                            self.typ, 
                                            ", inherit" if self.inherit else "",
                                            ", out" if self.out else "")

class FuncSym(Symbol):
    def __init__(self, name : str, typ : Type, params: List[Symbol] = [], inherit: str or None = None, parentparams: List[ParaSym] = [],):
        super().__init__(name, typ)
        self.params = params
        self.inherit = inherit
        self.parentparams = parentparams

    def __str__(self):
        return f"FuncSym({self.name}, {self.typ}, [{', '.join(str(param) for param in self.params)}], {self.inherit}{' ' if self.inherit is not None else ''}, [{', '.join(str(parentparam) for parentparam in self.parentparams)}])"


""" Every node points to a symbol table where there is a field received from parent and its own field
Function prototypes must be saved separately in precheck
Every node returns a pair of st and type which can be used by parent
"""

class Properties:
    def __init__(self, inFunc = None, inLoop = 0, isSuper = False, returnType = None):

        # This is in a Funcdecl
        self.inFunc = inFunc

        # This is in some loops
        self.inLoop = inLoop

        # This call statement is called through super()
        self.isSuper = isSuper

class SymbolTable:
    def __init__(self, 
                 envs = [[]], 
                 funcprototype : List[FuncSym] = [], 
                 properties : Properties = Properties()):
        """Local environments"""
        self.envs = [[]] if envs == [[]] else envs

        """Global function prototypes"""
        self.funcprototype = [] if funcprototype == [] else funcprototype
        self.library = [FuncSym("readInteger", IntegerType()),
                        FuncSym("printInteger", VoidType(), [ParaSym("veryStrange", IntegerType())]),
                        FuncSym("readFloat", FloatType()),
                        FuncSym("writeFloat", VoidType(), [ParaSym("veryStrange", FloatType())]),
                        FuncSym("readBoolean", BooleanType()),
                        FuncSym("printBoolean", VoidType(), [ParaSym("veryStrange", BooleanType())]),
                        FuncSym("readString", StringType()),
                        FuncSym("printString", VoidType(), [ParaSym("veryStrange", StringType())])]
        
        # Properties
        self.properties = properties

class Utils:

    def addSym(sym : Symbol, st : SymbolTable):
        st.envs[0] = [sym] + st.envs[0]
        return SymbolTable(st.envs, st.funcprototype, st.properties)

    def findVar(name : str, st : SymbolTable):
        for scope in st.envs:
            for sym in scope:
                if sym.name == name: return sym
    
    def findFunc(name : str, st : SymbolTable):
        for sym in st.library + st.funcprototype:
            if sym.name == name: return sym
    
    def find(name : str, st : SymbolTable):
        sym = None
        sym = Utils.findVar(name, st)
        if not sym: sym = Utils.findFunc(name, st)
        return sym

        
    def isCoercionable(typ1 : Type, typ2 : Type):
        if type(typ1) is not type(typ2):
            if type(typ1) is FloatType and type(typ2) is IntegerType: return True
            return False
        else:
            if type(typ1) is ArrayType and type(typ2) is ArrayType: 
                if typ1.dimensions != typ2.dimensions: return False
                if not Utils.isCoercionable(typ1.typ, typ2.typ): return False
            return True
    
    """Come into a function body"""
    def comeInFunc(st : SymbolTable, info : FuncSym):
        return SymbolTable([[]]+st.envs, st.funcprototype, Properties(info, st.properties.inLoop, st.properties.isSuper))

    """Come into a loop body"""
    def comeInLoop(st : SymbolTable):
        return SymbolTable([[]]+st.envs, st.funcprototype, Properties(st.properties.inFunc, st.properties.inLoop + 1, st.properties.isSuper))
    
    def comeInBlock(st : SymbolTable):
        return SymbolTable([[]]+st.envs, st.funcprototype, st.properties)
    
    def comeOutLoop(st : SymbolTable):
        return SymbolTable([[]]+st.envs, st.funcprototype, Properties(st.properties.inFunc, st.properties.inLoop - 1, st.properties.isSuper))


    """Turn decl to symbol"""
    def transform(decl : Decl):
        if type(decl) is VarDecl: return VarSym(decl.name, decl.typ)
        if type(decl) is ParamDecl: return ParaSym(decl.name, decl.typ, decl.out, decl.inherit)
        if type(decl) is FuncDecl: return FuncSym(decl.name, decl.return_type, list(map(lambda x: Utils.transform(x), decl.params)), decl.inherit, [])
    
    def findLocal(name : str, st : SymbolTable):
        results = filter(lambda sym: sym.name == name, st.envs[0])
        return next(results, None)
    
    def infer(name : str, typ : Type, st : SymbolTable):
        Utils.find(name, st).typ = typ
        return typ
     
class PreCheck(Visitor):
    
    def __init__(self, ast):
        self.ast = ast
    
    """Visit funcdecls"""
    def visitProgram(self, ast: Program, st: SymbolTable):
        for decl in ast.decls:
            if type(decl) is FuncDecl: 
                st = self.visit(decl, st)
        return st
    
    """Append prototypes"""
    def visitFuncDecl(self, ast : FuncDecl, st : SymbolTable):
        return SymbolTable(st.envs, st.funcprototype + [Utils.transform(ast)], st.properties)
    

class StaticChecker(Visitor):

    def __init__(self, ast):
        self.ast = ast
 
    def check(self):
        return self.visitProgram(self.ast, [])

    def visitIntegerLit(self, ast : IntegerLit, st): return st, IntegerType()

    def visitFloatLit(self, ast : FloatLit, st): return st, FloatType()

    def visitStringLit(self, ast : StringLit, st): return st, StringType()

    def visitBooleanLit(self, ast : BooleanLit, st): return st, BooleanType()

    def visitArrayLit(self, ast : ArrayLit, st : SymbolTable):
        """ All elements must be of the same type and not be AutoType"""
        typ = AutoType()
        for exp in ast.explist:
            st, exptyp = self.visit(exp, st)
            # Element is invalid
            if type(exptyp) is IllegalType: 
                return st, IllegalType()
            elif type(typ) is AutoType: typ = exptyp
            elif type(exptyp) is AutoType: exptyp = Utils.infer(exp.name, typ, st)
            elif type(exp) is not type(exptyp) or type(exp) != type(exptyp): return st, IllegalType()
          
        # All elements are of AutoType       
        if type(typ) is AutoType: return st, IllegalType()    

        # Infer elements
        for exp in ast.explist:
            st, exptyp = self.visit(exp, st)
            if type(exptyp) is AutoType: exptyp.typ = typ     

        # Elements are arrays
        if type(typ) is ArrayType:
            return st, ArrayType([len(ast.explist)] + typ.dimensions, typ.typ)
        return st, ArrayType([len(ast.explist)], typ)

    def visitId(self, ast : Id, st: SymbolTable):
        sym = Utils.findVar(ast.name, st)
        if not sym: 
            raise Undeclared(Identifier(), ast.name)
        if type(sym) not in [VarSym, ParaSym]: raise TypeMismatchInExpression(ast) 
        return st, sym.typ

    def visitArrayCell(self, ast : ArrayCell, st : SymbolTable):
        sym = Utils.findVar(ast.name, st)
        if not sym: 
            raise Undeclared(Identifier(), ast.name)
        if type(sym) not in [VarSym, ParaSym] or type(sym.typ) is not ArrayType: raise TypeMismatchInExpression(ast)

        if len(ast.cell) > len(sym.typ.dimensions): raise TypeMismatchInExpression(ast)

        for idx in ast.cell:
            st, idxtype = self.visit(idx, st)
            if type(idxtype) is AutoType:
                if type(idx) is FuncCall: 
                    Utils.findFunc(idx.name, st).typ = IntegerType()
                else: Utils.findVar(idx.name, st).typ = IntegerType()
            elif type(idxtype) is not IntegerType:
                raise TypeMismatchInExpression(ast)
            
        subdim = sym.typ.dimensions[len(ast.cell):]
        if len(subdim) == 0: return st, sym.typ.typ
        return st, ArrayType(subdim, sym.typ.typ)

    def visitBinExpr(self, ast : BinExpr, st : SymbolTable):
        st, rtype = self.visit(ast.right, st)
        st, ltype = self.visit(ast.left, st)
        
        # One is AutoType, infer the other
        if type(rtype) is AutoType:
            Utils.infer(ast.right.name, ltype, st)
            rtype = ltype
            
        if type(ltype) is AutoType:
            Utils.infer(ast.left.name, rtype, st)
            ltype = rtype

        if ast.op in ["+", "-", "*"]:
            if type(ltype) not in [IntegerType, FloatType] or type(rtype) not in [IntegerType, FloatType]: raise TypeMismatchInExpression(ast)
            if FloatType in [type(ltype), type(rtype)]: return st, FloatType()
            return st, IntegerType()
        elif ast.op == "/":
            if type(rtype) not in [IntegerType, FloatType] or type(ltype) not in [IntegerType, FloatType]: raise TypeMismatchInExpression(ast)
            return st, FloatType()
        elif ast.op == "%":
            if type(rtype) is not IntegerType or type(ltype) is not IntegerType: raise TypeMismatchInExpression(ast)
            return st, IntegerType()
        elif ast.op in ["&&", "||"]:
            if type(rtype) is not BooleanType or type(ltype) is not BooleanType: raise TypeMismatchInExpression(ast)
            return st, BooleanType()
        elif ast.op == "::":
            if type(rtype) is not StringType or type(ltype) is not StringType: raise TypeMismatchInExpression(ast)
            return st, StringType()
        elif ast.op in ["==", "!="]:
            if type(rtype) is not type(ltype): raise TypeMismatchInExpression(ast)
            if ltype not in [IntegerType, BooleanType]: raise TypeMismatchInExpression(ast)
            return st, BooleanType()
        elif ast.op in ["<", ">", "<=", ">="]:
            if type(rtype) not in [IntegerType, FloatType] or type(ltype) not in [IntegerType, FloatType]: raise TypeMismatchInExpression(ast)
            return st, BooleanType()

    def visitUnExpr(self, ast, st):
        st, typ = self.visit(ast.val, st)
        if ast.op == "-":
            if type(typ) is AutoType: 
                typ = Utils.infer(ast.val.name, IntegerType(), st)
            elif type(typ) not in [IntegerType, FloatType]: raise TypeMismatchInExpression(ast)
            return st, typ
        elif ast.op == "!":
            if type(typ) is AutoType: 
                typ = Utils.infer(ast.val.name, BooleanType(), st)
            elif type(typ) is not BooleanType: raise TypeMismatchInExpression(ast)
            return st, BooleanType()

    def visitFuncCall(self, ast: FuncCall, st: SymbolTable):
        # Check if there is callee
        funcsym = Utils.findFunc(ast.name, st)
        if not funcsym: raise Undeclared(Function(), ast.name)
        if type(funcsym.typ) is VoidType: 
            raise TypeMismatchInExpression(ast)

        """ Check its args """
        # Different number of arguments
        if len(funcsym.params) < len(ast.args): 
            raise TypeMismatchInExpression(ast.args[len(funcsym.params)])
        if len(funcsym.params) > len(ast.args): 
            raise TypeMismatchInExpression(ast)

        for i in range(len(funcsym.params)):
            if funcsym.params[i].out and type(ast.args[i]) not in [Id, ArrayCell]:
                raise TypeMismatchInExpression(ast.args[i])
            
        # Infer for param or check param - arg agreements
        for i in range(len(funcsym.params)):
            st, argType = self.visit(ast.args[i], st)
            if type(funcsym.params[i].typ) is AutoType: 
                funcsym.params[i].typ = argType
            elif type(argType) is AutoType:
                Utils.infer(ast.args[i].name, funcsym.params[i].typ, st)
            elif not Utils.isCoercionable(funcsym.params[i].typ, argType): 
                raise TypeMismatchInExpression(ast.args[i])
        return st, funcsym.typ

    def visitAssignStmt(self, ast : AssignStmt, st : SymbolTable):
        st, rtype = self.visit(ast.rhs, st)
        st, ltype = self.visit(ast.lhs, st)

        """Cannot be assigned"""
        if type(ltype) in [VoidType, ArrayType]: raise TypeMismatchInStatement(ast)
        elif type(ltype) is AutoType: Utils.infer(ast.lhs.name, rtype, st)
        elif type(rtype) is AutoType: Utils.infer(ast.rhs.name, ltype, st)
        elif not Utils.isCoercionable(ltype, rtype): 
            raise TypeMismatchInStatement(ast)            
        return st, AssignStmtType()

    def visitIfStmt(self, ast : IfStmt, st : SymbolTable):
        """Check cond"""
        st, condtype = self.visit(ast.cond, st)

        if type(condtype) is AutoType: Utils.infer(ast.cond.name, BooleanType, st)
        if type(condtype) is not BooleanType: raise TypeMismatchInStatement(ast)
        
        newst = Utils.comeInBlock(st)

        newst, _ = self.visit(ast.tstmt, newst)

        if ast.fstmt: newst, _ = self.visit(ast.fstmt, newst)

        return st, IfStmtType()

    def visitForStmt(self, ast : ForStmt, st : SymbolTable):
        """ Visit assign statement to infer if there is any"""
        st, _ = self.visit(ast.init, st)
        st, lhs = self.visit(ast.init.lhs, st)
        st, rhs = self.visit(ast.init.rhs, st)

        if type(rhs) is not IntegerType or type(lhs) is not IntegerType: raise TypeMismatchInStatement(ast)
        """ Make sure cond is BooleanType"""
        st, condType = self.visit(ast.cond, st)
        if type(condType) is AutoType: Utils.infer(ast.cond.name, BooleanType, st)
        if type(condType) is not BooleanType: raise TypeMismatchInStatement(ast)
        
        """Make sure upd is IntegerType"""
        st, updType = self.visit(ast.upd, st)
        if type(updType) is not IntegerType: raise TypeMismatchInStatement(ast)

        """Pass infor before visiting child stmt"""
        st, _ = self.visit(ast.stmt, Utils.comeInLoop(st))
        return Utils.comeOutLoop(st), LoopStmtType()

    def visitWhileStmt(self, ast : WhileStmt, st : SymbolTable):
        st, condType = self.visit(ast.cond, st)
        if type(condType) is AutoType: Utils.infer(ast.cond.name, BooleanType, st)
        if type(condType) is not BooleanType: raise TypeMismatchInStatement(ast)
        
        st, _ = self.visit(ast.stmt, Utils.comeInLoop(st))
        return Utils.comeOutLoop(st), LoopStmtType()

    def visitDoWhileStmt(self, ast, st):
        st, condType = self.visit(ast.cond, st)

        if type(condType) is AutoType: Utils.infer(ast.cond.name, BooleanType, st)
        if type(condType) is not BooleanType: 
            raise TypeMismatchInStatement(ast)
        
        st, _ = self.visit(ast.stmt, Utils.comeInLoop(st))
        return Utils.comeOutLoop(st), LoopStmtType()
    
    def visitBreakStmt(self, ast : BreakStmt, st : SymbolTable):
        if st.properties.inLoop == 0:
            raise MustInLoop(ast)
        return st, MustInLoopStmtType()

    def visitContinueStmt(self, ast : ContinueStmt, st : SymbolTable):
        if st.properties.inLoop == 0:
            raise MustInLoop(ast)
        return st, MustInLoopStmtType()

    def visitReturnStmt(self, ast : ReturnStmt, st : SymbolTable):
        if not st.properties.inFunc: InvalidStatementInFunction(ast)

        if ast.expr is not None:
            st, exprtyp =  self.visit(ast.expr, st)
            """ Return type of the return statement expression"""
            # Compare and update return type
            if type(st.properties.inFunc.typ) is AutoType: 
                st.properties.inFunc.typ = exprtyp
            elif not Utils.isCoercionable(st.properties.inFunc.typ, exprtyp):
                raise TypeMismatchInStatement(ast) 
        else: 
            if type(st.properties.inFunc.typ) is AutoType: st.properties.inFunc.typ = VoidType()
            elif type(st.properties.inFunc.typ) is not VoidType: raise TypeMismatchInStatement(ast)

        return st, ReturnStmt()         

    def visitCallStmt(self, ast : CallStmt, st : SymbolTable):
        
        # Check if there is callee
        funcsym = Utils.findFunc(ast.name, st)
        if not funcsym: raise Undeclared(Function(), ast.name)
        if type(funcsym) is not FuncSym: 
            raise TypeMismatchInStatement(ast)
        if st.properties.isSuper: ast.name = 'super'
        """ Check its args """
        # Different number of arguments
        if ast.name != "super" and len(funcsym.params) != len(ast.args):
            raise TypeMismatchInStatement(ast)
        
        if len(funcsym.params) < len(ast.args): 
            raise TypeMismatchInExpression(ast.args[len(funcsym.params)])
        if len(funcsym.params) > len(ast.args): 
            raise TypeMismatchInExpression(None)

        # Out but not LHS
        for i in range(len(funcsym.params)):
            if funcsym.params[i].out and type(ast.args[i]) not in [Id, ArrayCell]:
                if ast.name != "super":
                    raise TypeMismatchInStatement(ast)
                raise TypeMismatchInExpression(ast.args[i])

        # Infer for param or check param - arg agreements
        for i in range(len(funcsym.params)):
            _, argType = self.visit(ast.args[i], st)
            if type(funcsym.params[i].typ) is AutoType: 
                funcsym.params[i].typ = argType
            elif type(argType) is AutoType:
                Utils.infer(ast.args[i].name, funcsym.params[i].typ, st)
            elif not Utils.isCoercionable(funcsym.params[i].typ, argType): 
                if ast.name != "super": raise TypeMismatchInStatement(ast)
                raise TypeMismatchInExpression(ast.args[i])
        return st, CallStmtType()
    
    def visitBlockStmt(self, ast : BlockStmt, st : SymbolTable):
        for ele in ast.body:
            # Ignore super or preventDefault
            if type(ele) is CallStmt and ele.name in ['super', 'preventDefault']: continue
            st, _ = self.visit(ele, st)
            if type(ele) is ReturnStmt: break
            
        return st, BlockStmtType()

    def visitVarDecl(self, ast: VarDecl, st: SymbolTable):
        """Check if there is the same name in scope 0"""
        if len(list(filter(lambda sym: sym.name == ast.name, st.envs[0]))) > 0: raise Redeclared(Variable(), ast.name)                
        
        """Check semantics"""
        # There is no init
        if not ast.init:
            if type(ast.typ) is AutoType: raise Invalid(Variable(), ast.name)
        # There is init
        else:
            st, inityp = self.visit(ast.init, st)
            st = Utils.addSym(VarSym(ast.name, ast.typ), st)

            if type(inityp) is IllegalType: raise IllegalArrayLiteral(ast.init)
            if type(ast.typ) is AutoType and type(inityp) is AutoType: 
                raise TypeMismatchInVarDecl(ast) 

            if type(ast.typ) is AutoType:
                ast.typ = Utils.infer(ast.name, inityp, st)
                """This is a function or parameter"""
            elif type(inityp) is AutoType:
                Utils.infer(ast.init.name, ast.typ, st)
            elif not Utils.isCoercionable(ast.typ, inityp): 
                raise TypeMismatchInVarDecl(ast)
        return Utils.addSym(VarSym(ast.name, ast.typ), st), DeclType()

    def visitParamDecl(self, ast: ParamDecl, st: SymbolTable): pass
    
    def visitFuncDecl(self, ast: FuncDecl, st: SymbolTable):
        # If there is already the same name, raise
        for sym in st.envs[0]:
            if sym.name == ast.name:
                raise Redeclared(Function(), ast.name)
        
        # Find its prototype in global scope
        for funcsym in st.funcprototype:
            if funcsym.name == ast.name:
                st = Utils.addSym(funcsym, st)
                break
        
        # Access this function
        funcsym = st.envs[0][0]
        
        """Create a new scope"""
        newst = Utils.comeInFunc(st, funcsym)

        """ If this function inherits """
        if ast.inherit:
            # Find its parent, if there is not raise Undeclared
            parentsym = Utils.findFunc(ast.inherit, st)
            if not parentsym: raise Undeclared(Function(), ast.inherit)
            """ Append its parent's inherit params into scope 0 """
            for parentparam in parentsym.params:
                if parentparam.inherit:
                    newst = Utils.addSym(parentparam, newst)
            """ Traverse its params """
            # If same name as parent's raise Invalid
            for param in funcsym.params:
                if Utils.findLocal(param.name, newst): 
                    raise Invalid(Parameter(), param.name)
                
            # If same nams as its own raise Redeclared
            for param in funcsym.params:
                if Utils.findVar(param.name, newst): 
                    raise Redeclared(Parameter(), param.name)
                newst = Utils.addSym(param, newst)
        
            """Traverse first statement"""
            # Nothing or not in ['prevendefaut', 'super'], does not have name 
            if len(ast.body.body) == 0 or not hasattr(ast.body.body[0], 'name') or ast.body.body[0].name not in ['preventDefault', 'super']: 
                if len(parentsym.params) != 0: raise TypeMismatchInExpression(None)
            elif ast.body.body[0].name == 'super':
                newst.properties.isSuper = True
                newst, _ = self.visit(CallStmt(parentsym.name, ast.body.body[0].args), newst)
        else:
            """Traverse its own params"""
            for param in funcsym.params:
                if Utils.findLocal(param.name, newst): raise Redeclared(Parameter(), param.name)
                newst = Utils.addSym(param, newst)
            
            if len(ast.body.body) > 0 and type(ast.body.body[0]) is CallStmt and ast.body.body[0].name in ['preventDefault', 'super']:
                raise InvalidStatementInFunction(ast.name)            

        """Traverse its body"""
        newst, _ = self.visit(ast.body, newst)
        return st, DeclType()

    def visitProgram(self, ast : Program, st : SymbolTable):
        st = SymbolTable()
        st = PreCheck(ast).visit(ast, st)

        for decl in ast.decls:
            st, _ = self.visit(decl, st)
        
        hasMain = False
        for funcsym in st.funcprototype:
            if funcsym.name == 'main' and funcsym.params == [] and type(funcsym.typ) is VoidType:
                hasMain = True
        if not hasMain: raise NoEntryPoint()