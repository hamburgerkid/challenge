#!/usr/bin/python
# coding: UTF-8

'''
Copyright 2013 hamburgerkid

Question
Given an array of integers, 
output a list of four integers that sum to zero (the same input integer can be used multiple times), 
or indicate that no such set of four integers exists. 
For example, given the array (2 3 1 0 -4 -1), 
the set of four integers (3 1 0 -4) sums to zero, as does the set (0 0 0 0).
'''

import sys
import itertools

def onlyIntegerIncluded(l):
	for x in l:
		try:
			int(x)
		except Exception,e:
			print e
			return False
	return True

def getSetOfFourIntegers(l):
	if not onlyIntegerIncluded(l):
		print 'The list must contain only integer.',l
		return
	f = False
	for c in itertools.combinations_with_replacement(l,4):
		s = 0
		for n in c:
			s += int(n)
		if s == 0:
			f = True
			print c
	if f == False:
		print 'No such set of 4 integers exists.'

if __name__ == '__main__':
	getSetOfFourIntegers(sys.argv[1:])
