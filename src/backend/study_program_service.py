from backend.models.study_program import StudyProgram
from backend.models.module import BESTANDEN, NICHT_BESTANDEN, NICHT_BEGONNEN

from datetime import date
from typing import Optional, Tuple, Dict, List

from backend.study_data_loader import StudyDataLoader
from backend.study_data_writer import StudyDataWriter
from config import ZIEL_ID_DURCHSCHNITTSNOTE


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
    def get_target_average_grade(study_program):
        """Gibt das Studienziel für die Durchschnittsnote zurück, falls vorhanden."""
        return StudyProgramService.get_study_target(study_program, ZIEL_ID_DURCHSCHNITTSNOTE)

    @staticmethod
    def get_study_target(study_program, target_id: int):
        """Gibt den Wert eines Studienziels anhand der Ziel-ID zurück, falls vorhanden."""
        for target in study_program.targets:
            if target.target_id == target_id:
                return target.target
        return None  # Falls kein Ziel mit dieser ID existiert

    @staticmethod
    def get_modules_per_semester(study_program: StudyProgram) -> Dict[int, Tuple[int, int, int]]:
        """
        Gibt ein Dictionary zurück, das die Anzahl bestandener, nicht bestandener und nicht begonnener Module pro Semester enthält.
        Format: {semester_id: (bestandene, nicht bestandene, nicht begonnene)}
        """
        semester_data = {}

        for module in study_program.modules:
            semester_id = module.semester_id
            is_completed = module.state == BESTANDEN
            is_failed = module.state == NICHT_BESTANDEN
            is_not_started = module.state == NICHT_BEGONNEN

            if semester_id not in semester_data:
                semester_data[semester_id] = (0, 0, 0)

            completed, not_completed, not_started = semester_data[semester_id]

            if is_completed:
                completed += 1
            elif is_failed:
                not_completed += 1
            elif is_not_started:
                not_started += 1

            semester_data[semester_id] = (completed, not_completed, not_started)

        return semester_data

    @staticmethod
    def get_all_modules(study_program: StudyProgram) -> List[Tuple[int, str]]:
        """Gibt eine Liste aller Module mit ID und Namen zurück."""
        return [(module.module_id, module.module_name) for module in study_program.modules]

    @staticmethod
    def get_exams(study_program: StudyProgram) -> List[dict]:
        """ Liefert die Pruefungen des Studienprogramms als Liste von Dicts."""
        exams = []
        for module in study_program.modules:
            for exam in module.exams:
                exams.append({
                    "exam_id": exam.id,
                    "module_id": module.module_id,
                    "module_name": module.module_name,
                    "exam_type": exam.type_of_exam,
                    "exam_date": exam.exam_date,
                    "grade": exam.grade
                })
        exams.sort(key=lambda x: x["exam_date"] or date.min, reverse=True)
        return exams

    @staticmethod
    def save_exam(study_program: StudyProgram, exam_data: dict):
        """Speichert eine neue Prüfung über den StudyDataWriter."""
        StudyDataWriter.save_exam(exam_data)
        StudyProgramService._process_exam_data(exam_data)
        StudyProgramService.reload_study_programs()

    @staticmethod
    def update_exam(study_program: StudyProgram, exam_data: dict):
        """Aktualisiert eine bestehende Prüfung über den StudyDataWriter."""
        StudyDataWriter.update_exam(exam_data)
        StudyProgramService._process_exam_data(exam_data)
        StudyProgramService.reload_study_programs()

    @staticmethod
    def _process_exam_data(exam_data: dict):
        """Verarbeitet Noten-Logik und aktualisiert ggf. den Modulstatus."""

        if exam_data["grade"] is not None:
            try:
                grade = float(exam_data["grade"])
                if grade <= 4:
                    StudyProgramService.mark_module_as_passed(
                        exam_data["module_id"], grade, exam_data["exam_date"]
                    )
                else:
                    StudyProgramService.mark_module_as_failed(
                        exam_data["module_id"], grade, exam_data["exam_date"]
                    )
            except ValueError:
                pass  # Ungültige Note ignorieren

    @staticmethod
    def mark_module_as_passed(module_id: int, grade: float, exam_date: str):
        """Setzt ein Modul auf 'BESTANDEN'."""

        # Modul als bestanden markieren und Prüfungsdatum speichern
        StudyDataWriter.update_module_status(module_id, BESTANDEN, exam_date)

    @staticmethod
    def mark_module_as_failed(module_id: int, grade: float, exam_date: str):
        """Setzt ein Modul auf 'NICHT_BESTANDEN'."""

        # Modul als nicht bestanden markieren und Prüfungsdatum speichern
        StudyDataWriter.update_module_status(module_id, NICHT_BESTANDEN, exam_date)

    @staticmethod
    def reload_study_programs():
        """Lädt die Studienprogramme neu und gibt sie zurück."""
        study_data_loader=StudyDataLoader()
        study_data_loader.load_data()
        study_programs = study_data_loader.get_study_programs()
        return study_programs
