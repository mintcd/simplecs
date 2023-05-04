import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test0(self):
        testcase = '''y :      function          auto      (  )      inherit     ci {  } T :      function          void      (      inherit          out     m7Gq :      array      [ 0 , 6_21 , 4 ]      of          integer      ,      inherit          out     r :      array      [ 8930_5 , 0 , 0 , 6_467_9356 ]      of          integer      ,      inherit     uOe :      string      )  {      break      ;  } '''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 100))
    def test1(self):
        testcase = '''z:    string    ;Y,AxC,gK,W:    array[0] of integer    ;v:    string    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 101))
    def test2(self):
        testcase = '''Xei: function  void ( inherit  out t: float ) inherit wt{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 102))
    def test3(self):
        testcase = '''wpk: array [1_3_4] of string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 103))
    def test4(self):
        testcase = '''h: function  float ( inherit y: array [0,2_1,0,0,32_3_2] of  boolean ) inherit M{}G: array [813_16_000,2_47] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 104))
    def test5(self):
        testcase = '''T: function  void ( inherit x: array [1_83_97165_55_65_1_5_718,70388] of  string , inherit S: string , out kLib: string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 105))
    def test6(self):
        testcase = '''LA: function  array [0] of  float ( inherit p: boolean ) inherit XXX3{}R: function  float () inherit UULLW{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 106))
    def test7(self):
        testcase = '''Jj: function  auto ( out x: array [0] of  string ) inherit bg47y_{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 107))
    def test8(self):
        testcase = '''mn: function  boolean ( inherit Y: auto , out c: array [0,0] of  boolean , inherit h: auto , inherit  out c: auto ) inherit MN{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 108))
    def test9(self):
        testcase = '''i: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 109))
    def test10(self):
        testcase = '''qw: function  auto ( inherit  out l: array [8703_97] of  float ) inherit AD{}Ef8d,R,XS3x,Y: array [4,424_8_1_2_51,71_3] of  float ;fu: function  auto ( inherit Y: array [0,4_7_7_28,450,0] of  float , out P: float , inherit aX: auto ) inherit n{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 110))
    def test11(self):
        testcase = '''cm: function  array [3_6,85] of  integer ( inherit  out b: array [0,39] of  integer , inherit  out Y: auto , inherit m1y: float ) inherit u{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 111))
    def test12(self):
        testcase = '''ntO5: function  array [0,44_6_58_7,246] of  boolean ( inherit Bk: array [0,4_817] of  boolean , inherit  out z: array [0,64] of  integer , out y: array [0,2,9_11356336_984_1] of  boolean , inherit  out hJ: auto , out l: integer , inherit  out h: auto , inherit E: integer ) inherit mz8{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 112))
    def test13(self):
        testcase = '''G: function  float ( inherit  out YmssX: boolean ){}W,r: array [0,0,0] of  string ;k,Q: string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 113))
    def test14(self):
        testcase = '''T: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 114))
    def test15(self):
        testcase = '''Q: function  array [5,0] of  boolean (){}GG: function  integer ( out aq: array [2,3762_5] of  integer ,y: auto , out h: string ) inherit U{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 115))
    def test16(self):
        testcase = '''r: function  array [0] of  integer ( out o: integer ,Iiws: array [97] of  string , out oc: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 116))
    def test17(self):
        testcase = '''kq,EW: float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 117))
    def test18(self):
        testcase = '''Gxkn: function  auto () inherit RGBb{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 118))
    def test19(self):
        testcase = '''w: float ;i6_: function  void () inherit OPSF{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 119))
    def test(self):
        testcase = '''mu: function  array [756] of  integer ( inherit  out Z9S: boolean ,L: auto , out A: array [0] of  integer ) inherit W{}O: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 1))
    def test21(self):
        testcase = '''co,__J,Wj,cIR,c,S: array [0,6] of  boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 121))
    def test22(self):
        testcase = '''gxM: function  boolean (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 122))
    def test23(self):
        testcase = '''main : function void (){
            if (1 + 2 == 3) print("OK");
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 123))
    def test24(self):
        testcase = '''main : function void (){
            if (1 + 2 == 3) {print("OK");}
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 124))
    def test25(self):
        testcase = '''a : integer = ((1 + 2*3) / 4) || 5;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 125))

    def test26(self):
        testcase = '''a,b,c : integer = 1,2,3;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 126))
    
    def test27(self):
        testcase = '''a,b,c : integer = 1,2;'''
        expect = '''Error on line 1 col 21: ;'''
        self.assertTrue(TestParser.test(testcase, expect, 127))
    
    def test28(self):
        testcase = '''a,b : integer = 1,2,3;'''
        expect = '''Error on line 1 col 19: ,'''
        self.assertTrue(TestParser.test(testcase, expect, 128))

    def test29(self):
        testcase = '''a : string = "abc"::"def";'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 129))

    def test30(self):
        testcase = '''a : string = "abc"::"def";'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 130))
    def test31(self):
        testcase = '''id1 : function string    ( inherit out id4 : array [ 10 , 4   ] of integer     , id3 : auto     )  { {  }     }  '''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 131))
    def test32(self):
        testcase = '''id1 : function float    (  ) inherit id5  {  }    id2 : function void  (  )  {  }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 132))

    def test33(self):
        testcase = '''main : function void (){
            if (1 + 2 == 3) print("OK");
            else print("ERROR");

        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 133))
    def test34(self):
        testcase = '''main : function void (){
            if (1 + 2 == 3) print("OK");
            else {print("ERROR"); return;}

        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 134))
    
    def test35(self):
        testcase = '''main : function void (){
            if ((1 + 2 == 3) && (1+4 > 5)) print("OK");
            else {print("ERROR"); return;}

        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 135))

    def test36(self):
        testcase = '''main : function void (){
            for (i < 2) print(i);

        }'''
        expect = '''Error on line 2 col 19: <'''
        self.assertTrue(TestParser.test(testcase, expect, 36))

    def test37(self):
        testcase = '''main : function void (){
            for (i = 0, i < 10, i + 1) print(i);

        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 137))
    def test38(self):
        testcase = '''main : function void (){
            while ((i > 2) && (i < 5)) print(i);

        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 138))

    def test39(self):
        testcase = '''main : function void (){
            for (i = 0, i < 10, i + 1) {
                print(i);
                return;
                break;
            }

        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 139))

    def test40(self):
        testcase = '''main : function void (){
            do {break;} while (x == 2);

        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 140))

    def test41(self):
        testcase = '''main : function void (){
            do {break;} while (x == 2)

        }'''
        expect = '''Error on line 4 col 8: }'''
        self.assertTrue(TestParser.test(testcase, expect, 141))

    def test41(self):
        testcase = '''main : function void (){
            do {break;} while (x == 2)

        }'''
        expect = '''Error on line 4 col 8: }'''
        self.assertTrue(TestParser.test(testcase, expect, 141))

    def test42(self):
        testcase = '''main : function void (){
            break;
            continue;
            return;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 142))

    def test43(self):
        testcase = '''main : function void (){
            {{{{{{{}}}}}}}
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 143))

    def test44(self):
        testcase = '''main : function void (){
            {{{{{{{}}}}}}}}
        }'''
        expect = '''Error on line 3 col 8: }'''
        self.assertTrue(TestParser.test(testcase, expect, 144))

    def test45(self):
        testcase = '''main : function void (){
            f(1,2,3,a,b,c);
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 145))

    def test46(self):
        testcase = '''main : function void (){
            if ( 4.0 ) id5 , id1 : boolean   = 2.0   , 2.0  ;   else continue ; 
            if ( 4.0 ) while ( 3.0 ) return ;     else id2 [ 5.0  ]   = 4.0 ;
        }'''
        expect = '''Error on line 2 col 27: ,'''
        self.assertTrue(TestParser.test(testcase, expect, 146))

    def test47(self):
        testcase = '''main : function void (){
            if ( 4.0 ) id5 , id1 : boolean   = 2.0   , 2.0  ;   else continue ; 
            if ( 4.0 ) while ( 3.0 ) return ;     else id2 [ 5.0  ]   = 4.0 ;
        }'''
        expect = '''Error on line 2 col 27: ,'''
        self.assertTrue(TestParser.test(testcase, expect, 147))
    
    def test48(self):
        testcase = '''main : function void (){
            if ( 4.0 ) 
                while ( 3.0 ) 
                    id4 ( 2.0 , 2.0 , 1     ) ;     
            else {id5 : integer}  ;  
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 148))

    def test49(self):
        testcase = '''main : function void (){
            do { if ( 2.0 ) continue ;   else while ( 5.0 )     return 3.0 ;      }  while ( 5.0 ) ;  
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 149))

    def test50(self):
        testcase = '''main: function void() {
            do { 
                for ( id5 = 4.0 , 4.0 , 4.0 ) 
                    if ( 1 ) id1 [ 1 , 4.0 , 1    ]   = 1 ;   
                    else id1 ( 3.0   ) ;        id5 , id4 : boolean   = 4.0   , 1  ;      
            }  while ( 4.0 ) ;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 150))

    def test51(self):
        testcase = '''main: function void() {
            { 
                id2  : integer   ;   
                continue ;   
                for ( id4 = 1 , 2.0 , 1 ) 
                    while ( 2.0 ) 
                        while ( 2.0 ) 
                            id5  = 4.0 ;             } 
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 151))

    def test52(self):
        testcase = '''main: function void() {
            a = ! - {1, "array", lit} ;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 152))

    def test53(self):
        testcase = '''main: function void() {
            a = ! - {1, "array", lit}      % - World     * ! 6   ;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 153))

    def test54(self):
        testcase = '''HvU7Kw:    string    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 154))
    
    def test55(self):
        testcase = '''a: function  auto ( out o: array [0] of  float , inherit AC1: string ) inherit IIi{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 155))

    def test56(self):
        testcase = '''E5l:    array    [0]    of        boolean    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 156))
    def test57(self):
        testcase = '''z:    function        array    [0,5_14_6_50,0,0,9_482_0_82891_7]    of        boolean    ()    inherit    Xb{RMo:    boolean    ;    break    ;}itLWJn7:    array    [64_04]    of        string    ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 157))
    def test58(self):
        testcase = '''p:    function        auto    (    inherit        out    iX:    array    [2,0,0]    of        string    ,    inherit        out    W5C:    integer    ,    out    i:    array    [0,60,0]    of        integer    )    inherit    H{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 158))
    def test59(self):
        testcase = ''''''
        expect = '''Error on line 1 col 0: <EOF>'''
        self.assertTrue(TestParser.test(testcase, expect, 159))
    def test60(self):
        testcase = '''eRVKH: array [0,0,4,0,0,0,0,7] of  float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 160))
    def test61(self):
        testcase = '''TA: function  float ( inherit V: auto , out h: auto ) inherit wt{ return ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 161))
    def test62(self):
        testcase = '''C: auto ;A: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 162))
    def test63(self):
        testcase = '''Tk: function  void (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 163))
    def test64(self):
        testcase = '''E: float ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 164))
    def test65(self):
        testcase = '''b77: function  array [38_10_9_38,421_01,0,0] of  integer ( out x6O: string , out C: array [0,26_3,2,94] of  integer , inherit  out HJ: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 165))
    def test66(self):
        testcase = '''Q: function  array [0] of  integer () inherit Y{}H4: function  array [6931] of  string ( inherit O: auto , inherit H: auto ,y: auto , inherit LfBUQ: array [772] of  integer , out A: array [0] of  boolean , inherit  out OZ: boolean , inherit  out RL: array [0] of  boolean ){}nM0,GA: integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 166))
    def test67(self):
        testcase = '''IO: integer = 1_2_3_4_5 ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 167))
    def test68(self):
        testcase = '''SHJ: function  void ( inherit Ov: integer , inherit U: array [0] of  float ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 168))
    def test69(self):
        testcase = '''c,QF7: array [1014_82,10_6_43_0] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 169))
    def test70(self):
        testcase = '''cD: function  array [41_7_2] of  integer () inherit Xn{}y,k,V,a,y,jVX: auto ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 170))
    def test71(self):
        testcase = '''C: function  void ( inherit Q82SG: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 171))
    def test72(self):
        testcase = '''q: function  auto ( inherit  out Ri: array [0] of  float , inherit  out q: string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 172))
    def test73(self):
        testcase = '''i3: function  void ( inherit WG: array [3_3_59_0_2,0] of  integer ) inherit VL{{}}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 173))
    def test74(self):
        testcase = '''Spl,b0a: auto ;Z: function  array [41] of  string (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 174))
    def test75(self):
        testcase = '''WV: function  string ( out u: auto ,Fk2: auto , inherit BG: auto ,exU6og: auto , inherit  out U: auto ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 175))
    def test76(self):
        testcase = '''L,f7WdGj: array [0] of  string ;f8,Ta: integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 176))
    def test77(self):
        testcase = '''S: function  void ( inherit JHHW: float , inherit G4: array [0] of  string , inherit  out n: auto ) inherit fh{ break ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 177))
    def test78(self):
        testcase = '''iPT8Z: function  array [49,93_1] of  string (cx: array [0] of  float , inherit wX: string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 178))
    def test79(self):
        testcase = '''jP: function  void ( out c: float ) inherit D{c: integer ; return ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 179))
    def test80(self):
        testcase = '''Q4: auto ;C: function  auto ( inherit  out Ag: float , inherit U: array [0] of  string , out vd: array [28,0] of  boolean , out Y3: array [0,8_5_8_16_63775_8,0] of  float ) inherit l{}iS: integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 180))
    def test81(self):
        testcase = '''K3: function  string ( inherit  out Nl: string ){}b: function  integer (P: integer ) inherit q{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 181))
    def test82(self):
        testcase = '''n: function  array [61012,289,23] of  float ( inherit  out DJoAG: float , inherit  out J: string ) inherit fj{}aZF8Q7: function  float ( inherit ZGEd: string ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 182))
    def test83(self):
        testcase = '''t: array [1,2] of boolean ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 183))
    def test84(self):
        testcase = '''s7: array [8_2_2] of  integer ;z: function  string (jcivbhg: boolean ) inherit Igwi{ continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 184))
    def test85(self):
        testcase = '''crD: function  void ( inherit  out E: array [1_6] of  float ){U();}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 185))
    def test86(self):
        testcase = '''d: function  auto ( inherit  out c: auto ) inherit Gh_wY{ return ;}j9: function  array [5_723] of  boolean ( inherit M: auto ) inherit gI{ break ; continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 186))
    def test87(self):
        testcase = '''C1: function  auto (G: array [52,345_79_08_06,431,0] of  float , inherit  out yS: integer , out EY: string ,Crp: array [99_5_2] of  string ) inherit v8{}d: function  array [0,0,7,27] of  integer ( inherit p: string , inherit v: boolean , inherit  out l: integer ,p: boolean ) inherit zn{}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 187))
    def test88(self):
        testcase = '''H: function  array [2] of  boolean ( inherit  out V: array [0,7732_8] of  integer ) inherit Zjr{}n: function  void (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 188))
    def test89(self):
        testcase = '''JN: function  auto ( inherit a7v: boolean ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 189))
    def test90(self):
        testcase = '''aj: array [0] of  integer ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 190))
    def test91(self):
        testcase = '''l,L: array [476_8] of  string ;'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 191))
    def test92(self):
        testcase = '''b71Al: function  void () inherit xZ{ break ; break ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 192))
    def test93(self):
        testcase = '''RQoR: function  array [49] of  integer ( inherit vH0: array [0,745,0,1_9_3_11487_3_40] of  boolean , inherit O: array [4,0] of  float ) inherit o{k();}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 193))
    def test94(self):
        testcase = '''
                    main : function void() {
                        if(!a){
                            flag=true;
                            continue;
                        }
                }'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 194))
    def test95(self):
        testcase = '''Xt: function  auto (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 195))
    def test96(self):
        testcase = '''lT: function  float ( out AtS: float , out BRDo3: auto , inherit  out f: auto ) inherit u{}iW: function  auto (W: auto ,O: boolean ) inherit V{ continue ;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 196))
    def test97(self):
        testcase = '''U: function  void ( out wZ: array [44_3287,57,0,23,0] of  integer ){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 197))
    def test98(self):
        testcase = '''k3: function  array [4,0,0,78429_2_8559,0,9] of  float (){}'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 198))
    def test99(self):
        testcase = '''
                    main : function void () {
                        a : array [10] of integer = {};
                    }
                '''
        expect = '''successful'''
        self.assertTrue(TestParser.test(testcase, expect, 199))

    