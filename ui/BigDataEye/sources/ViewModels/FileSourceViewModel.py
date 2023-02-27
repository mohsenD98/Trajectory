from PySide6.QtCore import QObject


class FileSourceViewModel(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.file_url = "N/A"
        self.clustering_type = "N/A"
        self.min_samples = "N/A"
        self.max_distance = "N/A"

    def setFilePath(self, path):
        self.file_url = path

    def setClusteringType(self, type):
        self.clustering_type = type

    def setClusteringParams(self, min_samples=1 ,max_distance=3):
        self.min_samples = min_samples
        self.max_distance = max_distance
