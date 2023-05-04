import unittest
from TestUtils import TestLexer


# class LexerSuite(unittest.TestCase):
#     def test0(self):
#         input = "zeFWytGX h03fektIGSu zjFWBohVHdD l90EvBNob ___ oY1ait id ___abcd"
#         expected = "zeFWytGX,h03fektIGSu,zjFWBohVHdD,l90EvBNob,___,oY1ait,id,___abcd,<EOF>"
#         self.assertTrue(TestLexer.test(input,expected, 0))

#     def test1(self):
#         input = '''SuR LY I6 pBKY?o5xp39'''
#         expected = '''SuR,LY,I6,pBKY,Error Token ?'''
#         self.assertTrue(TestLexer.test(input,expected, 1))

#     def test2(self):
#         input = """// inline comment
#                    // inline comment"""
#         expected = "<EOF>"
#         self.assertTrue(TestLexer.test(input,expected, 2))

#     def test3(self):
#         input = """/* This is
#                     a block
#                     comment*/"""
#         expected = "<EOF>"
#         self.assertTrue(TestLexer.test(input,expected, 3))

#     def test4(self):
#         input = """/* This is
#                     a block
#                     comment*/ */"""
#         expected = "*,/,<EOF>"
#         self.assertTrue(TestLexer.test(input,expected, 4))

#     def test5(self):
#         input = """ /***************************\
#                     *                           *
#                     *                           *
#                     * This comment is nice      *
#                     *                           *
#                     \***************************/"""
#         expected = "<EOF>"
#         self.assertTrue(TestLexer.test(input,expected, 5))

#     def test6(self):
#         input = """ /* This is a block comment */
#                     // This is a line comment
#                     /* Comment with multiple lines
#                        Hello comments
#                     */
#                     /*
#                         Comment multiple lines
#                     */
#                     /* nested comments
#                         # inline comment
#                         # inline comment
#                     */"""
#         expected = "<EOF>"
#         self.assertTrue(TestLexer.test(input,expected, 6))

#     def test7(self):
#         input = """ /* /* # // /b/r/n */ */
#                     /*/* Comment is non-greedy */ */"""
#         expected = "*,/,*,/,<EOF>"
#         self.assertTrue(TestLexer.test(input,expected,7))
    
#     def test8(self):
#         input = """ // line 1 \b \t
#                         line 2 not allowed
#                     // line 3"""
#         expected = "line,2,not,allowed,<EOF>"
#         self.assertTrue(TestLexer.test(input,expected, 8))
    
#     def test9(self):
#         input = """ //!/usr/bin/env python3
#                     #// -*- coding: UTF-8 -*-"""
#         expected = "Error Token #"
#         self.assertTrue(TestLexer.test(input,expected, 9))

#     def test10(self):
#         input = """ <!-- begin& wsf_resource_nodes -->
#                     <!-- end: wsf_resource_nodes -->"""
#         expected = "<,!,-,-,begin,Error Token &"
#         self.assertTrue(TestLexer.test(input,expected, 111))

#     def test11(self):
#         input = """ 0 27_916095 787 9__8733437 2921594589_ """
#         expected = "0,27916095,787,9,__8733437,2921594589,_,<EOF>"
#         self.assertTrue(TestLexer.test(input,expected, 11))

#     def test12(self):
#         input = """ 0x131321 0X89ABC 0xffffff 0xABC 0X2132 """
#         expected = "0,x131321,0,X89ABC,0,xffffff,0,xABC,0,X2132,<EOF>"
#         self.assertTrue(TestLexer.test(input,expected, 12))
    
#     def test13(self):
#         self.assertTrue(TestLexer.test("""true false""", "true,false,<EOF>", 13))

#     def test14(self):
#         self.assertTrue(TestLexer.test("""TRUE True TRue TRUe falSe
#                                         falSE FAlse truE False FAlSE""",
#                                         "TRUE,True,TRue,TRUe,falSe,falSE,FAlse,truE,False,FAlSE,<EOF>",14))
#     def test15(self):
#         self.assertTrue(TestLexer.test(
#             """0._74991 36_.34200E6 64_613.8155906524 0.794833581e-68 0.061 0E-01 34_6e88 0.23_758E9008 0E+36169 0.08403 """,
#             "0.,_74991,36,_,.,34200E6,64613.8155906524,0.794833581e-68,0.061,0E-01,346e88,0.23,_758E9008,0E+36169,0.08403,<EOF>",
#             15
#         ))
#     def test16(self):
#         self.assertTrue(TestLexer.test(
#             """00001.12 0e-432 01e-542400 000313121.e000313""",
#             "0,0,0,0,1.12,0e-432,0,1e-542400,0,0,0,313121.e000313,<EOF>", 16
#         ))
    
