from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class DashboardScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Dashboard label and buttons
        self.dashboard_label = QLabel('Dashboard - Main app functionality', self)
        self.settings_button = QPushButton('Settings', self)
        self.logout_button = QPushButton('Logout', self)

        self.settings_button.clicked.connect(self.gotoSettings)
        self.logout_button.clicked.connect(self.logout)

        layout.addWidget(self.dashboard_label)
        layout.addWidget(self.settings_button)
        layout.addWidget(self.logout_button)

        # QWebEngineView for Google Maps
        self.map_view = QWebEngineView()
        self.map_view.load(QUrl.fromLocalFile(r"C:\Users\georg\Documents\GitHub\FindMySpot-G9\maps.html"))
        layout.addWidget(self.map_view)

        self.setLayout(layout)
        self.setWindowTitle('Dashboard')

    def gotoSettings(self):
        self.stacked_widget.setCurrentIndex(2)

    def logout(self):
        self.stacked_widget.setCurrentIndex(0)
