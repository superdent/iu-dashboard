from backend.models.study_program import StudyProgram
from backend.models.module import *

from datetime import date
from typing import Optional, Tuple, Dict, List

from backend.study_data_loader import StudyDataLoader
from backend.study_data_writer import StudyDataWriter


class StudyProgramService:
    @staticmethod
    def get_next_exam_date(study_program: StudyProgram) -> Tuple[Optional[date], Optional[str]]:
        today = date.today()
        future_exams = [
            (exam.exam_date, module.module_name)
            for module in study_program.modules
            for exam in module.exams if exam.exam_date and exam.exam_date >= today
        ]
        return min(future_exams, default=(None, None))

    @staticmethod
    def get_completed_modules(study_program: StudyProgram) -> Tuple[int, int]:
        total_modules = len(study_program.modules)
        completed_modules = sum(1 for module in study_program.modules if module.state == BESTANDEN)
        return completed_modules, total_modules

    @staticmethod
    def calculate_average_grade(study_program: StudyProgram) -> float:
        best_grades = [
            min([exam.grade for exam in module.exams if exam.grade is not None])
            for module in study_program.modules if any(exam.grade is not None for exam in module.exams)
        ]
        return round(sum(best_grades) / len(best_grades), 2) if best_grades else 0

    @staticmethod
    def calculate_credit_points(study_program: StudyProgram) -> int:
        return sum(module.ects_points for module in study_program.modules if module.state == BESTANDEN)

    @staticmethod
    def get_modules_per_semester(study_program: StudyProgram) -> Dict[int, Tuple[int, int]]:
        """
        Gibt ein Dictionary zurück, das die Anzahl bestandener und nicht bestandener Module pro Semester enthält.
        Format: {semester_id: (bestandene, nicht bestandene)}
        """
        semester_data = {}

        for module in study_program.modules:
            semester_id = module.semester_id
            is_completed = module.state == BESTANDEN

            if semester_id not in semester_data:
                semester_data[semester_id] = (0, 0)

            completed, not_completed = semester_data[semester_id]

            if is_completed:
                completed += 1
            else:
                not_completed += 1

            semester_data[semester_id] = (completed, not_completed)

        return semester_data

    @staticmethod
    def get_all_modules(study_program: StudyProgram) -> List[Tuple[int, str]]:
        """Gibt eine Liste aller Module mit ID und Namen zurück."""
        return [(module.module_id, module.module_name) for module in study_program.modules]

    @staticmethod
    def save_exam(study_program: StudyProgram, exam_data: dict):
        """Speichert eine neue Prüfung über den StudyDataWriter."""

        # Validierung: Modul-ID muss existieren
        module_ids = {module.module_id for module in study_program.modules}
        if exam_data["module_id"] not in module_ids:
            raise ValueError(f"Ungültige Modul-ID: {exam_data['module_id']}")

        # Speicherung der Prüfung
        StudyDataWriter.save_exam(exam_data)

        # Falls eine Note vorhanden ist und ≤ 4, Modul als bestanden markieren
        if exam_data["grade"] is not None:
            try:
                grade = float(exam_data["grade"])  # Sicherstellen, dass es eine Zahl ist
                if grade <= 4:
                    StudyProgramService.mark_module_as_passed(exam_data["module_id"], grade, exam_data["exam_date"])
            except ValueError:
                pass  # Falls die Note unerwartet nicht konvertierbar ist, ignorieren

        StudyProgramService.reload_study_programs()

    @staticmethod
    def mark_module_as_passed(module_id: int, grade: float, exam_date: str):
        """Setzt ein Modul auf 'BESTANDEN'."""

        # Modul als bestanden markieren und Prüfungsdatum speichern
        StudyDataWriter.update_module_status(module_id, BESTANDEN, exam_date)

    @staticmethod
    def reload_study_programs():
        """Lädt die Studienprogramme neu und gibt sie zurück."""
        study_data_loader=StudyDataLoader()
        study_data_loader.load_data()
        study_programs = study_data_loader.get_study_programs()
        return study_programs