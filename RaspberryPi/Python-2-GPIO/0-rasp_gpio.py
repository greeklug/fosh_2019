#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# ΠΡΟΣΟΧΗ! Τα παρακάτω είναι εισαγωγικά για την βιβλιοθήκη RPi.GPIO και
# δεν πρέπει να χρησιμοποιηθούν ως script ελέγχου για την αποφυγή βλάβης!

# Εισαγωγή βιβλιοθήκης RPi.GPIO
# https://sourceforge.net/p/raspberry-gpio-python/wiki/
import RPi.GPIO as GPIO 

# Ορισμός του συστήματος αρίθμησης των pin σε BCM
GPIO.setmode(GPIO.BCM)

mode = GPIO.getmode()
print("Το GPIO mode έχει οριστεί σε",mode,"!")


# Ορισμός pin ως INPUT ή OUTPUT
#
# Ορισμός του GPIO17 ως INPUT
GPIO.setup(17,GPIO.INPUT)
# Ορισμός του GPIO27 ως OUTPUT
GPIO.setup(27,GPIO.OUT)


# Ορισμός κατάσταση pin ως HIGH (παροχή ρεύματος) ή LOW (μη παροχή ρεύματος)
#
# Ορισμός του OUTPUT GPIO17 ως HIGH, το οποίο συνεπάγεται ότι 3v3 θα είναι ενεργά στο pin
GPIO.output(17,GPIO.HIGH)
# Ορισμός του OUTPUT GPIO27 ως LOW, το οποίο συνεπάγεται ότι 3v3 δεν θα είναι ενεργά στο pin
GPIO.output(27,GPIO.LOW)


# Αποδέσμευση των pin
GPIO.cleanup()
