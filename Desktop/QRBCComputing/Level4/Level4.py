#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
	print "Incorrect number of command line arguments."
	print "Usage: python file.py <arg1>"
	exit(1)
result = 1
for x in range(int(sys.argv[1])):
	result = result + 6 - 2;

if result == 21:
	print "correct the key is " + str(hash("Level3"))
