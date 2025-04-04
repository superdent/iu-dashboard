import unittest

from backend.study_data_loader import StudyDataLoader


class TestStudyDataLoader(unittest.TestCase):
    def setUp(self):
        # Instanziiere den DataManager vor jedem Test
        self.study_data_loader = StudyDataLoader()

    def test_load_data(self):
        # when
        self.study_data_loader.load_data()
        
        # then
        self.assertGreater(len(self.study_data_loader.study_programs), 0, "Es wurden keine Studiengänge geladen")
        self.assertGreater(len(self.study_data_loader.modules), 0, "Es wurden keine Module geladen")
        self.assertGreater(len(self.study_data_loader.semester), 0, "Es wurden keine Semester geladen")
        if self.study_data_loader.exams:
            self.assertGreater(len(self.study_data_loader.exams), 0, "Es wurden keine Prüfungen geladen")

    def test_study_program_fields_present (self):
        # when
        self.study_data_loader.load_data()
        study_program = self.study_data_loader.study_programs[0]

        # then
        self.assertIsInstance(study_program.study_program_id, int)
        self.assertIsInstance(study_program.study_program_name, str)

if __name__ == '__main__':
    unittest.main()
