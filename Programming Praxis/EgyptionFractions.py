########################
## Egyption Fractions ##
##   Joseph Dykstra   ##
########################

#constants
tries=5
num = 7
den = 12
NOanswersAllowed = 10


frac = num/den #float
answer = bytearray([NOanswersAllowed,tries]) #int array

num = 7  #int(input('Numerator: '))
den = 15 #int(input('Denominator : '))
looped1=0
looped2=0
looped1.int = 0 #int
looped2.int = 0 #int
while looped1<NOanswersAllowed:
	while looped2<tries:
		answer[looped1,looped2]=0
		looped2+=1
	looped1+=1
	looped2=0

while looped1<tries:
	while frac>0 and looped2<NOanswersAllowed:
		exit=false #bool
		n=1 #int
		while exit==false:
			if (1/n+1)>frac:
				exit=true
			else:
				n+=1
		answer[looped2,looped1]=n
		frac=frac-(1/n)
		looped2+=1
	looped1+=1
	looped2=0

looped1=0 #reset
looped2=0 #reset
while looped1<NOanswersAllowed:
	while looped2<tries:
		print('1/',answer[looped1,looped2])
		looped2+=1
	print()
	looped1+=1
	looped2=0
