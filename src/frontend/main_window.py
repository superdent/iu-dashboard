import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from frontend.complete_modules_widget import CompletedModulesWidget
from frontend.credit_points_widget import CreditPointsWidget
from frontend.next_exam_widget import NextExamWidget
from frontend.average_grade_widget import AverageGradeWidget
from backend.study_program_service import StudyProgramService
from frontend.semester_bar_chart_widget import SemesterBarChartWidget


class MainApp(QMainWindow):
    def __init__(self, study_programs):
        super().__init__()

        # Fenster-Konfiguration
        self.setWindowTitle("Studien Dashboard")
        self.setGeometry(100, 100, 800, 600)

        study_program = study_programs[0]  # TODO: Auswahl des study_programs implementieren

        # Werte berechnen
        next_exam = StudyProgramService.get_next_exam_date(study_program)
        complete_modules = StudyProgramService.get_completed_modules(study_program)
        average_grade = StudyProgramService.calculate_average_grade(study_program)
        credit_points = StudyProgramService.calculate_credit_points(study_program)
        modules_per_semester = StudyProgramService.get_modules_per_semester(study_program)

        # Widgets mit berechneten Werten initialisieren
        self.next_exam_widget = NextExamWidget(next_exam)
        self.complete_modules_widget = CompletedModulesWidget(*complete_modules)
        self.notenschnitt_widget = AverageGradeWidget(average_grade)
        self.credit_points_widget = CreditPointsWidget(credit_points)
        self.semester_bar_chart_widget = SemesterBarChartWidget(modules_per_semester)

        # Layout für die erste Zeile
        erste_zeile_layout = QVBoxLayout()
        erste_zeile_layout.setDirection(QVBoxLayout.LeftToRight)
        erste_zeile_layout.addWidget(self.next_exam_widget)
        erste_zeile_layout.addWidget(self.complete_modules_widget)
        erste_zeile_layout.addWidget(self.notenschnitt_widget)
        erste_zeile_layout.addWidget(self.credit_points_widget)

        # Hauptlayout
        haupt_layout = QVBoxLayout()
        haupt_layout.addLayout(erste_zeile_layout)
        haupt_layout.addWidget(self.semester_bar_chart_widget)
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
