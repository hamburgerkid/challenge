#!/usr/bin/python
# coding: UTF-8

'''
Copyright 2013 hamburgerkid

Question
A simple word game starts with a word and repeatedly removes a single letter from the word,
forming a new word, until there are no letters left.
The act of removing a letter is called chopping and the resulting list of words is a chopping chain.
For instance:
planet → plane → plan → pan → an → a
Your task is to write a program that takes a word
and returns a list of all possible chopping chains that can be formed from the word,
given a suitable dictionary.
'''

import sys
import itertools

def existInDictionary(s):
	with open('/usr/share/dict/words','r') as f:
		ls = f.readlines()
		for l in ls:
			if s == l.rstrip():
				return True
	return False

def createNextWordList(l):
	l2 = []
	for w in l:
		for c in itertools.combinations(w,len(w)-1):
			s = ''.join(ch for ch in c)
			if existInDictionary(s):
				l2.append(s)
	if len(l2) > 0:
		l2 = list(set(l2))
		print l2
		createNextWordList(l2)

def createChoppingWordChains(s):
	if existInDictionary(s):
		l = [s]
		print l
		createNextWordList(l)

if __name__ == '__main__':
	createChoppingWordChains(sys.argv[1])
