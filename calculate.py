# Wheel diameter in inches:
wheelInDia = 3.212598

# Distance between wheels in inches
robotTrack = 5.01

### DO NOT CHANGE ANYTHING BELOW THIS ###
import math
import string

inchesTraveledForEachRotation = wheelInDia * math.pi
inchesTraveledForEachDegree = inchesTraveledForEachRotation / 360
trackCircumference = robotTrack * math.pi

def straight(num):
	return num / inchesTraveledForEachDegree

def turn(num):
	return num * trackCircumference / inchesTraveledForEachRotation #was degree

def printHelp():
	print ""
	print "Enter 'q' to quit,"
	print "      't' to switch to turning mode,"
	print "      's' to switch to straight mode,"
	print "      'h' to view this help again,"
	print "      a number to calculate the degrees,"
	print "      and <enter> to submit your input."

def longMode(mode):
	if mode == "s": return "Straight"
	elif mode == "t": return "Turn"
	else: return "Quit"

printHelp()
mode = "s"
while mode != "q":
	print ""
	inpt = raw_input(longMode(mode) + ": ")
	lwrInpt = string.lower(inpt)
	if lwrInpt == "t" or lwrInpt == "s":
		mode = lwrInpt
		print "Switching to " + string.lower(longMode(lwrInpt)) + " mode."
	elif lwrInpt == "q":
		mode = lwrInpt
	elif lwrInpt == "h":
		printHelp()
	else:
		try: flt = float(inpt)
		except: print "Unknown input"
		else:
			if mode == "t":
				print turn(flt)
			elif mode == "s":
				print straight(flt)
