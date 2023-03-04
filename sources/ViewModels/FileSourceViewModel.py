from PySide6.QtCore import QObject
import geopandas as gpd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from ..Core.EagleEye import EagleEye
from ..Core.EagleEye.Algorithm.AlgorithmType import AlgorithmType
from ..Core.EagleEye.Clustering.ClusteringType import ClusteringType

class FileSourceViewModel(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.file_url = "N/A"
        self.clustering_type = "N/A"
        self.min_samples = "N/A"
        self.max_distance = "N/A"
        self.id_name_in_header = "N/A"
        self.time_name_in_header = "N/A"
        self.format_name_in_header = "N/A"
        self.geometery_name_in_header = "N/A"
        self.dataset = "N/A"
        self.algorithm = "N/A"

    def __str__(self):
        return((" - File Url: "+ self.file_url + "\n")
        +(" - Clustering Type: "+ self.clustering_type + "\n")
        +(" - Min Samples: "+ self.min_samples + "\n")
        +(" - Max Distance: "+ self.max_distance + "\n")
        +(" - Id Name In Header: "+ self.id_name_in_header + "\n")
        +(" - Time Name In Header: "+ self.time_name_in_header + "\n")
        +(" - Format Name In Header: "+ self.format_name_in_header + "\n")
        +(" - Geometery Name In Header: "+ self.geometery_name_in_header) + "\n")

    def preProcessing(self):
        self.dataset = gpd.read_file(self.file_url);

    def getDataSetHead(self):
        return(self.dataset.head(20))

    def getMatplotLibDbImgUrl(self):
        self.dataset = gpd.read_file(self.file_url);
        self.dataset.plot()
        plt.savefig('outputs/matplotlib/MatplotLibDbImgUrl.png')
        return ("../../outputs/matplotlib/MatplotLibDbImgUrl.png")

    def setFilePath(self, path):
        self.file_url = path

    def setClusteringType(self, type):
        self.clustering_type = type

    def setClusteringParams(self, min_samples=1 ,max_distance=3):
        self.min_samples = min_samples
        self.max_distance = max_distance

    def setIdNameInHeader(self, value):
        self.id_name_in_header = value

    def setTimeNameInHeader(self, value):
        self.time_name_in_header = value

    def setFormatNameInHeader(self, value):
        self.format_name_in_header = value

    def setGeometeryNameInHeader(self, value):
        self.geometery_name_in_header = value

    def co_movementPatternDetection(self):
        eye = EagleEye()
        eye.setAlgorithm(AlgorithmType.TRADITIONAL)
        eye.loadDataset(dname= self.file_url)
        eye.setDatasetInfo(idColName= self.id_name_in_header, timeColName=self.time_name_in_header,
        timeFormat= self.format_name_in_header, geometryColName= self.geometery_name_in_header)
        eye.setClusteringType(ClusteringType.DBSCAN)
        eye.setClusteringParams(min_samples=self.min_samples ,max_distance=self.max_distance)
        print("eye p1")
#        eye.findPatterns()