#     def test17(self):
#         self.assertTrue(TestLexer.test(
#             """123e e123 e-1 -e12 13e1 1.e3 .e10""",
#             """123,e,e123,e,-,1,-,e12,13e1,1.e3,.,e10,<EOF>""",
#             17
#         ))

#     def test18(self):
#         self.assertTrue(TestLexer.test(
#             """ "" "String" " " "?" "-" "//" "Mulitiple Characters" """,
#             """,String, ,?,-,//,Mulitiple Characters,<EOF>""",
#             18
#         ))

#     def test19(self):
#         self.assertTrue(TestLexer.test(
#             """
#             ""
#             "OK"
#             'OK'
#             "OK'
#             'OK"
#             """,
#             """,OK,Error Token '""",
#             19
#         ))
#     def test20(self):
#         testcase = '''{true, false, true, false}'''
#         expect = '''{,true,,,false,,,true,,,false,},<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 20))
#     def test21(self):
#         testcase = '''{1.23, 4.56, 7.89}'''
#         expect = '''{,1.23,,,4.56,,,7.89,},<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 21))
#     def test22(self):
#         testcase = '''{1, "hello", true, 3.14}'''
#         expect = '''{,1,,,hello,,,true,,,3.14,},<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 22))
#     def test23(self):
#         testcase = '''XHYX9jKkW'''
#         expect = '''XHYX9jKkW,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 23))
#     def test24(self):
#         testcase = '''"string unclosed'''
#         expect = '''Unclosed String: string unclosed'''
#         self.assertTrue(TestLexer.test(testcase, expect, 24))
#     def test25(self):
#         testcase = '''21312 3124 _234'''
#         expect = '''21312,3124,_234,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 25))
#     def test26(self):
#         testcase = '''123.213'''
#         expect = '''123.213,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 26))
#     def test27(self):
#         testcase = '''"Hello'''
#         expect = '''Unclosed String: Hello'''
#         self.assertTrue(TestLexer.test(testcase, expect, 27))
#     def test28(self):
#         testcase = '''"Hello\n World'''
#         expect = '''Unclosed String: Hello'''
#         self.assertTrue(TestLexer.test(testcase, expect, 28))
#     def test29(self):
#         testcase = '''{1, 2, 3, 4, 5}'''
#         expect = '''{,1,,,2,,,3,,,4,,,5,},<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 29))
#     def test30(self):
#         testcase = '''nKBGqD v3_wmG DrL_0FjArj xVf'''
#         expect = '''nKBGqD,v3_wmG,DrL_0FjArj,xVf,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 30))
#     def test31(self):
#         testcase = '''== = = ====='''
#         expect = '''==,=,=,==,==,=,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 31))
#     def test32(self):
#         testcase = '''-=-=----*&&&&'''
#         expect = '''-,=,-,=,-,-,-,-,*,&&,&&,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 32))
#     def test33(self):
#         testcase = '''[] () }{{{}}}}}}'''
#         expect = '''[,],(,),},{,{,{,},},},},},},<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 33))
#     def test34(self):
#         testcase = '''!= >= <= ?'''
#         expect = '''!=,>=,<=,Error Token ?'''
#         self.assertTrue(TestLexer.test(testcase, expect, 34))
#     def test35(self):
#         testcase = '''-1_000'''
#         expect = '''-,1000,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 35))
#     def test36(self):
#         testcase = '''"abc \\t xyz"'''
#         expect = '''abc \\t xyz,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 36))
#     def test37(self):
#         testcase = '''"Escaped characters: \\\\ \\n \\t \\r \\f \\b \\' \\""'''
#         expect = '''Escaped characters: \\\\ \\n \\t \\r \\f \\b \\' \\",<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 37))
#     def test38(self):
#         testcase = '''"A string with a double quote (\\") in it"'''
#         expect = '''A string with a double quote (\\") in it,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 38))
#     def test39(self):
#         testcase = '''"A string with an empty \\n line"'''
#         expect = '''A string with an empty \\n line,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 39))
#     def test40(self):
#         testcase = '''"Hello \\a"'''
#         expect = '''Illegal Escape In String: Hello \\a'''
#         self.assertTrue(TestLexer.test(testcase, expect, 40))
#     def test41(self):
#         testcase = '''a[0, 0], a[0, 1], a[0, 2], a[1, 0], a[1, 1], a[1, 2]'''
#         expect = '''a,[,0,,,0,],,,a,[,0,,,1,],,,a,[,0,,,2,],,,a,[,1,,,0,],,,a,[,1,,,1,],,,a,[,1,,,2,],<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 41))
#     def test42(self):
#         testcase = '''a : array[1, 2] of integer;'''
#         expect = '''a,:,array,[,1,,,2,],of,integer,;,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 42))
#     def test43(self):
#         testcase = '''123acb345'''
#         expect = '''123,acb345,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 43))
#     def test44(self):
#         testcase = '''+=++=='''
#         expect = '''+,=,+,+,==,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 44))
#     def test45(self):
#         testcase = '''sad$sad'''
#         expect = '''sad,Error Token $'''
#         self.assertTrue(TestLexer.test(testcase, expect, 45))
#     def test46(self):
#         testcase = '''== = = ====='''
#         expect = '''==,=,=,==,==,=,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 46))
#     def test47(self):
#         testcase = '''-=-=----*&&&&||||'''
#         expect = '''-,=,-,=,-,-,-,-,*,&&,&&,||,||,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 47))
#     def test48(self):
#         testcase = '''-=-=----*&&&&|||'''
#         expect = '''-,=,-,=,-,-,-,-,*,&&,&&,||,Error Token |'''
#         self.assertTrue(TestLexer.test(testcase, expect, 48))
#     def test49(self):
#         testcase = '''-=-=----*&&&'''
#         expect = '''-,=,-,=,-,-,-,-,*,&&,Error Token &'''
#         self.assertTrue(TestLexer.test(testcase, expect, 49))
#     def test50(self):
#         testcase = '''0_0_0'''
#         expect = '''0,_0_0,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 50))
#     def test51(self):
#         testcase = '''01_23'''
#         expect = '''0,123,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 51))
#     def test52(self):
#         testcase = '''_'''
#         expect = '''_,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 52))
#     def test53(self):
#         testcase = '''1__2__3'''
#         expect = '''1,__2__3,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 53))
#     def test54(self):
#         testcase = '''123_'''
#         expect = '''123,_,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 54))
#     def test55(self):
#         testcase = '''0.0'''
#         expect = '''0.0,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 55))
#     def test56(self):
#         testcase = '''0.123_456'''
#         expect = '''0.123,_456,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 56))
#     def test57(self):
#         testcase = '''1_000.0'''
#         expect = '''1000.0,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 57))
#     def test58(self):
#         testcase = '''-1.23'''
#         expect = '''-,1.23,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 58))
#     def test59(self):
#         testcase = '''1.23e+10'''
#         expect = '''1.23e+10,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 59))
#     def test60(self):
#         testcase = '''.'''
#         expect = '''.,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 60))
#     def test61(self):
#         testcase = '''abc()?'''
#         expect = '''abc,(,),Error Token ?'''
#         self.assertTrue(TestLexer.test(testcase, expect, 61))
#     def test62(self):
#         testcase = '''1e'''
#         expect = '''1,e,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 62))
#     def test63(self):
#         testcase = '''1.23e-'''
#         expect = '''1.23,e,-,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 63))
#     def test64(self):
#         testcase = '''""'''
#         expect = ''',<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 64))
#     def test65(self):
#         testcase = '''"He asked me: \\"Where is John?\\""'''
#         expect = '''He asked me: \\"Where is John?\\",<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 65))
#     def test66(self):
#         testcase = '''"tab and newline \\t \\n"'''
#         expect = '''tab and newline \\t \\n,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 66))
#     def test67(self):
#         testcase = '''1.2_e3'''
#         expect = '''1.2,_e3,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 67))
#     def test68(self):
#         testcase = '''1.e10'''
#         expect = '''1.e10,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 68))
#     def test69(self):
#         testcase = '''"\\  "'''
#         expect = '''Illegal Escape In String: \\ '''
#         self.assertTrue(TestLexer.test(testcase, expect, 69))
#     def test70(self):
#         testcase = '''"Hello'''
#         expect = '''Unclosed String: Hello'''
#         self.assertTrue(TestLexer.test(testcase, expect, 70))
#     def test71(self):
#         testcase = '''{1.23, 4.56, 7.89}'''
#         expect = '''{,1.23,,,4.56,,,7.89,},<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 71))
#     def test72(self):
#         testcase = '''{1, "hello", true, 3.14}'''
#         expect = '''{,1,,,hello,,,true,,,3.14,},<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 72))
#     def test73(self):
#         testcase = '''12312 _234'''
#         expect = '''12312,_234,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 73))
#     def test74(self):
#         testcase = '''"Many escapes \\n \\t \\r \\b \\f \\a \\" "'''
#         expect = '''Illegal Escape In String: Many escapes \\n \\t \\r \\b \\f \\a'''
#         self.assertTrue(TestLexer.test(testcase, expect, 74))
#     def test75(self):
#         testcase = '''2k2'''
#         expect = '''2,k2,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 75))
#     def test76(self):
#         testcase = '''!= >= <= ?'''
#         expect = '''!=,>=,<=,Error Token ?'''
#         self.assertTrue(TestLexer.test(testcase, expect, 76))
#     def test77(self):
#         testcase = '''[] ()[{] {}'''
#         expect = '''[,],(,),[,{,],{,},<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 77))
#     def test78(self):
#         testcase = '''::'''
#         expect = '''::,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 78))
#     def test79(self):
#         testcase = '''+ - * / %'''
#         expect = '''+,-,*,/,%,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 79))
#     def test80(self):
#         testcase = '''000'''
#         expect = '''0,0,0,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 80))
#     def test81(self):
#         testcase = '''i : integer; a : array[1, 2] of integer;'''
#         expect = '''i,:,integer,;,a,:,array,[,1,,,2,],of,integer,;,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 81))
#     def test82(self):
#         testcase = '''! && || == !='''
#         expect = '''!,&&,||,==,!=,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 82))
#     def test83(self):
#         testcase = '''-123_456_789'''
#         expect = '''-,123456789,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 83))
#     def test84(self):
#         testcase = '''0123'''
#         expect = '''0,123,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 84))
#     def test85(self):
#         testcase = '''{true, false, true, false}'''
#         expect = '''{,true,,,false,,,true,,,false,},<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 85))
#     def test86(self):
#         testcase = '''0. 39472e-83258 0.49E+8 0e-49 5931245.69E6 772.944 0.773 76.2542e-3'''
#         expect = '''0.,39472e-83258,0.49E+8,0e-49,5931245.69E6,772.944,0.773,76.2542e-3,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 86))
#     def test87(self):
#         testcase = '''1_2.3'''
#         expect = '''12.3,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 87))
#     def test88(self):
#         testcase = '''29 84_9_709_58_7_9 7_81_77'''
#         expect = '''29,8497095879,78177,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 88))
#     def test89(self):
#         testcase = '''== != > >= < <='''
#         expect = '''==,!=,>,>=,<,<=,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 89))
#     def test90(self):
#         testcase = '''lt SGIjhYX B5OFBaUo i9R3hM _ogmzn'''
#         expect = '''lt,SGIjhYX,B5OFBaUo,i9R3hM,_ogmzn,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 90))
#     def test91(self):
#         testcase = '''______a_______'''
#         expect = '''______a_______,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 91))
#     def test92(self):
#         testcase = '''{true, false, true, false}'''
#         expect = '''{,true,,,false,,,true,,,false,},<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 92))
#     def test93(self):
#         testcase = '''{"Kangxi", "Yongzheng", "Qianlong"}.'''
#         expect = '''{,Kangxi,,,Yongzheng,,,Qianlong,},.,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 93))
#     def test93(self):
#         testcase = '''and or for do if else while'''
#         expect = '''and,or,for,do,if,else,while,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 93))
#     def test94(self):
#         testcase = ''''''
#         expect = '''<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 94))
#     def test95(self):
#         testcase = '''1.2_3_4_5'''
#         expect = '''1.2,_3_4_5,<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 95))
#     def test96(self):
#         testcase = '''"\\'a\\"b\\"\\"" '''
#         expect = '''\\'a\\"b\\"\\",<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 96))
#     def test97(self):
#         testcase = '''/**/'''
#         expect = '''<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 97))
#     def test98(self):
#         testcase = '''{1, 2, 3}'''
#         expect = '''{,1,,,2,,,3,},<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 98))
#     def test99(self):
#         testcase = '''"\\"This is a string containing tab \\t \\""'''
#         expect = '''\\"This is a string containing tab \\t \\",<EOF>'''
#         self.assertTrue(TestLexer.test(testcase, expect, 99))
#     def test100(self):
#         testcase = '''"abc \b"'''
#         expect = '''Unclosed String: abc '''
#         self.assertTrue(TestLexer.test(testcase, expect, 100))


