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
		toPeg =   int(input("Move peg to: "),10)
		if (fromPeg>=0 and fromPeg<15 and toPeg>=0 and toPeg<15):		# move if valid
			for i in range(0,18):
				if (moves[md2sd(i,0)]==fromPeg and moves[md2sd(i,2)]==toPeg):
					if (board[moves[md2sd(i,0)]] and board[moves[md2sd(i,1)]] and not board[moves[md2sd(i,2)]]):
						valid=1
						board[moves[md2sd(i,2)]]=board[moves[md2sd(i,0)]]
						board[moves[md2sd(i,1)]]=0
						board[moves[md2sd(i,0)]]=0
					#break
				elif (moves[md2sd(i,2)]==fromPeg and moves[md2sd(i,0)]==toPeg):
					if (board[moves[md2sd(i,2)]] and board[moves[md2sd(i,1)]] and not board[moves[md2sd(i,0)]]):
						valid=1
						board[moves[md2sd(i,0)]]=board[moves[md2sd(i,2)]]
						board[moves[md2sd(i,1)]]=0
						board[moves[md2sd(i,2)]]=0
					#break
		print("{0}alid move".format("V" if valid else "Inv"));		# print valid yes/no
	
	##check if more moves available
	options=0
	for n in range(0,18):
		if(board[moves[md2sd(n,2)]] and board[moves[md2sd(n,1)]] and (not board[moves[md2sd(n,0)]])):
			options+=1
		if(board[moves[md2sd(n,0)]] and board[moves[md2sd(n,1)]] and (not board[moves[md2sd(n,2)]])):
			options+=1
draw()
options=0
for n in board:
	if n: options+=1
print("You had {0} pieces left!".format(options))



