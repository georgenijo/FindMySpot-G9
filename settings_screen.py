from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from user_management_screen import UserManagementScreen

class SettingsScreen(QWidget):
    def __init__(self, stacked_widget, main_app):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.main_app = main_app  # reference to MainApp to access other screens
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Add buttons for settings options
        settings_buttons = [
            ('User Management', 'Edit'),
            ('Notifications', 'Edit'),
            ('Payment Information', 'Edit'),
            ('Parking Preferences', 'Edit'),
            ('Map Settings', 'Edit'),
            ('Privacy Settings', 'Edit'),
            ('Help and Support', 'Edit')
        ]

        for option, button_text in settings_buttons:
            button = QPushButton(f'{option} - {button_text}', self)
            if option == 'User Management':
                button.clicked.connect(self.gotoUserManagementScreen)
            else:
                button.clicked.connect(self.onButtonClick)
            layout.addWidget(button)

        # Set the main layout for the widget
        self.setLayout(layout)

    def onButtonClick(self):
        # Handle button click event for settings options
        sender = self.sender()
        if sender:
            button_text = sender.text()
            print(f'Clicked: {button_text}')

    def gotoUserManagementScreen(self):
        # Switch to the User Management Screen
        index = self.stacked_widget.indexOf(self.main_app.user_management_screen)
        if index != -1:
            self.stacked_widget.setCurrentIndex(index)
        else:
            print("User Management Screen not found in QStackedWidget")

    # Additional methods to handle navigation to other screens as needed
    # Example:
    # def gotoNotificationsScreen(self):
    #     # Logic to navigate to the Notifications screen
