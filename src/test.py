# from main.mt22.checker.StaticChecker import *

a = [1,2,3]

b = [4,5,6]

c = list(zip(a,b))

for ele in c: print(ele)
c[0][0] = 9
for ele in c: print(ele)
print(a)