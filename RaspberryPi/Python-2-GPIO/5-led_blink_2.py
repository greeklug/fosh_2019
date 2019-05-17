#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from time import sleep
import RPi.GPIO as GPIO 


GPIO.setmode(GPIO.BCM)

print("Γεια σου χρήστη!")
print("Πάμε να αναβοσθήσουμε τα led μας με μη συνεχόμενη σειρά!")

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

#
print "Το 1ο LED άνοιξε!"
GPIO.output(17,GPIO.HIGH)
sleep(2)
print "Το 2ο LED άνοιξε!"
GPIO.output(27,GPIO.HIGH)
sleep(2)
print "Το 1ο LED έσβησε!"
GPIO.output(17,GPIO.LOW)
sleep(1)
print "Το 1ο LED άνοιξε!"
GPIO.output(17,GPIO.HIGH)
sleep(1)
print "Το 2ο LED έσβησε!"
GPIO.output(27,GPIO.LOW)
sleep(1)
print "Το 1ο LED έσβησε!"
GPIO.output(17,GPIO.LOW)
sleep(0.5)
print "Το 2ο LED άνοιξε!"
GPIO.output(27,GPIO.HIGH)
sleep(0.5)
print "Το 2ο LED έσβησε!"
GPIO.output(27,GPIO.LOW)
sleep(2)
print "Το 1ο LED άνοιξε!"
GPIO.output(17,GPIO.HIGH)
sleep(0.5)
print "Το 2ο LED άνοιξε!"
GPIO.output(27,GPIO.HIGH)
print "Το 1ο LED έσβησε!"
GPIO.output(17,GPIO.LOW)
sleep(0.5)
print "Το 2ο LED έσβησε!"
GPIO.output(27,GPIO.LOW)
#
GPIO.cleanup()
