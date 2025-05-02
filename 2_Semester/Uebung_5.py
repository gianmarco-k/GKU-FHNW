#Uebung 5

import urllib.parse
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createMenu()
        self.createConnects()

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("GUI-Programmierung")
        ### LAYOUT WÄHLEN:
        layout = QFormLayout()
        self.setMinimumSize(300,200)

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
        ## Widgets erstellen

        self.vorname_input = QLineEdit()
        self.name_input = QLineEdit()
        self.geburtstag_input = QDateEdit()
        self.adresse_input = QLineEdit()
        self.plz_input = QLineEdit()
        self.ort_input = QLineEdit()
        self.land_input = QComboBox()
        self.land_input.addItems(["Schweiz", "Österreich", "Deutschland", "Italien"]) #Hinzufügen der möglichen auswahlen
        self.button_map = QPushButton("Auf Karte zeigen")
        self.button_laden = QPushButton("Laden")
        self.button_save = QPushButton("Save")

        ## Layout füllen
        layout.addRow("Vorname:", self.vorname_input)
        layout.addRow("Name:", self.name_input)
        layout.addRow("Geburtstag:", self.geburtstag_input)
        layout.addRow("Adresse:", self.adresse_input)
        layout.addRow("Postleitzahl", self.plz_input)
        layout.addRow("Ort:", self.ort_input)
        layout.addRow("Land:", self.land_input)
        layout.addRow(self.button_map)
        layout.addRow(self.button_laden)
        layout.addRow(self.button_save)

        ## Fenster anzeigen
        self.show()

    def createMenu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        self.action_laden = QAction("Laden", self)
        self.action_save = QAction("Save", self)
        self.action_quit = QAction("Quit", self)

        view_menu = menubar.addMenu("View")

        self.action_map = QAction("Karte", self)

        file_menu.addAction(self.action_laden)
        file_menu.addAction(self.action_save)
        file_menu.addAction(self.action_quit)
        view_menu.addAction(self.action_map)
    
    def show_map(self):
        adresse = f"{self.adresse_input.text()} {self.plz_input.text()} {self.ort_input.text()} {self.land_input.currentText()}"
        url_encoded = urllib.parse.quote(adresse)
        link = f"https://www.google.ch/maps/place/{url_encoded}"
        QDesktopServices.openUrl(QUrl(link))
    
    def laden_data(self):
        """filename, _ = QFileDialog.getOpenFileName(self, "Datei laden", "", "Textdateien (*.txt)")
        if not filename:
            return #Abbrechen des Ladevorgangs
        
        dformat = QLocale().dateFormat(format=QLocale.FormatType.ShortFormat)
        self.dateEdit.setDate(QDate.formStrin(text, dformat))"""
        #Funktioniert noch nicht darum:
        pass
        

    def save_data(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Textdateien (*.txt)")
        if not filename:
            return #Abbrechen des Speichervorgangs
        
        vorname = self.vorname_input.text()
        name = self.name_input.text()
        geburtstag = self.geburtstag_input.date().toString("d/M/yyyy") #Format: 17/12/2001
        adresse = self.adresse_input.text()
        plz = self.plz_input.text()
        ort = self.ort_input.text()
        land = self.land_input.currentText()

        daten_zeile = f"{vorname}, {name}, {geburtstag}, {adresse}, {plz}, {ort}, {land}\n"

        try:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(daten_zeile)
            QMessageBox.information(self, "Erfolg", "Daten wurden gespeichert")
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim Speichern: {e}")

    def createConnects(self):
        self.action_laden.triggered.connect(self.laden_data)
        self.action_save.triggered.connect(self.save_data)
        self.action_quit.triggered.connect(self.close)
        self.action_map.triggered.connect(self.show_map)
        self.button_map.clicked.connect(self.show_map)
        self.button_laden.clicked.connect(self.laden_data)
        self.button_save.clicked.connect(self.save_data)


def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()