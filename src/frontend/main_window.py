from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QApplication
from PyQt5.QtGui import QScreen
from frontend.bar_chart_widget import BarChartWidget
from frontend.metric_widget import MetricWidget, SingleLineWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dashboard')

        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        width, height = screen.width(), screen.height()
        self.resize(int(width * 0.8), int(height * 0.8))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QVBoxLayout()
        top_layout = QGridLayout()
        
        # Kennzahl-Kachel hinzufügen
        metric_widget = MetricWidget()
        top_layout.addWidget(metric_widget, 0, 0)

        # Einfache Textzeile-Kachel hinzufügen
        single_line_widget = SingleLineWidget()
        top_layout.addWidget(single_line_widget, 0, 1)
        
        # Platzhalter für zusätzliche Widgets
        placeholder_widget1 = QWidget()
        top_layout.addWidget(placeholder_widget1, 0, 2)
        placeholder_widget2 = QWidget()
        top_layout.addWidget(placeholder_widget2, 0, 2)

        main_layout.addLayout(top_layout)
        
        # Adding the BarChartWidget to the layout
        plot_widget = BarChartWidget(self)
        main_layout.addWidget(plot_widget)

        self.central_widget.setLayout(main_layout)
