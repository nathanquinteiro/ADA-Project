#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.exit
#

#from __future__ import print_function

# $example on$
from numpy import array
from math import sqrt
# $example off$

from pyspark import SparkContext
# $example on$
from pyspark.mllib.clustering import KMeans, KMeansModel
# $example off$

if __name__ == "__main__":


#>>>     f.write([center[0],',',center[1]])
#        f.write(str((round(center[0].item(),4)))+'\n')
    sc = SparkContext(appName="KMeansExample")  # SparkContext

    #file = '/user/jjmayor/example.txt'
    file = '/user/jjmayor/sample_loc_cleaned.tsv'
    data = sc.textFile(file)

    def show(x):
        print(x)

    #data.foreach(show)


    #Convert text to numerical values

    #parsedData = data.map(lambda line: array([float(x) for x in line.split(' ')])).cache()
    parsedData = data.map(lambda line: array([float(x) for x in line.split(',')])).cache()
    #parsedData.foreach(show)

    #Run models
    #clusters = KMeans.train(parsedData, 2, maxIterations=10, runs=10, initializationMode='random')
    clusters = KMeans.train(parsedData, 2500, maxIterations=10, runs=10, initializationMode='random')


    #Evaluating
    def error(point):
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x**2 for x in (point - center)]))

    WSSSE = (parsedData.map(lambda point:error(point)).reduce(lambda x, y: x+y))
    print('Within Set Sum of Squared Error = ' + str(WSSSE))


    # Save models
    file_save_path ='/user/jjmayor/Result1'
    clusters.save(sc, file_save_path)

    # Reload models
    #clusters = KMeansModel.load(sc, file_save_path)
