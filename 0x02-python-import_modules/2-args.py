#!/usr/bin/python3
import argparse
import sys
if len(sys.argv) == 0:
    print("{} argument".format(len(sys.argv)))
else:
    i = 1
    print("{} arguments".format(len(sys.argv) - 1))
    while i <= len(sys.argv) - 1:
        print("{} : {}".format(i, sys.argv[i]))
        i += 1
