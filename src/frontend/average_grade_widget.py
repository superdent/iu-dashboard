from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame, QSpacerItem, QSizePolicy


class AverageGradeWidget(QWidget):
    def __init__(self, average_grade):
        super().__init__()

        target = 2.5

        # Widget Layout
        self.layout = QVBoxLayout()

        # Rahmen erstellen, um beide Labels gemeinsam zu umschließen
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(2)
        
        # Layout für den Rahmen
        frame_layout = QVBoxLayout(self.frame)

        # Spacer hinzufügen, um die Note eher mittig zu platzieren
        frame_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Label zur Anzeige der Note
        self.label_note = QLabel(f"{average_grade:.2f}")
        self.label_note.setAlignment(Qt.AlignCenter)
        self.label_note.setStyleSheet("font-size: 48px; font-weight: bold; color: black;")
        frame_layout.addWidget(self.label_note)

        # Spacer hinzufügen, um den Text nach unten zu verschieben
        frame_layout.addSpacerItem(QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Label zur Anzeige der Durchschnittsnote
        self.label_title = QLabel("⌀-Note")
        self.label_title.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.label_title.setStyleSheet("font-size: 18px; color: black;")
        frame_layout.addWidget(self.label_title)

        # Setze das Rahmenlayout
        self.layout.addWidget(self.frame)
        self.setLayout(self.layout)

        # Farbe des Rahmens basierend auf der Note und dem Schwellwert setzen
        self.set_note_color(average_grade, target)

        # Styling
        self.setStyleSheet("padding: 5px;")

    def update_grade(self, new_grade, target):
        """Aktualisiert die angezeigte Durchschnittsnote."""
        self.label_note.setText(f"{new_grade:.2f}")
        self.set_note_color(new_grade, target)

    def set_note_color(self, grade, target):
        """Setzt die Hintergrundfarbe des Rahmens abhängig vom Wert und dem Schwellwert."""
        if grade <= target:
            self.frame.setStyleSheet("background-color: #D9F2D0; border-radius: 15px;")  # Hintergrund in Grün
        else:
            self.frame.setStyleSheet("background-color: #F5C5AD; border-radius: 15px;")  # Hintergrund in Rot
