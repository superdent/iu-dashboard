from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class MetricWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Haupt-Layout des Widgets
        layout = QVBoxLayout()

        # Symbol und Durchschnittsnote in einem einzigen QLabel mit HTML
        self.metric_label = QLabel()
        self.metric_label.setAlignment(Qt.AlignCenter)
        self.metric_label.setStyleSheet("border: 1px solid black; padding: 10px;")
        self.metric_label.setText('<div style="font-size: 16px;">Ø-Note</div><div style="font-size: 24px; font-weight: bold; color: green;">2,7</div>')

        # Hinzufügen des QLabel zum Layout
        layout.addWidget(self.metric_label)

        # Setzen des Layouts für das Widget
        self.setLayout(layout)

class SingleLineWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Haupt-Layout des Widgets
        layout = QVBoxLayout()

        # Einfache Textzeile in einem QLabel
        self.single_line_label = QLabel()
        self.single_line_label.setAlignment(Qt.AlignCenter)
        self.single_line_label.setStyleSheet("border: 1px solid black; padding: 10px;")
        self.single_line_label.setText('Einfache Textzeile')

        # Hinzufügen des QLabel zum Layout
        layout.addWidget(self.single_line_label)

        # Setzen des Layouts für das Widget
        self.setLayout(layout)
