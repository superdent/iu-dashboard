from backend.studium_data_loader import StudiumDataLoader
from frontend.main_window import MainApp
from PyQt5.QtWidgets import QApplication
import logging
import sys

class Main:
    def __init__(self):
        self.studium_data_loader = StudiumDataLoader()

    def run(self):
        # Daten laden
        self.studium_data_loader.load_data()
        studien = self.studium_data_loader.get_studien()
        logging.info("Daten laden beendet")

        # Start der GUI
        app = QApplication(sys.argv)
        main_window = MainApp(studien)
        main_window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = Main()
    app.run()

