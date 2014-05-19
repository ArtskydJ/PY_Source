###### TriangleSolver.py ######
####### Joseph  Dykstra #######
##### Written: 2013-09-04 #####

from array import *
import random

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

def md2sd(d1,d2):
	return ((d1*3)+d2)

def drawHelp(n):
	result = ''
	if board[n]>0:
		result = 'Y '
	else:
		result = '. '
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
	

#while more than 1 pieces
#	while moves are available
#		loop through move database
#			match found?
#				add to db
#		get rand num from db indices
#		execute move
#		check for available moves
#	check num of pieces
#show solution


board = []
options = []
history = []
pegs = 14

while pegs>1:
	pegs=14
	random.seed()
	history.clear()
	options.clear()
	board.clear()
	for i in range(0,15):
		board.append(i)

	while openMoves():
		# loop through database
		options.clear()
		for i in range(0,18):
			if moveWorks(i):
				options.append(i)
		
		n=random.choice(options)
		history.append(n)
		executeMove(n)
				
	pegs=0
	for n in board:
		if n>0:
			pegs+=1

board.clear()
for i in range(0,15):
	board.append(i)

j=0
for i in history:
	draw()
	j+=1
	print("\nMove:{0}".format(j))
	executeMove(i)

draw()

