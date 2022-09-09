from EagleEye.Algorithm.Algorithm import Algorithm
from EagleEye.Algorithm.AlgorithmType import AlgorithmType

from EagleEye.Clustering.ClusteringType import ClusteringType
from EagleEye.Pattern.PatternType import PatternType
from EagleEye.Algorithm.traditional.Traditional import Traditional
from libs import *

class EagleEye:
    def __init__(self):
        log("[+] initialing Eagle Eye")
        self.patternType = PatternType.ALL
        self.clusteringType = ClusteringType.DISTANCE
        self.trajCollection = ""
        self.algorithmType = ""
        self.algorithm = Algorithm()

    def setAlgorithm(self, alg):
        log(f"[+] setting algorithm {alg}")
        self.algorithmType = alg

        if inputsType == InputsType.USER_TERMINAL: 
            paramList= get("enter M, K, L, G (seperated by space): ", inputLen=4)
        elif inputsType == InputsType.DEFAULT_TESTS: 
            paramList= [2, 2, 2, 2]


        if self.algorithmType == AlgorithmType.TRADITIONAL:
            self.algorithm = Traditional(m=paramList[0], k=paramList[1], l=paramList[2], g=paramList[3])

    @classmethod
    def setClusteringType(self, ctype) -> None:
        log(f"[+] setting clustering type to {ctype}")
        self.clusteringType = ctype
    
    @classmethod
    def setPatternType(self, ptype) -> None:
        log(f"[+] setting patteron type to {ptype}. eye will look for {ptype}")
        self.patternType = ptype

    def loadDataset(self, dname):
        log(f"[+] loading {dname} dataset" )
        self.algorithm.setInputDataset(dname)
    
    def extractTrajectories(self):
        self.algorithm.extractTrajectories()

    def setDatasetInfo(self, idColName, timeColName, timeFormat):
        log("[+] setting dataset info")
        self.algorithm.setDatasetInfo(idColName, timeColName, timeFormat)

    def findPatterns(self) -> None:
        log("[+] searching for patterns")
        self.algorithm.findPatterns()
        
    def plotTrajectories(self):
        log("[+] plotting trajectories")
        self.algorithm.plotTrajectories()