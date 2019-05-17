#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Εισαγωγή βιβλιοθήκης RPi.GPIO
import RPi.GPIO as GPIO 

# Ορισμός του συστήματος αρίθμησης των pin σε BCM
GPIO.setmode(GPIO.BCM)

# Ορισμός του GPIO17 ως OUTPUT
GPIO.setup(17,GPIO.OUT)
# Ορισμός του GPIO27 ως OUTPUT
GPIO.setup(27,GPIO.OUT)

# Εκτύπωση πληροφοριακού μηνύματος στον χρήστη
print "Τα LED άνοιξαν!"

# Ορισμός του OUTPUT GPIO17 ως HIGH, το οποίο συνεπάγεται ότι 3v3 θα είναι ενεργά στο pin
GPIO.output(17,GPIO.HIGH)
# Ορισμός του OUTPUT GPIO27 ως HIGH, το οποίο συνεπάγεται ότι 3v3 θα είναι ενεργά στο pin
GPIO.output(27,GPIO.HIGH)
