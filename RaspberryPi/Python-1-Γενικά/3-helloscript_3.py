#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

print("Γεια σου επισκέπτη!")
print('Πες μου το 1ο νούμερo:')
user_num_1 = input()
print('Πες μου το 2ο νούμερo:')
user_num_2 = input()

compare_num = user_num_1 == user_num_2

if compare_num == True:
	print('Τα δύο νούμερα είναι ίδια!')
else:
	if compare_num == False and user_num_1 > user_num_2 :
		print('Τα δύο νούμερα είναι διαφορετικά και το 1ο είναι μεγαλύτερο από το 2ο!')
	else:
		print('Τα δύο νούμερα είναι διαφορετικά και το 2ο είναι μεγαλύτερο από το 1ο!')

