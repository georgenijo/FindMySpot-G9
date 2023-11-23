import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from db_module import Database
from settings_screen import SettingsScreen
from login_screen import LoginScreen
from dashboard_screen import DashboardScreen
from user_management_screen import UserManagementScreen  # Import UserManagementScreen
from notifications_screen import NotificationsScreen  # Import NotificationsScreen
from payment_information_screen import PaymentInformationScreen  # Import PaymentInformationScreen
from parking_preferences_screen import ParkingPreferencesScreen  # Import ParkingPreferencesScreen
from map_settings_screen import MapSettingsScreen  # Import MapSettingsScreen
from privacy_settings_screen import PrivacySettingsScreen  # Import PrivacySettingsScreen
from help_support_screen import HelpScreen  # Import HelpAndSupportScreen
from map_services import MapsService

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
        self.notifications_screen = NotificationsScreen(self.stacked_widget)
        self.payment_information_screen = PaymentInformationScreen(self.stacked_widget)
        self.parking_preferences_screen = ParkingPreferencesScreen(self.stacked_widget)
        self.map_settings_screen = MapSettingsScreen(self.stacked_widget)
        self.privacy_settings_screen = PrivacySettingsScreen(self.stacked_widget)
        self.help_and_support_screen = HelpScreen(self.stacked_widget)
    

        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.dashboard_screen)
        self.stacked_widget.addWidget(self.settings_screen)
        self.stacked_widget.addWidget(self.user_management_screen)  # Add UserManagementScreen to QStackedWidget
        self.stacked_widget.addWidget(self.notifications_screen)  # Add NotificationsScreen
        self.stacked_widget.addWidget(self.payment_information_screen)
        self.stacked_widget.addWidget(self.parking_preferences_screen)
        self.stacked_widget.addWidget(self.map_settings_screen)
        self.stacked_widget.addWidget(self.privacy_settings_screen)
        self.stacked_widget.addWidget(self.help_and_support_screen)



        self.loadStylesheet("style.qss")
        self.stacked_widget.show()

    def setup_services(self):
        # Replace 'Your-API-Key' with your actual Google Maps API key
        self.maps_service = MapsService('Your-API-Key')

    def loadStylesheet(self, filename):
        with open(filename, "r") as file:
            self.setStyleSheet(file.read())

if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())
