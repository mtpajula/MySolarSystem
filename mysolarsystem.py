from PySide import QtCore, QtGui
from gui.mainwindow import Ui_MainWindow
from controller import controller

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    controller = controller()
    
    ui = Ui_MainWindow(controller)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
