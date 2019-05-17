#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os
from time import sleep
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.OUT)

#
print("Γεια σου χρήστη!")
sleep(1)
#
buzzes_choice = 0
os.system('clear')
print "Πόσες φορές θα ήθελες να ακούσεις το κουδούνι;"
buzzes_choice = input("Γράψε έναν αριθμό: ")
buzzed = buzzes_choice
#
while buzzes_choice > 0:
	GPIO.output(22,GPIO.HIGH)
	print("*")
	sleep(.2)
	GPIO.output(22,GPIO.LOW)
	sleep(.2)
	buzzes_choice = buzzes_choice - 1
#
os.system('clear')
print("Το ακούσαμε " + str(buzzed) + " φορές!")
#
GPIO.cleanup()
