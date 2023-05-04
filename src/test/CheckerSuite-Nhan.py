import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # def test2(self):
    #     input = Program([VarDecl("a", IntegerType()),
    #                     VarDecl("c", FloatType())])

    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 4021))

    # def test3(self):
    #     input = """
    #     Ha: function array [2, 3] of integer() {
    #         a: auto = {{1,2,3},{1,2,3}};
    #         return a;
    #     }

    #     main: function void() {
    #         a: array [2, 3] of integer = {{4,4,4},{4,4,8+7}};
    #     }"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 4031))

    # def test4(self):
    #     input = """
    #     Ha: function array [2, 3] of integer() {
    #         a: auto = {{1,2,{7}},{1,2,3}};
    #         return a;
    #     }

    #     main: function void() {

    #     }"""
    #     expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(7)])])"
    #     self.assertTrue(TestChecker.test(input, expect, 4041))

    # def test5(self):
    #     input = """
    #     Ha: function array [2, 3] of integer() {
    #         a: auto = {{1},{1,2,{7,5,9}},{1,2,3}};
    #         return a;
    #     }

    #     main: function void() {

    #     }"""
    #     expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(7), IntegerLit(5), IntegerLit(9)])])"
    #     self.assertTrue(TestChecker.test(input, expect, 4051))

    # def test6(self):
    #     input = """
    #     Ha: function array [1, 3] of integer() {
    #         a: auto = {{{1},{4}},{{3},{6}},{{1},{6}}};
    #         return a;
    #     }

    #     main: function void() {

    #     }"""
    #     expect = "Type mismatch in statement: ReturnStmt(Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 4061))

    # def test7(self):
    #     input = """
    #     Ha: function auto() {
    #         a: auto = {{1,2,3},{1,2,3}};
    #         return a;
    #     }

    #     main: function void() {
    #         a: array [2, 3] of integer = Ha();
    #     }"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 4071))

    # def test8(self):
    #     input = """
    #     main: function void() {
    #         a: array [2, 3] of integer = Ha();
    #     }
        
    #     Ha: function auto() {
    #         a: auto = {{1,2,3},{1,2,3}};
    #         return a;
    #     }"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 4081))

    # def test9(self):
    #     input = """
    #     main: function void() {
    #         a: string = "ghgf"::Ha();
    #     }

    #     Ha: function auto() {
    #         a: auto = {{1,2,3},{1,2,3}};
    #         return a;
    #     }"""
    #     expect = "Type mismatch in statement: ReturnStmt(Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 4091))

    # def test10(self):
    #     input = """
    #     main: function void() {
    #         a: string = "ghgf"::Ha();
    #     }

    #     Ha: function string(e:auto) {
    #         return "";
    #     }

    #     Ha: function auto() {
    #         a: auto = {{1,2,3},{1,2,3}};
    #         return a;
    #     }"""
    #     expect = "Type mismatch in expression: FuncCall(Ha, [])"
    #     self.assertTrue(TestChecker.test(input, expect, 4101))

    # def test11(self):
    #     input = """
    #     main: function void() {
    #         a: string = "ghgf"::Ha(6.8);
    #     }

    #     Ha: function string(e:auto) {
    #         return "";
    #     }

    #     Ha: function auto() {
    #         a: auto = {{1,2,3},{1,2,3}};
    #         return a;
    #     }"""
    #     expect = "Redeclared Function: Ha"
    #     self.assertTrue(TestChecker.test(input, expect, 4111))

    # def test12(self):
    #     input = """
    #     main: function void() {
    #         a: string = "ghgf"::Ha({{{1,2,3}}});
    #     }
        
    #     Ha: function string(e:array [1,1,3] of integer) {
    #         return e[1,2+e[1,1]];
    #     }
        
    #     Ha: function auto() {
    #         a: auto = {{1,2,3},{1,2,3}};
    #         return a;
    #     }"""
    #     expect = "Type mismatch in expression: BinExpr(+, IntegerLit(2), ArrayCell(e, [IntegerLit(1), IntegerLit(1)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 4121))

    # def test13(self):
    #     input = """
    #     main: function void() {
    #         a: array[3] of integer = Ha({{{1,2,3}}});
    #     }
        
    #     Ha: function auto(e:array [1,1,3] of integer) {
    #         return e[1,2+e[1,1,0]];
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 4131))

    # def test14(self):
    #     input = """
    #     main: function void() {
    #         a: integer = Ha(foo());
    #     }
        
    #     Ha: function auto(a: auto) {
    #         e:array [1,1,3] of integer;
    #         a = e[1,2+e[1,1,0],a];
    #         return a;
    #     }
        
    #     foo: function auto() {}
    #     """
    #     expect = "Type mismatch in expression: Id(a)"
    #     self.assertTrue(TestChecker.test(input, expect, 4141))

    # def test15(self):
    #     input = """
    #     main: function void() {
    #         a: array[1,2,2] of boolean = {{{1,2},{3,foo()}}};
    #     }

    #     foo: function auto() {}
    #     """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1, 2, 2], BooleanType), ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), FuncCall(foo, [])])])]))"
    #     self.assertTrue(TestChecker.test(input, expect, 4151))

    # def test16(self):
    #     input = """
    #     main: function void() {
    #         a: array[1,2,2] of boolean = {{{true,false},{true,foo()}}};
    #         printBoolean(foo());
    #     }

    #     foo: function auto() {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 4161))

    # def test17(self):
    #     input = """
    #     main: function void() {
    #         a: array[3] of integer = Ha({{{1,2,3}}});
    #     }

    #     Ha: function auto(e:array [1,1,3] of integer) {
    #         return e[1,2+e[1,1,0],9,0];
    #     }
    #     """
    #     expect = "Type mismatch in expression: ArrayCell(e, [IntegerLit(1), BinExpr(+, IntegerLit(2), ArrayCell(e, [IntegerLit(1), IntegerLit(1), IntegerLit(0)])), IntegerLit(9), IntegerLit(0)])"
    #     self.assertTrue(TestChecker.test(input, expect, 4171))

    # def test18(self):
    #     input = """
    #     main: function void() {
    #         a: float;
    #         b: float = 3.4;
    #         printFloat(foo(b));
    #     }

    #     foo: function auto(a: float) {
    #         if (a < 1) return a;
    #         return foo(a - 1) + a;
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 4181))

    # def test19(self):
    #     input = """
    #     main: function void() {
    #         a: float;
    #         b: float = 3.4;
    #         printFloat(foo(b));
    #     }

    #     foo: function auto(a: float) {
    #         if (a < 1) return a;
    #         return 2;
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 4191))

    # def test20(self):
    #     input = """
    #     main: function void() {
    #         a: float;
    #         b: float = 3.4;
    #         printInteger(foo(b));
    #     }

    #     foo: function float(a: float) {
    #         if (a < 1) return a;
    #         return 2;
    #     }
    #     """
    #     expect = "Type mismatch in statement: CallStmt(printInteger, FuncCall(foo, [Id(b)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 4201))

    # def test21(self):
    #     input = """
    #     main: function void() {
    #         a,b,c: auto = 1,"Hell",{{1,2},{21.9,7},{16,4}};
    #         printFloat(a);
    #         b = readString();
    #         printInteger(c[0,0]);
    #     }
    #     """
    #     expect = "Type mismatch in statement: CallStmt(printInteger, ArrayCell(c, [IntegerLit(0), IntegerLit(0)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 4211))

    # def test22(self):
    #     input = """
    #     main: function void() {
    #         a,b,c: auto = 1,"Hell",{{1,2},{21,7},{16,4}};
    #         printFloat(a);
    #         b = readString();
    #         printFloat(c[0,0]);
    #     }

    #     foo: function auto(a: float) {
    #         if (a < 1) return a;
    #         else return "shskdskkkh";
    #         return;
    #         return 2;
    #     }
    #     """
    #     expect = "Type mismatch in statement: ReturnStmt(StringLit(shskdskkkh))"
    #     self.assertTrue(TestChecker.test(input, expect, 4221))

    # def test23(self):
    #     input = """
    #     main: function void() {
    #         a,b,c: auto = 1,"Hell",{{1,2},{21,7},{16,4}};
    #         printFloat(a);
    #         b = readString();
    #         printFloat(c[0,0]);
    #     }

    #     foo: function auto(a: float) {
    #         if (a < 1) return a;
    #         else return 0;
    #         return;
    #         return 2;
    #     }
    #     """
    #     expect = "Type mismatch in statement: ReturnStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 4231))

    # def test24(self):
    #     input = """
    #     main: function void() {
    #         a,b,c: auto = 1,"Hell",{{1,2},{21,7},{16,4}};
    #         printFloat(a);
    #         b = readString();
    #         printFloat(c[0,0]);
    #     }

    #     foo: function auto(a: float) {
    #         if (a < 1) return a;
    #         else return 0;
    #         return 0.0003;
    #         return "hkshds";
    #         if (a < 1) return true;
    #     }
    #     """
    #     expect = "Type mismatch in statement: ReturnStmt(StringLit(hkshds))"
    #     self.assertTrue(TestChecker.test(input, expect, 424))

    # def test25(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 0;
    #         b: auto = "dgjhdf"::foo(a+foo(a,"daaad"),"");
    #     }

    #     foo: function auto(a: auto, b: auto) {
    #         b = "ffhg";
    #         return a;
    #     }
    #     """
    #     expect = "Type mismatch in expression: BinExpr(::, StringLit(dgjhdf), FuncCall(foo, [BinExpr(+, Id(a), FuncCall(foo, [Id(a), StringLit(daaad)])), StringLit()]))"
    #     self.assertTrue(TestChecker.test(input, expect, 425))

    # def test26(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 0;
    #         b: integer = foo(a+foo(a,"daaad"),"") + 1;
    #     }

    #     foo: function auto(a: auto, b: auto) {
    #         b = "ffhg";
    #         return a;
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 426))

    # def test27(self):
    #     input = """
    #     foo: integer;
    #     main: function void() {}
    #     foo: function auto(a: auto, b: auto) {}
    #     """
    #     expect = "Redeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input, expect, 427))

    # def test28(self):
    #     input = """
    #     main: function void() {}
    #     foo: function auto(a: auto, b: auto) {}
    #     foo: integer;
    #     """
    #     expect = "Redeclared Variable: foo"
    #     self.assertTrue(TestChecker.test(input, expect, 428))

    # def test29(self):
    #     input = """
    #     main: function void() {
    #         a: string = foo;
    #     }
    #     foo: function string(a: auto, b: auto) {}
    #     """
    #     expect = "Undeclared Identifier: foo"
    #     self.assertTrue(TestChecker.test(input, expect, 429))

    # def test30(self):
    #     input = """
    #     main: function void() {
    #         a: string = foo;
    #     }
    #     foo: string = "";
    #     """
    #     expect = "Undeclared Identifier: foo"
    #     self.assertTrue(TestChecker.test(input, expect, 430))

    # def test31(self):
    #     input = """
    #     foo: string = "";
    #     main: function void() {
    #         a: string = foo();
    #     }
    #     """
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input, expect, 431))

    # def test32(self):
    #     input = """
    #     main: function void() {
    #         a: string = 1::2;
    #     }
    #     """
    #     expect = "Type mismatch in expression: BinExpr(::, IntegerLit(1), IntegerLit(2))"
    #     self.assertTrue(TestChecker.test(input, expect, 432))

    # def test33(self):
    #     input = """
    #     main: function void() {
    #         a: string;
    #         a = 1::2;
    #     }
    #     """
    #     expect = "Type mismatch in expression: BinExpr(::, IntegerLit(1), IntegerLit(2))"
    #     self.assertTrue(TestChecker.test(input, expect, 433))

    # def test34(self):
    #     input = """
    #     main: function void() {
    #         a: float;
    #         a = "Hello"::"me";
    #     }
    #     """
    #     expect = "Type mismatch in statement: AssignStmt(Id(a), BinExpr(::, StringLit(Hello), StringLit(me)))"
    #     self.assertTrue(TestChecker.test(input, expect, 434))

    # def test35(self):
    #     input = """
    #     main: function void() {
    #         a: array[10,3,4,5] of string;
    #         b: string = a[0,0,a,90];
    #     }
    #     """
    #     expect = "Type mismatch in expression: Id(a)"
    #     self.assertTrue(TestChecker.test(input, expect, 435))

    # def test36(self):
    #     input = """
    #     main: function void() {
    #         return "";
    #     }
    #     """
    #     expect = "Type mismatch in statement: ReturnStmt(StringLit())"
    #     self.assertTrue(TestChecker.test(input, expect, 436))

    # def test37(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 123;
    #         if (foo()>a) {
    #             printInteger(foo());
    #         }
    #     }

    #     foo: function auto() {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 437))

    # def test38(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 123.9;
    #         if (foo()>a) {
    #             printInteger(foo());
    #         }
    #     }

    #     foo: function auto() {}
    #     """
    #     expect = "Type mismatch in statement: CallStmt(printInteger, FuncCall(foo, []))"
    #     self.assertTrue(TestChecker.test(input, expect, 438))

    # def test39(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 123.9;
    #         if (a+8 == 4) {
    #             printInteger(foo());
    #         }
    #     }

    #     foo: function auto() {}
    #     """
    #     expect = "Type mismatch in expression: BinExpr(==, BinExpr(+, Id(a), IntegerLit(8)), IntegerLit(4))"
    #     self.assertTrue(TestChecker.test(input, expect, 439))

    # def test40(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 123.9;
    #         if (a+8) printInteger(foo());
    #     }
    #     """
    #     expect = "Type mismatch in statement: IfStmt(BinExpr(+, Id(a), IntegerLit(8)), CallStmt(printInteger, FuncCall(foo, [])))"
    #     self.assertTrue(TestChecker.test(input, expect, 440))

    # def test41(self):
    #     input = """
    #     main: function void() {
    #         a: auto = {123,3,9};
    #         for (a[0] = 8, true, a[2]+1) printInteger(foo());
    #     }
    #     foo: function integer() {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 441))

    # def test42(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 1.0;
    #         for (a = 8, true, foo()) printInteger(foo());
    #     }
    #     foo: function integer() {}
    #     """
    #     expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(a), IntegerLit(8)), BooleanLit(True), FuncCall(foo, []), CallStmt(printInteger, FuncCall(foo, [])))"
    #     self.assertTrue(TestChecker.test(input, expect, 442))

    # def test43(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 123;
    #         for (a = 8, true, "ghshdg") printInteger(foo());
    #     }
    #     foo: function integer() {}
    #     """
    #     expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(a), IntegerLit(8)), BooleanLit(True), StringLit(ghshdg), CallStmt(printInteger, FuncCall(foo, [])))"
    #     self.assertTrue(TestChecker.test(input, expect, 443))

    # def test44(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 123;
    #         for (a = 8, true, 9.0) printInteger(foo());
    #     }
    #     foo: function integer() {}
    #     """
    #     expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(a), IntegerLit(8)), BooleanLit(True), FloatLit(9.0), CallStmt(printInteger, FuncCall(foo, [])))"
    #     self.assertTrue(TestChecker.test(input, expect, 444))

    # def test45(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 123.9;
    #         while (a > 8) printInteger(foo());
    #     }
    #     foo: function integer() {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 445))

    # def test46(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 1.0;
    #         while (-a + 8) printInteger(foo());
    #     }
    #     foo: function integer() {}
    #     """
    #     expect = "Type mismatch in statement: WhileStmt(BinExpr(+, UnExpr(-, Id(a)), IntegerLit(8)), CallStmt(printInteger, FuncCall(foo, [])))"
    #     self.assertTrue(TestChecker.test(input, expect, 446))

    # def test47(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 123;
    #         while (!a + 8) printInteger(foo());
    #     }
    #     foo: function integer() {}
    #     """
    #     expect = "Type mismatch in expression: UnExpr(!, Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 447))

    # def test48(self):
    #     input = """
    #     main: function void() {
    #         a: auto = 123;
    #         while (!foo()) printBoolean(foo());
    #     }
    #     foo: function auto() {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 448))

    # def test49(self):
    #     input = """
    #     main: function void() {
    #         a: string = "wtfyt";
    #         do {
    #             a: auto = 123;
    #             printInteger(a);
    #         }
    #         while (!foo());
    #     }
    #     foo: function auto() {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 449))

    # def test50(self):
    #     input = """
    #     main: function void() {
    #         a: string = "wtfyt";
    #         b: integer;
    #         do {
    #             a: auto = 123;
    #             printInteger(b);
    #         }
    #         while (!foo());
    #     }
    #     b: string;
    #     foo: function auto() {
    #         return true;
    #         if (!foo())
    #             return a;
    #         while (false) return "false";
    #     }
    #     """
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input, expect, 450))

    # def test51(self):
    #     input = """
    #     main: function void() {
    #         a: string = "wtfyt";
    #         b: integer;
    #         do {
    #             a: auto = 123;
    #             printInteger(b);
    #         }
    #         while (2-foo());
    #     }
    #     b: string;
    #     foo: function auto() {
    #         return true;
    #         if (!foo())
    #             return a;
    #         while (false) return "false";
    #     }
    #     """
    #     expect = "Type mismatch in statement: DoWhileStmt(BinExpr(-, IntegerLit(2), FuncCall(foo, [])), BlockStmt([VarDecl(a, AutoType, IntegerLit(123)), CallStmt(printInteger, Id(b))]))"
    #     self.assertTrue(TestChecker.test(input, expect, 451))

    # def test52(self):
    #     input = """
    #     main: function void() {
    #         a: auto = {{1},{2},{3}};
    #         b: integer;
    #         do {
    #             printInteger(b);
    #             {{{{break;}}}}
    #         }
    #         while (a[1,0] > 0.1);
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 452))

    # def test53(self):
    #     input = """
    #     main: function void() {
    #         a: auto = {{1},{2},{3}};
    #         b: integer;
    #         do {
    #             printInteger(b);
    #             if (true)
    #                 {{{{continue;}}}}
    #         }
    #         while (a[1,0] > 0.1);
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 453))

    # def test54(self):
    #     input = """
    #     main: function void() {
    #         a: auto = {{1},{2},{3}};
    #         b: integer;
    #         while (a[1,0] > 0.1)
    #             while (a[1,0] > 0.1)
    #                 while (a[1,0] > 0.1) {
    #                     break;
    #                     continue;
    #                 }

    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 454))

    # def test55(self):
    #     input = """
    #     main: function void() {
    #         a: auto = {{1},{2},{3}};
    #         b: integer;
    #         while (a[1,0] > 0.1)
    #             while (a[1,0] > 0.1)
    #                 while (a[1,0] > 0.1) {
    #                     break;
    #                     continue;
    #                 }
    #         printFloat(a[0,0]);
    #         break;
    #     }
    #     """
    #     expect = "Must in loop: BreakStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 455))

    # def test56(self):
    #     input = """
    #     main: function void() {}

    #     mom: function void() {}

    #     child: function void() inherit mom {}

    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 456))

    # def test57(self):
    #     input = """
    #     main: function void() {}

    #     mom: function void() {}

    #     child: function void() inherit mom {
    #         super();
    #     }

    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 457))

    # def test58(self):
    #     input = """
    #     main: function void() {}

    #     mom: function void() {}

    #     child: function void() inherit mom {
    #         super(1,2,3);
    #     }

    #     """
    #     expect = "Type mismatch in expression: IntegerLit(1)"
    #     self.assertTrue(TestChecker.test(input, expect, 458))

    # def test59(self):
    #     input = """
    #     main: function void() {}

    #     mom: function void() {}

    #     child: function void() inherit mom {
    #         preventDefault();
    #         a: integer = readInteger();
    #     }

    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 459))

    # def test60(self):
    #     input = """
    #     main: function void() {}

    #     mom: function void() {}

    #     child: function void() inherit mom {
    #         a: integer = readInteger();
    #     }

    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 460))

    # def test61(self):
    #     input = """
    #     main: function void() {}

    #     mom: function void(a: auto, b: integer, c: auto) {}

    #     child: function void() inherit mom {}

    #     """
    #     expect = "Invalid statement in function: child"
    #     self.assertTrue(TestChecker.test(input, expect, 461))

    # def test62(self):
    #     input = """
    #     main: function void() {}

    #     mom: function void(a: auto, b: integer, c: auto) {}

    #     child: function void() inherit mom {
    #         preventDefault();
    #         a: string;
    #     }

    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 462))

    # def test63(self):
    #     input = """
    #     main: function void() {}

    #     mom: function void(a: auto, b: integer, c: auto) {}

    #     child: function void(a: string) inherit printString {
    #         super(a);
    #         a: integer = 9;
    #     }

    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 463))

    # def test64(self):
    #     input = """
    #     main: function void() {}

    #     mom: function void(a: auto, b: integer, c: auto) {}

    #     child: function void(a: string, b: integer) inherit mom {
    #         super(a,b,b);
    #         a: integer = 9;
    #     }

    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 464))

    # def test65(self):
    #     input = """
    #     main: function void() {}

    #     mom: function void(out a: auto, inherit b: integer, c: auto) {}

    #     child: function void(a: string, b: integer) inherit mom {
    #         super(a,b,b);
    #         a: integer = 9;
    #     }

    #     """
    #     expect = "Invalid Parameter: b"
    #     self.assertTrue(TestChecker.test(input, expect, 465))

    # def test66(self):
    #     input = """
    #     main: function void() {}

    #     mom: function void(out a: auto, inherit b: integer, c: auto) {}

    #     child: function void(a: string, a: integer) inherit mom {
    #         super(a,b,b);
    #         a: integer = 9;
    #     }

    #     """
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input, expect, 466))

    # def test66(self):
    #     input = """
    #     mom: function void(out a: auto, inherit b: integer, c: auto) {}

    #     child: function void(a: string) inherit mom {
    #         super(a,b,b);
    #     }

    #     main: function void() {
    #         mom(1,2,1);
    #     }
    #     """
    #     expect = "Type mismatch in statement: CallStmt(mom, IntegerLit(1), IntegerLit(2), IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 466))

    # def test67(self):
    #     input = """
    #     mom: function void(out a: auto, inherit b: auto, c: auto) {}

    #     child: function void(a: string) inherit mom {
    #         super(a,b,b);
    #         b = true;
    #     }

    #     main: function void() {
    #         mom("ds",2,1);
    #     }
    #     """
    #     expect = "Type mismatch in statement: CallStmt(mom, StringLit(ds), IntegerLit(2), IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 467))

    # def test68(self):
    #     input = """
    #     mom: function void(out a: auto, inherit b: auto, c: auto) {}

    #     child: function void(a: string) inherit mom {
    #         super(a,b,b);
    #         b = true;
    #     }

    #     main: function void() {
    #         mom("ds",true,false);
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 468))

    # def test_redeclvar_1(self):
    #     input = """x, x: integer;"""
    #     expect = "Redeclared Variable: x"
    #     self.assertTrue(TestChecker.test(input, expect, 400))

    # def test_redeclvar_2(self):
    #     input = """x: integer;
    #     x: string;"""
    #     expect = "Redeclared Variable: x"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_redeclvar_3(self):
    #     input = """x: function integer(){}
    #     x: float;"""
    #     expect = "Redeclared Variable: x"
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_redeclvar_4(self):
    #     input = """x: integer;
    #     y: boolean;
    #     x: string;"""
    #     expect = "Redeclared Variable: x"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclfunc_1(self):
    #     input = """x: integer;
    #     x: function string(){}"""
    #     expect = "Redeclared Function: x"
    #     self.assertTrue(TestChecker.test(input, expect, 404))

    # def test_redeclfunc_2(self):
    #     input = """x: function void(){}
    #     x: function string(){}"""
    #     expect = "Redeclared Function: x"
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_redeclfunc_3(self):
    #     input = """y: function string(){}
    #     x: integer;
    #     y: function array[2] of float(){}"""
    #     expect = "Redeclared Function: y"
    #     self.assertTrue(TestChecker.test(input, expect, 406))

    # def test_redeclpara_1(self):
    #     input = """foo: function void(x: integer, x:string){}"""
    #     expect = "Redeclared Parameter: x"
    #     self.assertTrue(TestChecker.test(input, expect, 407))

    # def test_redeclpara_2(self):
    #     input = """foo: function void(inherit y: float, out x: integer, inherit out z: string, x:array[1,2,3,4] of integer, z: boolean){}"""
    #     expect = "Redeclared Parameter: x"
    #     self.assertTrue(TestChecker.test(input, expect, 408))

    # def test_undeclid_1(self):
    #     input = """x: integer = y;"""
    #     expect = "Undeclared Identifier: y"
    #     self.assertTrue(TestChecker.test(input, expect, 409))

    # def test_undeclid_2(self):
    #     input = """x: integer = 5;
    #     main: function void() {
    #         y = x;
    #     }"""
    #     expect = "Undeclared Identifier: y"
    #     self.assertTrue(TestChecker.test(input, expect, 410))

    # def test_undeclid_3(self):
    #     input = """x: auto = 2 + 3 * y;
    #     y: integer = 4;"""
    #     expect = "Undeclared Identifier: y"
    #     self.assertTrue(TestChecker.test(input, expect, 411))

    # def test_undeclid_4(self):
    #     input = """x: function string(y: integer){}
    #     y: auto = x(z);"""
    #     expect = "Undeclared Identifier: z"
    #     self.assertTrue(TestChecker.test(input, expect, 412))

    # def test_undeclfunc_1(self):
    #     input = """foo: function integer(){}
    #     x: integer = bar();"""
    #     expect = "Undeclared Function: bar"
    #     self.assertTrue(TestChecker.test(input, expect, 413))

    # def test_undeclfunc_2(self):
    #     input = """foo: function integer(){bar();}
    #     """
    #     expect = "Undeclared Function: bar"
    #     self.assertTrue(TestChecker.test(input, expect, 414))

    # def test_noentrypoint(self):
    #     input = """a: integer;
    #     b: float;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 417))

    # def test_arrlit_1(self):
    #     input = """main: function void(){}
    #             foo: function auto(){}
    #             bar: function auto(){}
    #             zar: function auto(){}
    #             a: auto = {{1,2},foo(), {bar(), zar()}};
    #             b,c: integer = bar(), zar();
    #             d: array[2] of boolean = foo();"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(d, ArrayType([2], BooleanType), FuncCall(foo, []))"
    #     self.assertTrue(TestChecker.test(input, expect, 415))

    # def test_arrlit_2(self):
    #     input = """main: function void(){}
    #             foo: function auto(){}
    #             bar: function auto(){}
    #             zar: function auto(){}
    #             a: array[2, 2] of float = {foo(), {bar(), zar()}};
    #             b,c: float = bar(), zar();
    #             d: array[2] of string = foo();"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(d, ArrayType([2], StringType), FuncCall(foo, []))"
    #     self.assertTrue(TestChecker.test(input, expect, 416))
    # def test51(self):
    #     input = """
    #     main: function void() {
    #         a: string = "wtfyt";
    #         b: integer;
    #         do {
    #             a: auto = 123;
    #             printInteger(b);
    #         }
    #         while (2-foo());
    #     }
    #     b: string;    
    #     foo: function auto() {
    #         return true;
    #         if (!foo())
    #             return a;
    #         while (false) return "false";
    #     }
    #     """
    #     expect = "Type mismatch in statement: DoWhileStmt(BinExpr(-, IntegerLit(2), FuncCall(foo, [])), BlockStmt([VarDecl(a, AutoType, IntegerLit(123)), CallStmt(printInteger, Id(b))]))"
    #     self.assertTrue(TestChecker.test(input, expect, 451))
    def test21(self):
        input = """
        main: function void() {
            a,b,c: auto = 1,"Hell",{{1.0,2},{21.9,7},{16,4}};
            writeFloat(a);
            b = readString();
            printInteger(c[0,0]);
        }
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([FloatLit(1.0), IntegerLit(2)]), ArrayLit([FloatLit(21.9), IntegerLit(7)]), ArrayLit([IntegerLit(16), IntegerLit(4)])])"
        self.assertTrue(TestChecker.test(input, expect, 421))