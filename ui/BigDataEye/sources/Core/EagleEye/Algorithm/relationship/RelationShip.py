import movingpandas as mpd
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import ast

from ..Algorithm import Algorithm
from ...Clustering.Cluster import Cluster
from ...Clustering.ClusteringType import ClusteringType
from ...Pattern.Pattern import Pattern
from ...Pattern.PatternType import PatternType

from ....libs.Utils import *
from pandas import DataFrame
from geopandas import GeoDataFrame
import movingpandas as mpd
import pandas as pd


class RelationShip(Algorithm):
    def __init__(self, m, k, l, g) -> None:
        Algorithm.__init__(self)
        log(f"[+] init RelationShip params M={m}, K={k}, L={l}, G={g}")
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
        log(f"[+] [RelationShip] setting cluster type {self.cluster.clusteringType}")

    def setDatasetInfo(self, idColName, timeColName, timeFormat, geometryColName):
        self.timeColName = timeColName
        self.idColName = idColName
        self.timeFormat = timeFormat
        self.geometryColName = geometryColName

    def setInputDataset(self, dname) -> None:
        log(f"[+] [RelationShip] setting dataset {dname}")
        self.dataset = gpd.read_file(dname);
        self.dataset.plot()
        run(plt.show)
        log(self.dataset.head(2))

    def extractTrajectories(self):
        log("[+] [RelationShip] extractTrajectories")

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
        log("[+] [RelationShip] plotting Trajectories") 
        f, axs = plt.subplots(1,1, figsize=(14, 6))
        for traj in self.trajectoryCollection.trajectories: 
            traj.plot(linestyle='dashed',marker=11, ax=axs, color=np.random.rand(3,))
        plt.show()

    """
    The discretization maps the real clock times to indices of the time 
    intervals during which they occurred. For instance, assume that
    we partition the time line into intervals of duration 5s and that 
    the start time is 13:00:20 UTC. Then the time series ⟨13:00:21 UTC,
    13:00:24 UTC, 13:00:28 UTC, 13:00:32 UTC, 13:00:42 UTC⟩ is discretized
    into ⟨0, 0, 1, 2, 4⟩.
    """
    def generateTimeSnapshots(self, ):
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
        
        return listOfTimeSnapshots
    
    def generateClusterSnapshots(self, listOfTimeSnapshots):
        clusters= []
        for snapshot in listOfTimeSnapshots:
            points= []
            for index, record in listOfTimeSnapshots[snapshot].iterrows():
                x = record[self.geometryColName].x
                y = record[self.geometryColName].y
                id = record[self.idColName]
                points.append([x, y, id])
            
            log("\n")
            log(listOfTimeSnapshots[snapshot])            
            d = DataFrame(data=points)
            self.cluster.setData(d)
            cluster = self.cluster.calculate()
            clusters.append(cluster)
            # run(self.cluster.plot)
            log(cluster)
            log("\n")

        return clusters
    
    '''
        N = (math.ceil(K/L) - 1) * (G - 1) + K + L - 1
        this formula guarantees that no valid pattern is missed
    '''
    def calculateMinNumberOfRequiredSnapshots(self, clusters):
        import math
        n = (math.ceil(self.minDurationOfConsecutive / self.minLengthOfConsecutive) - 1) * (self.maxConsecutiveGap - 1) + self.minDurationOfConsecutive + self.minLengthOfConsecutive - 1
        if n> len(clusters): 
            log("[+] [RelationShip] n is bigger than size. setting n as max ")
            n = len(clusters)
        return n

    def replicateClustersInPartions(self, n, clusters):
        partions = {}
        beginIndex = 0
        lastIndex = beginIndex + n
        

        while lastIndex <= len(clusters):
            for i in range(int(beginIndex), int(lastIndex)):
                if beginIndex in partions:
                    partions[beginIndex].append(clusters[i])
                else:
                    partions[beginIndex] = [clusters[i]]
            beginIndex += 1
            lastIndex += 1
        return partions

    def isLastSegmentsLenInListSmallerThanL(self, mList):
        counter = 1
        flag = False
        if self.minLengthOfConsecutive == 1:
            flag = True
        lastElement = mList[-1]
        for element in mList[-2::-1]:
            if lastElement - element == 1:
                counter += 1
                if counter >= self.minLengthOfConsecutive:
                    flag = True
                    break
            else:
                if counter >= self.minLengthOfConsecutive:
                    flag = True
                    break
        return flag

    def findCoMovementsInPartions(self, partions):
        setOfCoMovements = list()
        for _, clusterList in partions.items():
            log(f"[+] [RelationShip] - partion# {_}\n-------------------------------")

            # init c with first snapshot
            values = clusterList[0].values()
            c = {}
            for value in values:
                if len(value) >= self.minNumberOfElementsInCluster:
                    c[str(value)] = [[_ + 1], [1,1]]
            
            # finding new candidates 
            for i in range(1, len(clusterList)):
                st = list(clusterList[i].values())
                
                # REMOVE clusters with min num less than minNumberOfElementsInCluster
                st=[x for x in st if len(x)>=self.minNumberOfElementsInCluster]

                log(f"[+] [RelationShip] c[{i}] * s[{i+1}]")
                log(f"[+] [RelationShip] s[{i+1}] = " + str(st))
                log(f"[+] [RelationShip] c[{i}] = " + str(c))
                product = cartesianProductDictInList(c, st)
                listOfNewCandidates = {}
                
                for key, value in product.items():
                    keys = key.split("-")
                    cObjects = ast.literal_eval(keys[0])
                    stObjects = ast.literal_eval(keys[1])
                    objectsIntersect = list(set(cObjects) & set(stObjects))
                    timeSerie = value[0].copy()
                    timeSerie.append(_ + i + 1)
                    relation = value[1].copy()
                    relation[0] += 1
                    relation[1] += 1
                    if len(objectsIntersect) >= self.minNumberOfElementsInCluster : 
                        if (str(objectsIntersect) not in listOfNewCandidates) or (str(objectsIntersect) in listOfNewCandidates and len(timeSerie) > len(listOfNewCandidates[str(objectsIntersect)][0])):
                            listOfNewCandidates[str(objectsIntersect)] = (timeSerie, relation)
                            log(f"[+] [new] " +str(objectsIntersect)+ "->"+str((timeSerie, relation)))

                # update all times in c
                for key, value in c.items():
                    c[key][1][1] += 1

                # append listOfNewCandidates to c
                for key, value in listOfNewCandidates.items():
                    if str(key) not in c:
                        c[str(key)] = value  
                    elif len(value[0]) > len(c[str(key)][0]):
                        c[str(key)] = value        
                
                # append new values that appeared just now!
                for key in st:
                    if str(key) not in c:
                        log("[+] [new] appeared just now" + str(key))
                        c[str(key)] = [[_ + i + 1],[1,1]]   
                         
                log("new c = ")
                for key, value in c.items():
                    log(str(key) + str(value))
                
            setOfCoMovements.append(c)
 
        return setOfCoMovements

    # TRPM
    def findPatterns(self):
        log("[+] [RelationShip] find - Relation - Patterns")

        listOfTimeSnapshots = self.generateTimeSnapshots()

        clusters = self.generateClusterSnapshots(listOfTimeSnapshots)
            
        log(f"[+] [RelationShip] array of clusters generated. len = {len(clusters)}")

        n = self.calculateMinNumberOfRequiredSnapshots(clusters)

        log(f"[+] [RelationShip] n = {n} guarantees that no valid pattern is missed")

        partions = self.replicateClustersInPartions(n, clusters)

        log(f"[+] [RelationShip] partion list generated! {len(partions)} partion is generated and each length is {len(partions[0.0])}\n")

        setOfCoMovements = self.findCoMovementsInPartions(partions)
        
        log(f"\n\n[+] [RelationShip] Each Results\n")
        partion = 0
        for element in setOfCoMovements:
            partion += 1
            print(f"~>  partion #{partion}")
            for key, val in element.items():
                print("~>  ",key, val, " -> rel = ", val[1][0]/val[1][1])    
            print("------------------------------------------------------------") 
        
        # merge results
        results = dict()
        for element in setOfCoMovements:
            for key, val in element.items():
                if key in results:
                    for time in val[0]:
                        results[key].append(time)
                else:
                    results[key] = val[0]
        
        # remove duplicate results
        for key, value in results.items():
            results[key] = [set(value)]

        # calculate final relations 
        lastTime= len(clusters)
        for key, value in results.items():
            rel = len(value[0]) / (lastTime - min(value[0]) +1 )
            results[key].append(rel)
        
        log(f"\n\n[+] [RelationShip] final Results")
        for key, value in results.items():
            print(key, " - ", value)
