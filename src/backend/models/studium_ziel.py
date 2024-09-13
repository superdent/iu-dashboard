class StudiumZiel:
    def __init__(self, ziel_id, studium_id, ziel_name, ziel_wert):
        self.ziel_id = ziel_id
        self.studium_id = studium_id  # Referenz auf das zugehörige Studium
        self.ziel_name = ziel_name  # Name des Ziels (z.B. "Durchschnittsnote")
        self.ziel_wert = ziel_wert  # Wert des Ziels (z.B. 2.0)
