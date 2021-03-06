from objectmanager import Ui_ObjectManager
from PySide import QtCore, QtGui

'''
QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.create_object)
'''


class Ui_MainObjectManager(Ui_ObjectManager):
    
    def __init__(self, controller, uni_object = None):
        
        self.controller = controller
        self.uni_object = uni_object
        self.color = QtGui.QColor(255, 255, 255)
        #self.Dialog = None
        
    def startMain(self, Dialog):
        '''
        Init object manager -dialog with edit object or empty
        '''
        
        self.setupUi(Dialog)
        #self.Dialog = Dialog
        
        self.label.setText('Mass ('+self.controller.units.mass.unit+')')
        self.label_12.setText('Radius (km)')
        self.label_4.setText('x ('+self.controller.units.dist.unit+')')
        self.label_5.setText('y ('+self.controller.units.dist.unit+')')
        self.label_6.setText('z ('+self.controller.units.dist.unit+')')
        self.label_9.setText('Speed ('+self.controller.units.speed.unit+')')
        
        if self.uni_object is not None:
            self.label_3.setText(QtGui.QApplication.translate("Dialog", "Edit object", None, QtGui.QApplication.UnicodeUTF8))
            self.lineEdit.setText(self.uni_object.name)
            self.lineEdit_2.setText(str(self.controller.units.mass.num(self.uni_object.mass)))
            self.lineEdit_3.setText(str(self.controller.units.dist.to_unit(self.uni_object.radius, 'km')))
            
            self.lineEdit_4.setText(str(self.controller.units.dist.num(self.uni_object.x)))
            self.lineEdit_5.setText(str(self.controller.units.dist.num(self.uni_object.y)))
            self.lineEdit_6.setText(str(self.controller.units.dist.num(self.uni_object.z)))
            
            ( speed, angle2d, angle3d ) = self.controller.get_object_angle_speed(self.uni_object)
            
            self.lineEdit_7.setText(str(self.controller.units.speed.num(speed)))
            self.lineEdit_8.setText(str(angle2d))
            self.lineEdit_9.setText(str(angle3d))
            
            self.lineEdit_10.setText(str(self.uni_object.object_type))
            
            (r,g,b) = self.uni_object.color
            self.color = QtGui.QColor(r, g, b)
        
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.colorDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.create_object)
        self.frame.setStyleSheet("QWidget { background-color: %s }" 
            % self.color.name())

    def create_object(self):
        '''
        Save changes or create new based on gui values
        '''
        
        name = self.controller.validate_input('string',self.lineEdit.text())
        mass = self.controller.validate_input('float',self.lineEdit_2.text(),True)
        radius = self.controller.validate_input('float',self.lineEdit_3.text(),True)
        
        mass = self.controller.units.mass.si(mass)
        radius = self.controller.units.dist.to_si_from(radius, 'km')
        
        x = self.controller.validate_input('float',self.lineEdit_4.text())
        y = self.controller.validate_input('float',self.lineEdit_5.text())
        z = self.controller.validate_input('float',self.lineEdit_6.text())
        
        x = self.controller.units.dist.si(x)
        y = self.controller.units.dist.si(y)
        z = self.controller.units.dist.si(z)
        
        speed = self.controller.validate_input('float',self.lineEdit_7.text())
        
        speed = self.controller.units.speed.si(speed)
        
        angle2d = self.controller.validate_input('float',self.lineEdit_8.text())
        angle3d = self.controller.validate_input('float',self.lineEdit_9.text())
        
        obj_type = self.controller.validate_input('int',self.lineEdit_10.text(),True)
        
        if self.uni_object is not None:
            new_obj = self.uni_object
            
            new_obj.name = name
            new_obj.mass = mass
            new_obj.radius = radius
        else:
            new_obj = self.controller.create_object(name, mass, radius)
                
        new_obj.set_location(x,y,z)
        new_obj.set_object_type(obj_type)
        new_obj.color = (self.color.red(),self.color.green(),self.color.blue())

        self.controller.set_object_angle_speed(new_obj,speed,angle2d,angle3d)
            
    def colorDialog(self):
        '''
        open color dialog and set color
        '''
        
        col = QtGui.QColorDialog.getColor(self.color)
        
        if col.isValid():
            self.color = col
            self.frame.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
        
        
        
