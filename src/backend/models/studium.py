from backend.models.modul import * 

class Studium:
    def __init__(self, studium_id, studium_name):
        self.studium_id = studium_id
        self.studium_name = studium_name
        self.semester = []  # Liste von Semestern, die dem Studium zugeordnet sind
        self.ziele = []  # Liste von Studienzielen, die dem Studium zugeordnet sind
        self.module = []  # Liste von Modulen, die dem Studium zugeordnet sind

    def berechne_durchschnittsnote(self):
        # Liste für die besten Noten pro Modul, wird später für den Durchschnitt benötigt
        beste_noten = []

        for modul in self.module:
            noten = [pruefung.note for pruefung in modul.pruefungen if pruefung.note is not None]
            
            # Wenn das Modul Noten hat, die beste (niedrigste) Note wählen
            if noten:
                beste_note = min(noten)
                beste_noten.append(beste_note)

        # Wenn es keine Noten gibt, None zurückgeben
        if not beste_noten:
            return 0

        # Durchschnitt berechnen und auf 2 Dezimalstellen runden
        durchschnitt = sum(beste_noten) / len(beste_noten)
        return round(durchschnitt, 2)
    
    def berechne_credit_points(self):
        return sum([modul.ects_punkte for modul in self.module if modul.status == BESTANDEN])
