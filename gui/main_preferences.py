from preferences import Ui_Preferences
from PySide import QtCore, QtGui


class Ui_MainPreferences(Ui_Preferences):
    
    def __init__(self, helper):
        
        self.controller = helper.controller
        self.helper = helper
        self.color = helper.background_color
        self.line_color = helper.line_color
    
    def startMain(self, Dialog):
        '''
        init preferences dialog with current preferences
        '''
        
        self.setupUi(Dialog)
        
        self.lineEdit.setText(str(self.controller.universe.maths.time))
        self.lineEdit_2.setText(str(self.controller.timer_time))
        self.lineEdit_3.setText(str(self.controller.steps_between_paint))
        self.lineEdit_4.setText(str(self.helper.line_lenght))
        
        for unit, divider in self.controller.units.time_units.items():
            self.comboBox.addItem(unit)
        
        for unit, divider in self.controller.units.dist_units.items():
            self.comboBox_2.addItem(unit)
        
        for unit, divider in self.controller.units.mass_units.items():
            self.comboBox_3.addItem(unit)
            
        for unit, divider in self.controller.units.speed_units.items():
            self.comboBox_4.addItem(unit)
            
        for unit, divider in self.controller.units.force_units.items():
            self.comboBox_5.addItem(unit)
            
        self.comboBox.setCurrentIndex(self.comboBox.findText(self.controller.units.time.unit))
        self.comboBox_2.setCurrentIndex(self.comboBox_2.findText(self.controller.units.dist.unit))
        self.comboBox_3.setCurrentIndex(self.comboBox_3.findText(self.controller.units.mass.unit))
        self.comboBox_4.setCurrentIndex(self.comboBox_4.findText(self.controller.units.speed.unit))
        self.comboBox_5.setCurrentIndex(self.comboBox_5.findText(self.controller.units.force.unit))
        
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.colorDialog)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.lineColorDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.set_preferences)
        self.frame.setStyleSheet("QWidget { background-color: %s }" 
            % self.color.name())
        self.frame_2.setStyleSheet("QWidget { background-color: %s }" 
            % self.line_color.name())
        
        self.checkBox.setChecked(self.helper.draw_lines)
        
        
    def set_preferences(self):
        '''
        set new preferences
        '''

        time = self.controller.validate_input('int',self.lineEdit.text(),True)
        timer_time = self.controller.validate_input('int',self.lineEdit_2.text(),True)
        steps_between_paint = self.controller.validate_input('int',self.lineEdit_3.text(),True)
        line_lenght = self.controller.validate_input('int',self.lineEdit_4.text(),True)
        
        self.controller.universe.maths.time = time
        self.controller.timer_time = timer_time
        self.controller.steps_between_paint = steps_between_paint
        self.helper.line_lenght = line_lenght
        
        self.controller.units.time.unit = self.comboBox.currentText()
        self.controller.units.dist.unit = self.comboBox_2.currentText()
        self.controller.units.mass.unit = self.comboBox_3.currentText()
        self.controller.units.speed.unit = self.comboBox_4.currentText()
        self.controller.units.force.unit = self.comboBox_5.currentText()
        
        self.helper.set_background_color(self.color)
        self.helper.set_line_color(self.line_color)
        
        self.helper.draw_lines = self.checkBox.isChecked()
        
    def colorDialog(self):
        '''
        open color dialog and set color
        '''
        
        col = QtGui.QColorDialog.getColor(self.color)
        
        if col.isValid():
            self.color = col
            self.frame.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
    
    def lineColorDialog(self):
        '''
        open color dialog and set color
        '''
        
        col = QtGui.QColorDialog.getColor(self.line_color)
        
        if col.isValid():
            self.line_color = col
            self.frame_2.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
