#!/usr/bin/python
from time import sleep
import time, subprocess, os							
import RPi.GPIO as GPIO
from decimal import *
from subprocess import call							# I dont know what this is, or if I need it.
													# But damn am I scared to delete it.

GPIO.setmode(GPIO.BCM)								# set pins to BCM
GPIO.setwarnings(False)								# Never tell me the odds

os.chdir('/var/www/drum/ht')						# change directory 
speed = 0.01
hold = 2


#####################################################
def Que(x):
	if x == "blue":
		x = "Solid Blue"
	elif x == "green":
		x = "Solid Green"
	elif x == "orange":
		x = "Solid Orange"
	elif x == "purple":
		x = "Solid Purple"
	elif x == "red":
		x = "Solid Red"			
	elif x == "white":
		x = "Solid White"
	elif x == "yellow":
		x = "Solid Yellow"
	elif x == "indigo":
		x = "Solid Indigo"
	elif x == "pink":
		x = "Solid Pink"
		
	elif x == "breathred":
		x = "Fading Red"
	elif x == "fadeblue":
		x = "Fading Blue"
	elif x == "fadegreen":
		x = "Fading Green"
	elif x == "breathwhite":
		x = "Fading White"
	elif x == "breathyellow":
		x = "Fading Yellow"
		
	elif x == "redbluealt":
		x = "Fluctuating values for Red and Blue"
	elif x == "redgreenalt"
		x = "Fluctuating values for Red and Green"
		elif x == "bluegreenalt"
		x = "Fluctuating values for Blue and Green"
	






				
	else:
		x = "I have no idea."
	
	os.system("echo " + x + ">/var/www/drum/ht/Q")

#####################################################
def FadePrint(R, B, G):
	R=str(R)
	B=str(B)
	G=str(G)
	r = "echo " + "\"20=0."+R+"\" >/dev/pi-blaster" 
	g = "echo " + "\"21=0."+G+"\" >/dev/pi-blaster" 
	b = "echo " + "\"16=0."+B+"\" >/dev/pi-blaster" #echo cmd into pi
	RemoveRun(r, g, b) 
#####################################################
def RemoveRun(x, y, z):
	x = x.replace('\n', '') 						# remove line break x3
	y = y.replace('\n', '') 
	z = z.replace('\n', '') 
	os.system(x)									# run var to system x3
	os.system(y)
	os.system(z)
#####################################################
def FuckingFirstLine():
	fin = open( 'que', "r" )						# open file for read
	data_list = fin.readlines()						# list = array of whats in file
	fin.close()										# close file
	FirstLine = data_list[(0)]						# var = first line of array
	length = len(data_list)							# get length of list
	FirstLine = FirstLine.replace('\n', '') 		# Rmoves line break
	if length > 1:
		#print "Deleting first line."
		del data_list[(0)]							# remove first line
		fout = open("que", "w")						# opens file for writing
		fout.writelines(data_list)					# write the changed data (list) to a file
		fout.close()								# close file
	return(FirstLine)								# return contents of the first line
#####################################################
## COLORS##
#####################################################

#####################################################
def Blue():
	red = "echo 20=0 >/dev/pi-blaster"				# var = command x3
	blue = "echo 16=1 >/dev/pi-blaster"
	green = "echo 21=0 >/dev/pi-blaster" 
	RemoveRun(red, blue, green)
#####################################################
def Green():
	red = "echo 20=0 >/dev/pi-blaster"
	blue = "echo 16=0 >/dev/pi-blaster" 
	green = "echo 21=1 >/dev/pi-blaster"
	RemoveRun(red, blue, green)
#####################################################
def Orange():
	red = "echo 20=1 >/dev/pi-blaster"
	blue = "echo 16=0 >/dev/pi-blaster" 
	green = "echo 21=0.16 >/dev/pi-blaster"
	RemoveRun(red, blue, green)
#####################################################
def Purple():
	red = "echo 20=1 >/dev/pi-blaster"
	blue = "echo 16=1 >/dev/pi-blaster" 
	green = "echo 21=0 >/dev/pi-blaster"
	RemoveRun(red, blue, green)
