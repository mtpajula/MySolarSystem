# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Apr 18 17:54:36 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuAbout_MySolarSystem = QtGui.QMenu(self.menubar)
        self.menuAbout_MySolarSystem.setObjectName("menuAbout_MySolarSystem")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuShow = QtGui.QMenu(self.menuView)
        self.menuShow.setObjectName("menuShow")
        MainWindow.setMenuBar(self.menubar)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeWidget = QtGui.QTreeWidget(self.dockWidgetContents_2)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setAllColumnsShowFocus(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(140)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.dockWidgetContents_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.dockWidgetContents_5)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents_5)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_4 = QtGui.QPushButton(self.dockWidgetContents_5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.dockWidgetContents_5)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents_5)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.dockWidget_3.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_3)
        self.actionNew_Simulation = QtGui.QAction(MainWindow)
        self.actionNew_Simulation.setObjectName("actionNew_Simulation")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPrefenrences = QtGui.QAction(MainWindow)
        self.actionPrefenrences.setObjectName("actionPrefenrences")
        self.actionAbout_MySolarSystem = QtGui.QAction(MainWindow)
        self.actionAbout_MySolarSystem.setObjectName("actionAbout_MySolarSystem")
        self.actionNew_Object = QtGui.QAction(MainWindow)
        self.actionNew_Object.setObjectName("actionNew_Object")
        self.actionFull_screen = QtGui.QAction(MainWindow)
        self.actionFull_screen.setObjectName("actionFull_screen")
        self.actionLeave_Full_Screen = QtGui.QAction(MainWindow)
        self.actionLeave_Full_Screen.setObjectName("actionLeave_Full_Screen")
        self.actionObject_tree = QtGui.QAction(MainWindow)
        self.actionObject_tree.setCheckable(True)
        self.actionObject_tree.setChecked(True)
        self.actionObject_tree.setObjectName("actionObject_tree")
        self.actionNew_Force_Vector = QtGui.QAction(MainWindow)
        self.actionNew_Force_Vector.setObjectName("actionNew_Force_Vector")
        self.actionPlayer = QtGui.QAction(MainWindow)
        self.actionPlayer.setCheckable(True)
        self.actionPlayer.setChecked(True)
        self.actionPlayer.setObjectName("actionPlayer")
        self.menuFile.addAction(self.actionNew_Simulation)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionNew_Object)
        self.menuEdit.addAction(self.actionNew_Force_Vector)
        self.menuSettings.addAction(self.actionPrefenrences)
        self.menuAbout_MySolarSystem.addAction(self.actionAbout_MySolarSystem)
        self.menuShow.addAction(self.actionObject_tree)
        self.menuShow.addAction(self.actionPlayer)
        self.menuView.addAction(self.actionFull_screen)
        self.menuView.addAction(self.actionLeave_Full_Screen)
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuShow.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout_MySolarSystem.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QObject.connect(self.actionFull_screen, QtCore.SIGNAL("activated()"), MainWindow.showFullScreen)
        QtCore.QObject.connect(self.actionLeave_Full_Screen, QtCore.SIGNAL("activated()"), MainWindow.showNormal)
        QtCore.QObject.connect(self.actionObject_tree, QtCore.SIGNAL("toggled(bool)"), self.dockWidget_2.setVisible)
        QtCore.QObject.connect(self.actionPlayer, QtCore.SIGNAL("toggled(bool)"), self.dockWidget_3.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "My Solar System", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout_MySolarSystem.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuShow.setTitle(QtGui.QApplication.translate("MainWindow", "Show", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Objects", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Values", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Startpoint:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Set Startpoint", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Reverse", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Simulation.setText(QtGui.QApplication.translate("MainWindow", "New...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrefenrences.setText(QtGui.QApplication.translate("MainWindow", "Prefenrences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_MySolarSystem.setText(QtGui.QApplication.translate("MainWindow", "About MySolarSystem", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Object.setText(QtGui.QApplication.translate("MainWindow", "New Object", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFull_screen.setText(QtGui.QApplication.translate("MainWindow", "Full Screen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLeave_Full_Screen.setText(QtGui.QApplication.translate("MainWindow", "Leave Full Screen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionObject_tree.setText(QtGui.QApplication.translate("MainWindow", "Object tree", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Force_Vector.setText(QtGui.QApplication.translate("MainWindow", "New Force Vector", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlayer.setText(QtGui.QApplication.translate("MainWindow", "Player", None, QtGui.QApplication.UnicodeUTF8))

