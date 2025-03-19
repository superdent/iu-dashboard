from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame, QSpacerItem, QSizePolicy
from datetime import date

class NextExamWidget(QWidget):
    def __init__(self, next_exam: tuple[date | None, str | None]):
        super().__init__()

        exam_date, module_name = next_exam

        # Widget Layout
        self.layout = QVBoxLayout()

        # Rahmen erstellen
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(2)

        # Layout für den Rahmen
        frame_layout = QVBoxLayout(self.frame)

        # Spacer oben
        frame_layout.addSpacerItem(QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Label 'Naechste Pruefung'
        self.label_nextexam = QLabel("Nächste Prüfung")
        self.label_nextexam.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.label_nextexam.setStyleSheet("font-size: 18px; color: black;")
        frame_layout.addWidget(self.label_nextexam)

        # Label für das Datum
        self.label_date = QLabel(exam_date.strftime("%d.%m.%Y") if exam_date else "-")
        self.label_date.setAlignment(Qt.AlignCenter)
        self.label_date.setStyleSheet("font-size: 36px; font-weight: bold; color: black;")
        frame_layout.addWidget(self.label_date)

        # Spacer unten
        frame_layout.addSpacerItem(QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Label für den Modulnamen
        self.label_module = QLabel(module_name if module_name else "")
        self.label_module.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.label_module.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        self.label_module.setStyleSheet("font-size: 18px; color: black;")
        self.label_module.setWordWrap(True)
        frame_layout.addWidget(self.label_module)

        # Setze das Rahmenlayout
        self.layout.addWidget(self.frame)
        self.setLayout(self.layout)
        self.frame.setStyleSheet("background-color: #FFF9C4; border-radius: 15px;")

        # Styling
        self.setStyleSheet("padding: 5px;")

    def update_exam(self, next_exam: tuple[date | None, str | None]):
        """Aktualisiert das Widget mit neuen Daten."""
        exam_date, module_name = next_exam
        self.label_date.setText(exam_date.strftime("%d.%m.%Y") if exam_date else "Keine Prüfung")
        self.label_module.setText(module_name if module_name else "-")
