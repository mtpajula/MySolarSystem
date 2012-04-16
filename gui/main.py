from PySide import QtCore, QtGui
from mainwindow import Ui_MainWindow
from main_objectmanager import Ui_MainObjectManager
from main_preferences import Ui_MainPreferences
from main_force import Ui_MainForce
from about import Ui_About
import time
from random import randint
from controller import controller



from threading import Thread, Condition
from running_animation import RunningAnimation
'''
        QtCore.QObject.connect(self.actionNew_Object, QtCore.SIGNAL("activated()"), self.new_object)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.play)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.stop)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL("activated()"), self.openFile)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL("activated()"), self.saveFile)
        QtCore.QObject.connect(self.actionNew_Simulation, QtCore.SIGNAL("activated()"), self.newSimulation)
        QtCore.QObject.connect(self.actionPrefenrences, QtCore.SIGNAL("activated()"), self.preferences)
        QtCore.QObject.connect(self.actionAbout_MySolarSystem, QtCore.SIGNAL("activated()"), self.about)
'''

class Ui_Main(Ui_MainWindow):
    
    def __init__(self, controller):
        super(Ui_Main, self).__init__()
        
        self.controller = controller
        self.controller.file_name = "default.xml"
        self.controller.load()
        
        self.edit_uni_object = None
        self.edit_force = None
        
        self.run = True
        
    def startMain(self, MainWindow):
        
        self.setupUi(MainWindow)
        
        self.graphicscene = QtGui.QGraphicsScene()
        self.graphicsView.setScene(self.graphicscene)
        self.work_thread  = RunningAnimation(self.graphicscene)
        self.start()
        
        QtCore.QObject.connect(self.actionNew_Object, QtCore.SIGNAL("activated()"), self.new_object)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.work_thread.request_start)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), self.do_set_startpoint)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.do_reverse)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.work_thread.request_stop)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL("activated()"), self.openFile)
        QtCore.QObject.connect(self.actionNew_Force_Vector, QtCore.SIGNAL("activated()"), self.new_force)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL("activated()"), self.saveFile)
        QtCore.QObject.connect(self.actionNew_Simulation, QtCore.SIGNAL("activated()"), self.newSimulation)
        QtCore.QObject.connect(self.actionPrefenrences, QtCore.SIGNAL("activated()"), self.preferences)
        QtCore.QObject.connect(self.actionAbout_MySolarSystem, QtCore.SIGNAL("activated()"), self.about)
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
        new_object = QtGui.QDialog()
        
        if self.edit_uni_object is not None:
            new_object.uinh = Ui_MainForce(self.controller, self.edit_uni_object, None)
        else:
            new_object.uinh = Ui_MainForce(self.controller, None, None)
            
        new_object.uinh.startMain(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()
        self.refresh_tree()
    
    def do_set_startpoint(self):
        
        (result, message) = self.controller.set_startpoint()
        self.refresh_tree()
        self.statusbar.showMessage(message)
        
    def do_reverse(self):
        
        (result, message) = self.controller.reverse_startpoint()
        self.refresh_tree()
        self.statusbar.showMessage(message)
        
    
    def init_tree(self):
        
        self.edit_uni_object = None
        self.edit_force = None
        
        self.statusbar.showMessage('')
        
        for uni_object in self.controller.universe.object_list:
            
            root = QtGui.QTreeWidgetItem(self.treeWidget)
            root.setText(0, uni_object.name)
            
            rootItem = QtGui.QTreeWidgetItem(root)
            rootItem.setText(0, 'Mass')
            rootItem.setText(1, str(uni_object.mass))
            
            rootItem = QtGui.QTreeWidgetItem(root)
            rootItem.setText(0, 'Radius')
            rootItem.setText(1, str(uni_object.radius))
            
            locationRoot = QtGui.QTreeWidgetItem(root)
            locationRoot.setText(0, 'Location')
            
            locationItem = QtGui.QTreeWidgetItem(locationRoot)
            locationItem.setText(0, 'x')
            locationItem.setText(1, str(uni_object.x))
            
            locationItem = QtGui.QTreeWidgetItem(locationRoot)
            locationItem.setText(0, 'y')
            locationItem.setText(1, str(uni_object.y))
            
            locationItem = QtGui.QTreeWidgetItem(locationRoot)
            locationItem.setText(0, 'z')
            locationItem.setText(1, str(uni_object.z))
            
            speedRoot = QtGui.QTreeWidgetItem(root)
            speedRoot.setText(0, 'Speed')
            
            ( speed, angle2d, angle3d ) = self.controller.get_object_angle_speed(uni_object)
            
            speedItem = QtGui.QTreeWidgetItem(speedRoot)
            speedItem.setText(0, 'speed')
            speedItem.setText(1, str(speed))
            
            speedItem = QtGui.QTreeWidgetItem(speedRoot)
            speedItem.setText(0, 'angle2d')
            speedItem.setText(1, str(angle2d))
            
            speedItem = QtGui.QTreeWidgetItem(speedRoot)
            speedItem.setText(0, 'angle3d')
            speedItem.setText(1, str(angle3d))
            
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
                forceItem.setText(1, str(force.start))
                
                forceItem = QtGui.QTreeWidgetItem(forceRoot)
                forceItem.setText(0, 'stop')
                forceItem.setText(1, str(force.stop))
                
                forceItem = QtGui.QTreeWidgetItem(forceRoot)
                forceItem.setText(0, 'x')
                forceItem.setText(1, str(force.x))
                
                forceItem = QtGui.QTreeWidgetItem(forceRoot)
                forceItem.setText(0, 'y')
                forceItem.setText(1, str(force.y))
                
                forceItem = QtGui.QTreeWidgetItem(forceRoot)
                forceItem.setText(0, 'z')
                forceItem.setText(1, str(force.z))
            
    def refresh_tree(self):
        
        self.treeWidget.clear()
        self.init_tree()
        
    def treeMenu(self):
        
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
        
        print "location"
        print location
        
        if len(location) > 0:
            self.edit_uni_object = self.controller.universe.object_list[location[-1]]
            
            if len(location) > 2 and location[-2] == 5:
                print 'force on'
                
                self.edit_force = self.edit_uni_object.force_vector_list[location[-3]]
            else:
                self.edit_force = None
            
        else:
            self.edit_uni_object = None
            self.edit_force = None
        
        self.treeMenu.exec_(QtGui.QCursor.pos())
    
    def new_object(self):
        new_object = QtGui.QDialog()
        new_object.uinh = Ui_MainObjectManager(self.controller)
        new_object.uinh.startMain(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()
        
        self.refresh_tree()
    
    
    def delete(self):
        
        if self.edit_uni_object is not None:
            
            if self.edit_force is not None:
                self.do_delete_force()
            else:
                self.do_delete_object()
            
        else:
            self.statusbar.showMessage('No object selected to delete')
    
    def do_delete_force(self):
        
        (result, message) = self.controller.delete_force(self.edit_uni_object, self.edit_force)
        self.refresh_tree()
        self.statusbar.showMessage(message)
    
    def do_delete_object(self):

        (result, message) = self.controller.delete_object(self.edit_uni_object)
        self.refresh_tree()
        self.statusbar.showMessage(message)

    
    def edit(self):
        pass
        
        if self.edit_uni_object is not None:
            
            if self.edit_force is not None:
                self.do_edit_force()
            else:
                self.do_edit_object()
                
            self.refresh_tree()
            
        else:
            self.statusbar.showMessage('No object selected to edit')
            
    def do_edit_force(self):
        new_object = QtGui.QDialog()
        new_object.uinh = Ui_MainForce(self.controller, self.edit_uni_object, self.edit_force)
        new_object.uinh.startMain(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()
    
    def do_edit_object(self):

        new_object = QtGui.QDialog()
        new_object.uinh = Ui_MainObjectManager(self.controller, self.edit_uni_object)
        new_object.uinh.startMain(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()

        
    def preferences(self):
        new_object = QtGui.QDialog()
        new_object.uinh = Ui_MainPreferences(self.controller)
        new_object.uinh.startMain(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()
        
    def about(self):
        new_object = QtGui.QDialog()
        new_object.uinh = Ui_About()
        new_object.uinh.setupUi(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()
    
    def newSimulation(self):
        
        self.controller = controller()
        
        self.refresh_tree()
    
    def openFile(self):
        
        fileName = QtGui.QFileDialog.getOpenFileName(self.centralwidget,"Open universe","files/","*.xml")[0]
        
        self.controller.set_filePath(fileName)
        
        (result, message) = self.controller.load()
        self.refresh_tree()
        self.statusbar.showMessage(message+' file: '+self.controller.filePath)
        
        print self.controller.filePath
        
    def saveFile(self):
        
        fileName = QtGui.QFileDialog.getSaveFileName(self.centralwidget,"Save universe","files/","*.xml")[0]
        print fileName
        
        self.controller.set_filePath(fileName)
        
        (result, message) = self.controller.save()
        self.refresh_tree()
        self.statusbar.showMessage(message+' file: '+self.controller.filePath)
    
    def stop(self):
        
        print 'stop TODO'
        
        self.run = False
    
    def start(self):
        
        
        self.work_thread.start()
    
    def closeEvent(self, event):    
        self.work_thread.request_end()
        
        '''
        self.controller.animate()

        bru = QtGui.QBrush()
        bru.setColor(QtGui.QColor(255,255,000))
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor(255,000,255))
        pen.setWidth(5)
        self.graphicscene.addRect(50,100,50,100,pen,bru)
        self.graphicscene.addText("test")
        
        '''

        
        '''
        self.item = QtGui.QGraphicsEllipseItem(0, 0, 40, 20)
        self.graphicscene.addItem(self.item)

        # Remember to hold the references to QTimeLine and QGraphicsItemAnimation instances.
        # They are not kept anywhere, even if you invoke QTimeLine.start().
        self.tl = QtCore.QTimeLine(10000)
        self.tl.setFrameRange(0, 1000)
        self.a = QtGui.QGraphicsItemAnimation()
        self.a.setItem(self.item)
        self.a.setTimeLine(self.tl)
        self.tl.setDuration(10000)

        # Each method determining an animation state (e.g. setPosAt, setRotationAt etc.)
        # takes as a first argument a step which is a value between 0 (the beginning of the
        # animation) and 1 (the end of the animation)
        self.a.setPosAt(0, QtCore.QPointF(0, -10))

        self.a.setRotationAt(1, 360)

        self.tl.start()
        '''
