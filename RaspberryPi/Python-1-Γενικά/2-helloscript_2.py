#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

print("Γεια σου επισκέπτη!")
print('Ποιο είναι το όνομά σου;')
user_name = input()
print('Χάρηκα, ' + user_name)
user_name_length = len(user_name)
print('Το όνομά σου έχει: ' + str(user_name_length) + ' χαρακτήρες! WOW!')
print('Ποιό έτος γενήθηκες;')
user_date = input()
user_age = 2019 - int(user_date)
print('Αυτό σημαίνει ότι είσαι',user_age,'ετών!')
print('Ποια είναι η θερμοκρασία αυτή την στιγμή;')
user_temp = float(input())
critical_temp = 40.0
diff_temp = critical_temp - user_temp
print('Έχουμε',diff_temp,'βαθμούς διαφορά από την κρίσιμη θερμοκρασία των',critical_temp,'βαθμών!')
