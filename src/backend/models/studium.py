class Studium:
    def __init__(self, studium_id, studium_name):
        self.studium_id = studium_id
        self.studium_name = studium_name
        self.module = []  # Liste von Modulen, die dem Studium zugeordnet sind
