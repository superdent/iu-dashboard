from backend.data_manager import DataManager
import logging

class Main:
    def __init__(self):
        self.data_manager = DataManager()

    def run(self):
        # Daten laden
        self.data_manager.load_data()
        
        # Weitere Aktionen, z.B. die Daten an die GUI übergeben
        logging.info("Daten laden beendet")

if __name__ == "__main__":
    app = Main()
    app.run()
