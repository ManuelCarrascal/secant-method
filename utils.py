import csv
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QTableWidget, QMessageBox, QLabel, QPushButton, QDialog, QDesktopWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sympy as sp


def guardar_csv(resultado_table):
    if resultado_table.rowCount() == 0:
        mostrar_alerta("No hay datos para guardar.")
        return

    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly
    options |= QFileDialog.HideNameFilterDetails
    file_dialog = QFileDialog()
    file_dialog.setOptions(options)
    file_dialog.setAcceptMode(QFileDialog.AcceptSave)
    file_dialog.setNameFilter("CSV files (*.csv)")
    file_dialog.setDefaultSuffix("csv")

    if file_dialog.exec_():
        file_path = file_dialog.selectedFiles()[0]
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in range(resultado_table.rowCount()):
                data = []
                for col in range(resultado_table.columnCount()):
                    item = resultado_table.item(row, col)
                    if item is not None:
                        data.append(item.text())
                    else:
                        data.append("")
                writer.writerow(data)
        mostrar_alerta("Datos guardados en CSV correctamente.")

def mostrar_alerta(mensaje):
    alert = QMessageBox()
    alert.setIcon(QMessageBox.Warning)
    alert.setWindowTitle("Alerta")
    alert.setText(mensaje)
    alert.exec_()

def mostrar_manual(self):
        manual_dialog = QDialog(self)
        manual_dialog.setWindowTitle("Manual de Usuario")
        screen = QDesktopWidget().availableGeometry()
        manual_dialog.setGeometry(100, 100, 600, min(400, screen.height()))
        manual_layout = QVBoxLayout()

        font = QFont()
        font.setPointSize(12)

        manual_text = """
         **MANUAL DE USUARIO DE LA APP DEL METODO DE LA SECANTE.**

         **Cómo ingresar ecuaciones**

        Para ingresar una ecuación, sigue estas pautas:

        1. *Operadores matemáticos y funciones*: Utiliza operadores matemáticos estándar como `+`, `-`, `*`, `/` y `**` (para exponentes).
        También puedes utilizar funciones matemáticas comunes como `sin()`, `cos()`, `tan()`, `exp()`, `log()`, `sqrt()`, etc. 
        Asegúrate de que las funciones se escriban con paréntesis, por ejemplo, `sin(x)`.

        2. *Fracciones*: Para ingresar una fracción, utiliza `/`, por ejemplo, `1/3` para representar un tercio.

        3. *Potencias*: Utiliza el operador `**` para expresar potencias. Por ejemplo, `x**2` representa x al cuadrado.

        4. *Paréntesis*: Puedes utilizar paréntesis para establecer el orden de las operaciones en la ecuación. Por ejemplo, `(x + 2) * (x - 1)`.

        **Ejemplos de ecuaciones**

        Aquí tienes algunos ejemplos de ecuaciones y cómo deberían ingresarse:

        - Ecuación: 2x + sin(x)
        - Entrada: `2*x + sin(x)`

        - Ecuación cuadrática: x^2 - 4
        - Entrada: `x**2 - 4`

        - Ecuación con fracción: (1/3)x + 5
        - Entrada: `(1/3)*x + 5`

        - Ecuación con paréntesis: (x + 2)(x - 1)
        - Entrada: `(x + 2)*(x - 1)`

        Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en consultar la documentación de SymPy.

        """

        manual_label = QLabel(manual_text, manual_dialog)
        manual_label.setAlignment(Qt.AlignLeft)
        manual_label.setWordWrap(True)
        
        manual_label.setFont(font)
        
        manual_layout.addWidget(manual_label)
        close_button = QPushButton("Cerrar", manual_dialog)
        close_button.setFont(QFont("Arial", 20))
        close_button.clicked.connect(manual_dialog.close)
        manual_layout.addWidget(close_button, alignment=Qt.AlignRight)
        manual_dialog.setLayout(manual_layout)
        manual_dialog.exec_()

def verificar_metodo_adecuado(self, f, x0, x1):
        f_x0 = sp.N(f.subs('x', x0))
        f_x1 = sp.N(f.subs('x', x1))
        if f_x0 * f_x1 < 0:
            return True
        return False