FactorMe = 7 #modified
LastFactorMe = 0
i=2
inloop=True
FactorMe*=2 #used to not be able to calculate if it started as a prime
while inloop:
    if (FactorMe%i)==0: #if it can be divided by i
        FactorMe/=i     #then divide it by i
        if LastFactorMe==i: #if last is equal to i
            inloop=False    #then exit the loop
        else:   #otherwise...
            i=2 #reset
        LastFactorMe=FactorMe
    else :   #if it can not be divided by i
        i+=1 #add 1 to i
print("The largest prime number is",i)

