from datetime import date

from backend.models.exam import Exam
from backend.models.module import Module
from backend.models.study_program import StudyProgram


class TestCreateTestData:

    @staticmethod
    def erstelle_standard_studium():
        module_daten = [
            # M01 – bestanden, eine alte Note
            (1, "M01", "Modul 1", 1, 5, "bestanden", [
                (1, 1, "Klausur", date(2023, 2, 17), 1.3)
            ]),

            # M02 – bestanden, zwei Prüfungen, beste zählt
            (2, "M02", "Modul 2", 1, 5, "bestanden", [
                (2, 2, "Klausur", date(2023, 2, 17), 4.7),
                (3, 2, "Klausur", date(2023, 3, 9), 2.3)
            ]),

            # M03 – offen, keine Prüfung
            (3, "M03", "Modul 3", 2, 5, "offen", []),

            # M04 – offen, zukünftige Prüfung
            (4, "M04", "Modul 4", 2, 5, "offen", [
                (4, 4, "Hausarbeit", date.today().replace(year=date.today().year + 1), None)
            ]),

            # M05 – nicht bestanden, eine Note > 4
            (5, "M05", "Modul 5", 3, 5, "nicht bestanden", [
                (5, 5, "Klausur", date(2023, 4, 4), 5.0)
            ]),
        ]

        return TestCreateTestData.erstelle_studium(99, "Standard-Studium", module_daten)

    # noinspection PyShadowingBuiltins
    @staticmethod
    def erstelle_exam(id, modul_id, pruef_art, pruef_datum, note):
        exam = Exam(id, modul_id, pruef_art, pruef_datum, note)
        return exam

    # noinspection PyShadowingBuiltins
    @staticmethod
    def erstelle_modul(id, module_code, module_name, semester_id, ects_points, state, exams):
        module = Module(id, module_code, module_name, semester_id, ects_points, state)
        for exam_daten in exams:
            module.exams.append(TestCreateTestData.erstelle_exam(*exam_daten))
        return module

    @staticmethod
    def erstelle_studium(study_program_id, study_program_name, modules):
        study_program = StudyProgram(study_program_id, study_program_name)
        for module_data in modules:
            study_program.modules.append(TestCreateTestData.erstelle_modul(*module_data))
        return study_program
