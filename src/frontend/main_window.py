import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from backend.studium_data_loader import StudiumDataLoader
from frontend.notenschnitt_widget import NotenschnittWidget
import logging

class MainApp(QMainWindow):
    def __init__(self, studien):
        super().__init__()


        # Fenster-Konfiguration
        self.setWindowTitle("Studien Dashboard")
        self.setGeometry(100, 100, 800, 600)

        # Layout und Widgets
        self.layout = QVBoxLayout()

        studium = studien[0]  # Beispiel: Nimm das erste Studium
        self.notenschnitt_widget = NotenschnittWidget(studium)  # Neues Widget erstellen
        self.layout.addWidget(self.notenschnitt_widget)  # Neues Widget zum Layout hinzufügen

        # Zentrales Widget
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def load_data(self):
        try:
            # Daten laden
            self.studium_data_loader.load_data()
            self.label.setText("Daten erfolgreich geladen!")
            logging.info("Daten erfolgreich geladen")
        except Exception as e:
            self.label.setText("Fehler beim Laden der Daten")
            logging.error(f"Fehler beim Laden der Daten: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())
