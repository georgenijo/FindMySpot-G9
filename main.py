import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QStackedWidget
)
from PyQt5.QtCore import Qt

# Ensure db_module.py and settings_screen.py are set up correctly
from db_module import Database
from settings_screen import SettingsScreen

# Define the stylesheet to be applied to the whole application
stylesheet = """
QWidget {
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    color: #333;
    background: #f0f0f0;
}

QLabel {
    color: #555;
}

QLineEdit {
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 5px;
    margin-bottom: 10px;
    font-size: 16px;
}

QPushButton {
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 16px;
    background-color: #eee;
    color: #333;
}

QPushButton:hover {
    background-color: #ddd;
}

QPushButton:pressed {
    background-color: #ccc;
}
"""
class LoginScreen(QWidget):
    def __init__(self, stacked_widget, db):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.db = db
        self.initUI()

    def initUI(self):
        self.setStyleSheet(stylesheet)  # Apply the stylesheet to the LoginScreen

        self.username_label = QLabel('Username', self)
        self.username_input = QLineEdit(self)
        self.password_label = QLabel('Password', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login', self)
        self.register_button = QPushButton('Register', self)

        self.login_status_label = QLabel('', self)
        self.login_status_label.setStyleSheet("color: red;")

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        layout.addWidget(self.login_status_label)

        self.setLayout(layout)
        self.setWindowTitle('FindMySpot - Login')

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.db.validate_login(username, password):
            self.login_status_label.setText('')
            self.stacked_widget.setCurrentIndex(1)
        else:
            self.login_status_label.setText('Invalid username or password')

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            self.login_status_label.setText("Username and password cannot be empty")
            return

        if self.db.user_exists(username):
            self.login_status_label.setText("Username already exists")
            return

        self.db.add_user(username, password)
        self.login_status_label.setText("Registration successful")

class DashboardScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        # Initialize dashboard UI components
        self.dashboard_label = QLabel('Dashboard - Main app functionality', self)
        self.settings_button = QPushButton('Settings', self)
        self.settings_button.clicked.connect(self.gotoSettings)

        layout = QVBoxLayout()
        layout.addWidget(self.dashboard_label)
        layout.addWidget(self.settings_button)

        self.setLayout(layout)
        self.setWindowTitle('Dashboard')

    def gotoSettings(self):
        self.stacked_widget.setCurrentIndex(2)

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

        self.setStyleSheet(stylesheet)  # Apply the stylesheet to the entire application
        self.stacked_widget.show()

if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())