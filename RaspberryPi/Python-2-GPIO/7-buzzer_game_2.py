#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# GreekLUG Buzzer Game #2!

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

while True:

	print('Ξεκινάμε ' + str(user_name) + '! Άκουσε και κοίτα για να κερδίσεις!')
	sleep(2)
	#
	bot_choice_led1 = randint(1,5)
	bot_choice_led1_counter = bot_choice_led1
	bot_choice_led2 = randint(1,5)
	bot_choice_led2_counter = bot_choice_led2
	bot_choice_buz = randint(1,5)
	bot_choice_buz_counter = bot_choice_buz
	bot_choice_num = randint(1,3)


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


	if bot_choice_num == 1:
		print ("Πόσες φορές είδες το 1ο led να ανάβει;")
		user_answer = input("Γράψε τον αριθμό: ")
		correct_answer = bot_choice_led1
	else:
		if bot_choice_num == 2:
			print ("Πόσες φορές είδες το 2ο led να ανάβει;")
			user_answer = input("Γράψε τον αριθμό: ")
			correct_answer = bot_choice_led2
		else:
			print ("Πόσες φορές άκουσες το buzzer;")
			user_answer = input("Γράψε τον αριθμό: ")
			correct_answer = bot_choice_buz

	if user_answer == correct_answer:
		print('Το βρήκες!')
		sleep(2)
	else:
		print('Έκανες λάθος! Ήταν ' + str(correct_answer) + ' φορές!')
		sleep(2)
	#
	while True:
		os.system('clear')
		print ("Θέλεις να ξαναπαίξεις;")
		user_answer_restart = raw_input("Γράψε 1 για NAI, 0 για Έξοδο: ")
		if user_answer_restart in ('0', '1'):
            break
        print 'Μη έγκυρη επιλογή!'
	if user_answer_restart == '1':
		os.system('clear')
		continue
	else:
		print ("Τα λέμε!")
		break

GPIO.cleanup()
