def sigma2(num):
    j=0
    SUM=0
    for j in range(1,num+1,1):
        if ((num%j)==0):
            SUM+=j**2
    return SUM

def SIGMA2(num):
    SUM=0
    for i in range(num+1): 
        SUM+=sigma2(i)
    return SUM

print(SIGMA2(6)) #113
print(SIGMA2(10**15)%10**9) #RUNS TOO LONG!!!
