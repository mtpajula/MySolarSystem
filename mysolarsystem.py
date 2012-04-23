import sys
from controller import controller
import math

#sys.path.append("/home/leevi/projektit/MySolarSystem") 

def main_gui(controller):
    '''
    Function executes Qt GUI
    '''
    
    from PySide import QtCore, QtGui
    from gui.main import Ui_Main
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()

    ui = Ui_Main(controller)
    ui.startMain(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    
def main_cli(controller):
    '''
    Executes CLI
    '''
    from cli.cli import Cli_Main
    
    ui = Cli_Main(controller)
    
    ui.menu()
    

if __name__ == "__main__":
    '''
    Starts application.
    If no ui type is given as argv, then starts GUI
    '''
    controller = controller()

    if len(sys.argv) > 1:
        ui_type = sys.argv[1]
        
        # testdata here
        
        if ui_type == "cli":
            main_cli(controller)
        elif ui_type == "gui":
            main_gui(controller)
        else:
            print "unknown ui type: " + ui_type
            
    else:
        main_gui(controller)
        
    
        
