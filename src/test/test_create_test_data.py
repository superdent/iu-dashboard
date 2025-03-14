from backend.models.study_program import StudyProgram
from backend.models.module import Module
from backend.models.exam import Exam

class TestCreateTestData:

    @staticmethod
    def erstelle_exam(id, modul_id, pruef_art, pruef_datum, note):
        exam = Exam(id, modul_id, pruef_art, pruef_datum, note)
        return exam

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
