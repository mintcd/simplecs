import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test22(self):
        input = """
        main: function void() {
            a,b,c: auto = 1,"Hell",{{1,2},{21,7},{16,4}};
            writeFloat(a);
            b = readString();
            writeFloat(a);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, IntegerLit(1)), VarDecl(b, AutoType, StringLit(Hell)), VarDecl(c, AutoType, ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(21), IntegerLit(7)]), ArrayLit([IntegerLit(16), IntegerLit(4)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

#     def test_simple_program_2(self):
#         input = """x, y, z: integer = 1, 2, 3;"""
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(1))
# 	VarDecl(y, IntegerType, IntegerLit(2))
# 	VarDecl(z, IntegerType, IntegerLit(3))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 301))

#     def test_simple_program_3(self):
#         input = """x, y, z: integer = 1, 2, 3;
#             a, b: float;"""
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(1))
# 	VarDecl(y, IntegerType, IntegerLit(2))
# 	VarDecl(z, IntegerType, IntegerLit(3))
# 	VarDecl(a, FloatType)
# 	VarDecl(b, FloatType)
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 302))

#     def test_simple_program_4(self):
#         input = """main: function void () {
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 303))

#     def test_simple_program_5(self):
#         input = """main: function void (a:integer) {
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(a, IntegerType)], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 304))

#     def test_simple_program_6(self):
#         input = """main: function void () {
#             printInteger(4);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 305))
    
#     def test_simple_program_7(self):
#         input = """main: function void () {
#             a: integer;
#             b:float;
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, FloatType)]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 306))

#     def test_simple_program_8(self):
#         input = """main: function void () {
#             printInteger(4);
#             b:float;

#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4)), VarDecl(b, FloatType)]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 307))

#     def test_simple_program_9(self):
#         input = """main: function void () {
#             printInteger(4);
#             a: array [1,2] of integer;

#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4)), VarDecl(a, ArrayType([1, 2], IntegerType))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 308))

#     def test_simple_program_10(self):
#         input = """a,b,c: auto = x == y, {x * y - z, (x + y) * z / (x - y)}, "Hello " :: "World!" ;"""
#         expect = """Program([
# 	VarDecl(a, AutoType, BinExpr(==, Id(x), Id(y)))
# 	VarDecl(b, AutoType, ArrayLit([BinExpr(-, BinExpr(*, Id(x), Id(y)), Id(z)), BinExpr(/, BinExpr(*, BinExpr(+, Id(x), Id(y)), Id(z)), BinExpr(-, Id(x), Id(y)))]))
# 	VarDecl(c, AutoType, BinExpr(::, StringLit(Hello ), StringLit(World!)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 309))

#     def test_funcdecl_11(self):
#         input = """
#         main: function void(){
#             //a:integer;
#         }
#         func: function void(a:array [10] of integer,arr: string){
#             return 0;
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# 	FuncDecl(func, VoidType, [Param(a, ArrayType([10], IntegerType)), Param(arr, StringType)], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 310))

#     def test_funcdecl_12(self):
#         input = """
#         main: function void(){
#             //a:integer;
#         }
#         func: function void(a:array [7] of integer,arr: string){
#             return 0;
#         }
#         test: function integer(input: array [13] of float,a:integer,c: array [10] of string,d:boolean){
#             a, b, c:integer;
#             // Comment
#             // int c;
#             return a;
#         }
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# 	FuncDecl(func, VoidType, [Param(a, ArrayType([7], IntegerType)), Param(arr, StringType)], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
# 	FuncDecl(test, IntegerType, [Param(input, ArrayType([13], FloatType)), Param(a, IntegerType), Param(c, ArrayType([10], StringType)), Param(d, BooleanType)], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType), ReturnStmt(Id(a))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 311))

#     def test_funcdecl_13(self):
#         input = """test: function void (a: integer,b:integer){
#                 x:integer = 1+2*4+7;
#             }"""
#         expect = """Program([
# 	FuncDecl(test, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([VarDecl(x, IntegerType, BinExpr(+, BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(2), IntegerLit(4))), IntegerLit(7)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 312))

#     def test_funcdecl_14(self):
#         input = """swap: function void (a: integer,b:integer){
#                 temp: integer =a;
#                 a=b;
#                 b=temp;
#             }"""
#         expect = """Program([
# 	FuncDecl(swap, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([VarDecl(temp, IntegerType, Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(temp))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 313))

#     def test_block_stmt_15(self):
#         input = """main: function void (){
#                     {a, b:integer = 2,3;
#                         {
#                             c, d:integer = 2,3;
#                         }
#                     }
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(a, IntegerType, IntegerLit(2)), VarDecl(b, IntegerType, IntegerLit(3)), BlockStmt([VarDecl(c, IntegerType, IntegerLit(2)), VarDecl(d, IntegerType, IntegerLit(3))])])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 314))

#     def test_block_stmt_16(self):
#         input = """main: function void (){
#                     {a, b:integer = 2,3;
#                         {
#                             c, d:integer = 2,3;
#                         }
#                     }
#                     {a, b:integer = 2,3;
#                     }
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(a, IntegerType, IntegerLit(2)), VarDecl(b, IntegerType, IntegerLit(3)), BlockStmt([VarDecl(c, IntegerType, IntegerLit(2)), VarDecl(d, IntegerType, IntegerLit(3))])]), BlockStmt([VarDecl(a, IntegerType, IntegerLit(2)), VarDecl(b, IntegerType, IntegerLit(3))])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 315))

#     def test_block_stmt_17(self):
#         input = """main: function void (){
#            {
#                 {
#                     {
#                         {
#                             {
#                                 t:integer;
#                                 {
#                                     return 0;
#                                 }
#                                 a = 1+2;
#                             }
#                         }
#                     }
#                 }
#             }
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([VarDecl(t, IntegerType), BlockStmt([ReturnStmt(IntegerLit(0))]), AssignStmt(Id(a), BinExpr(+, IntegerLit(1), IntegerLit(2)))])])])])])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 316))

#     def test_block_stmt_18(self):
#         input = """main: function void (){
#                     {}
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 317))

