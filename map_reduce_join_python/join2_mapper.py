#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# This mapper allows two different types of file
#
# <Show>,<Channel>
# Hot_Talking,ABC
# Cold_Talking,XYZ
#
# <Show>,<Number>
# Hot_Taling,123
# Whatever_Talking,999
#
# Mapping process is to 1) Filter out ABC in first type, and pass all values of 2nd type
#
# The output should be tab separated as follows
#
# Hot_Talking	ABC
# Hot_Talking	123
# Whatever_Talking	999
#
# Note that Hadoop expects a tab to separate key value
# but this program assumes the input file has a ',' separating key value
#
# How to test this program
#
# cat join2_gen*.txt | python join2_mapper.py 
# cat join2_gen*.txt | python join2_mapper.py | grep ABC
# --------------------------------------------------------------------------

for line in sys.stdin:
    line = line.strip()   #strip out carriage return
    kv = line.split(",")   #split line, into key and value, returns a list

    # if the value_in is digit, it's gennum file, just printout all. At this point, 
    # it's only mapping, so I don't know which show could be used for total count
    # also, if the value is "ABC", it's in our target criteria, print out
    if kv[1].isdigit() or kv[1] == 'ABC':
        print( '%s\t%s' % (kv[0], kv[1]) )  # pass through the count or filter only ABC related lines
    else:
	pass #do nothing
