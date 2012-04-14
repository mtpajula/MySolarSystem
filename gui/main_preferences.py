from preferences import Ui_Preferences

'''
QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.set_preferences)
'''


class Ui_MainPreferences(Ui_Preferences):
    
    def __init__(self, controller):
        
        self.controller = controller

    def set_preferences(self):
        
        print "time in step: " + self.lineEdit.text()
