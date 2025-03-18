from backend.models.study_program import StudyProgram
from backend.models.module import *

from datetime import date
from typing import Optional, Tuple

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