#     def test_ifstmt_19(self):
#         input = """main: function void(){
#             if (isPrime(n)) {
#                 if (n > 999) flag = true; //check if n > 999
#                 else {
#                     n = 3 + n * 7;
#                     printInteger(n);
#                 }
#             }
#             else printString("n isn\\'t a prime number!");
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(FuncCall(isPrime, [Id(n)]), BlockStmt([IfStmt(BinExpr(>, Id(n), IntegerLit(999)), AssignStmt(Id(flag), BooleanLit(True)), BlockStmt([AssignStmt(Id(n), BinExpr(+, IntegerLit(3), BinExpr(*, Id(n), IntegerLit(7)))), CallStmt(printInteger, Id(n))]))]), CallStmt(printString, StringLit(n isn\\'t a prime number!)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 318))

#     def test_ifstmt_20(self):
#         input = """main: function void(){
#             if (t == 1) {
#                 if (a  < 1) a = 2;
#                 else k = foo(a);
#             }
#             else k = foo(a - 1);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(t), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(k), FuncCall(foo, [Id(a)])))]), AssignStmt(Id(k), FuncCall(foo, [BinExpr(-, Id(a), IntegerLit(1))])))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 319))

#     def test_ifstmt_21(self):
#         input = """main: function void(){
#             if (a == 1) k = foo(a-1);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(k), FuncCall(foo, [BinExpr(-, Id(a), IntegerLit(1))])))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 320))

#     def test_ifstmt_22(self):
#         input = """main: function void(){
#             if (flag == 0) x = 5;
#             else if (flag == 1) x = 6;
#             else x = 7;
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(flag), IntegerLit(0)), AssignStmt(Id(x), IntegerLit(5)), IfStmt(BinExpr(==, Id(flag), IntegerLit(1)), AssignStmt(Id(x), IntegerLit(6)), AssignStmt(Id(x), IntegerLit(7))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 321))

#     def test_ifstmt_23(self):
#         input = """fibonacci: function integer (n: integer){
#                     if( n == -1 )
#                         if ( n == 0 )
#                             return 1;
#                     return fibonacci(n-1)+ fibonacci(n+1);
#                 }"""
#         expect = """Program([
# 	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), UnExpr(-, IntegerLit(1))), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)))), ReturnStmt(BinExpr(+, FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibonacci, [BinExpr(+, Id(n), IntegerLit(1))])))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 322))

#     def test_forstmt_24(self):
#         input = """main: function void (){
#                 for (i = 0, i < 10,i+1) printInteger(i);
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, Id(i)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 323))

#     def test_forstmt_25(self):
#         input = """main: function void (){
#                 for (i = 0, i < 10,i+1) a = a+2;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 324))

#     def test_forstmt_26(self):
#         input = """main: function void (){
#                     for (i = 0, i < 10,i+1) {
#                         a=a+2;
#                     }
#                     printInteger(a);
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2)))])), CallStmt(printInteger, Id(a))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 325))

#     def test_forstmt_27(self):
#         input = """main: function void (){
#                     for (i = 0, i<10 ,i+1)
#                         for (j=0,j<i,j+1) sum = sum + 1;

#                     printInteger(sum);
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(i)), BinExpr(+, Id(j), IntegerLit(1)), AssignStmt(Id(sum), BinExpr(+, Id(sum), IntegerLit(1))))), CallStmt(printInteger, Id(sum))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 326))

#     def test_forstmt_28(self):
#         input = """main: function void (){
#                     for (i = 0,i<10 ,i+1) {
#                         a=a+2;
#                     }
#                     printInteger(a);
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2)))])), CallStmt(printInteger, Id(a))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 327))

#     def test_whilestmt_29(self):
#         input = """main: function void (){
#                     while(x<9) a = a + 1;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(9)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 328))

#     def test_whilestmt_30(self):
#         input = """main: function void (){
#                     while(x<9){
#                         a = a + 1;
#                         _ = !x || (y == 0) && (z > 12.5E-6);
#                     }
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(9)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(_), BinExpr(&&, BinExpr(||, UnExpr(!, Id(x)), BinExpr(==, Id(y), IntegerLit(0))), BinExpr(>, Id(z), FloatLit(1.25e-05))))]))]))
# ])"""

#         self.assertTrue(TestAST.test(input, expect, 329))

#     def test_dowhilestmt_31(self):
#         input = """main: function void (){
#             do {
#                 x = x + 3;
#             } while (true);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(3)))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 330))

#     def test_dowhilestmt_32(self):
#         input = """main: function void (){
#             do {
#                 x = x + 3;
#                 i = i + 1;
#             } while (i<3);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(3))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 331))

#     def test_dowhilestmt_33(self):
#         input = """main: function void (){
#             k,c: integer;
#             do{
#                 do{
#                     c: array [3] of integer;
#                 } while (x < 4);
#             } while (k == 0);
#             return 0;
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(k, IntegerType), VarDecl(c, IntegerType), DoWhileStmt(BinExpr(==, Id(k), IntegerLit(0)), BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(4)), BlockStmt([VarDecl(c, ArrayType([3], IntegerType))]))])), ReturnStmt(IntegerLit(0))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 332))

#     def test_dowhilestmt_34(self):
#         input = """main: function void (){
#             do{
#                 a = 3;
#                 foo:array [3] of integer;
#                 do{
#                     do{
#                         do{
#                             x = x + 1;
#                         }while (9);
#                     } while (x + 1 > 0);
#                 } while (x == 3);
#             } while (z < -3);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(z), UnExpr(-, IntegerLit(3))), BlockStmt([AssignStmt(Id(a), IntegerLit(3)), VarDecl(foo, ArrayType([3], IntegerType)), DoWhileStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([DoWhileStmt(BinExpr(>, BinExpr(+, Id(x), IntegerLit(1)), IntegerLit(0)), BlockStmt([DoWhileStmt(IntegerLit(9), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))]))]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 333))

#     def test_dowhilestmt_35(self):
#         input = """main: function void (){
#             do {
#             } while (true);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 334))

#     def test_breakstmt_36(self):
#         input = """main: function void(){
#             for(i =0, i<10 , i+1) {
#                   if(!a){
#                     flag=true;
#                     break;
#                 }
#             }

