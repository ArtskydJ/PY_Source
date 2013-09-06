###### TriangleSolver.py ######
####### Joseph  Dykstra #######
##### Written: 2013-09-04 #####

from array import *
import easygui as eg
import sys

def md2sd(d1,d2):
	return ((d1*3)+d2)

def draw():
	# DRAW
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
pegs=14

"""
while more than 1 pieces
	while moves are available
		loop through move database
			match found?
				execute move
				add move to history
			else
				undo last move
				
		check for available moves
	check num of pieces
"""

history = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
moveNum = 0
startScan = 0

while pegs>1:
	while options>0:
	
		# MOVE
		valid=0
		i=0
		if startScan<0: startScan=0
		for i in range(startScan,18):		#if backing up, start from history...
			if (board[moves[md2sd(i,0)]] and board[moves[md2sd(i,1)]] and not board[moves[md2sd(i,2)]]):
				valid=1
				board[moves[md2sd(i,2)]]=board[moves[md2sd(i,0)]]
				board[moves[md2sd(i,1)]]=0
				board[moves[md2sd(i,0)]]=0
				break
			elif (board[moves[md2sd(i,2)]] and board[moves[md2sd(i,1)]] and not board[moves[md2sd(i,0)]]):
				valid=1
				board[moves[md2sd(i,0)]]=board[moves[md2sd(i,2)]]
				board[moves[md2sd(i,1)]]=0
				board[moves[md2sd(i,2)]]=0
				break
		
		"""if valid==0 and startScan>1:
			print("\n\nrepeat")
			for i in range(0,18):		#if backed up, repeat if not found
				if (board[moves[md2sd(i,0)]] and board[moves[md2sd(i,1)]] and not board[moves[md2sd(i,2)]]):
					valid=1
					board[moves[md2sd(i,2)]]=board[moves[md2sd(i,0)]]
					board[moves[md2sd(i,1)]]=0
					board[moves[md2sd(i,0)]]=0
					break
				elif (board[moves[md2sd(i,2)]] and board[moves[md2sd(i,1)]] and not board[moves[md2sd(i,0)]]):
					valid=1
					board[moves[md2sd(i,0)]]=board[moves[md2sd(i,2)]]
					board[moves[md2sd(i,1)]]=0
					board[moves[md2sd(i,2)]]=0
					break"""
		
		print("\n{0}alid move".format("V" if valid else "Inv"));		# print validity
		for n in history:
			print(n)
		print("MoveNum:",moveNum)
		
		if valid==0:
			# undo last move
			history[moveNum] = -1
			moveNum -= 1
			if moveNum<0: moveNum=0
			startScan=history[moveNum]+1	# I think +1...
			print("startScan:",startScan)
		else:
			print("i:",i)
			history[moveNum] = i
			moveNum += 1
			startScan = 0
		
		options=0
		for n in range(0,18):		# check if more moves available
			if	(board[moves[md2sd(n,0)]] and board[moves[md2sd(n,1)]] and not board[moves[md2sd(n,0)]]):
				options+=1
			elif(board[moves[md2sd(n,0)]] and board[moves[md2sd(n,0)]] and not board[moves[md2sd(n,1)]]):
				options+=1
				
	pegs=0
	for n in board:
		if n>0:
			pegs+=1

draw()


