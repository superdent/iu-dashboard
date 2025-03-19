from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame, QSpacerItem, QSizePolicy


class CreditPointsWidget(QWidget):
    def __init__(self, credit_points):
        super().__init__()

        credit_points=int(credit_points)

        # Widget Layout
        self.layout = QVBoxLayout()

        # Rahmen erstellen, um beide Labels gemeinsam zu umschließen
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(2)
        
        # Layout für den Rahmen
        frame_layout = QVBoxLayout(self.frame)

        # Spacer hinzufügen, um die CreditPoints eher mittig zu platzieren
        frame_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Label zur Anzeige der Credit Points
        self.label_ects = QLabel(f"{credit_points:d}")
        self.label_ects.setAlignment(Qt.AlignCenter)
        self.label_ects.setStyleSheet("font-size: 48px; font-weight: bold; color: black;")
        frame_layout.addWidget(self.label_ects)

        # Spacer hinzufügen, um den Text nach unten zu verschieben
        frame_layout.addSpacerItem(QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Label zur Anzeige der Bezeichnung
        self.label_title = QLabel("Credit Points")
        self.label_title.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.label_title.setStyleSheet("font-size: 18px; color: black;")
        frame_layout.addWidget(self.label_title)

        # Setze das Rahmenlayout
        self.layout.addWidget(self.frame)
        self.setLayout(self.layout)

        # Hintergrund in Grün
        self.frame.setStyleSheet("background-color: #FFF9C4; border-radius: 15px;")

        # Styling
        self.setStyleSheet("padding: 5px;")

    def update_credit_points(self, ects):
        """Aktualisiert die angezeigten ECTS."""
        self.label_ects.setText(f"{int(ects)}")

