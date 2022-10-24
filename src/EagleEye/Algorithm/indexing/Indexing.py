from math import ceil, floor
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


class Index(Algorithm):
    def __init__(self, m, k, l, g) -> None:
        Algorithm.__init__(self)
        log(f"[+] init Index params M={m}, K={k}, L={l}, G={g}")
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
        log(f"[+] [Index] setting cluster type {self.cluster.clusteringType}")

    def setDatasetInfo(self, idColName, timeColName, timeFormat, geometryColName):
        self.timeColName = timeColName
        self.idColName = idColName
        self.timeFormat = timeFormat
        self.geometryColName = geometryColName

    def setInputDataset(self, dname) -> None:
        log(f"[+] [Index] setting dataset {dname}")
        self.dataset = gpd.read_file(dname);
        self.dataset.plot()
        run(plt.show)
        log(self.dataset.head(2))

    def extractTrajectories(self):
        log("[+] [Index] extractTrajectories")

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
        log("[+] [Index] plotting Trajectories") 
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
    
    def splitData(self, n, clusters):
        partions = {}
        eachPartionLen = ceil(len(clusters) / n)
        i = 0
        
        counter = 0
        for el in clusters:
            if counter >= eachPartionLen:
                i += 1
                counter = 0
                
            if i in partions: 
                partions[i].append(el)
            else:
                partions[i] = [el]
            counter += 1

        return partions


    def indexEach(self, partions):
        setOfCoMovements = list()
        for _, clusterList in partions.items():
            log(f"[+] [Index] - partion# {_}\n-------------------------------")
        
            for i in range(0, len(clusterList)):
                st = list(clusterList[i].values())
                st=[x for x in st if len(x)>=self.minNumberOfElementsInCluster]
                print(st)

                    
        return setOfCoMovements

    # TRPM
    def saveIndexedPatterns(self):
        log("[+] [Index] find - Relation - Patterns")

        listOfTimeSnapshots = self.generateTimeSnapshots()

        clusters = self.generateClusterSnapshots(listOfTimeSnapshots)
            
        log(f"[+] [Index] array of clusters generated. len = {len(clusters)}")

        n = 2

        log(f"[+] [Index] we will split all data to {n} segment. ")

        partions = self.splitData(n, clusters)

        log(f"[+] [Index] partion list generated! {len(partions)} partion is generated! \n")

        setOfCoMovements = self.indexEach(partions)
        
        log(f"\n\n[+] [Index] Each Results\n")

        log(f"\n\n[+] [Index] final Results")
