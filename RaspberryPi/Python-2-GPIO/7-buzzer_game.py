#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# GreekLUG Buzzer Game!

import os
from random import randint
from time import sleep
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT) #LED1
GPIO.setup(27,GPIO.OUT) #LED2
GPIO.setup(22,GPIO.OUT) #BUZZER

#
print("Γεια σου επισκέπτη!")
print('Ποιο είναι το όνομά σου;')
user_name = raw_input()
sleep(2)
os.system('clear')
#
print('Ξεκινάμε ' + str(user_name) + '! Άκουσε και κοίτα για να κερδίσεις!')
sleep(2)
#
bot_choice_led1 = randint(1,5)
bot_choice_led1_counter = bot_choice_led1
bot_choice_led2 = randint(1,5)
bot_choice_led2_counter = bot_choice_led2
bot_choice_buz = randint(1,5)
bot_choice_buz_counter = bot_choice_buz


while bot_choice_led1_counter > 0:
	GPIO.output(17,GPIO.HIGH)
	sleep(.5)
	GPIO.output(17,GPIO.LOW)
	sleep(.5)
	bot_choice_led1_counter = bot_choice_led1_counter - 1

while bot_choice_led2_counter > 0:
	GPIO.output(27,GPIO.HIGH)
	sleep(.5)
	GPIO.output(27,GPIO.LOW)
	sleep(.5)
	bot_choice_led2_counter = bot_choice_led2_counter - 1

while bot_choice_buz_counter > 0:
	GPIO.output(22,GPIO.HIGH)
	sleep(.2)
	GPIO.output(22,GPIO.LOW)
	sleep(.2)
	bot_choice_buz_counter = bot_choice_buz_counter - 1

print "Πόσες φορές είδες τα led να ανάβουν και ακούσες το κουδούνι;"
user_answer = input("Γράψε τον αριθμό: ")
correct_answer = bot_choice_led1 + bot_choice_led2 + bot_choice_buz

if user_answer == correct_answer:
	print('Το βρήκες!')
	sleep(1)
else:
	print('Έκανες λάθος! Ήταν ' + str(correct_answer) + ' φορές!')
	sleep(1)
#
GPIO.cleanup()
