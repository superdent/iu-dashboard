import unittest
from backend.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        # Instanziiere den DataManager vor jedem Test
        self.data_manager = DataManager()

    def test_load_data(self):
        # Lade die Daten
        self.data_manager.load_data()
        
        # Überprüfe, ob die Daten geladen wurden
        self.assertGreater(len(self.data_manager.studien), 0, "Es wurden keine Studiengänge geladen")
        self.assertGreater(len(self.data_manager.module), 0, "Es wurden keine Module geladen")
        self.assertGreater(len(self.data_manager.semester), 0, "Es wurden keine Semester geladen")
        # Wenn Prüfungen vorhanden sind, prüfe, ob diese geladen wurden
        if self.data_manager.pruefungen:
            self.assertGreater(len(self.data_manager.pruefungen), 0, "Es wurden keine Prüfungen geladen")

    def test_studium_data(self):
        # Überprüfe, ob die Studium-Daten korrekt geladen wurden
        self.data_manager.load_data()
        studium = self.data_manager.studien[0]
        self.assertEqual(studium.studium_name, "Angewandte Künstliche Intelligenz", "Studium Name ist falsch")

if __name__ == '__main__':
    unittest.main()
