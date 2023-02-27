from PySide6 import QtCore
from sources.ViewModels.FileSourceViewModel import FileSourceViewModel

class BaseAppParams(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self._source = "FileSource"
        self._sourceViewModel = FileSourceViewModel()

    @QtCore.Slot(str)
    def setFilePath(self, path):
        self._sourceViewModel.setFilePath(path)

    @QtCore.Slot(str)
    def setClusteringType(self, type):
        self._sourceViewModel.setClusteringType(type)

    @QtCore.Slot(str, str)
    def setClusteringParams(self, min_samples, max_distance):
        self._sourceViewModel.setClusteringParams(min_samples, max_distance)

