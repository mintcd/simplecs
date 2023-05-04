from functools import reduce

class IntType: pass
class Symbol: 
    def __init__(self, name, typ, val, params = None):
        self.name = name
        self.typ = typ
        self.val = val
        self.params = params
        self.isFunction = True if params else False

class STManipulator:
    def append(st, decl):
        if type(decl) is VarDecl: 
            st[0].append(Symbol(decl.name, decl.typ, None))
        elif type(decl) is ConstDecl : 
            st[0].append(Symbol(decl.name, None, decl.val))
        else: st[0].append(Symbol(decl.name, None, None, decl.param))
        
    def contains(st, name):
        for scope in st:
            for sym in scope:
                if sym.name == name: return True
        return False
        
    def containslocal(st, name):
        for sym in st[0]:
            if sym.name == name: return True
        return False
    
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,st:object):
        reduce(lambda st, decl: self.visit(decl, st), ctx.decl, [[]])

    def visitVarDecl(self,ctx:VarDecl,st):
        if STManipulator.containslocal(st,ctx.name): 
            raise RedeclaredVariable(ctx.name)
        STManipulator.append(st, ctx)
        return st

    def visitConstDecl(self,ctx:ConstDecl,st:object):
        if STManipulator.containslocal(st,ctx.name):  
            raise RedeclaredConstant(ctx.name)
        STManipulator.append(st, ctx)
        return st
        
    def visitFuncDecl(self,ctx:FuncDecl,st:object):
        if STManipulator.containslocal(st,ctx.name):
            raise RedeclaredFunction(ctx.name)
        
        STManipulator.append(st, ctx)
        
        subst = [[]] + st
        subst = reduce(lambda _, param: self.visit(param,_), ctx.param, subst)
        subst = reduce(lambda _, decl: self.visit(decl,_), ctx.body[0], subst)
        
        for expr in ctx.body[1]: self.visit(expr, subst)
            
        return st
        
    def visitId(self,ctx:Id,st):
        if not STManipulator.contains(st, ctx.name): raise UndeclaredIdentifier(ctx.name)
        return st

    def visitIntLit(self,ctx:IntLit,st:object): return IntType()