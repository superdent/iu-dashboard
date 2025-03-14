from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

class CreditPointsWidget(QWidget):
    def __init__(self, study_program):
        super().__init__()

        credit_points = int(study_program.calculate_credit_points())
        
        # Widget Layout
        self.layout = QVBoxLayout()

        # Rahmen erstellen, um beide Labels gemeinsam zu umschließen
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(2)
        
        # Layout für den Rahmen
        frame_layout = QVBoxLayout(self.frame)

        # Spacer hinzufügen, um die CreditPoints eher mittig zu platzieren
        frame_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Label zur Anzeige der Credit Points
        self.label_ects = QLabel(f"{credit_points:d}")
        self.label_ects.setAlignment(Qt.AlignCenter)
        self.label_ects.setStyleSheet("font-size: 72px; font-weight: bold; color: black;")
        frame_layout.addWidget(self.label_ects)

        # Spacer hinzufügen, um den Text nach unten zu verschieben
        frame_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Label zur Anzeige der Bezeichnung
        self.label_title = QLabel("Credit Points")
        self.label_title.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.label_title.setStyleSheet("font-size: 24px; color: black;")  
        frame_layout.addWidget(self.label_title)

        # Setze das Rahmenlayout
        self.layout.addWidget(self.frame)
        self.setLayout(self.layout)

        # Farbe des Rahmens
        self.frame.setStyleSheet("background-color: #E9EBCB; border-radius: 15px;")  # Hintergrund in Grün

        # Styling
        self.setStyleSheet("padding: 10px;")

    def update_credit_points(self, ects, target_value):
        """Aktualisiert die angezeigten ECTS."""
        self.label_ects.setText(f"{ects:d}")
