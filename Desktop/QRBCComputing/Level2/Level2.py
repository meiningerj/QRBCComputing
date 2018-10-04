#!/usr/bin/env python

import sys

if len(sys.argv) != 3:
	print "Incorrect number of command line arguments."
	print "Usage: python file.py <arg1> <arg2>"
	exit(1)
x = int(sys.argv[1])
y = int(sys.argv[2])
 
result = x * y

if result == 50:
	print "correct the key is " + str(hash("Level4"))
