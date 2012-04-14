from newobject import Ui_NewObject

'''
QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.create_object)
'''


class Ui_MainNewObject(Ui_NewObject):
    
    def __init__(self, controller):
        
        self.controller = controller

    def create_object(self):
        name = self.lineEdit.text()
        mass = self.lineEdit_2.text()
        print "3: " + self.lineEdit_3.text()
        print "4: " + self.lineEdit_4.text()
        print "5: " + self.lineEdit_5.text()
        print "6: " + self.lineEdit_6.text()
        print "7: " + self.lineEdit_7.text()
        
        if name != "" and mass != "":
            self.controller.create_object(name, mass)
        else:
            print 'No object created'
        
        
        
