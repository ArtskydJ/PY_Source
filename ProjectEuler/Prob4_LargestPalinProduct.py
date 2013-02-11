#A palindromic number reads the same both ways.
#The largest palindrome made from the product of
#two 2-digit numbers is 9009 = 91*99.
#
#--- http://projecteuler.net/problem=4 ---
#
#Find the largest palindrome made from the product of two 3-digit numbers.
#
# 5 or 6 digits

def palindrome(inx,ini,inj):
    ret=False
    a= (inx%10)
    b=((inx%100)            -a)//10
    c=((inx%1000)         -b-a)//100
    d=((inx%10000)      -c-b-a)//1000
    e=((inx%100000)   -d-c-b-a)//10000
    f=((inx%1000000)-e-d-c-b-a)//100000
    #if (b==f and c==e and a==0) or (a==f and b==e and c==d and f!=0):
    if (inx>=1000  and inx<=10000  and a==d and b==c)\
    or (inx>=10000 and inx<=100000 and a==e and b==d)\
    or (inx>=100000 and       a==f and b==e and c==d):
        ret=True
        print("palindrome:",inx,"=",ini,"*",inj)
    #print("A=",a," B=",b," C=",c," D=",d," E=",e," F=",f)
    return ret

x=0
y=0
i=10
j=10
ei=0
ej=0
lo=800
hi=999
for i in range(hi,lo,-1):
    for j in range(hi,lo,-1):
        y=i*j
        #print(y)
        if palindrome(y,i,j):
            if y>x:
                ei=i
                ej=j
                x=y
print("-----")
print(x,"=",ei,"*",ej)
