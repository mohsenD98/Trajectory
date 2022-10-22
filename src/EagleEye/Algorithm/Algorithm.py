class Algorithm():
    def __init__(self) -> None:
        pass

    def findPatterns(self) -> None:
        raise NotImplementedError()

    def setInputDataset(self, dname) -> None:
        raise NotImplementedError()

    def plotTrajectories(self): 
        raise NotImplementedError()

    def extractTrajectories(self):
        raise NotImplementedError()

    def setDatasetInfo(self, idColName, timeColName, timeFormat, geometryColName):
        raise NotImplementedError()

    def setClusteringParams(self, idColName, timeColName, timeFormat, geometryColName):
        raise NotImplementedError()

        