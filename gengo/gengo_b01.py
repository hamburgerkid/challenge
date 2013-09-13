#!/usr/bin/python
# coding: UTF-8

'''
Copyright 2013 hamburgerkid

Question
Consider a function f that takes a positive integer n
and returns the number of 1s in the decimal representation of all the integers from 0 to n, inclusive.
For example, f(13) = 6, for the numbers 1, 10, 11 (twice, for two 1s), 12 and 13. Notice that f(1) = 1.
After 1, what is the next largest n for which f(n) = n?
'''

import sys

def isPositiveInt(l):
	for x in l:
		if not x.isdigit():
			return False
	return True

def f(i):
	n = 0
	for x in range(i+1):
		n += str(x).count('1')
	print i,n
	return n

def findNextInteger(l):
	if not isPositiveInt(l):
		print 'The list must contain only positive integer.',l
		return
	i = int(l[0])
	while i < int(l[1]):
		if i == f(i) and i > 1:
			print i
			break
		i += 1

if __name__ == '__main__':
	findNextInteger(sys.argv[1:])
