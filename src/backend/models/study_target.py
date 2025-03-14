class StudyTarget:
    def __init__(self, target_id, study_program_id, target_name, target):
        self.target_id = target_id
        self.study_program_id = study_program_id  # Referenz auf das zugehörige Studium
        self.target_name = target_name  # Name des Ziels (z.B. "Durchschnittsnote")
        self.target = target  # Wert des Ziels (z.B. 2.0)
