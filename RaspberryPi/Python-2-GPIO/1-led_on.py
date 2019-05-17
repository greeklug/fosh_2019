#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Εισαγωγή βιβλιοθήκης RPi.GPIO
import RPi.GPIO as GPIO 

# Ορισμός του συστήματος αρίθμησης των pin σε BCM
GPIO.setmode(GPIO.BCM)

# Ορισμός του GPIO17 ως OUTPUT
GPIO.setup(17,GPIO.OUT)

# Εκτύπωση πληροφοριακού μηνύματος στον χρήστη
print "Το LED άνοιξε!"

# Ορισμός του OUTPUT GPIO17 ως HIGH, το οποίο συνεπάγεται ότι 3v3 θα είναι ενεργά στο pin
GPIO.output(17,GPIO.HIGH)