#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(UnExpr(!, Id(a)), BlockStmt([AssignStmt(Id(flag), BooleanLit(True)), BreakStmt()]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 335))

#     def test_continuestmt_37(self):
#         input = """main: function void(){
#              for(i =0, i<10 , i+1) {
#                     if(!a){
#                         flag=true;
#                         continue;
#                     }
#                 }
#             }

#              """

#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(UnExpr(!, Id(a)), BlockStmt([AssignStmt(Id(flag), BooleanLit(True)), ContinueStmt()]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 336))

#     def test_continuestmt_38(self):
#         input = """main: function void(){
#              for(i =0, i<10 , i+1) {
#                    if(!a){
#                     flag=true;
#                     continue;
#                 }
#                 else break;
#                 }
#             }

#              """

#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(UnExpr(!, Id(a)), BlockStmt([AssignStmt(Id(flag), BooleanLit(True)), ContinueStmt()]), BreakStmt())]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 337))

#     def test_returnstmt_39(self):
#         input = """main: function integer (){
#                     return 0;
#                 }
#                 """
#         expect = """Program([
# 	FuncDecl(main, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 338))

#     def test_returnstmt_40(self):
#         input = """main: function void (){
#                     return;
#                 }
#                 """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 339))

#     def test_returnstmt_41(self):
#         input = """main: function integer (a:integer, b: integer){
#                     if(a>1) return a;
#                     else if (a<1) return b;
#                     else return 1;
#                 }
#                 """
#         expect = """Program([
# 	FuncDecl(main, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(1)), ReturnStmt(Id(a)), IfStmt(BinExpr(<, Id(a), IntegerLit(1)), ReturnStmt(Id(b)), ReturnStmt(IntegerLit(1))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 340))

#     def test_variable_42(self):
#         input = """a:integer;
#         b:array [2,3] of integer ;
#         _flag: boolean;"""
#         expect = """Program([
# 	VarDecl(a, IntegerType)
# 	VarDecl(b, ArrayType([2, 3], IntegerType))
# 	VarDecl(_flag, BooleanType)
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 341))

#     def test_variable_43(self):
#         input = """main: function void (){
#             a, b: integer;
#             a = 3;
#             b = 5;
#             a = (6 - 5 * (b % a));
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), AssignStmt(Id(a), IntegerLit(3)), AssignStmt(Id(b), IntegerLit(5)), AssignStmt(Id(a), BinExpr(-, IntegerLit(6), BinExpr(*, IntegerLit(5), BinExpr(%, Id(b), Id(a)))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 342))

#     def test_variable_44(self):
#         input = """a: float;
#         b: array [2] of integer;
#         main: function void (){
#             c : integer;
#             a = a * b[0] + (a - 3) * b[1];
#         }"""
#         expect = """Program([
# 	VarDecl(a, FloatType)
# 	VarDecl(b, ArrayType([2], IntegerType))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(c, IntegerType), AssignStmt(Id(a), BinExpr(+, BinExpr(*, Id(a), ArrayCell(b, [IntegerLit(0)])), BinExpr(*, BinExpr(-, Id(a), IntegerLit(3)), ArrayCell(b, [IntegerLit(1)]))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 343))

#     def test_variable_45(self):
#         input = """main: function void (){
#             a: array [5] of integer;
#             return (a[0] && (a[1] >= a[2])) || (a[3] != a[4]);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType)), ReturnStmt(BinExpr(||, BinExpr(&&, ArrayCell(a, [IntegerLit(0)]), BinExpr(>=, ArrayCell(a, [IntegerLit(1)]), ArrayCell(a, [IntegerLit(2)]))), BinExpr(!=, ArrayCell(a, [IntegerLit(3)]), ArrayCell(a, [IntegerLit(4)]))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 344))

#     def test_variable_46(self):
#         input = """main: function void (){
#             a: string;
#             s = "1" + "2";
#             return s;
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType), AssignStmt(Id(s), BinExpr(+, StringLit(1), StringLit(2))), ReturnStmt(Id(s))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 345))

#     def test_variable_47(self):
#         input = """fact: function integer (arr: array [1] of integer){
#             return arr[arr[arr[0]]] % 3 == 0;
#         }
#         """
#         expect = """Program([
# 	FuncDecl(fact, IntegerType, [Param(arr, ArrayType([1], IntegerType))], None, BlockStmt([ReturnStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [ArrayCell(arr, [ArrayCell(arr, [IntegerLit(0)])])]), IntegerLit(3)), IntegerLit(0)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 346))

#     def test_function_48(self):
#         input = """find_gcd:function integer(n1: integer,n2: integer)
#         {
#             if (n2 != 0)
#             return find_gcd(n2, n1%n2);
#             else return n1;
#         }"""
#         expect = """Program([
# 	FuncDecl(find_gcd, IntegerType, [Param(n1, IntegerType), Param(n2, IntegerType)], None, BlockStmt([IfStmt(BinExpr(!=, Id(n2), IntegerLit(0)), ReturnStmt(FuncCall(find_gcd, [Id(n2), BinExpr(%, Id(n1), Id(n2))])), ReturnStmt(Id(n1)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 347))

#     def test_function_49(self):
#         input = """sumArray:function integer(n1: array [100] of integer,n2: integer){
#             i, sum: integer;
#             sum = 0;
#             for (i = 0, i < n2, i + 1) {
#                 sum = sum + n1[i];
#             }
#             return sum;
#         }"""
#         expect = """Program([
# 	FuncDecl(sumArray, IntegerType, [Param(n1, ArrayType([100], IntegerType)), Param(n2, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(sum, IntegerType), AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(n1, [Id(i)])))])), ReturnStmt(Id(sum))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 348))

#     def test_function_50(self):
#         input = """isPrime:function boolean(n: integer){
#             i, flag: integer;
#             for(i=2, i <= n/2, i+1){
#                 if (n % i == 0)
#                 {
#                     flag = 0;
#                     break;
#                 }
#             }
#             return flag;
#         }"""
#         expect = """Program([
# 	FuncDecl(isPrime, BooleanType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(flag, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(Id(flag), IntegerLit(0)), BreakStmt()]))])), ReturnStmt(Id(flag))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 349))

