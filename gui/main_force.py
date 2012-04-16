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
        
        if self.uni_object is not None:
            
            self.label_9 = QtGui.QLabel(Dialog)
            self.label_9.setObjectName("label_9")
            self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1)
            self.label_9.setText(self.uni_object.name)
            
            if self.force_vector is not None:
                
                self.label.setText("Edit Force Vector")
                
                self.lineEdit.setText(str(self.force_vector.start))
                self.lineEdit_2.setText(str(self.force_vector.stop))
                
                ( r, angle2d, angle3d ) = self.controller.get_force_angle(self.force_vector)
                
                self.lineEdit_3.setText(str(r))
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
        else:
            start = None
            
        if stop != "":
            stop = self.controller.validate_input('float',stop)
        else:
            stop = None
        
        force = self.controller.validate_input('float',self.lineEdit_3.text(),True)
        angle2d = self.controller.validate_input('float',self.lineEdit_4.text())
        angle3d = self.controller.validate_input('float',self.lineEdit_5.text())
        
        print 'FORCE:'
        print start
        print stop
        print force
        print angle2d
        print angle3d
        
        
        if self.force_vector is not None:
            self.controller.set_force_angle(self.force_vector, force, angle2d, angle3d)
        else:
            if self.uni_object is None:
                self.uni_object = self.controller.universe.object_list[self.comboBox.currentIndex()]
                
            self.force_vector = self.controller.create_angle_force(self.uni_object, force, angle2d, angle3d)
        
        self.force_vector.set_start_stop(start,stop)
        
        
