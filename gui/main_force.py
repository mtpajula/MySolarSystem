from force import Ui_Force
from PySide import QtCore, QtGui

'''
QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.create_object)
'''


class Ui_MainForce(Ui_Force):
    
    
    def __init__(self, controller, uni_object, force_vector):
        
        self.controller = controller
        self.uni_object = uni_object
        self.force_vector = force_vector
    
    def startMain(self, Dialog):
        
        self.setupUi(Dialog)
        
        self.label_2.setText('Start ('+self.controller.units.time.unit+')')
        self.label_3.setText('Stop ('+self.controller.units.time.unit+')')
        self.label_5.setText('Force ('+self.controller.units.force.unit+')')
        
        if self.uni_object is not None:
            
            self.label_9 = QtGui.QLabel(Dialog)
            self.label_9.setObjectName("label_9")
            self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1)
            self.label_9.setText(self.uni_object.name)
            
            if self.force_vector is not None:
                
                self.label.setText("Edit Force Vector")
                
                if self.force_vector.start is not None:
                    self.lineEdit.setText(str(self.controller.units.time.num(self.force_vector.start)))
                if self.force_vector.stop is not None:
                    self.lineEdit_2.setText(str(self.controller.units.time.num(self.force_vector.stop)))
                
                ( r, angle2d, angle3d ) = self.controller.get_force_angle(self.force_vector)
                
                self.lineEdit_3.setText(str(self.controller.units.force.num(r)))
                self.lineEdit_4.setText(str(angle2d))
                self.lineEdit_5.setText(str(angle3d))
                
        else:
            self.comboBox = QtGui.QComboBox(Dialog)
            self.comboBox.setObjectName("comboBox")
            
            for uni_object in self.controller.universe.object_list:
                self.comboBox.addItem(uni_object.name)
            
            self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.create_force)
            
    def create_force(self):
        
        start = self.lineEdit.text()
        stop = self.lineEdit_2.text()
        
        if start != "":
            start = self.controller.validate_input('float',start)
            start = self.controller.units.time.si(start)
        else:
            start = None
            
        if stop != "":
            stop = self.controller.validate_input('float',stop)
            stop = self.controller.units.time.si(stop)
        else:
            stop = None
        
        force = self.controller.validate_input('float',self.lineEdit_3.text(),True)
        force = self.controller.units.force.si(force)
        angle2d = self.controller.validate_input('float',self.lineEdit_4.text())
        angle3d = self.controller.validate_input('float',self.lineEdit_5.text())
        
        if self.force_vector is not None:
            self.controller.set_force_angle(self.force_vector, force, angle2d, angle3d)
        else:
            if self.uni_object is None:
                self.uni_object = self.controller.universe.object_list[self.comboBox.currentIndex()]
                
            self.force_vector = self.controller.create_angle_force(self.uni_object, force, angle2d, angle3d)
        
        self.force_vector.set_start_stop(start,stop)
        
        
