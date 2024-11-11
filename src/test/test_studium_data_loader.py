import unittest
from backend.studium_data_loader import StudiumDataLoader

class TestStudiumDataLoader(unittest.TestCase):
    def setUp(self):
        # Instanziiere den DataManager vor jedem Test
        self.studium_data_loader = StudiumDataLoader()

    def test_load_data(self):
        # Lade die Daten
        self.studium_data_loader.load_data()
        
        # Überprüfe, ob die Daten geladen wurden
        self.assertGreater(len(self.studium_data_loader.studien), 0, "Es wurden keine Studiengänge geladen")
        self.assertGreater(len(self.studium_data_loader.module), 0, "Es wurden keine Module geladen")
        self.assertGreater(len(self.studium_data_loader.semester), 0, "Es wurden keine Semester geladen")
        # Wenn Prüfungen vorhanden sind, prüfe, ob diese geladen wurden
        if self.studium_data_loader.pruefungen:
            self.assertGreater(len(self.studium_data_loader.pruefungen), 0, "Es wurden keine Prüfungen geladen")

    def test_studium_data(self):
        # Überprüfe, ob die Studium-Daten korrekt geladen wurden
        self.studium_data_loader.load_data()
        studium = self.studium_data_loader.studien[0]
        self.assertEqual(studium.studium_name, "Angewandte Künstliche Intelligenz", "Studium Name ist falsch")

if __name__ == '__main__':
    unittest.main()
