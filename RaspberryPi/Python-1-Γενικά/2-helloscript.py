#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

print("Γεια σου επισκέπτη!")
print('Ποιο είναι το όνομά σου;')
### Python 2
#user_name = raw_input()
###
# Python 3
user_name = input()
###
print('Χάρηκα, ' + user_name)
user_name_length = len(user_name)
print('Το όνομά σου έχει: ' + str(user_name_length) + ' χαρακτήρες! WOW!')
print('Ποιό έτος γενήθηκες;')
### Python 2
#user_date = raw_input()
###
# Python 3
user_date = input()
###
user_age = 2019 - int(user_date)
### Python 2
#print('Αυτό σημαίνει ότι είσαι ' + str(user_age) + ' ετών!')
###
# Python 3
print('Αυτό σημαίνει ότι είσαι',user_age,'ετών!')
###
