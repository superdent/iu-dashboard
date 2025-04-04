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
        """Erstellt das Balkendiagramm mit Modulzahlen pro Semester und einer Ziel-Linie bei 30 CP."""
        self.ax.clear()  # Vorherige Inhalte löschen

        semesters = sorted(modules_per_semester.keys())  # Semester sortieren
        completed = [modules_per_semester[s][0] * 5 for s in semesters]  # Bestandene Module
        not_completed = [modules_per_semester[s][1] * 5 for s in semesters]  # Nicht bestandene Module
        not_started = [modules_per_semester[s][2] * 5 for s in semesters] # Nicht begonnenen Module

        x = np.arange(len(semesters))  # X-Achsen-Positionen
        width = 0.4  # Balkenbreite

        # Farben: Bestanden (Grün), Nicht bestanden (Orange), Nicht begonnen (Grau)
        self.ax.bar(x - width / 2, completed, width, label='Bestanden', color='#4CAF50')  # Grün
        self.ax.bar(x + width / 2, not_completed, width, label='Nicht bestanden', color='#FFA500')  # Orange
        self.ax.bar(x, not_started, width, label='Nicht begonnen', color='#B0BEC5')  # Grau

        # Horizontale Linie für Zielwert (30 CP pro Semester)
        target_cp = 30
        self.ax.axhline(y=target_cp, color='red', linestyle='dashed', linewidth=2, label=f'Ziel: {target_cp} CP')

        # Achsenbeschriftungen
        self.ax.set_xticks(x)
        self.ax.set_xticklabels([f"Sem {s}" for s in semesters])
        self.ax.set_xlabel('Semester')
        self.ax.set_ylabel('Anzahl Module')
        self.ax.set_title('Module pro Semester')
        self.ax.legend()

        self.canvas.draw()

    def update_data(self, modules_per_semester: dict):
        """Aktualisiert das Balkendiagramm mit neuen Daten."""
        self.create_plot(modules_per_semester)
