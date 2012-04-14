from PySide import QtCore, QtGui
from mainwindow import Ui_MainWindow
from main_newobject import Ui_MainNewObject
from main_preferences import Ui_MainPreferences
from about import Ui_About
import time
from random import randint
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
        
        self.controller = controller
        self.controller.file_name = "default.xml"
        self.controller.load()
        
    def startMain(self, MainWindow):
        
        self.setupUi(MainWindow)
        self.treeWidget.customContextMenuRequested.connect(self.treeMenu)
        self.init_tree()
    
    def init_tree(self):
        
        for uni_object in self.controller.universe.object_list:
            
            root = QtGui.QTreeWidgetItem(self.treeWidget)
            root.setText(0, uni_object.name)
            
            
            rootItem = QtGui.QTreeWidgetItem(root)
            rootItem.setText(0, 'Mass: '+str(uni_object.mass))
            
            
            styleRoot = QtGui.QTreeWidgetItem(root)
            styleRoot.setText(0, 'Style')
            
            styleItem = QtGui.QTreeWidgetItem(styleRoot)
            styleItem.setText(0, 'Size: '+str(uni_object.object_type))
            
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
        
        
        print "Level:"
        print level
        
        menu = QtGui.QMenu()
        menu.addAction("Edit")
        
        #menu.exec_(self.treeWidget.viewport().mapToGlobal(QtGui.QCursor.pos()))
        
        #menu.popup(QtGui.QCursor.pos())
        
        menu.exec_(QtGui.QCursor.pos())
    
    def new_object(self):
		new_object = QtGui.QDialog()
		new_object.uinh = Ui_MainNewObject(self.controller)
		new_object.uinh.setupUi(new_object)
		new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		new_object.exec_()
        
    def preferences(self):
		new_object = QtGui.QDialog()
		new_object.uinh = Ui_MainPreferences(self.controller)
		new_object.uinh.setupUi(new_object)
		new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		new_object.exec_()
        
    def about(self):
		new_object = QtGui.QDialog()
		new_object.uinh = Ui_About()
		new_object.uinh.setupUi(new_object)
		new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		new_object.exec_()
    
    def newSimulation(self):
        
        # TODO
        print 'new simulation'
    
    def openFile(self):
        
        fileName = QtGui.QFileDialog.getOpenFileName(self.centralwidget,"Open file","*")[0]
        
        self.controller.set_filePath(fileName)
        
        self.controller.load()
        
        self.refresh_tree()
        
        print self.controller.filePath
        
    def saveFile(self):
        
        fileName = QtGui.QFileDialog.getSaveFileName(self.centralwidget,"Save file","*")[0]
        print fileName
    
    def stop(self):
        
        print 'stop TODO'
    
    def play(self):
        
        self.graphicscene = QtGui.QGraphicsScene()
        self.graphicsView.setScene(self.graphicscene)
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