#     def test_function_51(self):
#         input = """main:function void() {
#             n: integer;
#             readInteger(n);
#             for ( k = 0, k <= n, k+1) {
#                 tuso = 2 * (k + 1);
#                 mau1 = 1 + 2 * k;
#                 mau2 = 3 + 2 * k;
#                 nhantu = tuso * tuso / (mau1*mau2);
#                 sum = sum * nhantu;
#             }
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(readInteger, Id(n)), ForStmt(AssignStmt(Id(k), IntegerLit(0)), BinExpr(<=, Id(k), Id(n)), BinExpr(+, Id(k), IntegerLit(1)), BlockStmt([AssignStmt(Id(tuso), BinExpr(*, IntegerLit(2), BinExpr(+, Id(k), IntegerLit(1)))), AssignStmt(Id(mau1), BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(2), Id(k)))), AssignStmt(Id(mau2), BinExpr(+, IntegerLit(3), BinExpr(*, IntegerLit(2), Id(k)))), AssignStmt(Id(nhantu), BinExpr(/, BinExpr(*, Id(tuso), Id(tuso)), BinExpr(*, Id(mau1), Id(mau2)))), AssignStmt(Id(sum), BinExpr(*, Id(sum), Id(nhantu)))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 350))

#     def test_function_52(self):
#         input = """/*This is a program*/
#         main:function void() {
#             n, i: integer;
#             n = 100;
#             for (i = 0, true, i + 1)
#             {
#                 n = n - i;
#                 if (n < i) break;
#             }
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), VarDecl(i, IntegerType), AssignStmt(Id(n), IntegerLit(100)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BooleanLit(True), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(n), BinExpr(-, Id(n), Id(i))), IfStmt(BinExpr(<, Id(n), Id(i)), BreakStmt())]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 351))

#     def test_function_53(self):
#         input = """/*This is a program*/
#         flag: boolean;
#         round:function integer (a:float){}
#         main:function void() {
#             number: float;
#             flag=true;
#             do {
#                 number = random(1, 200) / 10;
#                 if (number == round(number)) flag = false;
#             } while (flag);
#             writeFloat(number);
#         }"""
#         expect = """Program([
# 	VarDecl(flag, BooleanType)
# 	FuncDecl(round, IntegerType, [Param(a, FloatType)], None, BlockStmt([]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(number, FloatType), AssignStmt(Id(flag), BooleanLit(True)), DoWhileStmt(Id(flag), BlockStmt([AssignStmt(Id(number), BinExpr(/, FuncCall(random, [IntegerLit(1), IntegerLit(200)]), IntegerLit(10))), IfStmt(BinExpr(==, Id(number), FuncCall(round, [Id(number)])), AssignStmt(Id(flag), BooleanLit(False)))])), CallStmt(writeFloat, Id(number))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 352))

#     def test_function_54(self):

#         input = """test: function integer () {
#             while (true)
#                 while (true)
#                     while (true) a= a-1;
#         }"""
#         expect = """Program([
# 	FuncDecl(test, IntegerType, [], None, BlockStmt([WhileStmt(BooleanLit(True), WhileStmt(BooleanLit(True), WhileStmt(BooleanLit(True), AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1))))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 353))

#     def test_function_55(self):

#         input = """test: function integer () {
#             do {
#                 do {
#                 }
#                 while (a>=abc);
#             }
#             while (a<-2);
#         }"""
#         expect = """Program([
# 	FuncDecl(test, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), UnExpr(-, IntegerLit(2))), BlockStmt([DoWhileStmt(BinExpr(>=, Id(a), Id(abc)), BlockStmt([]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 354))

#     def test_vardecl_56(self):
#         input = """a, b, c: integer;
#         x, y: boolean;"""
#         expect = """Program([
# 	VarDecl(a, IntegerType)
# 	VarDecl(b, IntegerType)
# 	VarDecl(c, IntegerType)
# 	VarDecl(x, BooleanType)
# 	VarDecl(y, BooleanType)
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 355))

#     def test_vardecl_57(self):
#         input = """a, b:integer = 2,3;"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, IntegerLit(2))
# 	VarDecl(b, IntegerType, IntegerLit(3))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 356))

#     def test_vardecl_58(self):
#         input = """a, b,c,d:float = 2.1,3E10-2,4.0,5.4;"""
#         expect = """Program([
# 	VarDecl(a, FloatType, FloatLit(2.1))
# 	VarDecl(b, FloatType, BinExpr(-, FloatLit(30000000000.0), IntegerLit(2)))
# 	VarDecl(c, FloatType, FloatLit(4.0))
# 	VarDecl(d, FloatType, FloatLit(5.4))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 357))

#     def test_vardecl_59(self):
#         input = """a, b,c,d:auto = "hi",1,_,2.10E3;"""
#         expect = """Program([
# 	VarDecl(a, AutoType, StringLit(hi))
# 	VarDecl(b, AutoType, IntegerLit(1))
# 	VarDecl(c, AutoType, Id(_))
# 	VarDecl(d, AutoType, FloatLit(2100.0))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 358))

#     def test_vardecl_60(self):
#         input = """a, b,c,d: array [2,3] of integer ;"""
#         expect = """Program([
# 	VarDecl(a, ArrayType([2, 3], IntegerType))
# 	VarDecl(b, ArrayType([2, 3], IntegerType))
# 	VarDecl(c, ArrayType([2, 3], IntegerType))
# 	VarDecl(d, ArrayType([2, 3], IntegerType))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 359))

#     def test_vardecl_61(self):
#         input = """a,b,c: string = 1 ,2 ,3;"""
#         expect = """Program([
# 	VarDecl(a, StringType, IntegerLit(1))
# 	VarDecl(b, StringType, IntegerLit(2))
# 	VarDecl(c, StringType, IntegerLit(3))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 360))

#     def test_idxOperator_62(self):
#         input = """main: function void (a:integer) {
#             a[1*-3 == 3] = 1 >= !abc[-10];
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(==, BinExpr(*, IntegerLit(1), UnExpr(-, IntegerLit(3))), IntegerLit(3))]), BinExpr(>=, IntegerLit(1), UnExpr(!, ArrayCell(abc, [UnExpr(-, IntegerLit(10))]))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 361))

