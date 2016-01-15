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


# Programming Notes

Spark put everything in memory, and it create partitions. A partition is a unit of dataset should be handled locally in one node.

## Local operation (aka Narrow Transform)

map()

## Network operation (aka Wider Transform)




## Useful Functions

glom()










