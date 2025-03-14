class Semester:
    def __init__(self, semester_id, semester_no, study_program_id, start_date, end_date):
        self.semester_id = semester_id
        self.semester_no = semester_no  # Nummer des Semesters (z.B. 1, 2, 3)
        self.study_program_id = study_program_id  # Referenz auf das zugehörige Studium
        self.start_date = start_date
        self.end_date = end_date
        self.modules = []  # Liste der Module für dieses Semester
