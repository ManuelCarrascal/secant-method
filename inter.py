import sympy as sp
import matplotlib.pyplot as plt
import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QMessageBox, QFileDialog, QDialog, QGroupBox, QGridLayout, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QCursor
from utils import guardar_csv, mostrar_alerta, mostrar_manual, verificar_metodo_adecuado
from metodo_secante import metodo_secante
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from plot_canvas import PlotCanvas  # Modifica esta línea para importar la clase PlotCanvas desde el nuevo archivo
from ui import initUI  # Importa la función initUI desde ui_config.py

import numpy as np

class MetodoSecanteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        initUI(self)

    def calcular(self):
        expresion = self.input_funcion.text()
        x0_text = self.input_x0.text()
        x1_text = self.input_x1.text()
        tol_text = self.input_tol.text()
        if not expresion:
            self.mostrar_alerta("Debe ingresar una función.")
            return
        if not x0_text:
            self.mostrar_alerta("Debe ingresar un valor para x0.")
            return
        try:
            x0 = float(x0_text)
        except ValueError:
            self.mostrar_alerta("x0 debe ser un número válido.")
            return
        if not x1_text:
            self.mostrar_alerta("Debe ingresar un valor para x1.")
            return
        try:
            x1 = float(x1_text)
        except ValueError:
            self.mostrar_alerta("x1 debe ser un número válido.")
            return
        if not tol_text:
            self.mostrar_alerta("Debe ingresar un valor para la tolerancia.")
            return
        try:
            tol = float(tol_text)
        except ValueError:
            self.mostrar_alerta("La tolerancia debe ser un número válido.")
            return
        
        f = sp.sympify(expresion)

        if verificar_metodo_adecuado(self,f, x0, x1):
            tabla_secante, x_vals, f_vals = metodo_secante(self, f, x0, x1, tol, max_iter=49)
            self.resultado_table.setRowCount(len(tabla_secante))
            for i, fila in enumerate(tabla_secante):
                for j, valor in enumerate(fila):
                    item = QTableWidgetItem(str(valor))
                    self.resultado_table.setItem(i, j, item)
            self.canvas.plot_graph(f, x_vals, f_vals, x0, x1)
        else:
            self.mostrar_alerta("El método de la secante no es adecuado para esta función y/o valores iniciales.")

    def mostrar_alerta(self, mensaje):
        alert = QMessageBox(self)
        alert.setIcon(QMessageBox.Warning)
        alert.setWindowTitle("Alerta")
        alert.setText(mensaje)
        alert.exec_()


    def guardar_csv(self):
        guardar_csv(self.resultado_table)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MetodoSecanteApp()
    window.showMaximized()
    sys.exit(app.exec_())