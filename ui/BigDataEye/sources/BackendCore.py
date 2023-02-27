from PySide6 import QtCore

class BackendCore(QtCore.QObject):
    sendLog = QtCore.Signal(str, str, str)
    sendDataHead = QtCore.Signal(str)

    def __init__(self, viewModel):
        QtCore.QObject.__init__(self)
        self.viewModel = viewModel

    @QtCore.Slot()
    def run(self):
        self.sendLog.emit(str(self.viewModel), "appCore", "info")
        self.viewModel.preprocessing()

    @QtCore.Slot()
    def getDataHead(self):
        self.sendDataHead.emit(str(self.viewModel.getDataSetHead()))

