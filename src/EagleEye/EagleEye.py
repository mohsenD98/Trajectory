import movingpandas as mpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from EagleEye.Algorithm.Algorithm import Algorithm
from EagleEye.Algorithm.AlgorithmType import AlgorithmType

from EagleEye.Clustering.ClusteringType import ClusteringType
from EagleEye.Pattern.PatternType import PatternType
from EagleEye.Algorithm.traditional.Traditional import Traditional
from Elibs import *

class EagleEye:
    def __init__(self) -> None:
        log("[+] initialing Eagle Eye")
        self.patternType = PatternType.ALL
        self.clusteringType = ClusteringType.DISTANCE
        self.trajCollection = ""
        self.algorithmType = ""
        self.algorithm = Algorithm()

    @classmethod
    def setAlgorithm(self, alg) -> None:
        log(f"[+] setting algorithm {alg}")
        self.algorithmType = alg

    @classmethod
    def setClusteringType(self, ctype) -> None:
        log(f"[+] setting clustering type to {ctype}")
        self.clusteringType = ctype
    
    @classmethod
    def setPatternType(self, ptype) -> None:
        log(f"[+] setting patteron type to {ptype}. eye will look for {ptype}")
        self.patternType = ptype

    @classmethod
    def loadDataset(self, dname) -> None:
        log(f"[+] loading {dname} dataset" )
    
    @classmethod
    def setGeoDf(self, gdf, idColName, timeColName, timeFormat) -> None:
        log(f"[+] setting geo df" )
        self.geoDf = gdf
        self.geoDf['time'] = pd.to_datetime(self.geoDf[timeColName], format=timeFormat)
        self.geoDf = self.geoDf.set_index('time')
        log(self.geoDf.head())
        self.trajCollection = mpd.TrajectoryCollection(self.geoDf, idColName)
        for trajectory in self.trajCollection.trajectories:
            # Calculate speed
            trajectory.add_speed(overwrite=True)
            
            # Determine direction of movement
            trajectory.add_direction(overwrite=True)


    @classmethod
    def findPatterns(self) -> None:
        log("[+] searching for patterns")
        if self.algorithmType == AlgorithmType.TRADITIONAL:
            self.algorithm = Traditional()
        self.algorithm.findPatterns()
        
        

    @classmethod
    def plotGeoDf(self) -> None:
        log("[+] plotting geoDf")
        f, axs = plt.subplots(1,1, figsize=(14, 6))

        for traj in self.trajCollection.trajectories: 
            traj.plot(linestyle='dashed',marker=11, ax=axs, color=np.random.rand(3,))

        plt.show()

    @classmethod
    def showPatterns(self) -> None:
        log("[+] patterns ")