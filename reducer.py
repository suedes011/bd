#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

cur_key = None
cur_count = 0

for line in sys.stdin:
    key, value = line.split()

    #Accumulate count for a word
    if key == cur_key:
        cur_count += int(value)
    else:
        #finish counting for a certain word
        if cur_key:
            print ('%s\t%s' % (cur_key, cur_count))
        cur_key = key
        cur_count = int(value)

#Output the last word
print ('%s\t%s' % (cur_key, cur_count))
