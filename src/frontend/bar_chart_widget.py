from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class BarChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout(self)
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.layout.addWidget(self.canvas)

        self.ax = self.canvas.figure.add_subplot(111)
        self.create_plot()

    def create_plot(self):
        # Generate some data
        x = np.arange(6)  # Six groups
        width = 0.2  # width of the bars

        y1 = np.random.randint(1, 10, 6)
        y2 = np.random.randint(1, 10, 6)
        y3 = np.random.randint(1, 10, 6)

        self.ax.bar(x - width, y1, width, label='A')
        self.ax.bar(x, y2, width, label='B')
        self.ax.bar(x + width, y3, width, label='C')

        self.ax.set_xlabel('Group')
        self.ax.set_ylabel('Values')
        self.ax.set_title('Test Bar Chart')
        self.ax.legend()
