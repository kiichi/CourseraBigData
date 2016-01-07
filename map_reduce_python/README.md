## Summary

1. Create Mapper and Reducer Files
2. Give permissions
3. Put input files into a hdfs folder
4. Run hadoop command and load .jar file with input dir and outoput dir
5. Get the file back

## Mapper and Reducer

* wordcount_mapper.py
* wordcount_reducer.py

```
chmod +x wordcount_mapper.py
chmod +x wordcount_reducer.py
```

## Test python program
```
cat input.txt | python wordcount_mapper.py | sort > mapped.txt
cat mapped.txt | python wordcount_reducer.py
```
## Upload files

```
hdfs dfs -put input.txt /user/cloudera/input
hdfs dfs -put input2.txt /user/cloudera/input
hdfs dfs -ls /user/cloudera/input
```

## Run Map / Reduce

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
   -input /user/cloudera/input \
   -output /user/cloudera/output_new_0 \
   -mapper /home/cloudera/wordcount_mapper.py \
   -reducer /home/cloudera/wordcount_reducer.py \
```

In case if you get the permission error (e.g. left safemode via hdfs user), specify the sudo with user

```
sudo -u hdfs hadoop jar ...(same command above)
```

In order to test without reduce process, use this option below
```
   -numReduceTasks 0
```

## Check the results

```
hdfs dfs -ls output_new_0
hdfs dfs -cat output_new_0/part-00000
```

## Download output

```
hdfs dfs -getmerge /user/cloudera/output_new_0/* wordcount_num0_output.txt
```



