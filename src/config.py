import logging
import os

# Logging konfigurieren
LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)

# Basisverzeichnis berechnen
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Verzeichnis für Input-Daten
DATA_DIR = os.path.join(BASE_DIR, 'data', 'input')

# Dateien
STUDIUM_FILE = os.path.join(DATA_DIR, 'studium.csv')
MODULE_FILE = os.path.join(DATA_DIR, 'modul.csv')
SEMESTER_FILE = os.path.join(DATA_DIR, 'semester.csv')
PRUEFUNG_FILE = os.path.join(DATA_DIR, 'pruefung.csv')
ZIEL_FILE = os.path.join(DATA_DIR, 'studiumziel.csv')