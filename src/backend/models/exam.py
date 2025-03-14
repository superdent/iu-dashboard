class Exam:
    def __init__(self, id, module_id, type_of_exam, exam_date, grade):
        self.id = id
        self.module_id = module_id
        self.type_of_exam = type_of_exam  # Art der Prüfung (z.B. Klausur, mündlich)
        self.exam_date = exam_date  # Datum der Prüfung
        self.grade = grade  # Abschlussnote der Prüfung
