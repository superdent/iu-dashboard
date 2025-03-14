import csv
import os
import logging
from config import STUDIUM_FILE, MODULE_FILE, SEMESTER_FILE, PRUEFUNG_FILE, ZIEL_FILE
from backend.models.study_program import StudyProgram
from backend.models.module import Module
from backend.models.semester import Semester
from backend.models.exam import Exam
from backend.models.study_target import StudyTarget

class StudyDataLoader:
    def __init__(self):
        self.study_programs = []
        self.modules = []
        self.semester = []
        self.exams = []
        self.targets = []

    def load_data(self):
        """Lädt alle CSV-Dateien und behandelt Fehler."""
        self._load_file(STUDIUM_FILE, self._load_study_programs)
        self._load_file(MODULE_FILE, self._load_modules)
        self._load_file(SEMESTER_FILE, self._load_semester)
        self._load_file(PRUEFUNG_FILE, self._load_exams)
        self._load_file(ZIEL_FILE, self._load_targets)

        # Neue Zuordnungsmethoden nach dem Laden der Daten aufrufen
        self._map_semester_to_study_program()
        self._map_modules_to_semester()
        self._map_exams_to_modules()
        self._map_targets_to_study_program()

    def get_study_programs(self):
        """Gibt die Liste der geladenen Studien zurück."""
        return self.study_programs

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

    def _convert_value(self, value, data_type):
        """Konvertiert den Wert in den angegebenen Datentyp."""
        if data_type == int:
            return int(value)
        elif data_type == float:
            return float(value)
        elif data_type == str:
            return str(value)
        else:
            raise ValueError(f"Unsupported data type: {data_type}")

    def _load_study_programs(self, file_path):
        """Lädt die Studium-Daten."""
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                study_program = StudyProgram(
                    self._convert_value(row['studium_id'], int),
                    self._convert_value(row['studium_name'], str)
                )
                self.study_programs.append(study_program)

    def _load_modules(self, file_path):
        """Lädt die Modul-Daten."""
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                module = Module(
                    self._convert_value(row['modul_id'], int),
                    self._convert_value(row['modul_kuerzel'], str),
                    self._convert_value(row['modul_name'], str),
                    self._convert_value(row['semester_id'], int),
                    self._convert_value(row['ECTS_Punkte'], float),
                    self._convert_value(row['status'], str)
                )
                self.modules.append(module)

    def _load_semester(self, file_path):
        """Lädt die Semester-Daten."""
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                semester = Semester(
                    self._convert_value(row['semester_id'], int),
                    self._convert_value(row['semester_no'], int),
                    self._convert_value(row['studium_id'], int),
                    self._convert_value(row['start_datum'], str),
                    self._convert_value(row['end_datum'], str)
                )
                self.semester.append(semester)

    def _load_exams(self, file_path):
        """Lädt die Prüfungs-Daten."""
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                exam = Exam(
                    self._convert_value(row['id'], int),
                    self._convert_value(row['modul_id'], int),
                    self._convert_value(row['pruef_art'], str),
                    self._convert_value(row['pruef_datum'], str),
                    self._convert_value(row['note'], float)
                )
                self.exams.append(exam)

    def _load_targets(self, file_path):
        """Lädt die Studienziele-Daten."""
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                target = StudyTarget(
                    self._convert_value(row['ziel_id'], int),
                    self._convert_value(row['studium_id'], int),
                    self._convert_value(row['ziel_name'], str),
                    self._convert_value(row['ziel_wert'], float)
                )
                self.targets.append(target)

    def _map_semester_to_study_program(self):
        """Ordnet Semester den jeweiligen Studien basierend auf study_program_id zu."""
        for semester in self.semester:
            for study_program in self.study_programs:
                if semester.study_program_id == study_program.study_program_id:
                    study_program.semester.append(semester)

    def _map_modules_to_semester(self):
        """Ordnet Module den jeweiligen Semestern basierend auf semester_id zu."""
        for module in self.modules:
            for semester in self.semester:
                if module.semester_id == semester.semester_id:
                    semester.modules.append(module)
                    # Hier wird das Modul auch dem Studium zugeordnet
                    for study_program in self.study_programs:
                        if semester.study_program_id == study_program.study_program_id:
                            study_program.modules.append(module)

    def _map_exams_to_modules(self):
        """Ordnet Prüfungen den jeweiligen Modulen basierend auf modul_id zu."""
        for exam in self.exams:
            for module in self.modules:
                if exam.module_id == module.module_id:
                    module.exams.append(exam)

    def _map_targets_to_study_program(self):
        """Ordnet Studienziele den jeweiligen Studien basierend auf study_program_id zu."""
        for target in self.targets:
            for study_program in self.study_programs:
                if target.study_program_id == study_program.study_program_id:
                    study_program.targets.append(target)
