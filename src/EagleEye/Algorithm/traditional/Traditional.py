import movingpandas as mpd
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import ast

from EagleEye.Algorithm.Algorithm import Algorithm
from EagleEye.Clustering.Cluster import Cluster
from EagleEye.Clustering.ClusteringType import ClusteringType
from EagleEye.Pattern.Pattern import Pattern
from EagleEye.Pattern.PatternType import PatternType

from libs.Utils import *
from pandas import DataFrame
from geopandas import GeoDataFrame
import movingpandas as mpd
import pandas as pd


class Traditional(Algorithm):
    def __init__(self, m, k, l, g) -> None:
        Algorithm.__init__(self)
        log(f"[+] init Traditional params M={m}, K={k}, L={l}, G={g}")
        # Discretization times in seconds
        self.discretizationTimeSteps = 60 # (seconds)
        # the min number of elements in cluster
        self.minNumberOfElementsInCluster = m
        # min duration constraint
        self.minDurationOfConsecutive = k
        # min length of each consecutive
        self.minLengthOfConsecutive = l
        # max gap between each consecutive
        self.maxConsecutiveGap = g

        # offline dataset to mining
        self.dataset = ""
        self.gdf =  GeoDataFrame()
        self.trajectoryCollection = mpd.TrajectoryCollection(data=[])

        # pattern class
        self.patternDetector = Pattern(m = self.minNumberOfElementsInCluster, k=self.minDurationOfConsecutive, l=self.minLengthOfConsecutive, g=self.maxConsecutiveGap)

        # clustering class
        self.cluster = Cluster()
        self.cluster.setClusteringType(ClusteringType.KMEANS)

        self.timeColName = ""
        self.timeFormat = ""
        self.idColName = ""
        self.geometryColName = ""

    def setClusteringParams(self, min_samples=2 ,max_distance=2, k_means_cluster_count= 3):
        self.cluster.setClusteringParams(min_samples=min_samples ,max_distance=max_distance, k_means_cluster_count= k_means_cluster_count) 

    def setClusteringType(self, type):
        self.cluster.setClusteringType(type)
        log(f"[+] [Traditional] setting cluster type {self.cluster.clusteringType}")

    def setDatasetInfo(self, idColName, timeColName, timeFormat, geometryColName):
        self.timeColName = timeColName
        self.idColName = idColName
        self.timeFormat = timeFormat
        self.geometryColName = geometryColName

    def setInputDataset(self, dname) -> None:
        log(f"[+] [Traditional] setting dataset {dname}")
        self.dataset = gpd.read_file(dname);
        log(self.dataset.head(2))

    def extractTrajectories(self):
        log("[+] [Traditional] extractTrajectories")

        # Create trajectories
        self.dataset['time'] = pd.to_datetime(self.dataset[self.timeColName], format=self.timeFormat)
        self.dataset = self.dataset.set_index('time')

        # Specify minimum length for a trajectory (in meters)
        minimum_length = 100 
        self.trajectoryCollection = mpd.TrajectoryCollection(self.dataset, self.idColName, min_length=minimum_length)

        for trajectory in self.trajectoryCollection.trajectories:
            # Calculate speed
            trajectory.add_speed(overwrite=True)
            
            # Determine direction of movement
            trajectory.add_direction(overwrite=True)
        
        log(self.trajectoryCollection)
    
    def plotTrajectories(self):
        log("[+] [Traditional] plotting Trajectories") 
        f, axs = plt.subplots(1,1, figsize=(14, 6))
        for traj in self.trajectoryCollection.trajectories: 
            traj.plot(linestyle='dashed',marker=11, ax=axs, color=np.random.rand(3,))
        plt.show()

    def findPatterns(self):
        log("[+] [Traditional] findPatterns")

        # make snapshot at time - -> end with time step x
        centralTime= self.dataset[self.timeColName][0]
        self.dataset['last_time'] = (self.dataset.apply(lambda x: (x[self.timeColName] - centralTime).seconds / self.discretizationTimeSteps ,axis=1))
        listOfTimeSnapshots = {}

        for index, row in self.dataset.iterrows():
            if row["last_time"] in listOfTimeSnapshots:
                df = pd.DataFrame(columns=self.dataset.columns, data=[row])
                geo_df = GeoDataFrame(df)
                listOfTimeSnapshots[row["last_time"]] = listOfTimeSnapshots[row["last_time"]].append(geo_df)
            else:
                df = pd.DataFrame(columns=self.dataset.columns, data=[row])
                geo_df = GeoDataFrame(df)
                listOfTimeSnapshots[row["last_time"]] = geo_df

        # make cluster snapshots at time - -> end
        clusters= []
        for snapshot in listOfTimeSnapshots:
            points= []
            for index, record in listOfTimeSnapshots[snapshot].iterrows():
                x = record[self.geometryColName].x
                y = record[self.geometryColName].y
                id = record[self.idColName]
                points.append([x, y, id])
            
            log("\n\n")
            log(listOfTimeSnapshots[snapshot])            
            d = DataFrame(data=points)
            self.cluster.setData(d)
            cluster = self.cluster.calculate()
            clusters.append(cluster)
            # run(self.cluster.plot)
            log(cluster)
            
        log("\n")
        log(f"[+] [Traditional] array of clusters generated. len = {len(clusters)}")

        # pattern enumration from clusters
        # TRPM
        # ----------------------------------

        # STAGE 1: CALCULATE N = (math.ceil(K/L) - 1) * (G - 1) + K + L - 1
        # this formula guarantees that no valid pattern is missed
        # ----------------------------------
        import math
        n = (math.ceil(self.minDurationOfConsecutive / self.minLengthOfConsecutive) - 1) * (self.maxConsecutiveGap - 1) + self.minDurationOfConsecutive + self.minLengthOfConsecutive - 1
        if n> len(clusters): 
            log("[+] [Traditional] n is bigger than size. setting n as max ")
            n = len(clusters)
        log(f"[+] [Traditional] n = {n} guarantees that no valid pattern is missed")

        # STAGE 2: partitioning clusters: 
        # ----------------------------------
        partions = {}
        beginIndex = 0
        lastIndex = beginIndex + n
        

        while lastIndex <= len(clusters):
            for i in range(beginIndex, lastIndex):
                if beginIndex in partions:
                    partions[beginIndex].append(clusters[i])
                else:
                    partions[beginIndex] = [clusters[i]]
            beginIndex += 1
            lastIndex += 1

        log(f"[+] [Traditional] partion list generated! {len(partions)} partion is generated and each length is {len(partions[0.0])}\n")

        # STAGE 3: search in each partion to find co-movements: 
        # ----------------------------------
        for _, clusterList in partions.items():
            log(f"[+] [Traditional] - partion# {_}\n---------------------")

            # init c with firs snapshot
            values = clusterList[0].values()
            c = {}
            for value in values:
                c[str(value)] = [1]
                
            log("[+] [Traditional] initial c = " + str(c))
            for i in range(1, len(clusterList)):
                st = list(clusterList[i].values())
                log(f"[+] [Traditional] s[{i+1}] = " + str(st))
                log(f"[+] [Traditional] c = " + str(c))
                product = cartesianProductDictInList(c, st)
                listOfNewCandidates = {}
                
                for key, value in product.items():
                    keys = key.split("-")
                    cObjects = ast.literal_eval(keys[0])
                    stObjects = ast.literal_eval(keys[1])
                    objectsIntersect = list(set(cObjects) & set(stObjects))
                    timeSerie = value.copy()
                    timeSerie.append(i+1)
                    if len(objectsIntersect) >= self.minNumberOfElementsInCluster : # timeSerie is valid output objectsIntersect
                        result =  self.patternDetector.validatePattern(timeSerie=timeSerie)
                        if result[0] == True:
                            log(f"[+] [Traditional] pattern found in {objectsIntersect} - {timeSerie} -> " + str(result[1]), True)
                        #else:
                        listOfNewCandidates[str(objectsIntersect)] = timeSerie

                log("[+] [Traditional] N = " + str(listOfNewCandidates))
                    
                # pruning c
                listToDelete = []
                for mkey, value in c.items():
                    if len(objectsIntersect) >= self.minNumberOfElementsInCluster : # timeSerie is valid output objectsIntersect
                        result =  self.patternDetector.validatePattern(timeSerie=timeSerie)
                        if result[0] == True:
                            log(f"[+] [Traditional] pattern found in {objectsIntersect} - {timeSerie} -> " + str(result[1]), True)
                        
                    key = ast.literal_eval(mkey)
                    # gap is bigger than specified
                    if i+1 - max(value) >= self.maxConsecutiveGap:
                        listToDelete.append(key)
                    # last segement len is < L
                    if len(value) < self.minLengthOfConsecutive: 
                        listToDelete.append(key)
                    
                    counter = 1
                    flag = False
                    if self.minLengthOfConsecutive == 1:
                        flag = True
                    lastElement = value[-1]
                    for element in value[-2::-1]:
                        if lastElement - element == 1:
                            counter += 1
                            if counter >= self.minLengthOfConsecutive:
                                flag = True
                                break
                        else:
                            if counter >= self.minLengthOfConsecutive:
                                flag = True
                                break
                    if not flag:
                        listToDelete.append(key)

                for key in listToDelete:
                    if str(key) in c: 
                        del c[str(key)]

                # append listOfNewCandidates to c
                for key, time in listOfNewCandidates.items():
                    c[str(key)] = time
                
            log("\n[+] [Traditional] discovered patterns: "+ str(c) + "\n", True)
                