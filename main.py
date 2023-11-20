import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from db_module import Database
from settings_screen import SettingsScreen
from login_screen import LoginScreen
from dashboard_screen import DashboardScreen
from user_management_screen import UserManagementScreen  # Import UserManagementScreen

class MainApp(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.stacked_widget = QStackedWidget()

        self.db = Database()
        self.login_screen = LoginScreen(self.stacked_widget, self.db)
        self.dashboard_screen = DashboardScreen(self.stacked_widget)
        # Assuming that SettingsScreen is updated to handle navigation
        self.settings_screen = SettingsScreen(self.stacked_widget, self)
        self.user_management_screen = UserManagementScreen(self.stacked_widget)

        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.dashboard_screen)
        self.stacked_widget.addWidget(self.settings_screen)
        self.stacked_widget.addWidget(self.user_management_screen)  # Add UserManagementScreen to QStackedWidget

        self.loadStylesheet("style.qss")
        self.stacked_widget.show()

    def loadStylesheet(self, filename):
        with open(filename, "r") as file:
            self.setStyleSheet(file.read())

if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())
