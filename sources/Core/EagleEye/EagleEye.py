from .Algorithm.Algorithm import Algorithm
from .Algorithm.AlgorithmType import AlgorithmType
from .Algorithm.relationship.RelationShip import RelationShip
from .Algorithm.indexing.Indexing import Index

from .Clustering.ClusteringType import ClusteringType
from .Algorithm.traditional.Traditional import Traditional

from ..libs.Utils import log
from ..libs import Utils
from ..libs.Utils import InputsType

class EagleEye:
    def __init__(self):
        log("[+] initialing Eagle Eye")
        self.clusteringType = ClusteringType.DISTANCE
        self.trajCollection = ""
        self.algorithmType = ""
        self.gcmpParamList = []
        self.algorithm = Algorithm()

    def setGCMPParamList(self, value):
        # [m, k, l, g]
        self.gcmpParamList = value


    def setAlgorithm(self, alg):
        log(f"[+] setting algorithm {alg}")
        self.algorithmType = alg

        if self.algorithmType == AlgorithmType.TRADITIONAL:
            self.algorithm = Traditional(m=self.gcmpParamList[0], k=self.gcmpParamList[1], l=self.gcmpParamList[2], g=self.gcmpParamList[3])
        
        elif self.algorithmType == AlgorithmType.RELATION:
            self.algorithm = RelationShip(m=self.gcmpParamList[0], k=self.gcmpParamList[1], l=self.gcmpParamList[2], g=self.gcmpParamList[3])
        
        elif self.algorithmType == AlgorithmType.INDEXING:
            self.algorithm = Index(m=self.gcmpParamList[0], k=self.gcmpParamList[1], l=self.gcmpParamList[2], g=self.gcmpParamList[3])

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

    def findComovementPatterns(self):
        log("[+] searching for patterns")
        return(self.algorithm.findPatterns())
    
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
