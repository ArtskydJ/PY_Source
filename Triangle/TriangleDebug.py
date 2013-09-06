###### Triangle.py ######
##### Ported from C #####
#### Joseph  Dykstra ####
### Free, Open Source ###
## Written: 2013-06-28 ##
# Ported: Tu 2013-09-03 #

from array import *

def md2sd(d1,d2):
	return ((d1*3)+d2)

def draw():
	print("\t\t\t\t\t0{0}\n\n\n".format(
		'====<|' if board[0]>0 else '\t'))
	print("\t\t\t\t1{0}\t2{1}\n\n\n".format(
		'====<|' if board[1]>0 else '\t',
		'====<|' if board[2]>0 else '\t'))
	print("\t\t\t3{0}\t4{1}\t5{2}\n\n\n".format(
		'====<|' if board[3]>0 else '\t',
		'====<|' if board[4]>0 else '\t',
		'====<|' if board[5]>0 else '\t'))
	print("\t\t6{0}\t7{1}\t8{2}\t9{3}\n\n\n".format(
		'====<|' if board[6]>0 else '\t',
		'====<|' if board[7]>0 else '\t',
		'====<|' if board[8]>0 else '\t',
		'====<|' if board[9]>0 else '\t'))
	print("\t10{0}\t11{1}\t12{2}\t13{3}\t14{4}\n".format(
		'====<|' if board[10]>0 else '\t',
		'====<|' if board[11]>0 else '\t',
		'====<|' if board[12]>0 else '\t',
		'====<|' if board[13]>0 else '\t',
		'====<|' if board[14]>0 else '\t'))

def countMoves():
	temp=0
	for n in range(0,18):		# check if more moves available
		if	(board[moves[md2sd(n,0)]]!=0 and board[moves[md2sd(n,1)]]!=0 and board[moves[md2sd(n,2)]]==0):
			temp+=1
		elif(board[moves[md2sd(n,2)]]!=0 and board[moves[md2sd(n,1)]]!=0 and board[moves[md2sd(n,0)]]==0):
			temp+=1
	return temp

def openMoves():
	ret=False
	if (countMoves()>0):
		ret=True
	return ret

def executeMove(x):
	ret=False
	if   (board[moves[md2sd(x,0)]]!=0 and board[moves[md2sd(x,1)]]!=0 and board[moves[md2sd(x,2)]]==0):
		board[moves[md2sd(x,2)]]=board[moves[md2sd(x,0)]]
		board[moves[md2sd(x,1)]]=0
		board[moves[md2sd(x,0)]]=0
		ret=True
	elif (board[moves[md2sd(x,2)]]!=0 and board[moves[md2sd(x,1)]]!=0 and board[moves[md2sd(x,0)]]==0):
		board[moves[md2sd(x,0)]]=board[moves[md2sd(x,2)]]
		board[moves[md2sd(x,1)]]=0
		board[moves[md2sd(x,2)]]=0
		ret=True
	return ret

def moveWorks(x):
	ret=False
	if ((board[moves[md2sd(x,0)]]!=0 and board[moves[md2sd(x,1)]]!=0 and board[moves[md2sd(x,2)]]==0) or
		(board[moves[md2sd(x,2)]]!=0 and board[moves[md2sd(x,1)]]!=0 and board[moves[md2sd(x,0)]]==0)):
		ret=True
	return ret

moves = [
	0, 1, 3 ,
	1, 3, 6 ,
	3, 6, 10,
	0, 2, 5 ,
	2, 5, 9 ,	#5
	5, 9, 14,
	2, 4, 7 ,
	4, 7, 11,
	1, 4, 8 ,
	4, 8, 13,	#10
	3, 7, 12,
	5, 8, 12,
	3, 4, 5 ,
	6, 7, 8 ,
	7, 8, 9 ,	#15
	10,11,12,
	11,12,13,
	12,13,14
]

board = array('i',range(0,15))
moveNum = 0
while openMoves():
	moveNum = int(input("\nMove #: "),10)
	if (moveNum>=0 and moveNum<18):		# move if valid
		if executeMove(moveNum):
			print("Valid move")
			draw()
			print("Available Moves: ",countMoves())
print(countMoves())
draw()
pieces=0
for n in board:
	if n: pieces+=1
print("You have {n} pieces left!".format(n=pieces))

#0
#12
#5
#4
#11
#15
#16
#7
#1
#4
#3
#12
#0

