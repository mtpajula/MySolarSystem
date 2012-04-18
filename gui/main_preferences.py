from preferences import Ui_Preferences
from PySide import QtCore, QtGui


class Ui_MainPreferences(Ui_Preferences):
    
    def __init__(self, helper):
        
        self.controller = helper.controller
        self.helper = helper
        self.color = helper.background_color
    
    def startMain(self, Dialog):
        
        self.setupUi(Dialog)
        
        self.lineEdit.setText(str(self.controller.universe.maths.time))
        
        for unit, divider in self.controller.units.time_units.items():
            self.comboBox.addItem(unit)
        
        for unit, divider in self.controller.units.dist_units.items():
            self.comboBox_2.addItem(unit)
        
        for unit, divider in self.controller.units.mass_units.items():
            self.comboBox_3.addItem(unit)
            
        self.comboBox.setCurrentIndex(self.comboBox.findText(self.controller.units.time.unit))
        self.comboBox_2.setCurrentIndex(self.comboBox_2.findText(self.controller.units.dist.unit))
        self.comboBox_3.setCurrentIndex(self.comboBox_3.findText(self.controller.units.mass.unit))
        
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.colorDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.set_preferences)
        self.frame.setStyleSheet("QWidget { background-color: %s }" 
            % self.color.name())
    
    def set_preferences(self):

        time = self.controller.validate_input('int',self.lineEdit.text(),True)
        
        self.controller.universe.maths.time = time
        
        self.controller.units.time_unit = self.comboBox.currentText()
        self.controller.units.dist_unit = self.comboBox_2.currentText()
        self.controller.units.mass_unit = self.comboBox_3.currentText()
        
        self.helper.set_background_color(self.color)
        
    def colorDialog(self):
        
        col = QtGui.QColorDialog.getColor(self.color)
        
        if col.isValid():
            self.color = col
            self.frame.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