#####################################################
def Red():
	red = "echo 20=1 >/dev/pi-blaster"
	blue = "echo 16=0 >/dev/pi-blaster" 
	green = "echo 21=0 >/dev/pi-blaster"
	RemoveRun(red, blue, green)
#####################################################
def White():
	red = "echo 20=1 >/dev/pi-blaster"
	blue = "echo 16=1 >/dev/pi-blaster" 
	green = "echo 21=1 >/dev/pi-blaster"
	RemoveRun(red, blue, green)
#####################################################
def Yellow():
	red = "echo 20=1 >/dev/pi-blaster"
	blue = "echo 16=0 >/dev/pi-blaster" 
	green = "echo 21=0.333  >/dev/pi-blaster"
	RemoveRun(red, blue, green)
#####################################################
def Indigo():
	red = "echo 20=0.5 >/dev/pi-blaster"
	blue = "echo 16=1 >/dev/pi-blaster" 
	green = "echo 21=0  >/dev/pi-blaster"
	RemoveRun(red, blue, green)
#####################################################
def Pink():
	red = "echo 20=1 >/dev/pi-blaster"
	blue = "echo 16=0.25 >/dev/pi-blaster" 
	green = "echo 21=0  >/dev/pi-blaster"
	RemoveRun(red, blue, green)
#####################################################
def Off():
	red = "echo 20=0 >/dev/pi-blaster"
	blue = "echo 16=0 >/dev/pi-blaster" 
	green = "echo 21=0 >/dev/pi-blaster"
	RemoveRun(red, blue, green)
#####################################################
## Fades And Transitions##
#####################################################

#####################################################
def ShowOff():
	Blue()
	sleep(hold)
	Green()
	sleep(hold)
	Red()
	sleep(hold)
	Orange()
	sleep(hold)
	Purple()
	sleep(hold)
	Red()
	sleep(hold)
	White()
	sleep(hold)
	Yellow()
	sleep(hold)
	Indigo()
	sleep(hold)
	Pink()
	sleep(hold)
	BreathRed()
	BreathBlue()
	BreathGreen()
	BreathPurp()
	BreathWhite()
	RedBlueAlt()
	RedGreenAlt()
	BlueGreenAlt()
#####################################################
def BreathRed():
	x = False
	RX = 00
	BX=GX = 00
	for i in range(198):
		RX = int(RX)
		if RX <= 00 or RX >= 99:
			x = not x
		if x == True:
			RX += 1
		else:
			RX -= 1
		RX = str(RX).zfill(2)
		FadePrint(RX, BX, GX)
		sleep(speed)
#####################################################
def BreathBlue():
	x = False
	BX = 00
	RX=GX = 00
	for i in range(198):
		BX = int(BX)
		if BX <= 00 or BX >= 99:
			x = not x
		if x == True:
			BX += 1
		else:
			BX -= 1
		BX = str(BX).zfill(2)
		FadePrint(RX, BX, GX)
		sleep(speed)
#####################################################
def BreathGreen():
	x = False
	GX = 00
	RX=BX = 00
	for i in range(198):
		GX = int(GX)
		if GX <= 00 or GX >= 99:
			x = not x
		if x == True:
			GX += 1
		else:
			GX -= 1
		GX = str(GX).zfill(2)
		FadePrint(RX, BX, GX)
		sleep(speed)
#####################################################
def BreathPurp():
	x = False
	BX=RX=GX = 00
	for i in range(198):
		RX = int(RX)
		if RX <= 00 or RX >= 99:
			x = not x
		if x == True:
			RX += 1
		else:
			RX -= 1
		RX = str(RX).zfill(2)
		BX = RX
		 
		FadePrint(RX, BX, GX)
		sleep(speed)
#####################################################
def BreathWhite():
	x = False
	BX=RX = 00
	GX = 00
	for i in range(198):
		RX = int(RX)
		if RX <= 00 or RX >= 99:
			x = not x
		if x == True:
			RX += 1
		else:
			RX -= 1
		RX=GX=BX = str(RX).zfill(2)
		FadePrint(RX, BX, GX)
		sleep(speed)
