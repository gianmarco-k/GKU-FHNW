#Uebung 4

import sys
from PyQt5.QtWidgets import *

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
        self.button_save = QPushButton("Save")

        ## Layout füllen
        layout.addRow("Vorname:", self.vorname_input)
        layout.addRow("Name:", self.name_input)
        layout.addRow("Geburtstag:", self.geburtstag_input)
        layout.addRow("Adresse:", self.adresse_input)
        layout.addRow("Postleitzahl", self.plz_input)
        layout.addRow("Ort:", self.ort_input)
        layout.addRow("Land:", self.land_input)
        layout.addRow(self.button_save)

        ## Fenster anzeigen
        self.show()

    def createMenu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        self.action_save = QAction("Save", self)
        self.action_quit = QAction("Quit", self)

        file_menu.addAction(self.action_save)
        file_menu.addAction(self.action_quit)

    def save_data(self):
        vorname = self.vorname_input.text()
        name = self.name_input.text()
        geburtstag = self.geburtstag_input.date().toString("d/M/yyyy") #Format: 17/12/2001
        adresse = self.adresse_input.text()
        plz = self.plz_input.text()
        ort = self.ort_input.text()
        land = self.land_input.currentText()

        daten_zeile = f"{vorname}, {name}, {geburtstag}, {adresse}, {plz}, {ort}, {land}\n"

        try:
            with open("output.txt", "w", encoding="utf-8") as file:
                file.write(daten_zeile)
            QMessageBox.information(self, "Erfolg", "Daten wurden gespeichert")
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim Speichern: {e}")

    def createConnects(self):
        self.action_quit.triggered.connect(self.close)
        self.action_save.triggered.connect(self.save_data)
        self.button_save.clicked.connect(self.save_data)


def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()