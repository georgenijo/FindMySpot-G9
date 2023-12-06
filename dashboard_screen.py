from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

from camera import MainWindow

class DashboardScreen(QWidget):
    def __init__(self, stacked_widget, widget_indices, db, current_user):  # Added widget_indices as a parameter
        super().__init__()
        self.stacked_widget = stacked_widget
        self.widget_indices = widget_indices
        self.db = db

        self.current_user = current_user
        layout = QVBoxLayout(self)

        # Header label
        self.dashboard_label = QLabel('           Dashboard - Reservations', self)
        layout.addWidget(self.dashboard_label)

        # Buttons for navigation
        self.ui_button = QPushButton('Camera', self)
        self.ui_button.clicked.connect(self.gotoUI)
        self.settings_button = QPushButton('Settings', self)
        self.settings_button.clicked.connect(self.gotoSettings)
        self.logout_button = QPushButton('Logout', self)
        self.logout_button.clicked.connect(self.logout)

        # Button layout
        button_layout = QHBoxLayout()  # Horizontal layout for buttons
        button_layout.addWidget(self.ui_button)
        button_layout.addWidget(self.settings_button)
        button_layout.addWidget(self.logout_button)
        layout.addLayout(button_layout)  # Add button layout to the main layout

        # Table for reservations
        self.reservation_table = QTableWidget(0, 1)  # 1 column for spot numbers
        self.reservation_table.setHorizontalHeaderLabels(['Reserved Spots'])
        header = self.reservation_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.reservation_table.setAlternatingRowColors(True)
        self.reservation_table.setStyleSheet("alternate-background-color: #f2f2f2; background-color: #ffffff;")
        layout.addWidget(self.reservation_table)
        self.update_reservations()


        # Horizontal layout for map and hyperlink
        map_layout = QHBoxLayout()

        # QWebEngineView for Google Maps
        self.map_view = QWebEngineView()
        self.map_view.load(QUrl.fromLocalFile(r"maps.html"))
        layout.addWidget(self.map_view)

        layout.addLayout(map_layout)  # Add map and hyperlink layout to the main layout
        self.setLayout(layout)
        self.setWindowTitle('Dashboard')


    def set_current_user(self, username):
        self.current_user = username

    def update_dashboard(self):
        self.update_reservations()

    def update_reservations(self):
        # Fetch user's reservations and update the table
        user_reservations = self.db.get_user_reservations(self.current_user)
        self.reservation_table.setRowCount(len(user_reservations))
        for row, spot_id in enumerate(user_reservations):
            self.reservation_table.setItem(row, 0, QTableWidgetItem(str(spot_id)))

    def gotoSettings(self):
        self.stacked_widget.setCurrentIndex(2)

    def logout(self):
        self.stacked_widget.setCurrentIndex(0)
    
    def gotoUI(self):
        # Navigate to the MainWindow (UI)
        main_window_index = self.widget_indices.get('main_window')
        if main_window_index is not None:
            self.stacked_widget.setCurrentIndex(main_window_index)

    # Add any additional methods needed for your dashboard functionality
