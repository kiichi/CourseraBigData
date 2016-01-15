## Description

This folder contains two examples.

Files that contains join1_* are example of Word Count with Dates. This is an example that bringing Date part as value, then join the counts.
join2_* files are example of number of shows and tv channels. This is an example that does filtering and aggregates counts to sum.

Note:

Hadoop stream can take multiple files. If you specify a mapper program, it should detect type of file in each lines and process accordingly.
For mapper output & reducer input, use tab delmited to pass it on. When you write reducer, be careful to code that execution might happen 
in multiple nodes. The result might be ended up with different from the test one.

These steps are very similar to what I described in ./map_reduce_python folder.

## Process

1. Change permission add +x on .py files

e.g.
```
chmod +x join2_mapper.py
chmod +x join2_reducer.py
```

2. Upload Data

```
hdfs dfs -mkdir input_join
hdfs dfs -put join2_gen*.txt input_join2
hdfs dfs -ls input_join
```

3. Test map and reduce before run

```
 cat join2_gen*.txt | python join2_mapper.py   | sort > mapped2.txt
 cat join2_gen*.txt | python join2_mapper.py   | sort | python join2_reducer.py 
 cat join2_gen*.txt | python join2_mapper.py   | sort | python join2_reducer.py | grep ABC
 cat join2_gen*.txt | python join2_mapper.py   | sort | python join2_reducer.py > output_join2_test.txt
```

4. Run
```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /user/cloudera/input_join2/ -output /user/cloudera/output_join2 -mapper /home/cloudera/work/map_reduce_join_python/join2_mapper.py -reducer /home/cloudera/work/map_reduce_join_python/join2_reduce --numReduceTasks 1
```

5. Check outpout

Proccessed by Hadoop and Unix command line test should match
```
hdfs dfs -ls /user/cloudera/output_join2
hdfs dfs -cat /user/cloudera/output_join2/part-00000
hdfs dfs -getmerge /user/cloudera/output_join2 output_join2.txt
diff output_join2.txt output_join2_test.txt
```

Appendix
Files have been generated make_... py program
