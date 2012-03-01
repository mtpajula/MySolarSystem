import sys
from controller import controller
import math

def main_gui(controller):
    from PySide import QtCore, QtGui
    from gui.mainwindow import Ui_MainWindow
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()

    ui = Ui_MainWindow(controller)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
def main_cli(controller):
    from cli.cli import Cli_Main
    
    ui = Cli_Main(controller)
    
    ui.menu()
    

if __name__ == "__main__":
    
    controller = controller()

    if len(sys.argv) > 1:
        ui_type = sys.argv[1]
        
        if len(sys.argv) > 2:
            action = sys.argv[2]
            
            if action == "testdata1":
                aurinko = controller.create_object("aurinko","0","696000000.0")
                merkurius = controller.create_object("merkurius","0","2440000.0")
                venus = controller.create_object("venus","0","6052000.0")
                maa = controller.create_object("maa","0","6371000.0")
                #kuu = controller.create_object("kuu","0","1737000.0")
                satellite = controller.create_object("kuu","0","1737000.0")
                
                kerroin = 10**21
                #kerroin = 1
                
                aurinko.mass = 1989100000.0 * kerroin
                merkurius.mass = 330.2 * kerroin
                venus.mass = 4868.5 * kerroin
                maa.mass = 5973.6 * kerroin
                #kuu.mass = 73.5 * kerroin
                satellite.mass = 5000
                
                merkurius.set_location(-58000000000.0,0,0)
                venus.set_location(0,108000000000.0,0)
                maa.set_location(149600000000.0,0,0)
                #kuu.set_location(149000000000.0,0,0)
                satellite.set_location(149500000000.0,0,0)

                
                aurinko.set_object_type(5)
                merkurius.set_object_type(2)
                venus.set_object_type(2)
                maa.set_object_type(2)
                #kuu.set_object_type(1)
                satellite.set_object_type(1)
                
                merkurius.set_speed(47870.0,-90,0)
                venus.set_speed(35020.0,180,0)
                maa.set_speed(29780.0,90,0)
                #kuu.set_speed(30000.0,90,0)
                satellite.set_speed(29850.0,100,0)

                
            if action == "testdata2":
                aurinko = controller.create_object("aurinko","40","5")
                maa = controller.create_object("maa","10","5")
                kuu = controller.create_object("kuu","10","5")

                maa.set_location(400,200,0)
                kuu.set_location(200,-200,0)
                
                aurinko.set_speed(0.3,-90,0)
                kuu.set_speed(0.3,180,0)
                
            if action == "testdata3":
                aurinko = controller.create_object("aurinko","40","5")
                kuu = controller.create_object("kuu","10","5")

                aurinko.set_location(-400,200,0)
                kuu.set_location(1000,-200,0)
                
                aurinko.set_speed(0.3,-90,0)
                kuu.set_speed(0.3,180,0)
            
        if ui_type == "cli":
            main_cli(controller)
        elif ui_type == "gui":
            main_gui(controller)
        else:
            print "unknown ui type: " + ui_type
            
    else:
        main_gui(controller)        
        
