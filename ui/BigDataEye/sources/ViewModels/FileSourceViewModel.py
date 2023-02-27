from PySide6.QtCore import QObject
import geopandas as gpd


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

    def __str__(self):
        return((" - file_url: "+ self.file_url + "\n")
        +(" - clustering_type: "+ self.clustering_type + "\n")
        +(" - min_samples: "+ self.min_samples + "\n")
        +(" - max_distance: "+ self.max_distance + "\n")
        +(" - id_name_in_header: "+ self.id_name_in_header + "\n")
        +(" - time_name_in_header: "+ self.time_name_in_header + "\n")
        +(" - format_name_in_header: "+ self.format_name_in_header + "\n")
        +(" - geometery_name_in_header: "+ self.geometery_name_in_header) + "\n")

    def preProcessing(self):
        self.dataset = gpd.read_file(self.file_url);

    def getDataSetHead(self):
        return(self.dataset.head(20))

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
