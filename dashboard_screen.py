from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class DashboardScreen(QWidget):
    def __init__(self, stacked_widget, widget_indices, db, current_user):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.widget_indices = widget_indices
        self.db = db
        self.current_user = current_user
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Dashboard label and buttons
        self.dashboard_label = QLabel('Dashboard - Main app functionality', self)
        self.settings_button = QPushButton('Settings', self)
        self.logout_button = QPushButton('Logout', self)
<<<<<<< HEAD

        self.ui_button = QPushButton('Go to UI', self)
        self.ui_button.clicked.connect(self.gotoUI)
        layout.addWidget(self.ui_button)

        self.settings_button.clicked.connect(self.gotoSettings)
        self.logout_button.clicked.connect(self.logout)

=======
        self.ui_button = QPushButton('Go to UI', self)
        self.ui_button.clicked.connect(self.gotoUI)
        layout.addWidget(self.ui_button)
        self.settings_button.clicked.connect(self.gotoSettings)
        self.logout_button.clicked.connect(self.logout)
>>>>>>> parent of 2fac40a (Revert "Fixed map and login data")
        layout.addWidget(self.dashboard_label)
        layout.addWidget(self.settings_button)
        layout.addWidget(self.logout_button)

        # QWebEngineView for Google Maps
        self.map_view = QWebEngineView()
        self.map_view.load(QUrl.fromLocalFile(r"/Users/georgenjio/Documents/Code/FindMySpot-G9/maps.html"))
        layout.addWidget(self.map_view)

        self.setLayout(layout)
        self.setWindowTitle('Dashboard')

<<<<<<< HEAD
=======
    def update_dashboard(self):
        # Placeholder for the actual update logic
        self.reserved_spots = self.db.get_all_reserved_spots()
        # Implement the logic to visually update parking spots based on their reserved status
        # Example (pseudocode):
        for spot_widget in self.parking_spot_widgets:
             if spot_widget.id in self.reserved_spots:
                 spot_widget.set_reserved_style()
             else:
                 spot_widget.set_available_style()

>>>>>>> parent of 2fac40a (Revert "Fixed map and login data")
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
<<<<<<< HEAD
=======

# Additional methods and logic would go here

>>>>>>> parent of 2fac40a (Revert "Fixed map and login data")
