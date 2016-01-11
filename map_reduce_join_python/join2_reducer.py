#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# Sample input file is sorted, and each line should contain the number or Channel
# at the end of each show segment, if there is not channel name appended,
# the channel does not broacast the show. discard accumulated subtotal and look for
# the next segment
# Surreal_Sports	983
# Surreal_Sports	998
# Surreal_Sports	ABC <--------- channel found... keep 983 and 998 as ABC's total
# Surreal_Talking	1002 <-------- reset and start again. Can you find ABC at the end?
# Surreal_Talking	1003
#
# How to test
# cat join2_gen*.txt | python join2_mapper.py   | sort > mapped2.txt
# cat mapped2.txt | python join2_reducer.py
#
# should create output like
# Almost_Games	48231
# Almost_News	45589
# Almost_Show	49186
# 
# the list of shows should match with this result
# cat mapped2.txt | grep ABC
# --------------------------------------------------------------------------

prev = None
ttl = 0
abc_found = False
key_out = None
for line in sys.stdin:
	line = line.strip() #strip out carriage return
	kv = line.split('\t') #split line, into key and value, returns a list
	
	val = 0
	if kv[1].isdigit():
		val = int(kv[1])

	# if key is same, keep adding, otherwise eimit the subtotal ONLY when you find ABC channel
	if kv[0] == prev:
		ttl += val
	else:
		if prev and abc_found:
			print("%s\t%d"%(key_out,ttl))
			abc_found = False
		ttl = val
	# if the value contains 'ABC', store the key (show name) and flag it as found
	if kv[1] == 'ABC':
		key_out = kv[0]
		abc_found = True
	# remember the current key for next iteration
	prev = kv[0]
