# CourseraBigData

## Basic Operations

start stop datanode or tasktracker
```
/usr/lib/hadoop/sbin/hadoop-daemon.sh tasktracker start
/usr/lib/hadoop/sbin/hadoop-daemon.sh datanode start
```

Note: most of services should be able to start via Cloudera Manager web interface localhost:7180. To start all services, click the down arrow on top of the list.

## HDFS

put some file to parse out

```
hdfs dfs -ls /user/cloudera
hdfs dfs -mkdir /user/cloudera
hdfs dfs -put ~/Downloads/iris.csv /user/cloudera
hdfs dfs -ls /user/cloudera
hdfs dfs -rm -r /user/cloudera/output_*
```

Another copy method

```
hdfs dfs -copyFromLocal /home/cloudera/testfile* /user/cloudera/myinput
```

Check File Stats (e.g. # of Blocks) or check the entire  DataNode Status
```
hdfs fsck /user/cloudera/iris.csv
hdfs dfsadmin -report
```

Misc - if you get an error about safe mode, turn it off
```
sudo -u hdfs hdfs dfsadmin -safemode leave
```


## Pig

Start Pig Shell, and import csv data using script. In this example, I am extracting only sepal and species columns.

```
pig -x mapreduce
iris = load '/user/cloudera/iris.csv' using PigStorage(',');
sepal = foreach iris generate $1,$2,$5;
dump B;
store sepal into '/user/cloudera/sepal';
quit
```

Go back to hdfs then check
```
hdfs dfs -ls /user/cloudera/sepal
```


## Hive

Use beeline to connect Hive

```
beeline -u jdbc:hive2://
```

Load data from csv and run some analysis

```
CREATE TABLE iris (id STRING,sepal_width FLOAT,sepal_height FLOAT,petal_width FLOAT,petal_height FLOAT,species STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE;

LOAD DATA INPATH '/user/cloudera/iris.csv' OVERWRITE INTO TABLE iris;


select species, avg(sepal_width) ave_sw from iris group by species;

!q
```

## Impala

After uploading data files into Metastore (Databrowser > Metastore > Create new), run refresh command
```
invalidate metadata;
show tables;
```

Note: when you import, the importer tend to pick tinyint, but becareful. Use int to preserve bigger number.


## HBase

(still not working - connection refused error)

```
hbase shell
```


```
create 'iris', {NAME=>'id'},{NAME=>'sepal_width'},{NAME=>'sepal_height'},{NAME=>'petal_width'},{NAME=>'petal_height'},{NAME=>'species'}

```

Put value in row1 species column
```
put 'iris','r1','species','setosa'
scan 'iris'
scan 'iris',{COLUMNS=>'species'}
```

## Spark

See spark/ folder

## Java API


How to compile and Run:
```
export CLASSPATH=$CLASSPATH:.:/usr/lib/crunch/lib/hadoop-common.jar:/usr/lib/crunch/lib/hadoop-annotations.jar
javac MyHadoopIOTest.java 
jar cvf MyHadoopIOTest.jar MyHadoopIOTest.class
/usr/bin/hadoop jar MyHadoopIOTest.jar MyHadoopIOTest
```
See MyHadoopIOTest.java for example. The Java program needs to import a few packages

```
import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
```

## Rest API

Sample URL GET File Status

```
http://quickstart.cloudera:14000/webhdfs/v1/user/cloudera?user.name=cloudera&op=GETFILESTATUS
```

also in curl

curl -i "http://quickstart.cloudera:14000/webhdfs/v1/user/cloudera?user.name=cloudera&op=GETFILESTATUS"


## Cloudera Manager

```
sudo /home/cloudera/cloudera-manager --express --force
```

## Map/Reduce in Python

See map_reduce_python and map_reduce_join_python folder

## Splunk
install Enterprise version
/Applications/Splunk/bin/splunk start

sample data
docs.splunk.com/images/Tutorial/tutorialdata.zip

upload a file. Note select segment 1 for this tutorial data when you upload.

search filter example
```
host="xxki.home" buttercup* (error* OR fail*)
```

use pipe (|) and command to aggregate for the final statistics. For example,

"Find all purchased product and Order by count per categoryId"

```
source="*tutorialdata_dec2015.zip:*" action=purchase status=200 | top categoryId
```

This will show you the purchase count per category.

## References

Web API Reference
https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/WebHDFS.html

Zeppelin
https://zeppelin.incubator.apache.org/