#####################################################
def BreathYellow():
	x = False
	BX=RX=GX = 00
	for i in range(198):
		RX = int(RX)
		if RX <= 00 or RX >= 99:
			x = not x
		if x == True:
			RX += 1
		else:
			RX -= 1
		if GX <= 1:
			GX == 1
		RX=GX = str(RX).zfill(2)
		GX = float(GX)
		GX = GX *.033
		print RX, GX
		FadePrint(RX, BX, GX)
		sleep(speed)
#####################################################
def RedBlueAlt():
	x = False
	BX = 99
	RX=GX= 00
	for i in range(198):
		RX = int(RX)
		BX = int(BX)
		if RX <= 00 or RX >= 99:
			x = not x
		if x == True:
			RX += 1
			BX -= 1
		else:
			RX -= 1
			BX += 1
		RX = str(RX).zfill(2)
		BX = str(BX).zfill(2)
		FadePrint(RX, BX, GX)
		sleep(speed)
#####################################################
def RedGreenAlt():
	x = False
	GX = 99
	RX=BX = 00
	for i in range(198):
		RX = int(RX)
		GX = int(GX)
		if RX <= 00 or RX >= 99:
			x = not x
		if x == True:
			RX += 1
			GX -= 1
		else:
			RX -= 1
			GX += 1
		RX = str(RX).zfill(2)
		GX = str(GX).zfill(2)
		FadePrint(RX, BX, GX)
		sleep(speed)
#####################################################
def BlueGreenAlt():
	x = False
	GX = 99
	RX=BX= 00
	for i in range(198):
		BX = int(BX)
		GX = int(GX)
		if BX <= 00 or BX >= 99:
			x = not x
		if x == True:
			BX += 1
			GX -= 1
		else:
			BX -= 1
			GX += 1
		BX = str(BX).zfill(2)
		GX = str(GX).zfill(2)
		FadePrint(RX, BX, GX)
		sleep(speed)
#####################################################
## Program ##
#####################################################

#####################################################
while True:
	try:
		que = FuckingFirstLine()							# variable = first line function
		Que(que)											# Send var to function
		if que == "blue":
			Blue()											# Turn Blue
			sleep(hold)
		elif que == "green":								
			Green()											# Turn Green
			sleep(hold)
		elif que == "orange":
			Orange()										# Turn Orange
			sleep(hold)
		elif que == "purple":
			Purple()										# Turn Purple
			sleep(hold)
		elif que == "red":
			Red()											# Turn Red
			sleep(hold)
		elif que == "white":
			White()											# Turn White
			sleep(hold)
		elif que == "yellow":
			Yellow()										# Turn Yellow
			sleep(hold)
		elif que == "indigo":
			Indigo()										# Turn Indigo
			sleep(hold)
		elif que == "pink":
			Pink()											# Turn Pink
			sleep(hold)
		elif que == "off":
			Off()											# Turn Off
			sleep(hold)
		elif que == "fade":
			Fade()											# Fade Everything


			sleep(hold)
		elif que == "breathred":
			BreathRed()										# Breth Red
		elif que == "breathblue":
			BreathBlue()									# Breath Blue
		elif que == "breathgreen":
			BreathGreen()									# Breath Green
		elif que == "breathpurp":
			BreathPurp()									# Breath Purple
		elif que == "breathwhite":
			BreathWhite()									# Breath White
		elif que == "breathyellow":
			BreathYellow()									# Breath Yellow	
		


		elif que == "redbluealt":
			RedBlueAlt()									# Fade Red and Blue
		elif que == "redgreenalt":
			RedGreenAlt()									# Fade Red and Green
		elif que == "bluegreenalt":
			BlueGreenAlt()									# Fade Red and Green
		elif que == "showoff":
			ShowOff()										# All colors
		else:
			sleep(1)										# Wait and check list later
		#print que											# print variable
		#sleep(1)											# wait
	except KeyboardInterrupt:
		break
		exit(0)
