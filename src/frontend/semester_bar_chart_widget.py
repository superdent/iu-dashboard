import numpy as np
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class SemesterBarChartWidget(QWidget):
    def __init__(self, modules_per_semester: dict):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.layout.addWidget(self.canvas)

        self.ax = self.canvas.figure.add_subplot(111)
        self.create_plot(modules_per_semester)

    def create_plot(self, modules_per_semester: dict):
        semesters = sorted(modules_per_semester.keys())  # Semester sortieren
        completed = [modules_per_semester[s][0] for s in semesters]  # Bestandene
        not_completed = [modules_per_semester[s][1] for s in semesters]  # Nicht bestandene

        x = np.arange(len(semesters))  # X-Achsen-Positionen
        width = 0.4  # Balkenbreite

        self.ax.clear()
        self.ax.bar(x - width / 2, completed, width, label='Bestanden', color='#4CAF50')  # Grün
        self.ax.bar(x + width / 2, not_completed, width, label='Nicht Bestanden', color='#F44336')  # Rot

        self.ax.set_xticks(x)
        self.ax.set_xticklabels([f"Sem {s}" for s in semesters])
        self.ax.set_xlabel('Semester')
        self.ax.set_ylabel('Anzahl Module')
        self.ax.set_title('Module pro Semester')
        self.ax.legend()

        self.canvas.draw()