#     def test_idxOperator_63(self):
#         input = """main: function void (a:integer) {
#             c[3+x] = a[b[2]] + 3;
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(c, [BinExpr(+, IntegerLit(3), Id(x))]), BinExpr(+, ArrayCell(a, [ArrayCell(b, [IntegerLit(2)])]), IntegerLit(3)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 362))

#     def test_idxOperator_64(self):
#         input = """main: function void (a:integer) {
#             sum = foo[5 * foo()] - !tran[5 % tran()] + -foo(a[3*b[c]]);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(Id(sum), BinExpr(+, BinExpr(-, ArrayCell(foo, [BinExpr(*, IntegerLit(5), FuncCall(foo, []))]), UnExpr(!, ArrayCell(tran, [BinExpr(%, IntegerLit(5), FuncCall(tran, []))]))), UnExpr(-, FuncCall(foo, [ArrayCell(a, [BinExpr(*, IntegerLit(3), ArrayCell(b, [Id(c)]))])]))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 363))

#     def test_idxOperator_65(self):
#         input = """main: function void (a:integer) {
#             test = arr[1 + foo()] - arr[1 + arr[1]];
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(Id(test), BinExpr(-, ArrayCell(arr, [BinExpr(+, IntegerLit(1), FuncCall(foo, []))]), ArrayCell(arr, [BinExpr(+, IntegerLit(1), ArrayCell(arr, [IntegerLit(1)]))])))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 364))

#     def test_idxOperator_66(self):
#         input = """main: function void (a:integer) {
#             test[1 + 4*a[3]]  = 3 * 2;
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(test, [BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(4), ArrayCell(a, [IntegerLit(3)])))]), BinExpr(*, IntegerLit(3), IntegerLit(2)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 365))

#     def test_idxOperator_67(self):
#         input = """main: function void (a:integer) {
#             t: float;
#             t = a + b[1 + 3];
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(a, IntegerType)], None, BlockStmt([VarDecl(t, FloatType), AssignStmt(Id(t), BinExpr(+, Id(a), ArrayCell(b, [BinExpr(+, IntegerLit(1), IntegerLit(3))])))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 366))

#     def test_idxOperator_68(self):
#         input = """main: function void (a:integer) {
#             trend: string;
#             trend = (foo(1) + foo(2))+v[1 + 9];
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(a, IntegerType)], None, BlockStmt([VarDecl(trend, StringType), AssignStmt(Id(trend), BinExpr(+, BinExpr(+, FuncCall(foo, [IntegerLit(1)]), FuncCall(foo, [IntegerLit(2)])), ArrayCell(v, [BinExpr(+, IntegerLit(1), IntegerLit(9))])))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 367))

#     def test_idxOperator_69(self):
#         input = """main: function void (a:integer) {
#             n: array [6] of float;
#             n = foo(v[-3]);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(a, IntegerType)], None, BlockStmt([VarDecl(n, ArrayType([6], FloatType)), AssignStmt(Id(n), FuncCall(foo, [ArrayCell(v, [UnExpr(-, IntegerLit(3))])]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 368))

#     def test_idxOperator_70(self):
#         input = """main: function void (a:integer) {
#             n: array [6] of boolean;
#             n = foo(v[b+c-d/e*9]);

#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(a, IntegerType)], None, BlockStmt([VarDecl(n, ArrayType([6], BooleanType)), AssignStmt(Id(n), FuncCall(foo, [ArrayCell(v, [BinExpr(-, BinExpr(+, Id(b), Id(c)), BinExpr(*, BinExpr(/, Id(d), Id(e)), IntegerLit(9)))])]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 369))

#     def test_exp_71(self):
#         input = """main: function void() {
#                 a= b+c-d/e*9;
#             }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(+, Id(b), Id(c)), BinExpr(*, BinExpr(/, Id(d), Id(e)), IntegerLit(9))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 370))

#     def test_exp_72(self):
#         input = """main: function void() {
#                 a= -b-c+d/e*f;
#             }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(-, UnExpr(-, Id(b)), Id(c)), BinExpr(*, BinExpr(/, Id(d), Id(e)), Id(f))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 371))

#     def test_exp_73(self):
#         input = """main: function void() {
#                 a= 2*(-3+f)/(2%5);
#             }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(/, BinExpr(*, IntegerLit(2), BinExpr(+, UnExpr(-, IntegerLit(3)), Id(f))), BinExpr(%, IntegerLit(2), IntegerLit(5))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 372))

#     def test_exp_74(self):
#         input = """main: function void() {
#                 a= !x || (y == 0);
#             }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, UnExpr(!, Id(x)), BinExpr(==, Id(y), IntegerLit(0))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 373))

#     def test_exp_75(self):
#         input = """main: function void() {
#                 _= !x || (y == 0) && (z > 12.5E-6);
#             }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(_), BinExpr(&&, BinExpr(||, UnExpr(!, Id(x)), BinExpr(==, Id(y), IntegerLit(0))), BinExpr(>, Id(z), FloatLit(1.25e-05))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 374))

#     def test_exp_76(self):
#         input = """main: function void() {
#                 _= (x*6) || (y == 0) && (z > 12.5E-6);
#             }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(_), BinExpr(&&, BinExpr(||, BinExpr(*, Id(x), IntegerLit(6)), BinExpr(==, Id(y), IntegerLit(0))), BinExpr(>, Id(z), FloatLit(1.25e-05))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 375))

#     def test_exp_77(self):
#         input = """main: function void() {
#                 a = 21 + (5.2-7.8E9)/(b-60);
#             }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, IntegerLit(21), BinExpr(/, BinExpr(-, FloatLit(5.2), FloatLit(7800000000.0)), BinExpr(-, Id(b), IntegerLit(60)))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 376))

#     def test_exp_78(self):
#         input = """main: function void() {
#             _a = func(5-b) - func1(5.3e-3,4-b)*6/12;
#             }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(_a), BinExpr(-, FuncCall(func, [BinExpr(-, IntegerLit(5), Id(b))]), BinExpr(/, BinExpr(*, FuncCall(func1, [FloatLit(0.0053), BinExpr(-, IntegerLit(4), Id(b))]), IntegerLit(6)), IntegerLit(12))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 377))

