from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame, QSpacerItem, QSizePolicy

class CompletedModulesWidget(QWidget):
    def __init__(self, completed_modules: int, total_modules: int):
        super().__init__()

        # Widget Layout
        self.layout = QVBoxLayout()

        # Rahmen erstellen
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(2)

        # Layout für den Rahmen
        frame_layout = QVBoxLayout(self.frame)

        # Spacer oben
        frame_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Label für die abgeschlossenen/gesamten Module
        self.label_modules = QLabel(f"{completed_modules}/{total_modules}")
        self.label_modules.setAlignment(Qt.AlignCenter)
        self.label_modules.setStyleSheet("font-size: 48px; font-weight: bold; color: black;")
        frame_layout.addWidget(self.label_modules)

        # Spacer unten
        frame_layout.addSpacerItem(QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Label für die Beschreibung
        self.label_description = QLabel("Module abgeschlossen")
        self.label_description.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.label_description.setStyleSheet("font-size: 18px; color: black;")
        self.label_description.setWordWrap(True)
        frame_layout.addWidget(self.label_description)

        # Setze das Rahmenlayout
        self.layout.addWidget(self.frame)
        self.setLayout(self.layout)

        # Styling
        self.setStyleSheet("padding: 5px;")
        self.frame.setStyleSheet("background-color: #D9F2D0; border-radius: 15px;")  # Mintgrün, wie im Noten-Widget

    def update_modules(self, completed_modules: int, total_modules: int):
        """Aktualisiert die angezeigten Modulzahlen."""
        self.label_modules.setText(f"{completed_modules} / {total_modules}")
