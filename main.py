import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QStackedWidget
)
from PyQt5.QtCore import Qt

from settings_screen import SettingsScreen

class Database:
    def validate_login(self, username, password):
        return True  # Dummy validation

    def add_user(self, username, password):
        print(f"Added user: {username}")

# Login screen class
class LoginScreen(QWidget):
    def __init__(self, stacked_widget, db):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.db = db
        self.initUI()

    def initUI(self):
        # Create a QVBoxLayout for the main layout
        layout = QVBoxLayout()

        # Add input fields
        username_label = QLabel('Username', self)
        self.username_input = QLineEdit(self)
        password_label = QLabel('Password', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)

        # Add buttons
        login_button = QPushButton('Login', self)
        login_button.clicked.connect(self.login)
        register_button = QPushButton('Register', self)
        register_button.clicked.connect(self.register)

        layout.addWidget(login_button)
        layout.addWidget(register_button)

        # Set the main layout for the widget
        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.db.validate_login(username, password):
            print("Login successful")
            self.stacked_widget.setCurrentIndex(1)  # Proceed to dashboard

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username and password:
            self.db.add_user(username, password)
            print("Registration successful")
        else:
            print("Username and password cannot be empty")

# Dashboard screen class
class DashboardScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        # Create a QVBoxLayout for the main layout
        layout = QVBoxLayout()

        # Add a label
        dashboard_label = QLabel('Dashboard - Main app functionality', self)

        layout.addWidget(dashboard_label)

        # Add a button
        settings_button = QPushButton('Settings', self)
        settings_button.clicked.connect(self.gotoSettings)

        layout.addWidget(settings_button)

        # Set the main layout for the widget
        self.setLayout(layout)

    def gotoSettings(self):
        self.stacked_widget.setCurrentIndex(2)  # Proceed to settings

# Main application class
class MainApp(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.stacked_widget = QStackedWidget()

        self.db = Database()
        self.login_screen = LoginScreen(self.stacked_widget, self.db)
        self.dashboard_screen = DashboardScreen(self.stacked_widget)
        self.settings_screen = SettingsScreen(self.stacked_widget, 1)

        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.dashboard_screen)
        self.stacked_widget.addWidget(self.settings_screen)

        self.stacked_widget.show()

# Entry point of the application
if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())
