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
                kuu = controller.create_object("kuu","0","1737000.0")
                satellite = controller.create_object("satellite","0","1737000.0")
                
                kerroin = 10**21
                #kerroin = 1
                
                aurinko.mass = 1989100000.0 * kerroin
                merkurius.mass = 330.2 * kerroin
                venus.mass = 4868.5 * kerroin
                maa.mass = 5973.6 * kerroin
                kuu.mass = 73.5 * kerroin
                satellite.mass = 5000
                
                merkurius.set_location(-10000000000.0,0,0) #-58000000000.0
                venus.set_location(0,108000000000.0,0)
                maa.set_location(149600000000.0,0,0)
                kuu.set_location(149200000000.0,0,0)
                satellite.set_location(149500000000.0,0,0)

                
                aurinko.set_object_type(6)
                merkurius.set_object_type(3)
                venus.set_object_type(3)
                maa.set_object_type(3)
                kuu.set_object_type(1)
                satellite.set_object_type(1)
                
                controller.set_object_angle_speed(merkurius, 147870.0,-90,0) #47870.0
                controller.set_object_angle_speed(venus, 35020.0,180,0)
                controller.set_object_angle_speed(maa, 29780.0,90,0)
                controller.set_object_angle_speed(kuu, 28780.0,90,0)
                controller.set_object_angle_speed(satellite, 29850.0,100,0)
                
                aurinko.color = (255,255,0)
                merkurius.color = (105,105,105)
                venus.color = (218,165,32)
                maa.color = (32,178,170)
                kuu.color = (190,190,190)
                satellite.color = (65,105,225)

                
            if action == "testdata2":
                aurinko = controller.create_object("aurinko","1","696000000.0")
                merkurius = controller.create_object("merkurius","1","2440000.0")
                venus = controller.create_object("venus","1","6052000.0")
                maa = controller.create_object("maa","1","6371000.0")
                kuu = controller.create_object("kuu","1","1737000.0")
                satellite = controller.create_object("kuu","1","1737000.0")
                
                kerroin = 10**21
                #kerroin = 1
                
                aurinko.mass = 1989100000.0 * kerroin
                merkurius.mass = 330.2 * kerroin
                venus.mass = 4868.5 * kerroin
                maa.mass = 5973.6 * kerroin
                kuu.mass = 73.5 * kerroin
                satellite.mass = 5000
                
                merkurius.set_location(-58000000000.0,0,0)
                venus.set_location(0,108000000000.0,0)
                maa.set_location(149600000000.0,0,0)
                kuu.set_location(149300000000.0,0,0)
                satellite.set_location(149500000000.0,0,0)

                
                aurinko.set_object_type(1)
                merkurius.set_object_type(3)
                venus.set_object_type(3)
                maa.set_object_type(3)
                kuu.set_object_type(1)
                satellite.set_object_type(1)
                
                controller.set_object_angle_speed(merkurius, 47870.0,-90,0)
                controller.set_object_angle_speed(venus, 35020.0,180,0)
                controller.set_object_angle_speed(maa, 29780.0,90,0)
                controller.set_object_angle_speed(kuu, 28780.0,90,0)
                controller.set_object_angle_speed(satellite, 29850.0,100,0)
                
                aurinko.color = (255,255,0)
                merkurius.color = (105,105,105)
                venus.color = (218,165,32)
                maa.color = (32,178,170)
                kuu.color = (190,190,190)
                satellite.color = (65,105,225)
                
            if action == "testdata3":
                
                controller.universe.maths.time = 10
                
                aurinko = controller.create_object("aurinko","20000000000","5")
                kuu = controller.create_object("kuu","100000","5")

                aurinko.set_location(0,0,0)
                kuu.set_location(200,200,0)
                
                #controller.set_object_angle_speed(aurinko, 0.3,-90,0)
                #controller.set_object_angle_speed(kuu, 1.0,-135,0)
                
                f1 = controller.create_angle_force(kuu, 50.0,180,0)
                f1.set_start_stop(50,100)
                f2 = controller.create_angle_force(kuu, 50.0,0,0)
                f2.set_start_stop(200,250)
                f3 = controller.create_angle_force(kuu, 20.0,45,0)
                f3.set_start_stop(300,350)
                f4 = controller.create_angle_force(kuu, 50.0,20,0)
                f4.set_start_stop(577,600)
                
                f5 = controller.create_angle_force(kuu, 50.0,20,0)
                
                
                
            if action == "testdata4":
                aurinko = controller.create_object("aurinko","0","696000000.0")
                maa = controller.create_object("maa","0","6371000.0")
                
                kerroin = 10**21
                
                aurinko.mass = 1989100000.0 * kerroin
                maa.mass = 5973.6 * kerroin
                
                distange = 149600000000.0
                
                maa.set_location(distange,0,0)
                
                controller.set_object_angle_speed(maa, 29780.0,90,0)
                
            
        if ui_type == "cli":
            main_cli(controller)
        elif ui_type == "gui":
            main_gui(controller)
        else:
            print "unknown ui type: " + ui_type
            
    else:
        main_gui(controller)
        
    
        
