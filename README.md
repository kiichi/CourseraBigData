# CourseraBigData


## HDFS

put some file to parse out

```
[cloudera@quickstart CourseraBigData]$ hdfs dfs -ls /user/coursera
[cloudera@quickstart CourseraBigData]$ hdfs dfs -mkdir /user/coursera
[cloudera@quickstart CourseraBigData]$ hdfs dfs -put ~/Downloads/iris.csv /user/cloudera
[cloudera@quickstart CourseraBigData]$ hdfs dfs -ls /user/coursera
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
