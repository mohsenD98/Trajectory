import movingpandas as mpd
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

from typing import overload
from EagleEye.Algorithm.Algorithm import Algorithm
from EagleEye.Clustering.Cluster import Cluster
from EagleEye.Clustering.ClusteringType import ClusteringType
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
        self.discretizationTimeSteps = 60

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
            run(self.cluster.plot)
            log(cluster)
        log(clusters)

        # pattern enumration from clusters