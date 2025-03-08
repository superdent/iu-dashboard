import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from backend.studium_data_loader import StudiumDataLoader
from frontend.notenschnitt_widget import NotenschnittWidget
from frontend.credit_points_widget import CreditPointsWidget
import logging

class MainApp(QMainWindow):
    def __init__(self, studien):
        super().__init__()

        # Fenster-Konfiguration
        self.setWindowTitle("Studien Dashboard")
        self.setGeometry(100, 100, 800, 600)

        studium = studien[0]  # TODO: Auswahl des Studiums implementieren
        self.notenschnitt_widget = NotenschnittWidget(studium) 
        self.credit_points_widget = CreditPointsWidget(studium)
        self.zweites_widget = NotenschnittWidget(studium)
        self.drittes_widget = NotenschnittWidget(studium)

        # Layout für die erste Zeile
        erste_zeile_layout = QVBoxLayout()
        erste_zeile_layout.setDirection(QVBoxLayout.LeftToRight)
        erste_zeile_layout.addWidget(self.notenschnitt_widget)
        erste_zeile_layout.addWidget(self.zweites_widget)
        erste_zeile_layout.addWidget(self.credit_points_widget)

        # Hauptlayout
        haupt_layout = QVBoxLayout()
        haupt_layout.addLayout(erste_zeile_layout)
        haupt_layout.addWidget(self.drittes_widget)
        self.layout = haupt_layout
        
        # Zentrales Widget
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())
