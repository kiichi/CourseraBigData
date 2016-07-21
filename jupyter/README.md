# How to run pyspark on jupyter

1. Download and build spark

```
build/mvn -DskipTests clean package
```

2. Change the last line of the launch script 

```
vim ./bin/pyspark
```

to

```
jupyter notebook
```

Try to imposrt one of python library and run 

```
from pyspark.mllib.clustering import KMeans, KMeansModel
```

Example slightly modified from  http://spark.apache.org/docs/latest/mllib-clustering.html#k-means

```
import pandas as pd
from pyspark.mllib.clustering import KMeans, KMeansModel
from numpy import array,sqrt

data = sc.textFile("data/mllib/kmeans_data.txt")
parsedData = data.map(lambda line: array([float(x) for x in line.split(' ')]))
# Build the model (cluster the data)
clusters = KMeans.train(parsedData, 2, maxIterations=10,
        runs=10, initializationMode="random")

# Evaluate clustering by computing Within Set Sum of Squared Errors
def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
print("Within Set Sum of Squared Error = " + str(WSSSE))

# Save and load model
clusters.save(sc, "myModelPath2")
sameModel = KMeansModel.load(sc, "myModelPath2")
print('done')
```
