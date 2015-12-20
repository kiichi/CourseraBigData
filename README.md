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
