#Uebung 8

import sys
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import numpy as np



class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Aufgabe 8")
        ### LAYOUT WÄHLEN:
        layout = QFormLayout()
        self.setMinimumSize(200,200)

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
        ## Widgets erstellen
        # ...

        ## Layout füllen
        # ...

        ## Fenster anzeigen
        self.show()


    def createConnects(self):
        pass




def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()