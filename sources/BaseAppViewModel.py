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

    def matplotLibDb(self):
        return(self._sourceViewModel.getMatplotLibDbImgUrl())

    def runCo_movementPatternDetection(self):
        result = self._sourceViewModel.co_movementPatternDetection()
        return result

    @QtCore.Slot(str, str, str, str, str)
    def setFileParams(self, id, geo, time, format, path):
        self._sourceViewModel.setFilePath(path)
        self._sourceViewModel.setGeometeryNameInHeader(geo)
        self._sourceViewModel.setFormatNameInHeader(format)
        self._sourceViewModel.setTimeNameInHeader(time)
        self._sourceViewModel.setIdNameInHeader(id)

    @QtCore.Slot(str, str, str)
    def setClusteringParams(self, min_samples, max_distance, type):
        self._sourceViewModel.setClusteringParams(min_samples, max_distance)
        self._sourceViewModel.setClusteringType(type)

    @QtCore.Slot(str, str, str, str)
    def setGCMPParams(self, m, l, k, g):
        self._sourceViewModel.setGcmpM(m)
        self._sourceViewModel.setGcmpG(g)
        self._sourceViewModel.setGcmpL(l)
        self._sourceViewModel.setGcmpK(k)

    @QtCore.Slot(str)
    def setRelationParams(self, r):
        self._sourceViewModel.setRelR(r)
