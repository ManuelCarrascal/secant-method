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

class Ui_MainWindow(object):
    """
    Clase que define la interfaz gráfica de usuario para el método de la secante.
    """

    def setupUi(self, MainWindow):
        """
        Configura la interfaz gráfica de usuario.

        :param MainWindow: objeto QMainWindow que representa la ventana principal de la aplicación.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.input_group = QGroupBox(self.centralwidget)
        self.input_group.setObjectName("input_group")
        self.verticalLayout = QVBoxLayout(self.input_group)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_funcion = QLabel(self.input_group)
        self.label_funcion.setObjectName("label_funcion")
        self.verticalLayout.addWidget(self.label_funcion)
        self.input_funcion = QLineEdit(self.input_group)
        self.input_funcion.setObjectName("input_funcion")
        self.verticalLayout.addWidget(self.input_funcion)
        self.label_x0 = QLabel(self.input_group)
        self.label_x0.setObjectName("label_x0")
        self.verticalLayout.addWidget(self.label_x0)
        self.input_x0 = QLineEdit(self.input_group)
        self.input_x0.setObjectName("input_x0")
        self.verticalLayout.addWidget(self.input_x0)
        self.label_x1 = QLabel(self.input_group)
        self.label_x1.setObjectName("label_x1")
        self.verticalLayout.addWidget(self.label_x1)
        self.input_x1 = QLineEdit(self.input_group)
        self.input_x1.setObjectName("input_x1")
        self.verticalLayout.addWidget(self.input_x1)
        self.label_tol = QLabel(self.input_group)
        self.label_tol.setObjectName("label_tol")
        self.verticalLayout.addWidget(self.label_tol)
        self.input_tol = QLineEdit(self.input_group)
        self.input_tol.setObjectName("input_tol")
        self.verticalLayout.addWidget(self.input_tol)
        self.gridLayout.addWidget(self.input_group, 0, 0, 1, 1)
        self.plot_group = QGroupBox(self.centralwidget)
        self.plot_group.setObjectName("plot_group")
        self.verticalLayout_2 = QVBoxLayout(self.plot_group)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.calcular_button = QPushButton(self.plot_group)
        self.calcular_button.setObjectName("calcular_button")
        self.verticalLayout_2.addWidget(self.calcular_button)
        self.guardar_csv_button = QPushButton(self.plot_group)
        self.guardar_csv_button.setObjectName("guardar_csv_button")
        self.guardar_csv_button.setIcon(QIcon("icons/save.svg"))
        self.guardar_csv_button.setStyleSheet("background-color: green; color: white;")
        self.verticalLayout_2.addWidget(self.guardar_csv_button)
        self.manual_button = QPushButton(self.plot_group)
        self.manual_button.setObjectName("manual_button")
        self.manual_button.setIcon(QIcon("icons/help.svg"))
        self.manual_button.setStyleSheet("background-color: #149fda; color: white;")
        self.verticalLayout_2.addWidget(self.manual_button)
        self.resultado_table = QTableWidget(self.plot_group)
        self.resultado_table.setObjectName("resultado_table")
        self.resultado_table.setColumnCount(4)
        self.verticalLayout_2.addWidget(self.resultado_table)
        self.gridLayout.addWidget(self.plot_group, 0, 1, 1, 1)
        self.canvas = PlotCanvas(self.centralwidget)
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 1, 0, 1, 2)
        self.toolbar = NavigationToolbar(self.canvas, self.centralwidget)
        self.toolbar.setObjectName("toolbar")
        self.gridLayout.addWidget(self.toolbar, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.calcular_button.clicked.connect(self.calcular)
        self.guardar_csv_button.clicked.connect(self.guardar_csv)
        self.manual_button.clicked.connect(lambda: mostrar_manual(self))

    def retranslateUi(self, MainWindow):
        """
        Traduce los textos de la interfaz gráfica de usuario.

        :param MainWindow: objeto QMainWindow que representa la ventana principal de la aplicación.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Método de la Secante"))
        self.input_group.setTitle(_translate("MainWindow", "Entrada"))
        self.label_funcion.setText(_translate("MainWindow", "Función f(x):"))
        self.label_x0.setText(_translate("MainWindow", "x0:"))
        self.label_x1.setText(_translate("MainWindow", "x1:"))
        self.label_tol.setText(_translate("MainWindow", "Tolerancia (%):"))
        self.plot_group.setTitle(_translate("MainWindow", "Gráfica y Tabla"))
        self.calcular_button.setText(_translate("MainWindow", "Calcular"))
        self.guardar_csv_button.setText(_translate("MainWindow", " Guardar CSV"))
        self.manual_button.setText(_translate("MainWindow", " Manual de Usuario"))
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