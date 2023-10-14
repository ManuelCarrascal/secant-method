import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class PlotCanvas(FigureCanvas):
    """
    Clase que define un objeto de gráfica para el Método de la Secante.

    Atributos:
    - zoom_factor: factor de zoom para la gráfica.
    - press: evento de presión del mouse.
    - fig: figura de la gráfica.
    - ax: ejes de la gráfica.

    Métodos:
    - on_scroll: método que maneja el evento de scroll del mouse.
    - zoom: método que realiza el zoom en la gráfica.
    - plot_graph: método que dibuja la gráfica del Método de la Secante.
    - on_pick: método que maneja el evento de selección de un punto en la gráfica.
    - set_pick_radius: método que establece el radio de selección de un punto en la gráfica.
    """
    def __init__(self, parent):
        """
        Constructor de la clase PlotCanvas.

        Parámetros:
        - parent: objeto padre de la gráfica.
        """
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)
        self.zoom_factor = 1.1
        self.mpl_connect('scroll_event', self.on_scroll)
        self.mpl_connect('pick_event', self.on_pick)
        self.press = None
        self.set_pick_radius(5)

    def on_scroll(self, event):
        """
        Método que maneja el evento de scroll del mouse.

        Parámetros:
        - event: evento de scroll del mouse.
        """
        if event.button == 'up':
            self.zoom(1 / self.zoom_factor)
        elif event.button == 'down':
            self.zoom(self.zoom_factor)

    def zoom(self, factor):
        """
        Método que realiza el zoom en la gráfica.

        Parámetros:
        - factor: factor de zoom para la gráfica.
        """
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        new_xlim = [x * factor for x in xlim]
        new_ylim = [y * factor for y in ylim]
        self.ax.set_xlim(new_xlim)
        self.ax.set_ylim(new_ylim)
        self.draw()

    def plot_graph(self, f, x_vals, f_vals, x0, x1):
        """
        Método que dibuja la gráfica del Método de la Secante.

        Parámetros:
        - f: función a graficar.
        - x_vals: valores de x para los puntos de la secante.
        - f_vals: valores de f(x) para los puntos de la secante.
        - x0: valor inicial de x para el Método de la Secante.
        - x1: valor siguiente de x para el Método de la Secante.
        """
        self.ax.clear()
        self.ax.axhline(0, color='black', linewidth=0.5)
        self.ax.axvline(0, color='black', linewidth=0.5)
        # crea un arreglo de 400 puntos entre el mínimo y el máximo de los valores de x
        x = np.linspace(min(min(x_vals), x0, x1) - 1, max(max(x_vals), x0, x1) + 1, 400)
        # evalúa la función en cada punto del arreglo x 
        y = [sp.N(f.subs('x', xi)) for xi in x]
        # grafica la función
        self.ax.plot(x, y, label='f(x)')

        for xi, fxi in zip(x_vals, f_vals):
            self.ax.plot(xi, fxi, 'ro')
            secant_x = [xi, x0]
            secant_y = [fxi, sp.N(f.subs('x', x0))]
            self.ax.plot(secant_x, secant_y, '-', label=f'Secante desde ({xi:.4f}, {fxi:.4f}) a ({x0:.4f}, {sp.N(f.subs("x", x0)):.4f})')

        self.ax.set_xlabel('x')
        self.ax.set_ylabel('f(x)')
        self.ax.set_title('Gráfica del Método de la Secante')
        self.ax.grid(True)
        self.ax.legend()
        self.draw()

    def on_pick(self, event):
        """
        Método que maneja el evento de selección de un punto en la gráfica.

        Parámetros:
        - event: evento de selección de un punto en la gráfica.
        """
        if isinstance(event, PickEvent):
            if event.mouseevent.button == 1:
                self.press = (event.mouseevent.xdata, event.mouseevent.ydata)
            elif event.mouseevent.button == 3:
                self.ax.set_xlim(auto=True)
                self.ax.set_ylim(auto=True)
                self.draw()

    def set_pick_radius(self, r):
        """
        Método que establece el radio de selección de un punto en la gráfica.

        Parámetros:
        - r: radio de selección de un punto en la gráfica.
        """
        for artist in self.ax.get_children():
            artist.set_picker(r)
