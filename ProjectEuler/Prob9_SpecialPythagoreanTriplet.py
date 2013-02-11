##A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
##
##a^2 + b^2 = c^2
##For example, 32 + 42 = 9 + 16 = 25 = 5^2.
##
##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.

a,b,c=0,0,0
for a in range(800):
    for b in range(800):
        c=1000-a-b
        if ((a*a) + (b*b) == (c*c)):
            print("a=",a,"b=",b,"c=",c,"a+b+c=",a+b+c,"a*b*c=",a*b*c)
