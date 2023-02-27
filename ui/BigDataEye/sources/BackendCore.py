from PySide6 import QtCore

class BackendCore(QtCore.QObject):
    sendLog = QtCore.Signal(str, str, str)

    def __init__(self, params):
        QtCore.QObject.__init__(self)
        self.params = params    

    @QtCore.Slot()
    def run(self):
        self.sendLog.emit(str(self.params), "appCore", "info")


    @QtCore.Slot()
    def getDataHead(self):
        print("getting data head!")

