#Übung 6

import urllib.parse
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        font = self.font()
        font.setPointSize(14)
        self.setFont(font)

        self.createLayout()
        self.createConnects()

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("MainWindow - [Preview]")
        ### LAYOUT WÄHLEN:
        layout = QFormLayout()
        self.setMinimumSize(600,200)

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
        ## Widgets erstellen

        self.laenge_input = QLineEdit()
        self.breite_input = QLineEdit()
        self.button_map = QPushButton("Auf Karte zeigen...")

        ## Layout füllen
        layout.addRow("Länge:", self.laenge_input)
        layout.addRow("Breite:", self.breite_input)
        layout.addRow(self.button_map)

        ## Fenster anzeigen
        self.show()

    def show_map(self):
        koordinaten = f"{self.laenge_input.text()},{self.breite_input.text()}"
        url_encoded = urllib.parse.quote(koordinaten)
        link = f"https://www.google.ch/maps/place/{url_encoded}"
        QDesktopServices.openUrl(QUrl(link))

    def createConnects(self):
        self.button_map.clicked.connect(self.show_map)


def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()