#     def test_exp_79(self):
#         input = """main: function void() {
#             local_var: integer;
#             local_var = local[1 + x] - 4 * 5;
#             a = min == 15 * 123 + (1 + 3);
#             //return local_var + 1;
#             }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(local_var, IntegerType), AssignStmt(Id(local_var), BinExpr(-, ArrayCell(local, [BinExpr(+, IntegerLit(1), Id(x))]), BinExpr(*, IntegerLit(4), IntegerLit(5)))), AssignStmt(Id(a), BinExpr(==, Id(min), BinExpr(+, BinExpr(*, IntegerLit(15), IntegerLit(123)), BinExpr(+, IntegerLit(1), IntegerLit(3)))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 378))

#     def test_exp_80(self):
#         input = """main: function void() {
#             local_var: integer;
#             a = !abc + -45 ;
#             return local_var >= a;
#             }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(local_var, IntegerType), AssignStmt(Id(a), BinExpr(+, UnExpr(!, Id(abc)), UnExpr(-, IntegerLit(45)))), ReturnStmt(BinExpr(>=, Id(local_var), Id(a)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 379))

#     def test_complex_program_81(self):
#         input = """
#             main:function integer(){
#                     a[b[2]] = 10;
#                     name();
#                     return;
#                 }
#             """
#         expect = """Program([
# 	FuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [ArrayCell(b, [IntegerLit(2)])]), IntegerLit(10)), CallStmt(name, ), ReturnStmt()]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 380))

#     def test_complex_program_82(self):
#         input = """
#         nah: function float(){
# 				s:integer;
#                 {
#                     if (s > 10) break;
# 					else {
#                         do {
#                         a = a + 1;
#                         }
#                         while(true);
#                     }
#                 }
#             }
#             """
#         expect = """Program([
# 	FuncDecl(nah, FloatType, [], None, BlockStmt([VarDecl(s, IntegerType), BlockStmt([IfStmt(BinExpr(>, Id(s), IntegerLit(10)), BreakStmt(), BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 381))

#     def test_complex_program_83(self):
#         input = """
# 		foo: function integer(){
#                 do{
#                     a = a-1;
#                     break;
#                     do{
#                         f = sqrt(a*a + b*b + c*c);
#                         if ((1>=0) == 2+a[1]+c+("abc"< 0)) { break; }
#                         else {}   
#                     }while (a>0);
               
#                 }while (a!=b) ;      

#             }
#             """
#         expect = """Program([
# 	FuncDecl(foo, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1))), BreakStmt(), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(f), FuncCall(sqrt, [BinExpr(+, BinExpr(+, BinExpr(*, Id(a), Id(a)), BinExpr(*, Id(b), Id(b))), BinExpr(*, Id(c), Id(c)))])), IfStmt(BinExpr(==, BinExpr(>=, IntegerLit(1), IntegerLit(0)), BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(2), ArrayCell(a, [IntegerLit(1)])), Id(c)), BinExpr(<, StringLit(abc), IntegerLit(0)))), BlockStmt([BreakStmt()]), BlockStmt([]))]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 382))

#     def test_complex_program_84(self):
#         input = """
# 		foo: function integer(){
#             a: integer;
#             a = 10;
#              do {
#                 if( a == 15) {
#                     a = a + 1;
#                     continue;
#                 }
#                 foo(a);
#                 a= a+1;
#             } while( a < 20 );
#             return 0;      

#             }
#             """
#         expect = """Program([
# 	FuncDecl(foo, IntegerType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), IntegerLit(10)), DoWhileStmt(BinExpr(<, Id(a), IntegerLit(20)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(15)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), ContinueStmt()])), CallStmt(foo, Id(a)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), ReturnStmt(IntegerLit(0))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 383))

#     def test_complex_program_85(self):
#         input = """
# 		foo: function integer(){
#             do{
#                  a = a-1;
#                 //Fighting!!
#                 //break;
#                 do{
#                     f = sqrt(a*a + b*b + c*c);
#                     if ((1>=0)== 2+a[1]+c+("abc"< 0)) { break; }
#                     else {} 
#                 } 
#                 while (a>0);
#                 //?/@!$$%**())               
#             } while (a!=b) ;
#         }
#             """
#         expect = """Program([
# 	FuncDecl(foo, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1))), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(f), FuncCall(sqrt, [BinExpr(+, BinExpr(+, BinExpr(*, Id(a), Id(a)), BinExpr(*, Id(b), Id(b))), BinExpr(*, Id(c), Id(c)))])), IfStmt(BinExpr(==, BinExpr(>=, IntegerLit(1), IntegerLit(0)), BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(2), ArrayCell(a, [IntegerLit(1)])), Id(c)), BinExpr(<, StringLit(abc), IntegerLit(0)))), BlockStmt([BreakStmt()]), BlockStmt([]))]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 384))

#     def test_complex_program_86(self):
#         input = """
#         a: integer;
#         b: array [3] of float;
#         foo: function integer(a:integer, b:array [10] of float) {
#             c:array [3] of integer;
#             if (a>0)
#                 foo(a-1, b);
#             return c;
#         }
#             """
#         expect = """Program([
# 	VarDecl(a, IntegerType)
# 	VarDecl(b, ArrayType([3], FloatType))
# 	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, ArrayType([10], FloatType))], None, BlockStmt([VarDecl(c, ArrayType([3], IntegerType)), IfStmt(BinExpr(>, Id(a), IntegerLit(0)), CallStmt(foo, BinExpr(-, Id(a), IntegerLit(1)), Id(b))), ReturnStmt(Id(c))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 385))

