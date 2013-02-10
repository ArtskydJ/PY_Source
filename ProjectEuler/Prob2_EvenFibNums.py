x=0
goto=4000000
temp=17
lasti=1
i=2
while i<goto:
    if i%2==0 : x=x+i
    temp=i
    i=lasti+i
    lasti=temp
print(x)
