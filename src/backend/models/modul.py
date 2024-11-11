class Modul:
    def __init__(self, modul_id, modul_kuerzel, modul_name, semester_id, ects_punkte, status):
        self.modul_id = modul_id
        self.modul_kuerzel = modul_kuerzel
        self.modul_name = modul_name
        self.semester_id = semester_id
        self.ects_punkte = ects_punkte
        self.status = status
        self.pruefungen = [] 