#     def test_complex_program_87(self):
#         input = """
#         foo:function integer (a:integer, b:array [10] of float)
#         {
#             c:boolean;
#             i:integer;
#             i = a + 3 ;
#             if (i > 0) {
#                 d:integer;
#                 d = i + 3;
#                 printInteger( d );
#             }
#             return i;
#         }
#             """
#         expect = """Program([
# 	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, ArrayType([10], FloatType))], None, BlockStmt([VarDecl(c, BooleanType), VarDecl(i, IntegerType), AssignStmt(Id(i), BinExpr(+, Id(a), IntegerLit(3))), IfStmt(BinExpr(>, Id(i), IntegerLit(0)), BlockStmt([VarDecl(d, IntegerType), AssignStmt(Id(d), BinExpr(+, Id(i), IntegerLit(3))), CallStmt(printInteger, Id(d))])), ReturnStmt(Id(i))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 386))

#     def test_complex_program_88(self):
#         input = """
#         i:integer;
#         f:function integer() {
#             return 200;
#         }
#         main:function void () {
#             main:integer ;
#             main = f() ;
#             printInteger( main ) ;
#         }
#             """
#         expect = """Program([
# 	VarDecl(i, IntegerType)
# 	FuncDecl(f, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(200))]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(main, IntegerType), AssignStmt(Id(main), FuncCall(f, [])), CallStmt(printInteger, Id(main))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 387))

#     def test_complex_program_89(self):
#         input = """
#         main:function void () {
#             main:integer ;
#             main = f() ;
#             printInteger( main ) ;
#             {
#                 i:integer ;
#                 main:integer ;
#                 f:integer ;
#                 main = e*f+g/h*10010;
#                 printInteger( i ) ;
#                 printInteger( main ) ;
#                 printInteger ( f ) ;
#             }
#             printInteger( main ) ;
#         }
#             """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(main, IntegerType), AssignStmt(Id(main), FuncCall(f, [])), CallStmt(printInteger, Id(main)), BlockStmt([VarDecl(i, IntegerType), VarDecl(main, IntegerType), VarDecl(f, IntegerType), AssignStmt(Id(main), BinExpr(+, BinExpr(*, Id(e), Id(f)), BinExpr(*, BinExpr(/, Id(g), Id(h)), IntegerLit(10010)))), CallStmt(printInteger, Id(i)), CallStmt(printInteger, Id(main)), CallStmt(printInteger, Id(f))]), CallStmt(printInteger, Id(main))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 388))

#     def test_complex_program_90(self):
#         input = """
#         main:function void () {
#             // printf() displays the string inside quotation
#             printString("Hello, World!");
#             return 0;
#         }
#             """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(Hello, World!)), ReturnStmt(IntegerLit(0))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 389))

#     def test_complex_program_91(self):
#         input = """
#         main:function void () {
#             number:integer;
#             //printf() displays the formatted output 
#             printf("Enter an integer: ");

#             //scanf() reads the formatted input and stores them
#             //scanf("%d", &number);

#             //printf() displays the formatted output
#             printInteger("You entered: %d", number);
#             return 0;
#         }
#             """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(number, IntegerType), CallStmt(printf, StringLit(Enter an integer: )), CallStmt(printInteger, StringLit(You entered: %d), Id(number)), ReturnStmt(IntegerLit(0))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 390))

#     def test_complex_program_92(self):
#         input = """
#         main:function void () {
#     		n, count:integer;
# 			count = 0;
#     		printString("Enter an integer: ");
#     		readInteger("%d", n);
# 			do {
#         		n = n / 10;
#         		count = count + 1;
#     		}while (n != 0);
    
#     		printInteger("Number of digits: %d", count);
# 			return 0;
#         }
#             """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), VarDecl(count, IntegerType), AssignStmt(Id(count), IntegerLit(0)), CallStmt(printString, StringLit(Enter an integer: )), CallStmt(readInteger, StringLit(%d), Id(n)), DoWhileStmt(BinExpr(!=, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(n), BinExpr(/, Id(n), IntegerLit(10))), AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))])), CallStmt(printInteger, StringLit(Number of digits: %d), Id(count)), ReturnStmt(IntegerLit(0))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 391))

#     def test_complex_program_93(self):
#         input = """
#         main:function void () {
#     		i, n:integer;
#     		arr:array [100] of float;
#     		printString("Enter total number of elements(1 to 100): ");
#     		readInteger("%d", n);
#     		//Stores number entered by the user
#     		for (i = 0, i < n,  i + 1){
#        			printInteger("Enter Number %d: ", i+1);
#        			readInteger("%f", arr[i]);
#     		}
#     		//Loop to store largest number to arr[0]
#     		for (i = 1, i < n, i + 1){
#        			if (arr[0] < arr[i])					//Change < to > if you want to find the smallest element
#            			arr[0] = arr[i];
#     		}
#     		printInteger("Largest element", arr[0]);
#     		return 0;
#         }
#             """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(n, IntegerType), VarDecl(arr, ArrayType([100], FloatType)), CallStmt(printString, StringLit(Enter total number of elements(1 to 100): )), CallStmt(readInteger, StringLit(%d), Id(n)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, StringLit(Enter Number %d: ), BinExpr(+, Id(i), IntegerLit(1))), CallStmt(readInteger, StringLit(%f), ArrayCell(arr, [Id(i)]))])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [IntegerLit(0)]), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(arr, [IntegerLit(0)]), ArrayCell(arr, [Id(i)])))])), CallStmt(printInteger, StringLit(Largest element), ArrayCell(arr, [IntegerLit(0)])), ReturnStmt(IntegerLit(0))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 392))

#     def test_complex_program_94(self):
#         input = """
# 		convertBinarytoOctal:function integer(binaryNumber:integer){
# 		/*Function convert binary to Octal */

#                 octalNumber, decimalNumber, i:integer;
#                 octalNumber = decimalNumber -i + 0;
#                 do {
#                     decimalNumber = decimalNumber + (binaryNumber%10);
#                     i = i + 1;
#                     binaryNumber = binaryNumber / 10;
#                 }while (binaryNumber != 0);
#                 i = 1;
#                 do {
#                     octalNumber = octalNumber + (decimalNumber % 8) * i;
#                     decimalNumber = decimalNumber / 8;
#                     i = i * 10;
#                 }while (decimalNumber != 0);
        
