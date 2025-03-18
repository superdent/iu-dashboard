import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from frontend.credit_points_widget import CreditPointsWidget
from frontend.notenschnitt_widget import NotenschnittWidget
from backend.study_program_service import StudyProgramService


class MainApp(QMainWindow):
    def __init__(self, study_programs):
        super().__init__()

        # Fenster-Konfiguration
        self.setWindowTitle("Studien Dashboard")
        self.setGeometry(100, 100, 800, 600)

        study_program = study_programs[0]  # TODO: Auswahl des study_programs implementieren

        # Werte berechnen
        average_grade = StudyProgramService.calculate_average_grade(study_program)
        credit_points = StudyProgramService.calculate_credit_points(study_program)

        # Widgets mit berechneten Werten initialisieren
        self.notenschnitt_widget = NotenschnittWidget(average_grade)
        self.credit_points_widget = CreditPointsWidget(credit_points)
        self.zweites_widget = NotenschnittWidget(average_grade)
        self.drittes_widget = NotenschnittWidget(average_grade)

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
