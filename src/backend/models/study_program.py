from backend.models.module import * 

class StudyProgram:
    def __init__(self, study_program_id, study_program_name):
        self.study_program_id = study_program_id
        self.study_program_name = study_program_name
        self.semester = []  # Liste von Semestern, die dem Studium zugeordnet sind
        self.targets = []  # Liste von Studienzielen, die dem Studium zugeordnet sind
        self.modules = []  # Liste von Modulen, die dem Studium zugeordnet sind

    def calculate_average_grade(self):
        # Liste für die besten Noten pro Modul, wird später für den Durchschnitt benötigt
        best_grades = []

        for module in self.modules:
            grades = [exam.grade for exam in module.exams if exam.grade is not None]
            
            # Wenn das Modul Noten hat, die beste (niedrigste) Note wählen
            if grades:
                best_grade = min(grades)
                best_grades.append(best_grade)

        # Wenn es keine Noten gibt, None zurückgeben
        if not best_grades:
            return 0

        # Durchschnitt berechnen und auf 2 Dezimalstellen runden
        durchschnitt = sum(best_grades) / len(best_grades)
        return round(durchschnitt, 2)
    
    def calculate_credit_points(self):
        return sum([module.ects_points for module in self.modules if module.state == BESTANDEN])
