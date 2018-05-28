import sys
from PyQt5 import QtCore, QtWidgets, uic

qtCreatorFile = "ks.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        ID = 0
    questionlist =0
    ID = self.readID()




    def readID(self):
        ID = self.ID.value()
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
