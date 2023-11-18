import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from db_module import Database
from settings_screen import SettingsScreen
from login_screen import LoginScreen
from dashboard_screen import DashboardScreen


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

        self.loadStylesheet("style.qss")
        self.stacked_widget.show()

    def loadStylesheet(self, filename):
        with open(filename, "r") as file:
            self.setStyleSheet(file.read())

if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())
