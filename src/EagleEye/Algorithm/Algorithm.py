class Algorithm():
    def __init__(self) -> None:
        pass

    def findPatterns(self) -> None:
        raise NotImplementedError()


    def setInputDataset(self, dname, idColName, timeColName, timeFormat) -> None:
        raise NotImplementedError()

    def plotTrajectories(self): 
        raise NotImplementedError()

    def extractTrajectories(self, idColName, timeColName, timeFormat):
        raise NotImplementedError()