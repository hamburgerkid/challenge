#!/usr/bin/python
# coding: UTF-8

'''
Copyright 2013 hamburgerkid

Question
A complement of a number is defined as inversion (if the bit value = 0, change it to 1 and vice-versa) 
of all bits of the number starting from the leftmost bit that is set to 1. 
For example, if N = 5, N is 101 in binary. 
The complement of N is 010, which is 2 in decimal. 
Similarly if N = 50, then complement of N is 13
Complete the function getIntegerComplement(). 
This function takes N as it's parameter. 
The function should return the complement of N.

Constraints
0 ≤ N ≤ 100000.
'''

import sys

def isInConstraints(n):
	if 0 <= n and n <= 100000:
		return True
	else:
		return False

def getIntegerComplement(s):
	if s.isdigit():
		n = int(s)
	else:
		print 'The argument must be a digit.',s
		return
	if not isInConstraints(n):
		print 'The argument must be between 0 and 100,000.',n
		return
	b = str(format(n,'b'))
	b2 = ''.join('1' if x == '0' else '0' for x in b)
	#print b,b2
	print int(b2,2)

if __name__ == '__main__':
	getIntegerComplement(sys.argv[1])
