import sympy as sp
from PyQt5.QtWidgets import (
    QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTableWidget,
    QTableWidgetItem, QGroupBox, QGridLayout, QDesktopWidget
)
from PyQt5.QtGui import QIcon, QFont
from utils import mostrar_manual, verificar_metodo_adecuado
from metodo_secante import metodo_secante
from plot_canvas import PlotCanvas  # Modifica esta línea para importar la clase PlotCanvas desde el nuevo archivo
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar

def initUI(self):
        self.setWindowTitle("Método de la Secante")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        input_group = QGroupBox("Entrada")
        input_layout = QVBoxLayout()
        input_group.setLayout(input_layout)

        self.label_funcion = QLabel("Función f(x):")
        self.label_x0 = QLabel("x0:")
        self.label_x1 = QLabel("x1:")
        self.label_tol = QLabel("Tolerancia (%):")

        font = QFont()
        font.setBold(True)
        self.label_funcion.setFont(font)
        self.label_x0.setFont(font)
        self.label_x1.setFont(font)
        self.label_tol.setFont(font)

        self.input_funcion = QLineEdit()
        self.input_x0 = QLineEdit()
        self.input_x1 = QLineEdit()
        self.input_tol = QLineEdit()

        input_layout.addWidget(self.label_funcion)
        input_layout.addWidget(self.input_funcion)
        input_layout.addWidget(self.label_x0)
        input_layout.addWidget(self.input_x0)
        input_layout.addWidget(self.label_x1)
        input_layout.addWidget(self.input_x1)
        input_layout.addWidget(self.label_tol)
        input_layout.addWidget(self.input_tol)

        plot_group = QGroupBox("Gráfica y Tabla")
        plot_layout = QVBoxLayout()
        plot_group.setLayout(plot_layout)

        self.calcular_button = QPushButton("Calcular")
        self.guardar_csv_button = QPushButton(" Guardar CSV")
        self.guardar_csv_button.setIcon(QIcon("icons/save.svg"))
        self.guardar_csv_button.setStyleSheet("background-color: green; color: white;")
        self.manual_button = QPushButton(" Manual de Usuario")

        self.resultado_table = QTableWidget()
        self.resultado_table.setColumnCount(4)

        plot_layout.addWidget(self.resultado_table)
        self.calcular_button = QPushButton("Calcular")
        button_layout = QHBoxLayout()  # Crea un QHBoxLayout para los botones
        self.guardar_csv_button = QPushButton(" Guardar CSV")
        self.guardar_csv_button.setIcon(QIcon("icons/save.svg"))
        self.guardar_csv_button.setStyleSheet("background-color: green; color: yellow;")  # Configura el color de fondo y del texto
        self.manual_button = QPushButton(" Manual de Usuario")
        self.manual_button.setIcon(QIcon("icons/help.svg"))
        self.manual_button.setStyleSheet("background-color: #149fda; color: white;")

        button_layout.addWidget(self.guardar_csv_button)  # Agrega el botón "Guardar CSV" al layout horizontal
        button_layout.addWidget(self.manual_button)  # Agrega el botón "Manual de Usuario" al layout horizontal

        plot_layout.addWidget(self.calcular_button)
        plot_layout.addLayout(button_layout)  # Agrega el layout horizontal de los botones al layout vertical principal

        grid_layout.addWidget(input_group, 0, 0, 2, 1)
        grid_layout.addWidget(plot_group, 0, 1, 2, 1)

        self.central_widget.setLayout(grid_layout)

        self.canvas = PlotCanvas(self)
        grid_layout.addWidget(self.canvas, 2, 0, 1, 2)

        navigation_toolbar = NavigationToolbar(self.canvas, self)
        grid_layout.addWidget(navigation_toolbar, 3, 0, 1, 2)

        self.calcular_button.clicked.connect(self.calcular)
        self.guardar_csv_button.clicked.connect(self.guardar_csv)
        self.manual_button.clicked.connect(lambda: mostrar_manual(self))