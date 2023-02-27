from PySide6 import QtCore
from sources.ViewModels.FileSourceViewModel import FileSourceViewModel

class BaseAppViewModel(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self._source = "FileSource"
        self._sourceViewModel = FileSourceViewModel()

    def __str__(self):
        return ("params for " + self._source + "\n" + str(self._sourceViewModel))

    def preprocessing(self):
        self._sourceViewModel.preProcessing()

    def getDataSetHead(self):
        return(self._sourceViewModel.getDataSetHead())

    @QtCore.Slot(str)
    def setFilePath(self, path):
        self._sourceViewModel.setFilePath(path)

    @QtCore.Slot(str)
    def setClusteringType(self, type):
        self._sourceViewModel.setClusteringType(type)

    @QtCore.Slot(str)
    def setIdNameInHeader(self, value):
        self._sourceViewModel.setIdNameInHeader(value)

    @QtCore.Slot(str)
    def setTimeNameInHeader(self, value):
        self._sourceViewModel.setTimeNameInHeader(value)

    @QtCore.Slot(str)
    def setFormatNameInHeader(self, value):
        self._sourceViewModel.setFormatNameInHeader(value)

    @QtCore.Slot(str)
    def setGeometeryNameInHeader(self, value):
        self._sourceViewModel.setGeometeryNameInHeader(value)

    @QtCore.Slot(str, str)
    def setClusteringParams(self, min_samples, max_distance):
        self._sourceViewModel.setClusteringParams(min_samples, max_distance)
