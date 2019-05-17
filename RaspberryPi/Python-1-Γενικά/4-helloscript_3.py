#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#Εισαγωγή module
import platform
import datetime
import time

print("Γεια σου επισκέπτη!")

# Αναμονή 3 δευτερόλεπτα
time.sleep(3)

os = platform.system()
print("Ο υπολογιστής σου τρέχει...",os,"!")

# Αναμονή 3 μιλιδευτερόλεπτα
time.sleep(.300)

ostime = datetime.datetime.now()
print ("Η τρέχουσα ημερομηνία και ώρα είναι...",ostime)

