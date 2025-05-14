#Uebung 8

import sys
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setLayout()
        self.createConnects()

    def setLayout(self):
        self.setWindowTitle("Übung 8")
        layout = QFormLayout()
        self.setMinimumSize(800,800)

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
        ## Matplotlib Figure
        self.figure = plt.figure(figsize = (160, 90))
        self.canvas = FigureCanvas(self.figure)

        ## Eingabefelder
        self.def_function = QLineEdit('Koeffizienten kommagetrennt eingeben (z.B. 1,2,-3,4)')
        
        self.range_min = QLineEdit('0')
        self.range_max = QLineEdit('10')
        range_layout = QHBoxLayout()
        range_layout.addWidget(QLabel("X-Min:"))
        range_layout.addWidget(self.range_min)
        range_layout.addSpacing(20)
        range_layout.addWidget(QLabel("X-Max:"))
        range_layout.addWidget(self.range_max)

        self.num_points = QLineEdit('100')

        self.color_select = QComboBox()
        self.color_select.addItems(["blue", "green", "red", "black"])

        self.button_plot = QPushButton("Plot")

        ## Layout füllen
        layout.addWidget(self.canvas)
        layout.addRow("Polynom-Koeffizienten:", self.def_function)
        layout.addRow(range_layout)
        layout.addRow("Anzahl Punkte:", self.num_points)
        layout.addRow("Farbe auswählen:", self.color_select)
        layout.addRow(self.button_plot)

        ## Fenster anzeigen
        self.show()

    def PlotFunktion(self):
        try:
            koeff = list(map(float, self.def_function.text().split(',')))
            f = np.poly1d(koeff)

            x_min = float(self.range_min.text())
            x_max = float(self.range_max.text())
            num = int(self.num_points.text())

            x = np.linspace(x_min, x_max, num)
            y = f(x)

            color = self.color_select.currentText()

            # Plot aktualisieren
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x, y, color=color)
            ax.set_title("Polynomplot")
            ax.grid(True)
            self.canvas.draw()

        except Exception as e:
            QMessageBox.warning(self, "Fehler", f"Ungültige Eingabe: {e}")

    def createConnects(self):
        self.button_plot.clicked.connect(self.PlotFunktion)



def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()