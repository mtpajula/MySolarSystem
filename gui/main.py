from PySide import QtCore, QtGui
from mainwindow import Ui_MainWindow
from main_objectmanager import Ui_MainObjectManager
from main_preferences import Ui_MainPreferences
from main_force import Ui_MainForce
from about import Ui_About
import sys, time
from random import randint
from controller import controller

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
    
    def __init__(self, controller, parent = None):
        
        self.controller = controller
        self.controller.file_name = "default.xml"
        self.controller.load()
        
        self.edit_uni_object = None
        self.edit_force = None
        
        self.run = True
        
        
    def startMain(self, MainWindow):
        
        self.setupUi(MainWindow)
        
        self.helper = Helper()
        self.native = Widget(self.helper, self)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.native.sizePolicy().hasHeightForWidth())
        
        self.native.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.native)
        
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.native.animate)
        
        QtCore.QObject.connect(self.actionNew_Object, QtCore.SIGNAL("activated()"), self.new_object)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.draw_qt)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), self.do_set_startpoint)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.do_reverse)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.stop_draw_qt)
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
        
        print 'stop'
        
        self.run = False
    
    def start(self):
        
        print 'start'
        #self.work_thread.start()
        
        
            
    def draw_qt(self):
        
        print 'timer start'
        
        self.helper
        
        self.timer.start(50)
        
    def stop_draw_qt(self):
        
        print 'timer stop'
        self.timer.stop()

        



class Helper:
    def __init__(self):
        gradient = QtGui.QLinearGradient(QtCore.QPointF(50, -20), QtCore.QPointF(80, 20))
        gradient.setColorAt(0.0, QtCore.Qt.white)
        gradient.setColorAt(1.0, QtGui.QColor(0xa6, 0xce, 0x39))

        self.background = QtGui.QBrush(QtGui.QColor(64, 32, 64))
        self.circleBrush = QtGui.QBrush(gradient)
        self.circlePen = QtGui.QPen(QtCore.Qt.black)
        self.circlePen.setWidth(1)
        self.textPen = QtGui.QPen(QtCore.Qt.white)
        self.textFont = QtGui.QFont()
        self.textFont.setPixelSize(20)
        
        self.width = 200
        self.height = 200

    def paint(self, painter, event, elapsed):
        painter.fillRect(event.rect(), self.background)
        
        painter.translate(painter.device().width()/2, painter.device().height()/2)

        painter.save()
        painter.setBrush(self.circleBrush)
        painter.setPen(self.circlePen)
        #painter.rotate(elapsed * 0.030)
        
        print elapsed
        
        r = elapsed/1000.0
        n = 30
        
        #print r
        
        
        for i in range(n):
            painter.rotate(30)
            radius = 0 + 120.0*((i+r)/n)
            circleRadius = 1 + ((i+r)/n)*20
            painter.drawEllipse(QtCore.QRectF(radius, -circleRadius,
                                       circleRadius*2, circleRadius*2))

        painter.restore()
        
        painter.setPen(QtGui.QColor(255, 0, 0))
        painter.drawEllipse(QtCore.QRectF(0, 0, 200, 200))
        painter.drawEllipse(-100, -100, 200, 200)
        
        
        painter.setPen(self.textPen)
        painter.setFont(self.textFont)
        painter.drawText(QtCore.QRect(-50, -50, 100, 100), QtCore.Qt.AlignCenter, "mikko")


class Widget(QtGui.QWidget):
    def __init__(self, helper, parent = None):
        QtGui.QWidget.__init__(self)
        
        self.helper = helper
        self.elapsed = 0
        #self.setFixedSize(200, 200)

    def animate(self):
        #print 'animate'
        self.elapsed = (self.elapsed + self.sender().interval()) % 1000
        self.repaint()

    def paintEvent(self, event):
        print 'paintevent'
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        self.helper.paint(painter, event, self.elapsed)
        painter.end()


