from controller import controller

'''
from main_newobject import Ui_MainNewObject

class Ui_NewObject(Ui_MainNewObject):

    QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.create_object)
'''


class Ui_MainNewObject(object):
    
    def __init__(self, controller):
        
        self.uni = controller

    def create_object(self):
        name = self.lineEdit.text()
        mass = self.lineEdit_2.text()
        print "3: " + self.lineEdit_3.text()
        print "4: " + self.lineEdit_4.text()
        print "5: " + self.lineEdit_5.text()
        print "6: " + self.lineEdit_6.text()

        self.uni.print_info()
        
        if name != "" and mass != "":
            self.controller.create_object(name, mass)
        
        
