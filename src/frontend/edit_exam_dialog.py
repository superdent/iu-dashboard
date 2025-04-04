from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QDialogButtonBox
from PyQt5.QtCore import QDate


class EditExamDialog(QDialog):
    def __init__(self, exams, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Prüfung bearbeiten")
        self.exams = exams
        self.exam_by_id = {exam["exam_id"]: exam for exam in exams}

        layout = QVBoxLayout()
        form_layout = QGridLayout()

        # Dropdown zur Auswahl eines Exams
        form_layout.addWidget(QLabel("Prüfung auswählen *"), 0, 0)
        self.exam_select = QComboBox()
        for exam in exams:
            label = f'{exam["module_name"]} – {exam["exam_date"].strftime("%d.%m.%Y")}'
            self.exam_select.addItem(label, exam["exam_id"])
        self.exam_select.currentIndexChanged.connect(self._fill_form_fields)
        form_layout.addWidget(self.exam_select, 0, 1)

        # Modul (nur anzeigen, nicht änderbar)
        form_layout.addWidget(QLabel("Modul"), 1, 0)
        self.module_label = QLabel()
        form_layout.addWidget(self.module_label, 1, 1)

        # Prüfungsart
        form_layout.addWidget(QLabel("Prüfungsart *"), 2, 0)
        self.exam_type_select = QComboBox()
        exam_types = [
            "Klausur", "Advanced Workbook", "Hausarbeit", "Seminararbeit",
            "Fallstudie", "Projektarbeit", "Fachpräsentation", "Konzeptpräsentation", "Projektpräsentation"
        ]
        self.exam_type_select.addItems(exam_types)
        form_layout.addWidget(self.exam_type_select, 2, 1)

        # Datum
        form_layout.addWidget(QLabel("Prüfungsdatum *"), 3, 0)
        self.exam_date_input = QDateEdit()
        self.exam_date_input.setCalendarPopup(True)
        form_layout.addWidget(self.exam_date_input, 3, 1)

        # Note
        form_layout.addWidget(QLabel("Note"), 4, 0)
        self.grade_input = QLineEdit()
        form_layout.addWidget(self.grade_input, 4, 1)

        layout.addLayout(form_layout)

        # Buttons
        self.button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)

        self.setLayout(layout)

        # Erstes Exam vorbefüllen
        self._fill_form_fields(0)

    def _fill_form_fields(self, index):
        exam_id = self.exam_select.itemData(index)
        if exam_id is None:
            return
        exam = self.exam_by_id.get(exam_id)
        if not exam:
            return

        self.module_label.setText(exam["module_name"])
        self.exam_type_select.setCurrentText(exam["exam_type"])
        self.exam_date_input.setDate(exam["exam_date"])
        self.grade_input.setText(str(exam["grade"]) if exam["grade"] is not None else "")

    def get_exam_data(self):
        exam_id = self.exam_select.currentData()
        exam = self.exam_by_id.get(exam_id)

        return {
            "exam_id": exam_id,
            "module_id": exam["module_id"],  # ← nötig fürs Backend
            "exam_type": self.exam_type_select.currentText(),
            "exam_date": self.exam_date_input.date().toString("dd.MM.yyyy"),
            "grade": self.grade_input.text() or None
        }