#                 return octalNumber;
#             }
#             """
#         expect = """Program([
# 	FuncDecl(convertBinarytoOctal, IntegerType, [Param(binaryNumber, IntegerType)], None, BlockStmt([VarDecl(octalNumber, IntegerType), VarDecl(decimalNumber, IntegerType), VarDecl(i, IntegerType), AssignStmt(Id(octalNumber), BinExpr(+, BinExpr(-, Id(decimalNumber), Id(i)), IntegerLit(0))), DoWhileStmt(BinExpr(!=, Id(binaryNumber), IntegerLit(0)), BlockStmt([AssignStmt(Id(decimalNumber), BinExpr(+, Id(decimalNumber), BinExpr(%, Id(binaryNumber), IntegerLit(10)))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(binaryNumber), BinExpr(/, Id(binaryNumber), IntegerLit(10)))])), AssignStmt(Id(i), IntegerLit(1)), DoWhileStmt(BinExpr(!=, Id(decimalNumber), IntegerLit(0)), BlockStmt([AssignStmt(Id(octalNumber), BinExpr(+, Id(octalNumber), BinExpr(*, BinExpr(%, Id(decimalNumber), IntegerLit(8)), Id(i)))), AssignStmt(Id(decimalNumber), BinExpr(/, Id(decimalNumber), IntegerLit(8))), AssignStmt(Id(i), BinExpr(*, Id(i), IntegerLit(10)))])), ReturnStmt(Id(octalNumber))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 393))

#     def test_complex_program_95(self):
#         input = """
# 		/*Enter and print an array of integers*/
# 		a:array [10] of integer;
#         b:integer;
# 		enter:function void(a: array [10] of integer, n:integer) {
# 			j:array [2] of integer;
#             i:integer;
# 			for (i = 0, i < n,i + 1) {
# 				printString("Enter an integer: ");
#             	readInteger (a[i]);
# 			}
# 		}
# 		print:function void(a:array [10] of integer, n:integer) {
# 			i:integer;
# 			for (i = 0, i < n, i + 1) printInteger("hihi, ", a[i]);
# 		}
# 		main:function integer() {
# 			enter(a, 10);
# 			printA(a, 10);
# 			return 0;
# 		}
#             """
#         expect = """Program([
# 	VarDecl(a, ArrayType([10], IntegerType))
# 	VarDecl(b, IntegerType)
# 	FuncDecl(enter, VoidType, [Param(a, ArrayType([10], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(j, ArrayType([2], IntegerType)), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, StringLit(Enter an integer: )), CallStmt(readInteger, ArrayCell(a, [Id(i)]))]))]))
# 	FuncDecl(print, VoidType, [Param(a, ArrayType([10], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, StringLit(hihi, ), ArrayCell(a, [Id(i)])))]))
# 	FuncDecl(main, IntegerType, [], None, BlockStmt([CallStmt(enter, Id(a), IntegerLit(10)), CallStmt(printA, Id(a), IntegerLit(10)), ReturnStmt(IntegerLit(0))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 394))

#     def test_complex_program_96(self):
#         input = """
# 		/*Enter and print an array of integers*/
# 		main:function integer(a:integer,v:integer) {
#             if (a + b < 1 * 3 / 7){
#                 c:array [4] of integer;
#                 a:integer;
#                 if (!(a - b))
#                     return 0;
#                 else{
#                 }
#             }
#             else
#                 return 10;
# 		}
#             """
#         expect = """Program([
# 	FuncDecl(main, IntegerType, [Param(a, IntegerType), Param(v, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, BinExpr(+, Id(a), Id(b)), BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(3)), IntegerLit(7))), BlockStmt([VarDecl(c, ArrayType([4], IntegerType)), VarDecl(a, IntegerType), IfStmt(UnExpr(!, BinExpr(-, Id(a), Id(b))), ReturnStmt(IntegerLit(0)), BlockStmt([]))]), ReturnStmt(IntegerLit(10)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 395))

#     def test_complex_program_97(self):
#         input = """foo: function integer () {
#             while (x == true && false)
#                 while (x == true && false)
#                     while (x == true && false)
#                         while (x == true && false)
#                             while (x == true && false)
#                                 return main() + x;
#         }"""
#         expect = """Program([
# 	FuncDecl(foo, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(x), BinExpr(&&, BooleanLit(True), BooleanLit(False))), WhileStmt(BinExpr(==, Id(x), BinExpr(&&, BooleanLit(True), BooleanLit(False))), WhileStmt(BinExpr(==, Id(x), BinExpr(&&, BooleanLit(True), BooleanLit(False))), WhileStmt(BinExpr(==, Id(x), BinExpr(&&, BooleanLit(True), BooleanLit(False))), WhileStmt(BinExpr(==, Id(x), BinExpr(&&, BooleanLit(True), BooleanLit(False))), ReturnStmt(BinExpr(+, FuncCall(main, []), Id(x))))))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 396))

#     def test_complex_program_98(self):
#         input = """
#         // asdfasdfadfadfasdfasd
#         main: function integer () {
#             {{{
#                 {{}}
#             }}}
#             return;
#         }"""
#         expect = """Program([
# 	FuncDecl(main, IntegerType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])]), ReturnStmt()]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 397))

#     def test_complex_program_99(self):
#         input = """
#         main: function integer() {}
#         main: function float(x: integer) {
#             if (x && x && x) return 0;
#             return x;    
#         }"""
#         expect = """Program([
# 	FuncDecl(main, IntegerType, [], None, BlockStmt([]))
# 	FuncDecl(main, FloatType, [Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(&&, Id(x), Id(x)), Id(x)), ReturnStmt(IntegerLit(0))), ReturnStmt(Id(x))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 398))

#     def test_complex_program_100(self):
#         input = """
#         /* Comment */
#         fn: function array[1] of boolean (cd: auto, temp: string) {
#             a=c[c[c[c[c[c12]]]]];
#             b=b[1,1,1,1,1];
#         }"""
#         expect = """Program([
# 	FuncDecl(fn, ArrayType([1], BooleanType), [Param(cd, AutoType), Param(temp, StringType)], None, BlockStmt([AssignStmt(Id(a), ArrayCell(c, [ArrayCell(c, [ArrayCell(c, [ArrayCell(c, [ArrayCell(c, [Id(c12)])])])])])), AssignStmt(Id(b), ArrayCell(b, [IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(1)]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 399))