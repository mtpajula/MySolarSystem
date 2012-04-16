from preferences import Ui_Preferences
from PySide import QtCore, QtGui

'''
QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.set_preferences)
'''


class Ui_MainPreferences(Ui_Preferences):
    
    def __init__(self, controller):
        
        self.controller = controller
    
    def startMain(self, Dialog):
        
        self.setupUi(Dialog)
        self.lineEdit.setText(str(self.controller.universe.maths.time))
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.set_preferences)
    
    def set_preferences(self):

        time = self.controller.validate_input('int',self.lineEdit.text(),True)
        
        self.controller.universe.maths.time = time
