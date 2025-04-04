import unittest
from datetime import date, timedelta
from backend.study_program_service import StudyProgramService
from backend.models.study_program import StudyProgram
from backend.models.module import Module
from backend.models.exam import Exam
from test.test_create_test_data import TestCreateTestData


class TestStudyProgramService(unittest.TestCase):

    def test_get_next_exam_date(self):
        # given
        today = date.today()
        future_date = today + timedelta(days=10)
        past_date = today - timedelta(days=10)
        m1 = Module(1, "M01", "Modul 1", 1, 5, "offen")
        m2 = Module(2, "M02", "Modul 2", 1, 5, "offen")
        m1.exams = [Exam(1, 1, "Klausur", past_date, 1.7)]
        m2.exams = [Exam(2, 2, "Hausarbeit", future_date, None)]
        program = StudyProgram(1, "Testprogramm")
        program.modules = [m1, m2]

        # when
        result = StudyProgramService.get_next_exam_date(program)

        # then
        self.assertEqual(result, (future_date, "Modul 2"))

    def test_get_completed_modules(self):
        # given
        studium = TestCreateTestData.erstelle_standard_studium()

        # when
        result = StudyProgramService.get_completed_modules(studium)

        # then
        self.assertEqual(result, (2, 5))

    def test_calculate_average_grade(self):
        # given
        studium = TestCreateTestData.erstelle_standard_studium()

        # when
        result = StudyProgramService.calculate_average_grade(studium)

        # then
        self.assertEqual(result, 2.87)

    def test_get_study_target_none(self):
        # given
        studium = TestCreateTestData.erstelle_standard_studium()

        # when
        result = StudyProgramService.get_study_target(studium, 999)  # beliebige Ziel-ID

        # then
        self.assertIsNone(result)

    def test_get_modules_per_semester(self):
        # given
        studium = TestCreateTestData.erstelle_standard_studium()

        # when
        result = StudyProgramService.get_modules_per_semester(studium)

        # then
        expected = {
            1: (2, 0, 0),  # M01, M02 → bestanden
            2: (0, 0, 2),  # Beide Module offen
            3: (0, 1, 0),  # M05 → nicht bestanden
        }
        self.assertEqual(result, expected)

    def test_get_all_modules(self):
        # given
        studium = TestCreateTestData.erstelle_standard_studium()

        # when
        result = StudyProgramService.get_all_modules(studium)

        # then
        self.assertEqual(len(result), 5)
        self.assertIn((1, "Modul 1"), result)

    def test_get_exams(self):
        # given
        studium = TestCreateTestData.erstelle_standard_studium()

        # when
        result = StudyProgramService.get_exams(studium)

        # then
        self.assertEqual(len(result), 5)  # 5 Prüfungen laut Testdaten
        self.assertTrue(all("exam_id" in exam for exam in result))
        self.assertTrue(all("exam_date" in exam for exam in result))
        self.assertTrue(result[0]["exam_date"] >= result[1]["exam_date"])  # Sortierung absteigend

