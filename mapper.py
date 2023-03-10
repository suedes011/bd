#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

for line in sys.stdin:
    for word in line.split():
        print ('%s\t%s' % (word, 1))
