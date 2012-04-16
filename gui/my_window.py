# *.* coding: latin-1 *.*

'''
Tämä esimerkki esittelee säikeiden toimintaa yleisesti ja käyttöliittymässä
ESIMERKKI JOTA LUET ON ESIMERKKI OIKEASTA TOTEUTUKSESTA, luithan kaikki
väärät esimerkit jotka alustivat tätä esimerkkiä.

Muutokset edellisiin esimerkkeihin löytyvät
luokasta RunningAnimation, tutustu siihen.

Otto Seppälä 2003-2006, santtu
''' 
from PySide import QtGui
from PySide import QtCore

import sys

from threading import *

from running_animation import RunningAnimation

class MyWindow(QtGui.QWidget):


    def __init__(self):
        super(MyWindow, self).__init__()
        grid = QtGui.QGridLayout()

        font = QtGui.QFont("helvetica", 30)

        self.text_field = QtGui.QLineEdit()
        stop_button  = QtGui.QPushButton("STOP")
        start_button = QtGui.QPushButton("START")
        self.work_thread  = RunningAnimation(self.text_field)
        
        stop_button.setFont(font)
        start_button.setFont(font)
        self.text_field.setFont(font)



        grid.addWidget(self.text_field, 0, 0)
        grid.addWidget(stop_button, 0, 1)
        grid.addWidget(start_button, 0, 2)

        stop_button.clicked.connect(self.work_thread.request_stop)

        start_button.clicked.connect(self.work_thread.request_start)

        self.setLayout(grid)   
        
        self.setWindowTitle('Running numbers')    
        self.show()
        
    def start(self):
        self.work_thread.start()

    def closeEvent(self, event):    
        self.work_thread.request_end()

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = MyWindow()
    ex.start()
    exit_value = app.exec_()
    
    sys.exit(exit_value)


if __name__ == '__main__':
    main()
