import sys
from PyQt5 import QtCore, QtWidgets, uic
import csv
import numpy as np

qtCreatorFile = "ks.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.ID=0
        csv_reader = csv.reader(open('question.csv'),encoding='utf-8')
        



    def randomfivequestion(self.csv_reader):
        return questionlist

    def doonequestion(self):
        return onequestionrecorde

    def readID(self):
        return ID

    def writeintoanswercsv(onequestionrecorde):
        
    def setonequestionrecorde(input)
        self.onequestionrecorde = input
    def getonequestionrecorde(self)
        return self.onequestionrecorde
    
    def readID(self):
        ID = self.ID.value()
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
