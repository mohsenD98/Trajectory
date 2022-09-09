import movingpandas as mpd
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

from typing import overload
from EagleEye.Algorithm.Algorithm import Algorithm
from libs.Utils import *
from geopandas import GeoDataFrame
import movingpandas as mpd
import pandas as pd


class Traditional(Algorithm):
    def __init__(self, m, k, l, g) -> None:
        Algorithm.__init__(self)
        log(f"[+] init Traditional params M={m}, K={k}, L={l}, G={g}")

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

    def setInputDataset(self, dname) -> None:
        log(f"[+] [Traditional] setting dataset {dname}")
        self.dataset = gpd.read_file(dname);
        log(self.dataset.head(2))

    def extractTrajectories(self,idColName, timeColName, timeFormat):
        log("[+] [Traditional] extractTrajectories")

        # Create trajectories
        self.dataset['time'] = pd.to_datetime(self.dataset[timeColName], format=timeFormat)
        self.dataset = self.dataset.set_index('time')

        # Specify minimum length for a trajectory (in meters)
        minimum_length = 100 
        self.trajectoryCollection = mpd.TrajectoryCollection(self.dataset, idColName, min_length=minimum_length)

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

        # make cluster snapshots at time - -> end

        # pattern enumration from clusters