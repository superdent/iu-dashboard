import csv
import os
import logging
from config import STUDIUM_FILE, MODULE_FILE, SEMESTER_FILE, PRUEFUNG_FILE, ZIEL_FILE
from backend.models.studium import Studium
from backend.models.modul import Modul
from backend.models.semester import Semester
from backend.models.pruefung import Pruefung
from backend.models.studium_ziel import StudiumZiel

class DataManager:
    def __init__(self):
        self.studien = []
        self.module = []
        self.semester = []
        self.pruefungen = []
        self.ziele = []

    def load_data(self):
        """Lädt alle CSV-Dateien und behandelt Fehler."""
        self._load_file(STUDIUM_FILE, self._load_studium)
        self._load_file(MODULE_FILE, self._load_module)
        self._load_file(SEMESTER_FILE, self._load_semester)
        self._load_file(PRUEFUNG_FILE, self._load_pruefungen)
        self._load_file(ZIEL_FILE, self._load_ziele)

    def _load_file(self, file_path, load_function):
        """Allgemeine Funktion zum Laden von Dateien mit Fehlerbehandlung."""
        if os.path.exists(file_path):
            try:
                load_function(file_path)
                logging.info(f"Datei erfolgreich geladen: {file_path}")
            except Exception as e:
                logging.error(f"Fehler beim Laden der Datei {file_path}: {e}")
        else:
            logging.warning(f"Datei nicht gefunden: {file_path}. Überspringe den Import.")

    def _load_studium(self, file_path):
        """Lädt die Studium-Daten."""
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                studium = Studium(row['studium_id'], row['studium_name'])
                self.studien.append(studium)

    def _load_module(self, file_path):
        """Lädt die Modul-Daten."""
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                modul = Modul(row['modul_id'], row['modul_kuerzel'], row['modul_name'], 
                              row['semester_id'], row['ECTS_Punkte'], row['status'], row['pruefungsdatum'])
                self.module.append(modul)

    def _load_semester(self, file_path):
        """Lädt die Semester-Daten."""
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                semester = Semester(row['semester_id'], row['semester_no'], row['studium_id'], 
                                    row['start_datum'], row['end_datum'])
                self.semester.append(semester)

    def _load_pruefungen(self, file_path):
        """Lädt die Prüfungs-Daten."""
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                pruefung = Pruefung(row['id'], row['modul_id'], row['pruef_art'], 
                                    row['pruef_datum'], row['note'])
                self.pruefungen.append(pruefung)

    def _load_ziele(self, file_path):
        """Lädt die Studienziele-Daten."""
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                ziel = StudiumZiel(row['ziel_id'], row['studium_id'], row['ziel_name'], row['ziel_wert'])
                self.ziele.append(ziel)
