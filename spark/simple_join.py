# Run those lines in spark console. 

def split_fileA(line):
	word,count=line.split(',')
	return (word,int(count))

def split_fileB(line):
	date,word_count = line.split(' ')
	word,count_string = word_count.split(',')	
	return (word, date + " " + count_string)

#test_line = "able,991"
#print(split_fileA(test_line))

#test_line = "Feb-22 actor,3"
#print(split_fileB(test_line))



# read files from previous map reduce example. see map reduce folder for those data sets
fileA = sc.textFile("/user/cloudera/input_join/join1_FileA.txt")
fileB = sc.textFile("/user/cloudera/input_join/join1_FileB.txt")

# Check contents
fileA.collect()
fileA.take(1)
fileB.collect()
fileB.take(1)


# Build key-value pair dictionaries
fileA_data = fileA.map(split_fileA)
fileB_data = fileA.map(split_fileB)

fileA_data.collect()
fileB_data.collect()

# now join them by the key
fileB_joined_fileA = fileB_data.join(fileA_data)
fileB_joined_fileA.collect()

