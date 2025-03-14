import unittest
from backend.study_data_loader import StudyDataLoader

class TestStudiumDataLoader(unittest.TestCase):
    def setUp(self):
        # Instanziiere den DataManager vor jedem Test
        self.study_data_loader = StudyDataLoader()

    def test_load_data(self):
        # Lade die Daten
        self.study_data_loader.load_data()
        
        # Überprüfe, ob die Daten geladen wurden
        self.assertGreater(len(self.study_data_loader.study_programs), 0, "Es wurden keine Studiengänge geladen")
        self.assertGreater(len(self.study_data_loader.modules), 0, "Es wurden keine Module geladen")
        self.assertGreater(len(self.study_data_loader.semester), 0, "Es wurden keine Semester geladen")
        # Wenn Prüfungen vorhanden sind, prüfe, ob diese geladen wurden
        if self.study_data_loader.exams:
            self.assertGreater(len(self.study_data_loader.exams), 0, "Es wurden keine Prüfungen geladen")

    def test_studium_data(self):
        # Überprüfe, ob die Studium-Daten korrekt geladen wurden
        self.study_data_loader.load_data()
        studium = self.study_data_loader.study_programs[0]
        self.assertEqual(studium.study_program_name, "Angewandte Künstliche Intelligenz", "Studium Name ist falsch")

if __name__ == '__main__':
    unittest.main()
