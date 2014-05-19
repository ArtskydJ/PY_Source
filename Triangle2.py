###### Triangle.py ######
##### Ported from C #####
#### Joseph  Dykstra ####
### Free, Open Source ###
## Written: 2013-06-28 ##
# Ported: Tu 2013-09-03 #

from array import *

def md2sd(d1,d2):
	return ((d1*3)+d2)

def drawHelp(n):
	result = ''
	if board[n]>0:
		if n>=10:
			result = '{0} '.format(n)
		else:
			result = ' {0} '.format(n)
	else:
		result = ' . '
	return result

def draw():
	# DRAW
	print("    {0}".format(
		drawHelp(0)
	))
	print("   {0}{1}".format(
		drawHelp(1),
		drawHelp(2)
	))
	print("  {0}{1}{2}".format(
		drawHelp(3),
		drawHelp(4),
		drawHelp(5)
	))
	print(" {0}{1}{2}{3}".format(
		drawHelp(6),
		drawHelp(7),
		drawHelp(8),
		drawHelp(9)
	))
	print("{0}{1}{2}{3}{4}".format(
		drawHelp(10),
		drawHelp(11),
		drawHelp(12),
		drawHelp(13),
		drawHelp(14)
	))

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
options = 2
fromPeg = 0
toPeg = 0
while options>0:
	draw()
	print("Available Moves: ",options)

	# MOVE
	valid=0
	while valid==0:
		##input box a-o and a-o
		fromPeg = int(input("\nMove peg from: "),10)
		toPeg =   int(input("Jump over peg: "),10)
		if (fromPeg>=0 and fromPeg<15 and toPeg>=0 and toPeg<15):		# move if valid
			for i in range(0,18):
				if (moves[md2sd(i,0)]==fromPeg and moves[md2sd(i,1)]==toPeg or
					moves[md2sd(i,2)]==fromPeg and moves[md2sd(i,1)]==toPeg):
					if executeMove(i):
						valid=1
		print("{0}alid move".format("V" if valid else "Inv"))		# print valid yes/no
	
	##check if more moves available
	options=countMoves()
draw()
options=0
for n in board:
	if n: options+=1
print("You had {0} pieces left!".format(options))



