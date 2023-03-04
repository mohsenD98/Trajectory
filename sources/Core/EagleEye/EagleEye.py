from .Algorithm.Algorithm import Algorithm
from .Algorithm.AlgorithmType import AlgorithmType
from .Algorithm.relationship.RelationShip import RelationShip
from .Algorithm.indexing.Indexing import Index

from .Clustering.ClusteringType import ClusteringType
from .Algorithm.traditional.Traditional import Traditional
from ..libs import *

class EagleEye:
    def __init__(self):
        log("[+] initialing Eagle Eye")
        self.clusteringType = ClusteringType.DISTANCE
        self.trajCollection = ""
        self.algorithmType = ""
        self.algorithm = Algorithm()

    def setAlgorithm(self, alg):
        log(f"[+] setting algorithm {alg}")
        self.algorithmType = alg

        if Utils.inputsType == InputsType.USER_TERMINAL: 
            paramList= get("enter M, K, L, G (seperated by space): ", inputLen=4)
        elif Utils.inputsType == InputsType.DEFAULT_TESTS: 
            # in platoon L should be 1
            paramList= [2, 3, 2, 2]
            log(f"using default params for M= {paramList[0]}, K={paramList[1]} L={paramList[2]} G={paramList[3]} ", important= True)
                
        if self.algorithmType == AlgorithmType.TRADITIONAL:
            self.algorithm = Traditional(m=paramList[0], k=paramList[1], l=paramList[2], g=paramList[3])
        
        elif self.algorithmType == AlgorithmType.RELATION:
            self.algorithm = RelationShip(m=paramList[0], k=paramList[1], l=paramList[2], g=paramList[3])
        
        elif self.algorithmType == AlgorithmType.INDEXING:
            self.algorithm = Index(m=paramList[0], k=paramList[1], l=paramList[2], g=paramList[3])

    def setClusteringType(self, ctype):
        log(f"[+] setting clustering type to {ctype}")
        self.algorithm.setClusteringType(ctype)
    
    def setClusteringParams(self, min_samples=2 ,max_distance=2, k_means_cluster_count= 3):
        self.algorithm.setClusteringParams(min_samples=min_samples ,max_distance=max_distance, k_means_cluster_count= k_means_cluster_count)

    def loadDataset(self, dname):
        log(f"[+] loading {dname} dataset" )
        self.algorithm.setInputDataset(dname)
    
    def extractTrajectories(self):
        self.algorithm.extractTrajectories()

    def setDatasetInfo(self, idColName, timeColName, timeFormat, geometryColName):
        log("[+] setting dataset info")
        self.algorithm.setDatasetInfo(idColName, timeColName, timeFormat, geometryColName)

    def findComovementPatterns(self) -> None:
        log("[+] searching for patterns")
        self.algorithm.findPatterns()
    
    def findeRelationPatterns(self):
        log("[+] searching for patterns")
        self.algorithm.findPatterns()
        
    def plotTrajectories(self):
        log("[+] plotting trajectories")
        self.algorithm.plotTrajectories()      

    def saveIndexedPatterns(self):
        log("[+] save Indexed Patterns")
        self.algorithm.saveIndexedPatterns()

    def loadIndexedPatterns(self):
        log("[+] load Indexed Patterns")
        self.algorithm.loadIndexedPatterns()
