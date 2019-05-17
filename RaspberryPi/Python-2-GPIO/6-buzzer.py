#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Εισαγωγή βιβλιοθήκης os
import os
# Εισαγωγή function sleep από την βιβλιοθήκη time
from time import sleep
# Εισαγωγή βιβλιοθήκης RPi.GPIO
import RPi.GPIO as GPIO 

# Ορισμός του συστήματος αρίθμησης των pin σε BCM
GPIO.setmode(GPIO.BCM)

print("Γεια σου χρήστη!")
print("Πάμε να ακούσουμε το κουδούνι μας!")

# Εκκαθάριση μηνυμάτων οθόνης
os.system('clear')

# Ορισμός του GPIO22 ως OUTPUT
GPIO.setup(22,GPIO.OUT)


# Εκτύπωση πληροφοριακού μηνύματος στον χρήστη
print "Το κουδούνι ακούγεται!"

# Ορισμός του OUTPUT GPIO22 ως HIGH, το οποίο συνεπάγεται ότι 3v3 θα είναι ενεργά στο pin
GPIO.output(22,GPIO.HIGH)
# Εισάγουμε καθυστέρηση 0,1 δευτερολέπτων όπου ο ήχος παραμένει ενεργός
sleep(.2)
os.system('clear')
print "Το κουδούνι είναι ήσυχο!"
GPIO.output(22,GPIO.LOW)
sleep(1)
os.system('clear')
print "Το κουδούνι ακούγεται!"
GPIO.output(22,GPIO.HIGH)
sleep(.2)
os.system('clear')
print "Το κουδούνι είναι ήσυχο!"
GPIO.output(22,GPIO.LOW)
sleep(.2)
os.system('clear')

print("Το ακούσαμε!")

# Καθώς είναι η τελευταία ενέργεια δεν απαιτείται αναμομή αλλά κάνουμε άμεσα αποδέσμευση των pin
GPIO.cleanup()