class LexerSuite(unittest.TestCase):
    #escape characters
    def test1(self):
        input = """123 "1234\\"yab" 456"""
        expected = """123,1234\\"yab,456,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected, 1))
    def test2(self):
        input = """123 "1234\"yab" 456"""
        expected = """123,1234,yab,Unclosed String:  456"""
        self.assertTrue(TestLexer.test(input,expected, 2))
    def test3(self):
        input = """123 "1234\\byab" 456"""
        expected = """123,1234\\byab,456,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected, 3))
    def test4(self):
        input = '''123 "1234\byab" 456'''
        expected = '''123,1234\byab,456,<EOF>'''
        self.assertTrue(TestLexer.test(input,expected, 4))
    def test5(self):
        input = """123 "123\\'yab" 456"""
        expected = """123,123\\'yab,456,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected, 5))
    def test6(self):
        input = """123 "1234\'yab" 456"""
        expected = """123,1234'yab,456,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected, 6))
    def test7(self):
        input = """123 "123\\xyab" 456"""
        expected = """123,Illegal Escape In String: 123\\x"""
        self.assertTrue(TestLexer.test(input,expected, 7))
    def test8(self):
        input = """123 "1234 \\\\ yab" 456"""
        expected = """123,1234 \\\\ yab,456,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected, 8))
    def test9(self):
        input = """123 "1234\\ byab" 456"""
        expected = """123,Illegal Escape In String: 1234\ """
        self.assertTrue(TestLexer.test(input,expected, 9))
    def test10(self):
        input = """123 "1234\ byab" 456"""
        expected = """123,Illegal Escape In String: 1234\ """
        self.assertTrue(TestLexer.test(input,expected, 10))
    #unclosed string
    def test11(self):
        input = """123 "1234\nyab" 456"""
        expected = """123,Unclosed String: 1234"""
        self.assertTrue(TestLexer.test(input,expected, 11))
    def test12(self):
        input = """123 "1234\\nyab" 456"""
        expected = """123,1234\\nyab,456,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected, 12))
    def test13(self):
        input = """123 "1234\fyab" 456"""
        expected = """123,Unclosed String: 1234"""
        self.assertTrue(TestLexer.test(input,expected, 13))
    def test14(self):
        input = """123 "1234\\fyab" 456"""
        expected = """123,1234\\fyab,456,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected, 14))
    def test15(self):
        input = """123 "123abc 456"""
        expected = """123,Unclosed String: 123abc 456"""
        self.assertTrue(TestLexer.test(input,expected, 15))
    def test16(self):
        input = """123 "1234\\"ab\\"?" 456"""
        expected = """123,1234\\"ab\\"?,456,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected, 16))
    def test17(self):
        input = """123 "1234\\byab""12\\"345" 456"""
        expected = """123,1234\\byab,12\\"345,456,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected, 17))
    def test18(self):
        input = """123 "1234\\byab""123\\"45 456"""
        expected = """123,1234\\byab,Unclosed String: 123\\"45 456"""
        self.assertTrue(TestLexer.test(input,expected, 18))
    def test19(self):
        input = """123 "1234\n" 456"""
        expected = """123,Unclosed String: 1234"""
        self.assertTrue(TestLexer.test(input,expected, 19))
    def test20(self):
        input = """123 1234"\nabcxyz" """
        expected = """123,1234,Unclosed String: """
        self.assertTrue(TestLexer.test(input,expected, 20))