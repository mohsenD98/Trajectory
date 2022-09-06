import movingpandas as mpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from EagleEye.Clustering.ClusteringType import ClusteringType
from EagleEye.Pattern.PatternType import PatternType


class EagleEye:
    def __init__(self) -> None:
        print("[+] initialing Eagle Eye")
        self.patternType = PatternType.ALL
        self.clusteringType = ClusteringType.DISTANCE
        self.trajCollection = ""

    @classmethod
    def setClusteringType(self, ctype) -> None:
        print(f"[+] setting clustering type to {ctype}")
        self.clusteringType = ctype
    
    @classmethod
    def setPatternType(self, ptype) -> None:
        print(f"[+] setting patteron type to {ptype}. eye will look for {ptype}")
        self.patternType = ptype

    @classmethod
    def loadDataset(self, dname) -> None:
        print(f"[+] loading {dname} dataset" )
    
    @classmethod
    def setGeoDf(self, gdf, idColName, timeColName, timeFormat) -> None:
        print(f"[+] setting geo df" )
        self.geoDf = gdf
        self.geoDf['time'] = pd.to_datetime(self.geoDf[timeColName], format=timeFormat)
        self.geoDf = self.geoDf.set_index('time')
        print(self.geoDf.head())
        self.trajCollection = mpd.TrajectoryCollection(self.geoDf, idColName)
        for trajectory in self.trajCollection.trajectories:
            # Calculate speed
            trajectory.add_speed(overwrite=True)
            
            # Determine direction of movement
            trajectory.add_direction(overwrite=True)


    @classmethod
    def findPatterns(self) -> None:
        print("[+] searching for patterns")

    @classmethod
    def plotGeoDf(self) -> None:
        print("[+] plotting geoDf")
        f, axs = plt.subplots(1,1, figsize=(14, 6))

        for traj in self.trajCollection.trajectories: 
            traj.plot(linestyle='dashed',marker=11, ax=axs, color=np.random.rand(3,))

        plt.show()

        

    @classmethod
    def showPatterns(self) -> None:
        print("[+] patterns ")
    
    @classmethod
    def plotPatterns(self) -> None:
        print("[+] plotting patterns")