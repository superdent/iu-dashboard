import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QAction, QMenu, QDialog, QDesktopWidget

from frontend.add_exam_dialog import AddExamDialog
from frontend.complete_modules_widget import CompletedModulesWidget
from frontend.credit_points_widget import CreditPointsWidget
from frontend.edit_exam_dialog import EditExamDialog
from frontend.next_exam_widget import NextExamWidget
from frontend.average_grade_widget import AverageGradeWidget
from backend.study_program_service import StudyProgramService
from frontend.semester_bar_chart_widget import SemesterBarChartWidget


class MainApp(QMainWindow):
    # noinspection PyShadowingNames
    def __init__(self, study_programs):
        super().__init__()

        # Fenster-Konfiguration
        self.next_exam_widget = None
        self.complete_modules_widget = None
        self.notenschnitt_widget = None
        self.credit_points_widget = None
        self.semester_bar_chart_widget = None
        self.layout = None
        self.study_programs = None
        self.setWindowTitle("Studien Dashboard")

        screen = QDesktopWidget().availableGeometry()
        width = int(screen.width() * 0.75)
        height = int(screen.height() * 0.75)
        self.resize(width, height)
        self.move(
            (screen.width() - width) // 2,
            (screen.height() - height) // 2
        )

        self.study_program = study_programs[0]  # TODO: Auswahl des study_programs implementieren

        # GUI & Widgets initialisieren
        self.setup_widgets()

        # Menü erzeugen
        self._create_menu()

    def setup_widgets(self):
        """Initialisiert oder aktualisiert alle Widgets mit neuen Daten."""
        # Werte berechnen
        next_exam = StudyProgramService.get_next_exam_date(self.study_program)
        complete_modules = StudyProgramService.get_completed_modules(self.study_program)
        average_grade = StudyProgramService.calculate_average_grade(self.study_program)
        credit_points = StudyProgramService.calculate_credit_points(self.study_program)
        modules_per_semester = StudyProgramService.get_modules_per_semester(self.study_program)

        # Falls Widgets existieren, nur aktualisieren
        if self.next_exam_widget is not None:
            self.next_exam_widget.update_exam(next_exam)
            self.complete_modules_widget.update_modules(*complete_modules)
            self.notenschnitt_widget.update_grade(average_grade, StudyProgramService.get_target_average_grade(self.study_program))  # 2.5 als Ziel-Schwelle
            self.credit_points_widget.update_credit_points(credit_points)
            self.semester_bar_chart_widget.update_data(modules_per_semester)
        else:
            # Widgets zum ersten Mal erzeugen
            self.next_exam_widget = NextExamWidget(next_exam)
            self.complete_modules_widget = CompletedModulesWidget(*complete_modules)
            self.notenschnitt_widget = AverageGradeWidget(average_grade, StudyProgramService.get_target_average_grade(self.study_program))
            self.credit_points_widget = CreditPointsWidget(credit_points)
            self.semester_bar_chart_widget = SemesterBarChartWidget(modules_per_semester)

            # Layout setzen
            erste_zeile_layout = QVBoxLayout()
            erste_zeile_layout.setDirection(QVBoxLayout.LeftToRight)
            erste_zeile_layout.addWidget(self.next_exam_widget)
            erste_zeile_layout.addWidget(self.complete_modules_widget)
            erste_zeile_layout.addWidget(self.notenschnitt_widget)
            erste_zeile_layout.addWidget(self.credit_points_widget)

            # Hauptlayout
            haupt_layout = QVBoxLayout()
            haupt_layout.addLayout(erste_zeile_layout, stretch=1)
            haupt_layout.addWidget(self.semester_bar_chart_widget, stretch=2)
            self.layout = haupt_layout

            # Zentrales Widget setzen
            central_widget = QWidget()
            central_widget.setLayout(self.layout)
            self.setCentralWidget(central_widget)

    def _create_menu(self):
        menu_bar = self.menuBar()
        exams_menu = QMenu("Prüfungen", self)
        add_exam_action = QAction("Prüfung anlegen", self)
        # noinspection PyUnresolvedReferences
        add_exam_action.triggered.connect(self._open_add_exam_dialog)
        exams_menu.addAction(add_exam_action)
        edit_exam_action = QAction("Prüfung bearbeiten", self)
        # noinspection PyUnresolvedReferences
        edit_exam_action.triggered.connect(self._open_edit_exam_dialog)
        exams_menu.addAction(edit_exam_action)
        menu_bar.addMenu(exams_menu)

    def _open_add_exam_dialog(self):
        modules = StudyProgramService.get_all_modules(self.study_program)
        dialog = AddExamDialog(modules, self)
        dialog.show()
        if dialog.exec_() == QDialog.Accepted:
            exam_data = dialog.get_exam_data()
            print("Neue Prüfung:", exam_data)
            StudyProgramService.save_exam(exam_data)
            self.refresh_gui()  # Nach dem Speichern aktualisieren

    def _open_edit_exam_dialog(self):
        exams = StudyProgramService.get_exams(self.study_program)
        dialog = EditExamDialog(exams, self)
        dialog.show()
        if dialog.exec_() == QDialog.Accepted:
            exam_data = dialog.get_exam_data()
            print("Prüfung bearbeitet:", exam_data)
            StudyProgramService.update_exam(exam_data)
            self.refresh_gui()  # Nach dem Speichern aktualisieren

    def refresh_gui(self):
        """Lädt die Daten neu und aktualisiert die Widgets."""
        self.study_programs = StudyProgramService.reload_study_programs()
        self.study_program = self.study_programs[0]  # Erstes Programm auswählen
        self.setup_widgets()

if __name__ == "__main__":
    from backend.study_data_loader import StudyDataLoader
    loader = StudyDataLoader()
    loader.load_data()
    study_programs = loader.get_study_programs()

    app = QApplication(sys.argv)
    main_window = MainApp(study_programs)
    main_window.show()
    sys.exit(app.exec_())

