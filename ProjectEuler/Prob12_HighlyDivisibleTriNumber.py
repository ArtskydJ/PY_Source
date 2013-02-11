##def triangular(num):
##    x=0
##    for k in range(num,0,-1):
##        x+=k
##    return x

def divisors(num):
    j=0
    divs=0
    for j in range(1,num+1,1):
        if ((num%j)==0):
            divs+=1
    return divs

def divisors2(num):
    j=1
    divs=1
    for j in range(1,num,1):
        if ((num%j)==0):
            divs+=1
            j=1
            num/=j
            if num==1:
                break
    return divs

i=1
tri=1
printing=False
inloop=True
while inloop:
    if divisors2(tri)>500:
        inloop=False
    if inloop==True:
        i+=1
        tri+=i
        if printing:
            print(tri)
            if tri%10==0:
                print(" ",divisors2(tri))
print(tri)
