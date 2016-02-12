

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

use ! sign to execute bash command

e.g.

```
!cat students.json
```

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

## Parallelize and RDD

Create some parallel rdd
```
int_rdd == sc.parallelize(range(10), 3)
int_rdd.collect()
```

## Counting

```
int_rdd.count()
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

## DataFrame and SQL

Dataframe is faster, and less line of code. Using the same mechanism, therefore, it's sort of Optimized RDD

### Create Dataset

Prepare Dataset like this below

```
students = sc.parallelize([
[100, "Alice", 8.5, "Computer Science"],
[101, "Bob", 7.1, "Engineering"],
[102, "Carl", 6.2, "Engineering"]
])
```

### Without Dataframe, Average:

```
def extract_grade(row):
	return row[2]

students.map(extract_grade).mean().collect()
```

### Without Dataframe, Group by Key and find Max of each Group:

```
def extract_degree_grade(row):
	return (row[3], row[2])

degree_grade_RDD = students.map(extract_degree_grade)
degree_grade_RDD.reduceByKey(max).collect()
```

### Setup Dataframe

```
students_df = sqlCtx.createDataFrame(students, ["id", "name", "grade", "degree"])
students_df.printSchema()
```

Specify Type per Column

```
from pyspark.sql.types import *
schema = StructType([
	StructField("id", LongType(), True),
	StructField("name", StringType(), True),
	StructField("grade", DoubleType(), True),
	StructField("degree", StringType(), True) ])
```

Output

```
root
 |-- id: long (nullable = true)
 |-- name: string (nullable = true)
 |-- grade: double (nullable = true)
 |-- degree: string (nullable = true)
```

### With Dataframe, Average:

Use agg() - aggregate function and pass the column and function name. 

```
students_df.agg({"grade": "mean"}).collect()
```

### With Dataframe, Group by Key and find Max of each Group:

```
students_df.groupBy("degree").max("grade").collect()
```

Simple!

### show() -  Pretty Print Function

```
students_df.groupBy("degree").max("grade").show()
```

Output:

```
+----------------+-----+---+-----+
|          degree|grade| id| name|
+----------------+-----+---+-----+
|Computer Science|  8.5|100|Alice|
|     Engineering|  7.1|101|  Bob|
+----------------+-----+---+-----+
```

### JSON


Write JSON

```
students_json = [ '{"id":100, "name":"Alice", "grade":8.5, "degree":"Computer Science"}', '{"id":101, "name":"Bob", "grade":7.1, "degree":"Engineering"}']
with open("students.json", "w") as f:
	f.write("\n".join(students_json))
```

Check using cat

```
!cat students.json
```

Read JSON

```
sqlCtx.jsonFile("file:///home/cloudera/students.json").show()
```

### CSV

You need to load csv plugin. Go to http://spark-packages.org/package/databricks/spark-csv

Start ipython with the plugin

```
PYSPARK_DRIVER_PYTHON=ipython pyspark --packages com.databricks:spark-csv_2.10:1.2.0
```

or


```
$SPARK_HOME/bin/spark-shell --packages com.databricks:spark-csv_2.10:1.3.0
```

Loading

```
yelp_df = sqlCtx.load(
	source="com.databricks.spark.csv",
	header = 'true',
	inferSchema = 'true',
	path = 'file:///usr/lib/hue/apps/search/examples/collections/solr_configs_yelp_demo/index_data.csv')
yelp_df.printSchema()
```

### Accessing Column

```
yelp_df["useful"]

or

yelp_df.useful
```

Display Columns

```
yelp_df.columns
```

### Select Statement / Filtering / Alias / Order by

There are a few ways to describe the filter 

```
yelp_df.filter(yelp_df.useful >= 1).count()
yelp_df.filter(yelp_df["useful"] >= 1).count()
yelp_df.filter("useful >= 1").count()
```

Selecting and Max

```
yelp_df["useful"].agg({"useful":"max"}).collect()
yelp_df.select("useful")
yelp_df.select("useful").agg({"useful":"max"}).collect()
```

```
yelp_df.select("useful").take(5)
```

Calculated Column

```
yelp_df.select("id", yelp_df.useful/28*100).show(5)
```

Use Cast to make them int.

This is almost like SELECT id, CAST(Int, useful/28*100) AS useful_perc FROM yelp_df

```
useful_perc_data = yelp_df.select("id", (yelp_df.useful/28*100).cast("int")).show(5)
useful_perc_data = yelp_df.select("id", (yelp_df.useful/28*100).cast("int")).alias('useful_perc').show(5)
```

Descending order. Import desc

```
from pyspark.sql.functions import asc, desc
useful_perc_data = yelp_df.select(
	yelp_df["id"].alias("uid"),
	(yelp_df.useful/28*100).cast("int").alias("useful_perc")
).orderBy(desc("useful_perc"))
```


### Join

Inner Join and select Cols ... Note it's using cache after Join

```
useful_perc_data.join(
	yelp_df,
	yelp_df.id == useful_perc_data.uid,
	"inner").cache.().select(useful_perc_data.uid, "useful_perc", "review_count").show()
```
### Average, Min, and Max

```
logs_df.groupBy("code").avg("bytes").show()
```

```
import pyspark.sql.functions as F
logs_df.groupBy("code").agg(
	logs_df.code,
	F.avg(logs_df.bytes),
	F.min(logs_df.bytes),
	F.max(logs_df.bytes)
	).show()
```


### Setting Hadoop Config (e.g. delimiter)

e.g. Allow windows new line \r\n to read data

```
sc._jsc.hadoopConfiguration().set('textinputforma t.record.delimiter', '\r\n')
```







