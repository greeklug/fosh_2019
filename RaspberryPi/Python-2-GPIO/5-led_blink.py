#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Εισαγωγή function sleep από την βιβλιοθήκη time
from time import sleep
# Εισαγωγή βιβλιοθήκης RPi.GPIO
import RPi.GPIO as GPIO 

# Ορισμός του συστήματος αρίθμησης των pin σε BCM
GPIO.setmode(GPIO.BCM)

print("Γεια σου χρήστη!")
print("Πάμε να αναβοσθήσουμε τα led μας!")


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

# Εισάγουμε καθυστέρηση 2 δευτερολέπτων ώστε τα LED να παραμείνουν ανοικτά
sleep(2)


# Εκτύπωση πληροφοριακού μηνύματος στον χρήστη
print "Τα LED έσβησαν!"

# Ορισμός του OUTPUT GPIO17 ως LOW, το οποίο συνεπάγεται ότι 3v3 δεν θα είναι ενεργά στο pin
GPIO.output(17,GPIO.LOW)
# Ορισμός του OUTPUT GPIO27 ως LOW, το οποίο συνεπάγεται ότι 3v3 δεν θα είναι ενεργά στο pin
GPIO.output(27,GPIO.LOW)

# Εισάγουμε καθυστέρηση 2 δευτερολέπτων ώστε τα LED να παραμείνουν κλειστά
sleep(2)

### Επανάληψη!

# Εκτύπωση πληροφοριακού μηνύματος στον χρήστη
print "Τα LED ξαναάνοιξαν!"

# Ορισμός του OUTPUT GPIO17 ως HIGH, το οποίο συνεπάγεται ότι 3v3 θα είναι ενεργά στο pin
GPIO.output(17,GPIO.HIGH)
# Ορισμός του OUTPUT GPIO27 ως HIGH, το οποίο συνεπάγεται ότι 3v3 θα είναι ενεργά στο pin
GPIO.output(27,GPIO.HIGH)

# Εισάγουμε καθυστέρηση 3 δευτερολέπτων ώστε τα LED να παραμείνουν ανοικτά
sleep(3)


# Εκτύπωση πληροφοριακού μηνύματος στον χρήστη
print "Τα LED ξαναέσβησαν!"

# Ορισμός του OUTPUT GPIO17 ως LOW, το οποίο συνεπάγεται ότι 3v3 δεν θα είναι ενεργά στο pin
GPIO.output(17,GPIO.LOW)
# Ορισμός του OUTPUT GPIO27 ως LOW, το οποίο συνεπάγεται ότι 3v3 δεν θα είναι ενεργά στο pin
GPIO.output(27,GPIO.LOW)

# Καθώς είναι η τελευταία ενέργεια δεν απαιτείται αναμομή αλλά κάνουμε άμεσα αποδέσμευση των pin
GPIO.cleanup()
