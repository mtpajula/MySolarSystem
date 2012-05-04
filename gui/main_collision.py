from collision import Ui_Collision
from PySide import QtCore, QtGui

class Ui_MainCollision(Ui_Collision):
    
    def __init__(self, controller):
        
        self.controller = controller

    def startMain(self, Dialog):
        
        self.setupUi(Dialog)
        
        for collision in self.controller.universe.collision_manager.collision_list:
            
            root = QtGui.QTreeWidgetItem(self.treeWidget)
            root.setText(0, collision.alive.name)
            root.setText(1, collision.deleted.name)
            root.setText(2, self.controller.units.time.str(collision.time))
            
