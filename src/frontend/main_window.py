from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dashboard')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.label = QLabel('Dashboard Prototyp')
        layout.addWidget(self.label)

        self.central_widget.setLayout(layout)
