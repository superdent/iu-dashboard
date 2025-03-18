import logging
import sys

from PyQt5.QtWidgets import QApplication

from backend.study_data_loader import StudyDataLoader
from frontend.main_window import MainApp


class Main:
    def __init__(self):
        self.study_data_loader = StudyDataLoader()

    def run(self):
        # Daten laden
        self.study_data_loader.load_data()
        study_programs = self.study_data_loader.get_study_programs()
        logging.info("Daten laden beendet")

        # Start der GUI
        app = QApplication(sys.argv)
        main_window = MainApp(study_programs)
        main_window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = Main()
    app.run()

