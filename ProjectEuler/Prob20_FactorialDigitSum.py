from math import *
import string
#from string import *

n=factorial(100)
s=format(n)
sTemp="hi"
x=0
for i in range(len(s)):
    sTemp=str.index(s,i)
    x+=int(sTemp)
print(x)
