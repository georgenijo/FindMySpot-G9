import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from db_module import Database
from settings_screen import SettingsScreen
from login_screen import LoginScreen
from dashboard_screen import DashboardScreen
from user_management_screen import UserManagementScreen
from notifications_screen import NotificationsScreen
from payment_info_screen import PaymentInfoScreen
from parking_preferences_screen import ParkingPreferencesScreen
from map_settings_screen import MapSettingsScreen
from privacy_settings_screen import PrivacySettingsScreen
from help_support_screen import HelpSupportScreen


class MainApp(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.stacked_widget = QStackedWidget()

        self.db = Database()
        self.login_screen = LoginScreen(self.stacked_widget, self.db)
        self.dashboard_screen = DashboardScreen(self.stacked_widget)
        self.user_management_screen = UserManagementScreen(self.stacked_widget)  # Pass stacked_widget
        self.notifications_screen = NotificationsScreen(self.stacked_widget)  # Pass stacked_widget
        self.payment_info_screen = PaymentInfoScreen(self.stacked_widget)  # Pass stacked_widget
        self.parking_preferences_screen = ParkingPreferencesScreen(self.stacked_widget)  # Pass stacked_widget
        self.map_settings_screen = MapSettingsScreen(self.stacked_widget)  # Pass stacked_widget
        self.privacy_settings_screen = PrivacySettingsScreen(self.stacked_widget)  # Pass stacked_widget
        self.help_support_screen = HelpSupportScreen(self.stacked_widget)  # Pass stacked_widget
        self.settings_screen = SettingsScreen(self.stacked_widget, self)  # Pass 'self' as reference

        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.dashboard_screen)
        self.stacked_widget.addWidget(self.settings_screen)
        self.stacked_widget.addWidget(self.user_management_screen)
        self.stacked_widget.addWidget(self.notifications_screen)
        self.stacked_widget.addWidget(self.payment_info_screen)
        self.stacked_widget.addWidget(self.parking_preferences_screen)
        self.stacked_widget.addWidget(self.map_settings_screen)
        self.stacked_widget.addWidget(self.privacy_settings_screen)
        self.stacked_widget.addWidget(self.help_support_screen)

        self.loadStylesheet("style.qss")
        self.stacked_widget.show()

    def loadStylesheet(self, filename):
        with open(filename, "r") as file:
            self.setStyleSheet(file.read())

if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())