#!/usr/bin/env python
from PySide import QtCore, QtGui
from mainwindow import Ui_MainWindow
from main_objectmanager import Ui_MainObjectManager
from main_preferences import Ui_MainPreferences
from main_force import Ui_MainForce
from about import Ui_About
import sys, time
from random import randint
from controller import controller
from paint import Helper, Widget
from main_collision import Ui_MainCollision


class Ui_Main(Ui_MainWindow):
    
    def __init__(self, controller, parent = None):
        
        self.controller = controller
        
        self.edit_uni_object = None
        self.edit_force = None
        
    def startMain(self, MainWindow):
        '''
        Init mainwindow
        '''
        
        self.setupUi(MainWindow)
        
        self.default_background_color = QtGui.QColor(64, 32, 64)
        self.default_line_color = QtGui.QColor(111, 111, 111)
        self.helper = Helper(self.controller, self.default_background_color, self.default_line_color)
        self.line_lenght = 10
        self.draw_lines = True
        
        self.helper.line_lenght = self.line_lenght
        self.helper.draw_lines = self.draw_lines
        
        self.native = Widget(self.helper, self)
        
        self.horizontalLayout.addWidget(self.native)
        
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.native.animate)
        
        QtCore.QObject.connect(self.actionNew_Object, QtCore.SIGNAL("activated()"), self.new_object)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.start)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), self.do_set_startpoint)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.do_reverse)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.stop)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL("activated()"), self.openFile)
        QtCore.QObject.connect(self.actionNew_Force_Vector, QtCore.SIGNAL("activated()"), self.new_force)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL("activated()"), self.saveFile)
        QtCore.QObject.connect(self.actionNew_Simulation, QtCore.SIGNAL("activated()"), self.newSimulation)
        QtCore.QObject.connect(self.actionPrefenrences, QtCore.SIGNAL("activated()"), self.preferences)
        QtCore.QObject.connect(self.actionAbout_MySolarSystem, QtCore.SIGNAL("activated()"), self.about)
        QtCore.QObject.connect(self.actionCollision_list, QtCore.SIGNAL("activated()"), self.collision_list)
        self.treeWidget.customContextMenuRequested.connect(self.treeMenu)
        self.init_tree()
        
        self.toolbar = QtGui.QToolBar()
        self.actionEdit = self.toolbar.addAction("Edit", self.edit)
        self.actionNew = self.toolbar.addAction("New Object", self.new_object)
        self.actionNewForce = self.toolbar.addAction("New Force", self.new_force)
        self.actionDelete = self.toolbar.addAction("Delete", self.delete)
        
        self.treeMenu = QtGui.QMenu()
        self.treeMenu.addAction(self.actionEdit)
        self.treeMenu.addAction(self.actionNew)
        self.treeMenu.addAction(self.actionNewForce)
        self.treeMenu.addSeparator()
        self.treeMenu.addAction(self.actionDelete)
        
    
    def new_force(self):
        '''
        Open force manager dialog
        '''
        new_object = QtGui.QDialog()
        
        if self.edit_uni_object is not None:
            new_object.uinh = Ui_MainForce(self.controller, self.edit_uni_object, None)
        else:
            new_object.uinh = Ui_MainForce(self.controller, None, None)
            
        if self.controller.not_empty():
            new_object.uinh.startMain(new_object)
            new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            new_object.exec_()
            self.refresh_tree()
        else:
            self.statusbar.showMessage('No object where to insert force')
    
    def do_set_startpoint(self):
        '''
        Set startpoint
        '''
        
        (result, message) = self.controller.set_startpoint()
        self.refresh_tree()
        self.statusbar.showMessage(message)
        
    def do_reverse(self):
        '''
        Reverse to startpoint
        '''
        
        (result, message) = self.controller.reverse_startpoint()
        self.refresh_tree()
        self.statusbar.showMessage(message)
    
    def init_tree(self):
        '''
        Redraw treeview
        '''
        
        for uni_object in self.controller.universe.object_list:
            
            root = QtGui.QTreeWidgetItem(self.treeWidget)
            root.setText(0, uni_object.name)
            
            rootItem = QtGui.QTreeWidgetItem(root)
            rootItem.setText(0, 'Mass')
            rootItem.setText(1, self.controller.units.mass.str(uni_object.mass))
            
            rootItem = QtGui.QTreeWidgetItem(root)
            rootItem.setText(0, 'Radius')
            rootItem.setText(1, self.controller.units.dist.to_unit_str(uni_object.radius, 'km'))
            
            locationRoot = QtGui.QTreeWidgetItem(root)
            locationRoot.setText(0, 'Location')
            
            locationItem = QtGui.QTreeWidgetItem(locationRoot)
            locationItem.setText(0, 'x')
            locationItem.setText(1, self.controller.units.dist.str(uni_object.x))
            
            locationItem = QtGui.QTreeWidgetItem(locationRoot)
            locationItem.setText(0, 'y')
            locationItem.setText(1, self.controller.units.dist.str(uni_object.y))
            
            locationItem = QtGui.QTreeWidgetItem(locationRoot)
            locationItem.setText(0, 'z')
            locationItem.setText(1, self.controller.units.dist.str(uni_object.z))
            
            speedRoot = QtGui.QTreeWidgetItem(root)
            speedRoot.setText(0, 'Speed')
            
            ( speed, angle2d, angle3d ) = self.controller.get_object_angle_speed(uni_object)
            
            speedItem = QtGui.QTreeWidgetItem(speedRoot)
            speedItem.setText(0, 'speed')
            speedItem.setText(1, self.controller.units.speed.str(speed))
            
            speedItem = QtGui.QTreeWidgetItem(speedRoot)
            speedItem.setText(0, 'angle2d')
            speedItem.setText(1, str(angle2d))
            
            speedItem = QtGui.QTreeWidgetItem(speedRoot)
            speedItem.setText(0, 'angle3d')
            speedItem.setText(1, str(angle3d))
            
            forceRoot = QtGui.QTreeWidgetItem(root)
            forceRoot.setText(0, 'Force')
            
            ( force, angle2d, angle3d ) = self.controller.get_object_force_speed(uni_object)
            
            forceItem = QtGui.QTreeWidgetItem(forceRoot)
            forceItem.setText(0, 'force')
            forceItem.setText(1, self.controller.units.force.str(force))
            
            forceItem = QtGui.QTreeWidgetItem(forceRoot)
            forceItem.setText(0, 'angle2d')
            forceItem.setText(1, str(angle2d))
            
            forceItem = QtGui.QTreeWidgetItem(forceRoot)
            forceItem.setText(0, 'angle3d')
            forceItem.setText(1, str(angle3d))
            
            styleRoot = QtGui.QTreeWidgetItem(root)
            styleRoot.setText(0, 'Style')
            
            styleItem = QtGui.QTreeWidgetItem(styleRoot)
            styleItem.setText(0, 'Size')
            styleItem.setText(1, str(uni_object.object_type))
            
            (r,g,b) = uni_object.color
            
            styleItem = QtGui.QTreeWidgetItem(styleRoot)
            styleItem.setText(0, 'RGB')
            styleItem.setText(1, str(r)+','+str(g)+','+str(b))
            
            forcesRoot = QtGui.QTreeWidgetItem(root)
            forcesRoot.setText(0, 'Force vectors')
            
            for i, force in enumerate(uni_object.force_vector_list):
                
                forceRoot = QtGui.QTreeWidgetItem(forcesRoot)
                forceRoot.setText(0, 'Force '+str(i))
                
                forceItem = QtGui.QTreeWidgetItem(forceRoot)
                forceItem.setText(0, 'start')
                forceItem.setText(1, self.controller.units.time.str(force.start))
                
                forceItem = QtGui.QTreeWidgetItem(forceRoot)
                forceItem.setText(0, 'stop')
                forceItem.setText(1, self.controller.units.time.str(force.stop))
                
                ( force, angle2d, angle3d ) = self.controller.get_force_angle(force)
                
                forceItem = QtGui.QTreeWidgetItem(forceRoot)
                forceItem.setText(0, 'force')
                forceItem.setText(1, self.controller.units.force.str(force))
                
                forceItem = QtGui.QTreeWidgetItem(forceRoot)
                forceItem.setText(0, 'angle2d')
                forceItem.setText(1, str(angle2d))
                
                forceItem = QtGui.QTreeWidgetItem(forceRoot)
                forceItem.setText(0, 'angle3d')
                forceItem.setText(1, str(angle3d))
            
    def refresh_tree(self):
        '''
        redraw treeview
        remove edit objects
        clear statusbar
        Set startpoint status label text
        repaint universe map
        '''
        
        self.treeWidget.clear()
        self.init_tree()
        
        self.edit_uni_object = None
        self.edit_force = None
        
        self.statusbar.showMessage('')
        
        if self.controller.copy_universe is None:
            self.label_2.setText('Not set')
        else:
            self.label_2.setText('Is set')
            
        self.native.repaint()
        
    def treeMenu(self):
        '''
        Start treeview context menu
        '''
        
        indexes = self.treeWidget.selectedIndexes()
        
        level = 0
        
        location = []
        
        if len(indexes) > 0:
            
            index = indexes[0]
            
            location.append(index.row())
            
            while index.parent().isValid():
                index = index.parent()
                level += 1
                location.append(index.row())
        
        if len(location) > 0:
            self.edit_uni_object = self.controller.universe.object_list[location[-1]]
            
            if len(location) > 2 and location[-2] == 6:
                print 'force on'
                
                self.edit_force = self.edit_uni_object.force_vector_list[location[-3]]
            else:
                self.edit_force = None
            
        else:
            self.edit_uni_object = None
            self.edit_force = None
        
        self.treeMenu.exec_(QtGui.QCursor.pos())
    
    def new_object(self):
        '''
        Open object manager dialog
        '''
        new_object = QtGui.QDialog()
        new_object.uinh = Ui_MainObjectManager(self.controller)
        new_object.uinh.startMain(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()
        
        self.refresh_tree()
    


    def delete(self):
        '''
        Delete selected edit object or it's force
        '''
        
        if self.edit_uni_object is not None:
            
            if self.edit_force is not None:
                self.do_delete_force()
            else:
                self.do_delete_object()
            
        else:
            self.statusbar.showMessage('No object selected to delete')
    
    def do_delete_force(self):
        '''
        Delete force -action
        '''
        
        (result, message) = self.controller.delete_force(self.edit_uni_object, self.edit_force)
        self.refresh_tree()
        self.statusbar.showMessage(message)
    
    def do_delete_object(self):
        '''
        Delete object -action
        '''
        
        (result, message) = self.controller.delete_object(self.edit_uni_object)
        self.refresh_tree()
        self.statusbar.showMessage(message)

    
    def edit(self):
        '''
        start edit object or force
        '''
        
        if self.edit_uni_object is not None:
            
            if self.edit_force is not None:
                self.do_edit_force()
            else:
                self.do_edit_object()
                
            self.refresh_tree()
            
        else:
            self.statusbar.showMessage('No object selected to edit')
    
    def do_edit_force(self):
        '''
        open force manager dialog in edit mode
        '''
        
        new_object = QtGui.QDialog()
        new_object.uinh = Ui_MainForce(self.controller, self.edit_uni_object, self.edit_force)
        new_object.uinh.startMain(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()
    
    def do_edit_object(self):
        '''
        open object manager dialog in edit mode
        '''
        new_object = QtGui.QDialog()
        new_object.uinh = Ui_MainObjectManager(self.controller, self.edit_uni_object)
        new_object.uinh.startMain(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()

        
    def preferences(self):
        '''
        open preferences dialog
        '''
        
        new_object = QtGui.QDialog()
        new_object.uinh = Ui_MainPreferences(self.helper)
        new_object.uinh.startMain(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()
        
        self.refresh_tree()
        
    def about(self):
        '''
        open about dialog
        '''
        
        new_object = QtGui.QDialog()
        new_object.uinh = Ui_About()
        new_object.uinh.setupUi(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()
        
    def collision_list(self):
        '''
        open collision list
        '''
        
        new_object = QtGui.QDialog()
        new_object.uinh = Ui_MainCollision(self.controller)
        new_object.uinh.startMain(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()
    
    def newSimulation(self):
        '''
        Clear controller-object 
        '''
        self.controller.new_controller()
        self.helper.set_background_color(self.default_background_color)
        self.helper.set_line_color(self.default_line_color)
        self.helper.line_lenght = self.line_lenght
        self.helper.draw_lines = self.draw_lines
        self.refresh_tree()
        
    def openFile(self):
        '''
        Open file-open dialog and load simulation from file
        '''
        
        fileName = QtGui.QFileDialog.getOpenFileName(self.centralwidget,"Open universe",
                                                    self.controller.folder,"*.xml")[0]
        
        if fileName:
            self.controller.set_filePath(fileName)
            
            (result, message) = self.controller.load()
            
            self.helper.load()
            
            self.refresh_tree()
            self.statusbar.showMessage(message+' file: '+self.controller.filePath)
        
    def saveFile(self):
        '''
        Open file-save dialog and save current simulation in file
        '''
        
        fileName = QtGui.QFileDialog.getSaveFileName(self.centralwidget,"Save universe",
                                                    self.controller.folder,"*.xml")[0]
        
        if fileName:
            self.controller.set_filePath(fileName)
            
            self.helper.save()
            
            (result, message) = self.controller.save()
            self.refresh_tree()
            self.statusbar.showMessage(message+' file: '+self.controller.filePath)
    
    def stop(self):
        '''
        Stop simulation
        '''
        
        self.timer.stop()
        self.refresh_tree()
        self.statusbar.showMessage('Simulation stopped')
    
    def start(self):
        '''
        Start simulation
        '''
        
        self.timer.start(self.controller.timer_time)
        self.statusbar.showMessage('Running simulation')





