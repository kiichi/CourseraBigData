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

##
