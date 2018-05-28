import os
import platform
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import helpform
import newimagedlg
import qrc_resources
__version__ = "1.0.0"

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow)
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.mirroredvertically = False
        self.mirroredhorizontally = False

        self.imageLable = QLable()
        self.imageLable.setMinimumSize(200,200)
        self.imageLable.setAlignment(Qt.ALignCenter)
        self.imageLable.setContexMenuPolicy(Qt.ActionsContexMenu)
        self.setCentraWidget(self.imageLable)

        logDockWidget = QDockWidget("Log",self)
        logDockWidget.setObjectName("LogDockWidget")
        logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|
                                      Qt.RightDockWidgetArea)
        self.listWidget = QListWidget()
        logDockWidget.setWidget(self,listWidget)
        self.addDockWidget(Qt.RightDockWidgetArea,logDockWidget)
        self.printer = None


