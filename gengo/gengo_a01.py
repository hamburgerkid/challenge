#!/usr/bin/python
# coding: UTF-8

'''
Copyright 2013 hamburgerkid

Question
Complete the function getEqualSumSubstring, which takes a single argument. 
The single argument is a string s, which contains only non-zero digits.
This function should print the length of longest contiguous substring of s, 
such that the length of the substring is 2*N digits and 
the sum of the leftmost N digits is equal to the sum of the rightmost N digits.
If there is no such string, your function should print 0.
'''

import sys
import math

def onlyNonZeroDigit(s):
	if s.isdigit() and s.find('0') == -1:
		return True
	else:
		return False

def getEqualSumSubstring(s):
	a = 0
	if not onlyNonZeroDigit(s):
		print 'The argument must contain only non-zero digits.',s
		return
	l = len(s)
	for i in range(0,l+1):
		for j in range (i,l+1):
			if i < j:
				ss = s[i:j]
				l2 = len(ss)
				sl = ss[0:(l2/2)]
				sr = ss[(l2/2):]
				nl = 0
				nr = 0
				for n in sl:
					nl += int(n)
				for n in sr:
					nr += int(n)
				if nl == nr and l2 > a:
					#print s,ss,sl,sr
					#print nl,nr,l2
					a = l2
	print a

if __name__ == '__main__':
	getEqualSumSubstring(sys.argv[1])
