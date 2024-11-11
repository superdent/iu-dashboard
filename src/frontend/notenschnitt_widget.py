from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

class NotenschnittWidget(QWidget):
    def __init__(self, studium):
        super().__init__()

        durchschnittsnote = studium.berechne_durchschnittsnote()
        schwellwert = 2.5

        # Widget Layout
        self.layout = QVBoxLayout()

        # Rahmen erstellen, um beide Labels gemeinsam zu umschließen
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(2)
        
        # Layout für den Rahmen
        frame_layout = QVBoxLayout(self.frame)

        # Spacer hinzufügen, um die Note eher mittig zu platzieren
        frame_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Label zur Anzeige der Note
        self.label_note = QLabel(f"{durchschnittsnote:.2f}")
        self.label_note.setAlignment(Qt.AlignCenter)
        self.label_note.setStyleSheet("font-size: 72px; font-weight: bold; color: white;")  # Text in weiß
        frame_layout.addWidget(self.label_note)

        # Spacer hinzufügen, um den Text nach unten zu verschieben
        frame_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Label zur Anzeige der Durchschnittsnote
        self.label_title = QLabel("⌀-Note")
        self.label_title.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.label_title.setStyleSheet("font-size: 24px; color: white;")  # Text in weiß
        frame_layout.addWidget(self.label_title)

        # Setze das Rahmenlayout
        self.layout.addWidget(self.frame)
        self.setLayout(self.layout)

        # Farbe des Rahmens basierend auf der Note und dem Schwellwert setzen
        self.set_note_color(durchschnittsnote, schwellwert)

        # Styling
        self.setStyleSheet("padding: 10px;")

    def update_note(self, neue_note, schwellwert):
        """Aktualisiert die angezeigte Durchschnittsnote."""
        self.label_note.setText(f"{neue_note:.2f}")
        self.set_note_color(neue_note, schwellwert)

    def set_note_color(self, note, schwellwert):
        """Setzt die Hintergrundfarbe des Rahmens abhängig vom Wert und dem Schwellwert."""
        if note <= schwellwert:
            self.frame.setStyleSheet("background-color: green;")  # Hintergrund in Grün
        else:
            self.frame.setStyleSheet("background-color: red;")  # Hintergrund in Rot
