from PySide import QtCore, QtGui
from newobject import Ui_NewObject
import time
from random import randint
'''
from main import Ui_Main

class Ui_MainWindow(Ui_Main):

...

        QtCore.QObject.connect(self.actionNew_Object, QtCore.SIGNAL("activated()"), self.new_object)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.play)
'''

class Ui_Main(object):
    
    def __init__(self, controller):
        
        self.controller = controller
        
    
    def new_object(self):
		new_object = QtGui.QDialog()
		new_object.uinh = Ui_NewObject(self.controller)
		new_object.uinh.setupUi(new_object)
		new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		new_object.exec_()

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
