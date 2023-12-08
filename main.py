import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5.QtCore import Qt, QCoreApplication

# Set the attribute before creating the QApplication instance
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

# Now import the module that requires the attribute to be set
from PyQt5.QtWebEngineWidgets import QWebEngineView

from settings_screen import SettingsScreen
from camera import MainWindow
from db_module import Database
from login_screen import LoginScreen
from dashboard_screen import DashboardScreen
from user_management_screen import UserManagementScreen
from notifications_screen import NotificationsScreen
from payment_information_screen import PaymentInformationScreen
from parking_preferences_screen import ParkingPreferencesScreen
from map_settings_screen import MapSettingsScreen
from privacy_settings_screen import PrivacySettingsScreen
from help_support_screen import HelpScreen
from map_services import MapsService

class MainApp(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.stacked_widget = QStackedWidget()
        self.widget_indices = {}

        print("Testing Commit.")

        self.db = Database()

        # Initialize and add your screens
        
        self.login_screen = LoginScreen(self.stacked_widget, self.db, self.widget_indices)
        self.widget_indices['login_screen'] = self.stacked_widget.addWidget(self.login_screen)
        
        self.dashboard_screen = DashboardScreen(self.stacked_widget, self.widget_indices)
        self.widget_indices['dashboard_screen'] = self.stacked_widget.addWidget(self.dashboard_screen)

        self.settings_screen = SettingsScreen(self.stacked_widget, self)
        self.widget_indices['settings_screen'] = self.stacked_widget.addWidget(self.settings_screen)

        self.user_management_screen = UserManagementScreen(self.stacked_widget)
        self.widget_indices['user_management_screen'] = self.stacked_widget.addWidget(self.user_management_screen)

        self.notifications_screen = NotificationsScreen(self.stacked_widget)
        self.widget_indices['notifications_screen'] = self.stacked_widget.addWidget(self.notifications_screen)

        self.payment_information_screen = PaymentInformationScreen(self.stacked_widget)
        self.widget_indices['payment_information_screen'] = self.stacked_widget.addWidget(self.payment_information_screen)

        self.parking_preferences_screen = ParkingPreferencesScreen(self.stacked_widget)
        self.widget_indices['parking_preferences_screen'] = self.stacked_widget.addWidget(self.parking_preferences_screen)

        self.map_settings_screen = MapSettingsScreen(self.stacked_widget)
        self.widget_indices['map_settings_screen'] = self.stacked_widget.addWidget(self.map_settings_screen)

        self.privacy_settings_screen = PrivacySettingsScreen(self.stacked_widget)
        self.widget_indices['privacy_settings_screen'] = self.stacked_widget.addWidget(self.privacy_settings_screen)

        self.help_and_support_screen = HelpScreen(self.stacked_widget)
        self.widget_indices['help_and_support_screen'] = self.stacked_widget.addWidget(self.help_and_support_screen)

        self.main_window = MainWindow(self.db, self) # 'self' refers to the instance of MainApp
        self.widget_indices['main_window'] = self.stacked_widget.addWidget(self.main_window)

        self.loadStylesheet("style.qss")
        self.stacked_widget.show()

    def loadStylesheet(self, filename):
        with open(filename, "r") as file:
            self.setStyleSheet(file.read())

if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())
