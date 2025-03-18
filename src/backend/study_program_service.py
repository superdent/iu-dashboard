from backend.models.study_program import StudyProgram
from backend.models.module import *


class StudyProgramService:
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
