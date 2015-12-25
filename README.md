# CourseraBigData

## HDFS

put some file to parse out

```
[cloudera@quickstart CourseraBigData]$ hdfs dfs -ls /user/coursera
[cloudera@quickstart CourseraBigData]$ hdfs dfs -mkdir /user/coursera
[cloudera@quickstart CourseraBigData]$ hdfs dfs -put ~/Downloads/iris.csv /user/cloudera
[cloudera@quickstart CourseraBigData]$ hdfs dfs -ls /user/coursera
```

Check File Stats (e.g. # of Blocks) or check the entire  DataNode Status
```
hdfs fsck /user/cloudera/iris.csv
hdfs dfsadmin -report
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

## References

https://zeppelin.incubator.apache.org/


