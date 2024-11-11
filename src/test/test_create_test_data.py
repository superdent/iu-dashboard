from backend.models.studium import Studium
from backend.models.modul import Modul
from backend.models.pruefung import Pruefung

class TestCreateTestData:

    @staticmethod
    def erstelle_pruefung(id, modul_id, pruef_art, pruef_datum, note):
        pruefung = Pruefung(id, modul_id, pruef_art, pruef_datum, note)
        return pruefung

    @staticmethod
    def erstelle_modul(id, modul_kuerzel, modul_name, semester_id, ects_punkte, status, pruefungen):
        modul = Modul(id, modul_kuerzel, modul_name, semester_id, ects_punkte, status)
        for pruefung_daten in pruefungen:
            modul.pruefungen.append(TestCreateTestData.erstelle_pruefung(*pruefung_daten))
        return modul

    @staticmethod
    def erstelle_studium(studium_id, studium_name, module):
        studium = Studium(studium_id, studium_name)
        for modul_daten in module:
            studium.module.append(TestCreateTestData.erstelle_modul(*modul_daten))
        return studium
