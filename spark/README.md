## Setup

```
sudo easy_install ipython==1.2.1
```

## Start Spark Console

```
PYSPARK_DRIVER_PYTHON=ipython pyspark
```

all contexts are available under sc variable. Try
```
sc.version
```

if you get error, try to run with writable permission user

```
sudo -u hdfs PYSPARK_DRIVER_PYTHON=ipython pyspark
```

if still have problem, assign enviornment variable

```
export PYSPARK_SUBMIT_ARGS="--master local[2] pyspark-shell"
```

## Example

simple_join.py - split lines into key-value pairs, and count number of words. 

## Programming Notes

Spark put everything in memory, and it create partitions. A partition is a unit of dataset should be handled locally in one node.
RDD - Resilient Distributed Dataset. Immutable object that takes care distributed and paralell processing.


## Basics

```
sc.version
```

## I/O

```
f = sc.textFile("file:///home/cloudera/testfile1")
f.collect()
f.take(1)
```

# Parallelize and RDD

Create some parallel rdd
```
int_rdd == sc.parallelize(range(10), 3)
int_rdd.collect()
```

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

If you need to see the partition, use glom function

```
int_rdd.glom().collect()
```

[[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]

## Filtering

(local operation)

```
def starts_with_a(word):
  return word.lower().startswith("a")
words_RDD.filter(starts_with_a).collect()
```

## Mapping

(local operation)

```
def lower(line):
  return line.lower()
lower_text_RDD = text_RDD.map(lower)
```


```
def split_words(line):
  return line.split()

def create_pair(word):
  return (word, 1)

pairs_RDD=text_RDD.flatMap(split_words).map(create_pair)
pairs_RDD.collect()
```

## Grouping

These operations might go over network (shuffle).

```
pairs_RDD.groupByKey().collect()
```

```
for k,v in pairs_RDD.groupByKey().collect():
  print "Key:", k, ",Values:", list(v
```

```
def sum_counts(a, b):
  return a + b
  
wordcounts_RDD = pairs_RDD.reduceByKey(sum_counts)
wordcounts_RDD.collect()
```

## Broadcast

Usefult to send config params

```
config = sc.broadcast({"order":3, "filter":True})
config.value
```

## Accumulator

Global variable

```
accum = sc.accumulator(0)
def test_accum(x):
  accum.add(x)
sc.parallelize([1, 2, 3, 4]).foreach(test_accum)
accum.value
```


## Optimizing

Use cache() to remember after some operations

```
myrdd = ....
myrdd.cache()
```

Use coalesce() function to re-partition RDD

```
sc.parallelize(range(10), 4).coalesce(2).glom().collect()
```






