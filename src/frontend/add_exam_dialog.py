from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QDialogButtonBox


class AddExamDialog(QDialog):
    def __init__(self, modules, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Neue Prüfung anlegen")
        self.adjust_size_and_position()

        layout = QVBoxLayout()
        form_layout = QGridLayout()

        # Modul (Pflichtfeld)
        form_layout.addWidget(QLabel("Modul *"), 0, 0)
        self.module_select = QComboBox()
        for module_id, module_name in modules:
            self.module_select.addItem(module_name, module_id)
        form_layout.addWidget(self.module_select, 0, 1)

        # Prüfungsart (Pflichtfeld)
        form_layout.addWidget(QLabel("Prüfungsart *"), 1, 0)
        self.exam_type_select = QComboBox()
        exam_types = [
            "Klausur", "Advanced Workbook", "Hausarbeit", "Seminararbeit",
            "Fallstudie", "Projektarbeit", "Fachpräsentation", "Konzeptpräsentation", "Projektpräsentation"
        ]
        self.exam_type_select.addItems(exam_types)
        form_layout.addWidget(self.exam_type_select, 1, 1)

        # Prüfungsdatum (Pflichtfeld)
        form_layout.addWidget(QLabel("Prüfungsdatum *"), 2, 0)
        self.exam_date_input = QDateEdit()
        self.exam_date_input.setCalendarPopup(True)
        self.exam_date_input.setDate(QDate.currentDate())
        form_layout.addWidget(self.exam_date_input, 2, 1)

        # Note (optional)
        form_layout.addWidget(QLabel("Note"), 3, 0)
        self.grade_input = QLineEdit()
        form_layout.addWidget(self.grade_input, 3, 1)

        layout.addLayout(form_layout)

        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        # noinspection PyUnresolvedReferences
        button_box.accepted.connect(self.accept)
        # noinspection PyUnresolvedReferences
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        self.setLayout(layout)

    def accept(self):
        super().accept()
        self.done(QDialog.Accepted)

    def reject(self):
        super().reject()
        self.done(QDialog.Rejected)

    def get_exam_data(self) -> dict:
        """Sammelt die eingegebenen Daten und gibt sie als Dictionary zurück."""
        return {
            "module_id": self.module_select.currentData(),
            "exam_type": self.exam_type_select.currentText(),
            "exam_date": self.exam_date_input.date().toString("dd.MM.yyyy"),
            "grade": self.grade_input.text() if self.grade_input.text() else None
        }

    def adjust_size_and_position(self):
        parent = self.parent()
        if parent:
            parent_width = parent.width()
            dialog_width = int(parent_width * 0.5)
            self.resize(dialog_width, 200)

            parent_pos = parent.pos()
            x = parent_pos.x() + (parent_width - dialog_width) // 2
            y = parent_pos.y() + 100  # etwas unterhalb der Titelleiste
            self.move(x, y)

