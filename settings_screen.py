from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class SettingsScreen(QWidget):
    def __init__(self, stacked_widget, main_app):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.main_app = main_app  # reference to MainApp to access other screens
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Create buttons for each setting option and connect them to their handlers
        self.user_management_button = QPushButton('User Management - Edit', self)
        self.user_management_button.clicked.connect(lambda: self.gotoScreen(self.main_app.user_management_screen))

        self.notifications_button = QPushButton('Notifications - Edit', self)
        self.notifications_button.clicked.connect(lambda: self.gotoScreen(self.main_app.notifications_screen))

        self.payment_info_button = QPushButton('Payment Information - Edit', self)
        self.payment_info_button.clicked.connect(lambda: self.gotoScreen(self.main_app.payment_info_screen))

        self.parking_preferences_button = QPushButton('Parking Preferences - Edit', self)
        self.parking_preferences_button.clicked.connect(lambda: self.gotoScreen(self.main_app.parking_preferences_screen))

        self.map_settings_button = QPushButton('Map Settings - Edit', self)
        self.map_settings_button.clicked.connect(lambda: self.gotoScreen(self.main_app.map_settings_screen))

        self.privacy_settings_button = QPushButton('Privacy Settings - Edit', self)
        self.privacy_settings_button.clicked.connect(lambda: self.gotoScreen(self.main_app.privacy_settings_screen))

        self.help_support_button = QPushButton('Help and Support - Edit', self)
        self.help_support_button.clicked.connect(lambda: self.gotoScreen(self.main_app.help_support_screen))

        self.back_button = QPushButton('Back to Dashboard', self)
        self.back_button.clicked.connect(self.gotoDashboard)

        # Add buttons to the layout
        layout.addWidget(self.user_management_button)
        layout.addWidget(self.notifications_button)
        layout.addWidget(self.payment_info_button)
        layout.addWidget(self.parking_preferences_button)
        layout.addWidget(self.map_settings_button)
        layout.addWidget(self.privacy_settings_button)
        layout.addWidget(self.help_support_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def gotoScreen(self, screen):
        index = self.stacked_widget.indexOf(screen)
        if index != -1:
            self.stacked_widget.setCurrentIndex(index)
        else:
            print("Screen not found in QStackedWidget")

    def gotoDashboard(self):
        self.stacked_widget.setCurrentIndex(1)
