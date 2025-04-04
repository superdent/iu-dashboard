class StudyProgram:
    def __init__(self, study_program_id, study_program_name):
        self.study_program_id = study_program_id
        self.study_program_name = study_program_name
        self.semester = []  # Liste von Semestern, die dem Studium zugeordnet sind
        self.targets = []  # Liste von Studienzielen, die dem Studium zugeordnet sind
        self.modules = []  # Liste von Modulen, die dem Studium zugeordnet sind
