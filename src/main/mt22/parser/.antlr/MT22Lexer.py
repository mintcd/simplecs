# Generated from c:\Projects\MT22compiler\src\main\mt22-Jasmin\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01c7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\7/\u012b\n/\f/\16/\u012e\13/\3\60\3\60\3\60\5\60")
        buf.write("\u0133\n\60\3\60\6\60\u0136\n\60\r\60\16\60\u0137\3\61")
        buf.write("\3\61\3\61\3\61\5\61\u013e\n\61\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62")
        buf.write("\u014e\n\62\3\63\3\63\3\63\5\63\u0153\n\63\3\64\3\64\3")
        buf.write("\64\5\64\u0158\n\64\3\64\7\64\u015b\n\64\f\64\16\64\u015e")
        buf.write("\13\64\3\64\5\64\u0161\n\64\3\65\3\65\3\65\3\65\3\65\5")
        buf.write("\65\u0168\n\65\3\65\3\65\3\65\3\65\3\65\5\65\u016f\n\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\5\66\u017c\n\66\3\67\3\67\7\67\u0180\n\67\f\67\16\67")
        buf.write("\u0183\13\67\3\67\3\67\3\67\38\38\78\u018a\n8\f8\168\u018d")
        buf.write("\138\39\39\79\u0191\n9\f9\169\u0194\139\39\59\u0197\n")
        buf.write("9\39\39\3:\3:\7:\u019d\n:\f:\16:\u01a0\13:\3:\3:\3:\3")
        buf.write(";\3;\3;\3;\7;\u01a9\n;\f;\16;\u01ac\13;\3;\3;\3<\3<\3")
        buf.write("<\3<\7<\u01b4\n<\f<\16<\u01b7\13<\3<\3<\3<\3<\3<\3=\6")
        buf.write("=\u01bf\n=\r=\16=\u01c0\3=\3=\3>\3>\3>\3\u01b5\2?\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\2_\2a\2c\2e\2g\60i\61k\62m\63o\64q\65s\66")
        buf.write("u\67w8y9{:\3\2\f\3\2\62;\4\2GGgg\b\2\n\n\f\f\16\17$$)")
        buf.write(")^^\t\2$$^^ddhhppttvv\3\2\63;\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\b\3\n\n\f\f\16\17$$))^^\4\2\f\f\16\17\5\2\n\f\17\17")
        buf.write("\"\"\2\u01dc\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\3}\3\2\2\2\5\u0083\3\2\2\2\7\u0088")
        buf.write("\3\2\2\2\t\u0090\3\2\2\2\13\u0096\3\2\2\2\r\u009f\3\2")
        buf.write("\2\2\17\u00a2\3\2\2\2\21\u00a7\3\2\2\2\23\u00ad\3\2\2")
        buf.write("\2\25\u00b1\3\2\2\2\27\u00ba\3\2\2\2\31\u00c2\3\2\2\2")
        buf.write("\33\u00c5\3\2\2\2\35\u00cd\3\2\2\2\37\u00d0\3\2\2\2!\u00d4")
        buf.write("\3\2\2\2#\u00db\3\2\2\2%\u00e2\3\2\2\2\'\u00e7\3\2\2\2")
        buf.write(")\u00ed\3\2\2\2+\u00ef\3\2\2\2-\u00f1\3\2\2\2/\u00f3\3")
        buf.write("\2\2\2\61\u00f5\3\2\2\2\63\u00f7\3\2\2\2\65\u00f9\3\2")
        buf.write("\2\2\67\u00fc\3\2\2\29\u00ff\3\2\2\2;\u0102\3\2\2\2=\u0105")
        buf.write("\3\2\2\2?\u0107\3\2\2\2A\u0109\3\2\2\2C\u010c\3\2\2\2")
        buf.write("E\u010f\3\2\2\2G\u0112\3\2\2\2I\u0114\3\2\2\2K\u0116\3")
        buf.write("\2\2\2M\u0118\3\2\2\2O\u011a\3\2\2\2Q\u011c\3\2\2\2S\u011e")
        buf.write("\3\2\2\2U\u0120\3\2\2\2W\u0122\3\2\2\2Y\u0124\3\2\2\2")
        buf.write("[\u0126\3\2\2\2]\u0128\3\2\2\2_\u012f\3\2\2\2a\u013d\3")
        buf.write("\2\2\2c\u014d\3\2\2\2e\u0152\3\2\2\2g\u0160\3\2\2\2i\u016e")
        buf.write("\3\2\2\2k\u017b\3\2\2\2m\u017d\3\2\2\2o\u0187\3\2\2\2")
        buf.write("q\u018e\3\2\2\2s\u019a\3\2\2\2u\u01a4\3\2\2\2w\u01af\3")
        buf.write("\2\2\2y\u01be\3\2\2\2{\u01c4\3\2\2\2}~\7c\2\2~\177\7t")
        buf.write("\2\2\177\u0080\7t\2\2\u0080\u0081\7c\2\2\u0081\u0082\7")
        buf.write("{\2\2\u0082\4\3\2\2\2\u0083\u0084\7c\2\2\u0084\u0085\7")
        buf.write("w\2\2\u0085\u0086\7v\2\2\u0086\u0087\7q\2\2\u0087\6\3")
        buf.write("\2\2\2\u0088\u0089\7d\2\2\u0089\u008a\7q\2\2\u008a\u008b")
        buf.write("\7q\2\2\u008b\u008c\7n\2\2\u008c\u008d\7g\2\2\u008d\u008e")
        buf.write("\7c\2\2\u008e\u008f\7p\2\2\u008f\b\3\2\2\2\u0090\u0091")
        buf.write("\7d\2\2\u0091\u0092\7t\2\2\u0092\u0093\7g\2\2\u0093\u0094")
        buf.write("\7c\2\2\u0094\u0095\7m\2\2\u0095\n\3\2\2\2\u0096\u0097")
        buf.write("\7e\2\2\u0097\u0098\7q\2\2\u0098\u0099\7p\2\2\u0099\u009a")
        buf.write("\7v\2\2\u009a\u009b\7k\2\2\u009b\u009c\7p\2\2\u009c\u009d")
        buf.write("\7w\2\2\u009d\u009e\7g\2\2\u009e\f\3\2\2\2\u009f\u00a0")
        buf.write("\7f\2\2\u00a0\u00a1\7q\2\2\u00a1\16\3\2\2\2\u00a2\u00a3")
        buf.write("\7g\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5\7u\2\2\u00a5\u00a6")
        buf.write("\7g\2\2\u00a6\20\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9")
        buf.write("\7n\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac")
        buf.write("\7v\2\2\u00ac\22\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af")
        buf.write("\7q\2\2\u00af\u00b0\7t\2\2\u00b0\24\3\2\2\2\u00b1\u00b2")
        buf.write("\7h\2\2\u00b2\u00b3\7w\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5")
        buf.write("\7e\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8")
        buf.write("\7q\2\2\u00b8\u00b9\7p\2\2\u00b9\26\3\2\2\2\u00ba\u00bb")
        buf.write("\7k\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd\7j\2\2\u00bd\u00be")
        buf.write("\7g\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\30\3\2\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7h\2\2\u00c4\32\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca")
        buf.write("\7i\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7t\2\2\u00cc\34")
        buf.write("\3\2\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7h\2\2\u00cf\36")
        buf.write("\3\2\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7w\2\2\u00d2\u00d3")
        buf.write("\7v\2\2\u00d3 \3\2\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9")
        buf.write("\7t\2\2\u00d9\u00da\7p\2\2\u00da\"\3\2\2\2\u00db\u00dc")
        buf.write("\7u\2\2\u00dc\u00dd\7v\2\2\u00dd\u00de\7t\2\2\u00de\u00df")
        buf.write("\7k\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7i\2\2\u00e1$\3")
        buf.write("\2\2\2\u00e2\u00e3\7x\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7k\2\2\u00e5\u00e6\7f\2\2\u00e6&\3\2\2\2\u00e7\u00e8")
        buf.write("\7y\2\2\u00e8\u00e9\7j\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7n\2\2\u00eb\u00ec\7g\2\2\u00ec(\3\2\2\2\u00ed\u00ee")
        buf.write("\7-\2\2\u00ee*\3\2\2\2\u00ef\u00f0\7/\2\2\u00f0,\3\2\2")
        buf.write("\2\u00f1\u00f2\7,\2\2\u00f2.\3\2\2\2\u00f3\u00f4\7\61")
        buf.write("\2\2\u00f4\60\3\2\2\2\u00f5\u00f6\7\'\2\2\u00f6\62\3\2")
        buf.write("\2\2\u00f7\u00f8\7#\2\2\u00f8\64\3\2\2\2\u00f9\u00fa\7")
        buf.write("(\2\2\u00fa\u00fb\7(\2\2\u00fb\66\3\2\2\2\u00fc\u00fd")
        buf.write("\7~\2\2\u00fd\u00fe\7~\2\2\u00fe8\3\2\2\2\u00ff\u0100")
        buf.write("\7?\2\2\u0100\u0101\7?\2\2\u0101:\3\2\2\2\u0102\u0103")
        buf.write("\7#\2\2\u0103\u0104\7?\2\2\u0104<\3\2\2\2\u0105\u0106")
        buf.write("\7>\2\2\u0106>\3\2\2\2\u0107\u0108\7@\2\2\u0108@\3\2\2")
        buf.write("\2\u0109\u010a\7>\2\2\u010a\u010b\7?\2\2\u010bB\3\2\2")
        buf.write("\2\u010c\u010d\7@\2\2\u010d\u010e\7?\2\2\u010eD\3\2\2")
        buf.write("\2\u010f\u0110\7<\2\2\u0110\u0111\7<\2\2\u0111F\3\2\2")
        buf.write("\2\u0112\u0113\7]\2\2\u0113H\3\2\2\2\u0114\u0115\7_\2")
        buf.write("\2\u0115J\3\2\2\2\u0116\u0117\7*\2\2\u0117L\3\2\2\2\u0118")
        buf.write("\u0119\7+\2\2\u0119N\3\2\2\2\u011a\u011b\7}\2\2\u011b")
        buf.write("P\3\2\2\2\u011c\u011d\7\177\2\2\u011dR\3\2\2\2\u011e\u011f")
        buf.write("\7=\2\2\u011fT\3\2\2\2\u0120\u0121\7<\2\2\u0121V\3\2\2")
        buf.write("\2\u0122\u0123\7\60\2\2\u0123X\3\2\2\2\u0124\u0125\7.")
        buf.write("\2\2\u0125Z\3\2\2\2\u0126\u0127\7?\2\2\u0127\\\3\2\2\2")
        buf.write("\u0128\u012c\5W,\2\u0129\u012b\t\2\2\2\u012a\u0129\3\2")
        buf.write("\2\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d^\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0132")
        buf.write("\t\3\2\2\u0130\u0133\5)\25\2\u0131\u0133\5+\26\2\u0132")
        buf.write("\u0130\3\2\2\2\u0132\u0131\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133\u0135\3\2\2\2\u0134\u0136\t\2\2\2\u0135\u0134\3")
        buf.write("\2\2\2\u0136\u0137\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138`\3\2\2\2\u0139\u013e\n\4\2\2\u013a\u013e")
        buf.write("\5c\62\2\u013b\u013c\7^\2\2\u013c\u013e\7$\2\2\u013d\u0139")
        buf.write("\3\2\2\2\u013d\u013a\3\2\2\2\u013d\u013b\3\2\2\2\u013e")
        buf.write("b\3\2\2\2\u013f\u0140\7^\2\2\u0140\u014e\7)\2\2\u0141")
        buf.write("\u0142\7^\2\2\u0142\u014e\7^\2\2\u0143\u0144\7^\2\2\u0144")
        buf.write("\u014e\7d\2\2\u0145\u0146\7^\2\2\u0146\u014e\7h\2\2\u0147")
        buf.write("\u0148\7^\2\2\u0148\u014e\7p\2\2\u0149\u014a\7^\2\2\u014a")
        buf.write("\u014e\7t\2\2\u014b\u014c\7^\2\2\u014c\u014e\7v\2\2\u014d")
        buf.write("\u013f\3\2\2\2\u014d\u0141\3\2\2\2\u014d\u0143\3\2\2\2")
        buf.write("\u014d\u0145\3\2\2\2\u014d\u0147\3\2\2\2\u014d\u0149\3")
        buf.write("\2\2\2\u014d\u014b\3\2\2\2\u014ed\3\2\2\2\u014f\u0150")
        buf.write("\7^\2\2\u0150\u0153\n\5\2\2\u0151\u0153\7^\2\2\u0152\u014f")
        buf.write("\3\2\2\2\u0152\u0151\3\2\2\2\u0153f\3\2\2\2\u0154\u0161")
        buf.write("\7\62\2\2\u0155\u015c\t\6\2\2\u0156\u0158\7a\2\2\u0157")
        buf.write("\u0156\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159\u015b\t\2\2\2\u015a\u0157\3\2\2\2\u015b\u015e\3")
        buf.write("\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f")
        buf.write("\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0161\b\64\2\2\u0160")
        buf.write("\u0154\3\2\2\2\u0160\u0155\3\2\2\2\u0161h\3\2\2\2\u0162")
        buf.write("\u0163\5g\64\2\u0163\u0164\5]/\2\u0164\u016f\3\2\2\2\u0165")
        buf.write("\u0167\5g\64\2\u0166\u0168\5]/\2\u0167\u0166\3\2\2\2\u0167")
        buf.write("\u0168\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\5_\60\2")
        buf.write("\u016a\u016f\3\2\2\2\u016b\u016c\5]/\2\u016c\u016d\5_")
        buf.write("\60\2\u016d\u016f\3\2\2\2\u016e\u0162\3\2\2\2\u016e\u0165")
        buf.write("\3\2\2\2\u016e\u016b\3\2\2\2\u016f\u0170\3\2\2\2\u0170")
        buf.write("\u0171\b\65\3\2\u0171j\3\2\2\2\u0172\u0173\7v\2\2\u0173")
        buf.write("\u0174\7t\2\2\u0174\u0175\7w\2\2\u0175\u017c\7g\2\2\u0176")
        buf.write("\u0177\7h\2\2\u0177\u0178\7c\2\2\u0178\u0179\7n\2\2\u0179")
        buf.write("\u017a\7u\2\2\u017a\u017c\7g\2\2\u017b\u0172\3\2\2\2\u017b")
        buf.write("\u0176\3\2\2\2\u017cl\3\2\2\2\u017d\u0181\7$\2\2\u017e")
        buf.write("\u0180\5a\61\2\u017f\u017e\3\2\2\2\u0180\u0183\3\2\2\2")
        buf.write("\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0184\3")
        buf.write("\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\7$\2\2\u0185\u0186")
        buf.write("\b\67\4\2\u0186n\3\2\2\2\u0187\u018b\t\7\2\2\u0188\u018a")
        buf.write("\t\b\2\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018cp\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018e\u0192\7$\2\2\u018f\u0191\5a\61\2")
        buf.write("\u0190\u018f\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3")
        buf.write("\2\2\2\u0192\u0193\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0195\u0197\t\t\2\2\u0196\u0195\3\2\2\2\u0197")
        buf.write("\u0198\3\2\2\2\u0198\u0199\b9\5\2\u0199r\3\2\2\2\u019a")
        buf.write("\u019e\7$\2\2\u019b\u019d\5a\61\2\u019c\u019b\3\2\2\2")
        buf.write("\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3")
        buf.write("\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2")
        buf.write("\5e\63\2\u01a2\u01a3\b:\6\2\u01a3t\3\2\2\2\u01a4\u01a5")
        buf.write("\7\61\2\2\u01a5\u01a6\7\61\2\2\u01a6\u01aa\3\2\2\2\u01a7")
        buf.write("\u01a9\n\n\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01ac\3\2\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad\3")
        buf.write("\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae\b;\7\2\u01aev\3")
        buf.write("\2\2\2\u01af\u01b0\7\61\2\2\u01b0\u01b1\7,\2\2\u01b1\u01b5")
        buf.write("\3\2\2\2\u01b2\u01b4\13\2\2\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write("\u01b7\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b6\u01b8\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01b9\7")
        buf.write(",\2\2\u01b9\u01ba\7\61\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc")
        buf.write("\b<\7\2\u01bcx\3\2\2\2\u01bd\u01bf\t\13\2\2\u01be\u01bd")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0")
        buf.write("\u01c1\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3\b=\7\2")
        buf.write("\u01c3z\3\2\2\2\u01c4\u01c5\13\2\2\2\u01c5\u01c6\b>\b")
        buf.write("\2\u01c6|\3\2\2\2\27\2\u012c\u0132\u0137\u013d\u014d\u0152")
        buf.write("\u0157\u015c\u0160\u0167\u016e\u017b\u0181\u018b\u0192")
        buf.write("\u0196\u019e\u01aa\u01b5\u01c0\t\3\64\2\3\65\3\3\67\4")
        buf.write("\39\5\3:\6\b\2\2\3>\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARRAY = 1
    AUTO = 2
    BOOLEAN = 3
    BREAK = 4
    CONTINUE = 5
    DO = 6
    ELSE = 7
    FLOAT = 8
    FOR = 9
    FUNCTION = 10
    INHERIT = 11
    IF = 12
    INTEGER = 13
    OF = 14
    OUT = 15
    RETURN = 16
    STRING = 17
    VOID = 18
    WHILE = 19
    ADD = 20
    SUB = 21
    MUL = 22
    DIV = 23
    MOD = 24
    NOT = 25
    AND = 26
    OR = 27
    EQUAL = 28
    NOT_EQUAL = 29
    LT = 30
    GT = 31
    LE = 32
    GE = 33
    CONCATE = 34
    LSB = 35
    RSB = 36
    LP = 37
    RP = 38
    LB = 39
    RB = 40
    SM = 41
    CL = 42
    DOT = 43
    CM = 44
    ASSIGN = 45
    INTLIT = 46
    FLOATLIT = 47
    BOOLEANLIT = 48
    STRINGLIT = 49
    ID = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52
    LINE_CMT = 53
    BLOCK_CMT = 54
    WS = 55
    ERROR_CHAR = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'array'", "'auto'", "'boolean'", "'break'", "'continue'", "'do'", 
            "'else'", "'float'", "'for'", "'function'", "'inherit'", "'if'", 
            "'integer'", "'of'", "'out'", "'return'", "'string'", "'void'", 
            "'while'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'::'", 
            "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "':'", "'.'", 
            "','", "'='" ]

    symbolicNames = [ "<INVALID>",
            "ARRAY", "AUTO", "BOOLEAN", "BREAK", "CONTINUE", "DO", "ELSE", 
            "FLOAT", "FOR", "FUNCTION", "INHERIT", "IF", "INTEGER", "OF", 
            "OUT", "RETURN", "STRING", "VOID", "WHILE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", 
            "GT", "LE", "GE", "CONCATE", "LSB", "RSB", "LP", "RP", "LB", 
            "RB", "SM", "CL", "DOT", "CM", "ASSIGN", "INTLIT", "FLOATLIT", 
            "BOOLEANLIT", "STRINGLIT", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "LINE_CMT", "BLOCK_CMT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "ARRAY", "AUTO", "BOOLEAN", "BREAK", "CONTINUE", "DO", 
                  "ELSE", "FLOAT", "FOR", "FUNCTION", "INHERIT", "IF", "INTEGER", 
                  "OF", "OUT", "RETURN", "STRING", "VOID", "WHILE", "ADD", 
                  "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
                  "NOT_EQUAL", "LT", "GT", "LE", "GE", "CONCATE", "LSB", 
                  "RSB", "LP", "RP", "LB", "RB", "SM", "CL", "DOT", "CM", 
                  "ASSIGN", "DECPART", "EXPPART", "CHAR_LIT", "ESC_SEQ", 
                  "ESC_ILLEGAL", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", 
                  "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "LINE_CMT", 
                  "BLOCK_CMT", "WS", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[50] = self.INTLIT_action 
            actions[51] = self.FLOATLIT_action 
            actions[53] = self.STRINGLIT_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            actions[60] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text.replace('_','')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text = self.text.replace('_','')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            if self.text[-1] in ['\b', '\f', '\n', '\r', '"', '\'', '\\']: 
            	raise UncloseString(self.text[1:-1])
            else: 
            	raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


