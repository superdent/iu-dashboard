import csv
import os
from config import PRUEFUNG_FILE, MODULE_FILE


class StudyDataWriter:
    @staticmethod
    def save_exam(exam_data: dict):
        """Speichert eine neue Prüfung in die CSV-Datei."""

        # Prüfen, ob die Datei existiert und die höchste ID ermitteln
        next_id = 1
        if os.path.exists(PRUEFUNG_FILE):
            with open(PRUEFUNG_FILE, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                ids = [int(row["id"]) for row in reader if row["id"].isdigit()]
                if ids:
                    next_id = max(ids) + 1  # Neue ID um +1 erhöhen

        # Neue Zeile vorbereiten
        new_exam = {
            "id": next_id,
            "modul_id": exam_data["module_id"],
            "pruef_art": exam_data["exam_type"],
            "pruef_datum": exam_data["exam_date"],
            "note": exam_data["grade"] if exam_data["grade"] else ""
        }

        # Schreiben der neuen Zeile in die CSV-Datei
        file_exists = os.path.exists(PRUEFUNG_FILE)
        with open(PRUEFUNG_FILE, 'a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "modul_id", "pruef_art", "pruef_datum", "note"],
                                    delimiter=';')
            if not file_exists:
                writer.writeheader()  # Kopfzeile nur schreiben, wenn Datei neu erstellt wird
            writer.writerow(new_exam)

    @staticmethod
    def update_module_status(module_id: int, new_status: str, exam_date: str = None):
        """Aktualisiert den Status eines Moduls in der CSV-Datei.

        Falls `exam_date` gesetzt ist, wird es als Prüfungsdatum gespeichert.
        """

        updated_modules = []
        file_exists = os.path.exists(MODULE_FILE)

        if file_exists:
            with open(MODULE_FILE, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    if int(row["modul_id"]) == module_id:
                        row["status"] = new_status  # Status aktualisieren
                        if exam_date:
                            row["pruefungsdatum"] = exam_date  # Prüfungsdatum setzen, falls übergeben
                    updated_modules.append(row)

        # Änderungen in die Datei zurückschreiben
        with open(MODULE_FILE, 'w', encoding='utf-8', newline='') as file:
            fieldnames = ["modul_id", "modul_kuerzel", "modul_name", "semester_id", "ECTS_Punkte", "status",
                          "pruefungsdatum"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(updated_modules)
