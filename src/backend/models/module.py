BESTANDEN = "bestanden"
NICHT_BESTANDEN = "nicht bestanden"
NICHT_BEGONNEN = "offen"
IN_ARBEIT = "in Arbeit"

class Module:
    def __init__(self, module_id, module_code, module_name, semester_id, ects_points, state):
        self.module_id = module_id
        self.module_code = module_code
        self.module_name = module_name
        self.semester_id = semester_id
        self.ects_points = ects_points
        self.state = state
        self.exams = [] 

