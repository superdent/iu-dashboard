class Pruefung:
    def __init__(self, id, modul_id, pruef_art, pruef_datum, note):
        self.id = id
        self.modul_id = modul_id
        self.pruef_art = pruef_art  # Art der Prüfung (z.B. Klausur, mündlich)
        self.pruef_datum = pruef_datum  # Datum der Prüfung
        self.note = note  # Abschlussnote der Prüfung
