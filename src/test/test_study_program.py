import unittest
from backend.models.study_program import Studium  
from test_create_test_data import TestCreateTestData

class Pruefung:
    def __init__(self, note):
        self.note = note

class Modul:
    def __init__(self):
        self.pruefungen = []

class TestStudiumDurchschnitt(unittest.TestCase):
    def setUp(self):
        # Testdaten für Studium erstellen, inklusive Modulinformationen
        self.studium = TestCreateTestData.erstelle_studium(
            1, "Teststudium",
            [
                (1, "AI", "Artificial Intelligence", 1, 5, "bestanden", [(1, 1, 'Klausur', '01.02.2024', 4.7), (2, 1, 'Klausur', '01.04.2024', 2.3)]),  # Modul 1
                (2, "ML", "Machine Learning", 2, 5, "bestanden", [(3, 2, 'Klausur', '01.03.2024', 1.3)]),                                              # Modul 2
                (3, "CV", "Computer Vision", 3, 5, "bestanden", [(4, 3, 'Workbook', '10.02.2024', 4.3), (5, 1, 'Workbook', '02.05.2024', 2.3)])        # Modul 3
            ]
        )


    def test_berechne_durchschnittsnote(self):
        # Durchschnitt berechnen und überprüfen
        durchschnitt = self.studium.berechne_durchschnittsnote()
        self.assertEqual(durchschnitt, 1.97)  # Erwarteter Durchschnitt

if __name__ == "__main__":
    unittest.main()
