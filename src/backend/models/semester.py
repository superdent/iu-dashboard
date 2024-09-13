class Semester:
    def __init__(self, semester_id, semester_no, studium_id, start_datum, end_datum):
        self.semester_id = semester_id
        self.semester_no = semester_no  # Nummer des Semesters (z.B. 1, 2, 3)
        self.studium_id = studium_id  # Referenz auf das zugehörige Studium
        self.start_datum = start_datum
        self.end_datum = end_datum
        self.module = []  # Liste der Module für dieses Semester
