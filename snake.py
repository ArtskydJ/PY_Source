#snake.bas #INIT start
import time
import array
print("  /-----\  |\      |        /\        |   /  |-----  | ")
print(" (         | \     |       /  \       |  /   |       | ")
print("  \        |  \    |      /    \      | /    |       | ")
print("   \--\    |   \   |     /------\     |<     |-----  | ")
print("       \   |    \  |    /        \    | \    |       | ")
print("        )  |     \ |   /          \   |  \   |         ")
print(" \-----/   |      \|  /            \  |   \  |-----  * ")
print(" ")
print(" |\    /|   /\   |--\  |--     |--\ \  /     --|--  /--\  /--\ |-- |-\ |  |     |--\  \  / | / /--\ --|-- |-\   /\   ")
print(" | \  / |  /--\  |   ) |--     |--<  \/        |   (    ) \--\ |-- |-/ |--|     |   )  \/  |<  \--\   |   |-/  /--\  ")
print(" |  \/  | /    \ |--/  |--     |--/  |       \-|    \--/  \--/ |-- |   |  |     |--/   |   | \ \--/   |   | \ /    \ ")
print(" ")
print(" \    /\    / -|- --|-- |  |     --|--  /--\  /--\ -|-   /\   |  |     | / |-\ |  | --|-- \-- ")
print("  \  /  \  /   |    |   |--|       |   (    ) \--\  |   /--\  |--|     |<  |-/ |  |   |    \  ")
print("   \/    \/   -|-   |   |  |     \-|    \--/  \--/ -|- /    \ |  |     | \ | \ \--/   |   --\ ")
time.wait(3000)#
playing="y"
while playing=="y":
        #PLAY AGAIN loop
	#button 0, 0, 100, 20, type, "Slow|Medium|Fast|Death", "choice"
	grow=1          #if (type="Death", 25 if (type!="Death", 1)) #how much it grows
	startlength=3 #if (type="Death", 1, if (type!="Death", 3)) #constant, how long the snake is when the game starts
	b=16 #how many pixels each block is
	f=255 #constant for full transparency
	height=24 #how many blocks high it is
	width=24  #how many blocks wide it is
	dir=27 #direction, 25=L, 26=U, 27=R, 28=D
	dead=0 #0=false, 1=true, if the snake is dead
	foodeaten=0 #0=false, 1=true, if the food is eaten
	delaytime=100 #if(type="Death", 50 (if type!="Death", 80) #starting speed, lower value, more speed, 80 is good
	score=0 #how much score you start with
	length=startlength #how long the snake is
	#m="Game Over"
	x=1 #throwaway variable
	y=1 #throwaway variable
	z=1 #throwaway variable
	fx=startlength #x position of the front of the snake
	fy=1 #y position of the front of the snake
	lx=1 #x position of the back of the snake
	ly=1 #y position of the back of the snake
	#dim pos(width,height)
	x=1
	for x in width:
                y=1
		for y in height:
			#pos(x,y)=0
        x=1
	for x in startlength:
		pos(x,1)=x
	cls #INIT end
	while dead==0
		#ALIVE loop
		z=0 #reset z
		while z=0 #FOOD start
			{
			x=round((rnd)*(width-1))+1
			y=round((rnd)*(height-1))+1
			if pos(x,y)=0 :
				z=1
				pos(x,y)=-1 #FOOD end
			}
		if debug==True : at width*b+2,14 : print "x=";x;", y=";y
		x=0 #reset x
		y=0 #reset y
		z=0 #reset z
		foodeaten=0
		dead=0
		while (foodeaten=0 and dead=0):
			#ALIVE AND HUNGRY loop
			#delay delaytime #um...
			x=inkey #MOVING start
			if x=chr(27) + chr(4)  and dir!=27 : dir=25  #(Left)
			if x=chr(27) + chr(9)  and dir!=28 : dir=26  #(Up)
			if x=chr(27) + chr(5)  and dir!=25 : dir=27  #(Right)
			if x=chr(27) + chr(10) and dir!=26 : dir=28 #(Down)
			if dir=25 : #if moving LEFT
				n=pos(fx-1,fy)
				if fx<2 : dead=1
				if n>1 : dead=1
				if n<2 : fx=fx-1 : pos(fx,fy)=length+1
				if n=-1 : foodeaten=1 : length=length+grow
			if dir=26 : #if moving UP
				n=pos(fx,fy-1)
				if fy<2 : dead=1
				if n>1 : dead=1
				if n<2 : fy=fy-1 : pos(fx,fy)=length+1
				if n=-1 : foodeaten=1 : length=length+grow
			if dir=27 : #if moving RIGHT
				n=pos(fx+1,fy)
				if fx>width-1 : dead=1
				if n>1 : dead=1
				if n<2 : fx=fx+1 : pos(fx,fy)=length+1
				if n=-1 : foodeaten=1 : length=length+grow
			if dir=28 : #if moving DOWN
				n=pos(fx,fy+1)
				if fy>height-1 : dead=1
				if n>1 : dead=1
				if n<2 : fy=fy+1 : pos(fx,fy)=length+1
				if n=-1 : foodeaten=1 : length=length+grow
			if dead=0 :
				for x=1 to width
					for y=1 to height
					if pos(x,y)=1 : lx=x :  ly=y
					if pos(x,y)>0 : pos(x,y)=pos(x,y)-1
			#MOVING end
			#rect 0,0,480,640, color rgb(f,f,f) filled #no such drawing function in python
			if debug==True
				rect 0,160,480,640, color rgb(f,f,f) filled
			#rect lx*b-(b-1), ly*b-(b-1), STEP b-1, b-1, color rgb(f,f,f) filled
			#rect 0, 0, b*width, b*height, color rgb(0,0,100)
			for x=1 to width
				for y=1 to height
					if pos(x,y)>0 : rect x*b-(b-1), y*b-(b-1), STEP b-1, b-1, color rgb(0,f,0) filled
					if pos(x,y)<0 : rect x*b-(b-1), y*b-(b-1), STEP b-1, b-1, color rgb(f,0,0) filled
			#at width*b+2,2 : print "Score: ";score #no such command in python
			if debug==True
				for x=1 to width
					for y=1 to height
						at (x*b)*2, (y*b+(b*height)+2)*2 : print pos(x,y)
			#ALIVE AND HUNGRY loop
		if dead=0 :
			for x=1 to width
				for y=1 to height
					if pos(x,y)>0 then pos(x,y)=pos(x,y)+grow
			score=score+1
		delaytime=delaytime*0.9
		#HUNGRY loop
	#PLAY AGAIN loop
	#GAME OVER
	#at (width*b-textwidth(m))/2, (height*b-textheight(m))/2 : print m
	#delay 1000 #at width*b/2-50, height*b/2+5  : input "Play again, y/n", playing
	#cls
