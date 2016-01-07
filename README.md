# CourseraBigData

## Basic Operations

start stop datanode or tasktracker
```
/usr/lib/hadoop/sbin/hadoop-daemon.sh tasktracker start
/usr/lib/hadoop/sbin/hadoop-daemon.sh datanode start
```

Note: most of services should be able to start via Cloudera Manager web interface localhost:7180

## HDFS

put some file to parse out

```
[cloudera@quickstart CourseraBigData]$ hdfs dfs -ls /user/cloudera
[cloudera@quickstart CourseraBigData]$ hdfs dfs -mkdir /user/cloudera
[cloudera@quickstart CourseraBigData]$ hdfs dfs -put ~/Downloads/iris.csv /user/cloudera
[cloudera@quickstart CourseraBigData]$ hdfs dfs -ls /user/cloudera
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

Test python program
```
cat input.txt | python wordcount_mapper.py | sort > mapped.txt
cat mapped.txt | python wordcount_reducer.py
```


## References

Web API Reference
https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/WebHDFS.html

Zeppelin
https://zeppelin.incubator.apache.org/


