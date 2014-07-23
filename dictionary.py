#!/usr/bin/env python3

# program to check if word is in dictionaryPath
import os
import sys

#
# get the name of our program to use in error messages
#
progname = os.path.basename(sys.argv[0])

word = None
dictionaryPath = './dictionary.txt'

# get command line arguments (if they exist)
if len(sys.argv) > 1:
	word = sys.argv[1]

# check if word argument exists, if not get word via prompt:
if not word:
	word = input('enter word: ')
else:
	print('word: ' + word)

#check if the file exits first
if os.path.exists(dictionaryPath):
	#the file exists so go ahead with opening the file
	dictionary = open(dictionaryPath)
	#simply loop through the dictionary to find the word
	for line in dictionary:
		if (word.lower() == line.strip()):
			print('Yes! \'' + word + '\' is a valid word!')
			sys.exit()
	#word was not found:
	print('Uh-oh, it seems that \'' + word + '\' is NOT a valid word.')
else:
	print('couldnt \'locate dictionary.txt\'')
