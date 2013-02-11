def isprime(n): #from the internet :)
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


inloop=True
size=1
i=3
temp=0
while inloop:
    if isprime(i):
        size+=1
        #print("prime:",i)
    i+=2
    if size>=10001:
        i-=2
        temp+=1
        inloop=False
print(i)
