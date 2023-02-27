# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine
from mainWindow import MainWindow

from sources.BaseApp import BaseAppParams


if __name__ == "__main__":
    sys_argv = sys.argv
    sys.argv += ['--style', 'Material']
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Get Context
    main = MainWindow()
    baseApp = BaseAppParams()

    engine.rootContext().setContextProperty("backend", main)
    engine.rootContext().setContextProperty("baseApp", baseApp)

    # Set App Extra Info
    app.setOrganizationName("Dehghanzadeh Mohsen")
    app.setOrganizationDomain("N/A")

    # Set Icon
    app.setWindowIcon(QIcon("app.ico"))


    # Load Initial Window
    engine.load(os.path.join(os.path.dirname(__file__), "ui/splashScreen.qml"))


    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
