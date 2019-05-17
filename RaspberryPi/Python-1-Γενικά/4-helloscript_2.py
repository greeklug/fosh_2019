#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#Εισαγωγή module
import platform
import datetime

print("Γεια σου επισκέπτη!")
os = platform.system()
print("Ο υπολογιστής σου τρέχει...",os,"!")
ostime = datetime.datetime.now()
print ("Η τρέχουσα ημερομηνία και ώρα είναι...",ostime)

