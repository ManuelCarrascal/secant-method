import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class PlotCanvas(FigureCanvas):
    def __init__(self, parent):
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
        if event.button == 'up':
            self.zoom(1 / self.zoom_factor)
        elif event.button == 'down':
            self.zoom(self.zoom_factor)

    def zoom(self, factor):
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        new_xlim = [x * factor for x in xlim]
        new_ylim = [y * factor for y in ylim]
        self.ax.set_xlim(new_xlim)
        self.ax.set_ylim(new_ylim)
        self.draw()

    def plot_graph(self, f, x_vals, f_vals, x0, x1):
        self.ax.clear()
        self.ax.axhline(0, color='black', linewidth=0.5)
        self.ax.axvline(0, color='black', linewidth=0.5)
        x = np.linspace(min(min(x_vals), x0, x1) - 1, max(max(x_vals), x0, x1) + 1, 400)
        y = [sp.N(f.subs('x', xi)) for xi in x]
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
        if isinstance(event, PickEvent):
            if event.mouseevent.button == 1:
                self.press = (event.mouseevent.xdata, event.mouseevent.ydata)
            elif event.mouseevent.button == 3:
                self.ax.set_xlim(auto=True)
                self.ax.set_ylim(auto=True)
                self.draw()

    def set_pick_radius(self, r):
        for artist in self.ax.get_children():
            artist.set_picker(r)
