# Cluster

[Link to documentation](https://spark.apache.org/docs/latest/mllib-clustering.html)


## Example :

### Save clusters :

clusters.save(sc, "target/org/apache/spark/PythonKMeansExample/KMeansModel")

### Load clusters :

sameModel = KMeansModel.load(sc, "target/org/apache/spark/PythonKMeansExample/KMeansModel")
