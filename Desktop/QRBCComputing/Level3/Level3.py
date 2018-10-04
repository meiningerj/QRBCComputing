#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
	print "Incorrect number of command line arguments."
	print "Usage: python file.py <arg1>"
	exit(1)

var1 = ord(sys.argv[1])

if var1 == 14:
	print "correct the key is " + str(hash("Level2"))
