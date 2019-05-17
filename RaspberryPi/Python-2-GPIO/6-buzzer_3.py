#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os
from time import sleep
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

#
print("Γεια σου επισκέπτη!")
print('Πες μου το 1ο νούμερo:')
user_num_1 = input()
print('Πες μου το 2ο νούμερo:')
user_num_2 = input()
sleep(1)
#
compare_num = user_num_1 == user_num_2

if compare_num == True:
	print('Τα δύο νούμερα είναι ίδια!')
	GPIO.output(22,GPIO.HIGH)
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.HIGH)
	sleep(1)
	GPIO.output(22,GPIO.LOW)
	sleep(1)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
else:
	if compare_num == False and user_num_1 > user_num_2 :
		print('Τα δύο νούμερα είναι διαφορετικά και το 1ο είναι μεγαλύτερο από το 2ο!')
		GPIO.output(22,GPIO.HIGH)
		GPIO.output(17,GPIO.HIGH)
		sleep(.2)
		GPIO.output(22,GPIO.LOW)
		sleep(1.8)
		GPIO.output(17,GPIO.LOW)
	else:
		print('Τα δύο νούμερα είναι διαφορετικά και το 2ο είναι μεγαλύτερο από το 1ο!')
		GPIO.output(22,GPIO.HIGH)
		GPIO.output(27,GPIO.HIGH)
		sleep(.1)
		GPIO.output(22,GPIO.LOW)
		sleep(.1)
		GPIO.output(22,GPIO.HIGH)
		sleep(.1)
		GPIO.output(22,GPIO.LOW)
		sleep(1.6)
		GPIO.output(27,GPIO.LOW)
#
GPIO.cleanup()
