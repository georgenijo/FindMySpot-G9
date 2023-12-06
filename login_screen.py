from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from twilio.rest import Client

class LoginScreen(QWidget):
    def __init__(self, stacked_widget, db, widget_indices):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.db = db
        self.widget_indices = widget_indices  # Store widget indices
        self.initUI()


    def initUI(self):
        self.username_label = QLabel('Username', self)
        self.username_input = QLineEdit(self)
        self.password_label = QLabel('Password', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.phone_number_label = QLabel('Phone Number', self)
        self.phone_number_input = QLineEdit(self)


        self.login_button = QPushButton('Login', self)
        self.register_button = QPushButton('Register', self)

        self.login_status_label = QLabel('', self)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        layout.addWidget(self.login_status_label)
        layout.addWidget(self.phone_number_label)
        layout.addWidget(self.phone_number_input)

        self.setLayout(layout)
        self.setWindowTitle('FindMySpot - Login')

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.db.validate_login(username, password):
            self.login_status_label.setText('')
            # Correct the index according to where MainWindow is added to stacked_widget
            main_window_index = self.widget_indices['main_window']  # Use the stored index
            main_window = self.stacked_widget.widget(main_window_index)
            # Ensure that main_window is an instance of MainWindow
            if hasattr(main_window, 'set_current_user'):
                main_window.set_current_user(username)
                self.stacked_widget.setCurrentIndex(main_window_index)
                self.clearInputs()
            else:
                print("Error: The referenced widget does not have a 'set_current_user' method.")
                # Handle the error appropriately
        else:
            self.login_status_label.setText('Invalid username or password')

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        phone = self.phone_number_input.text()  # Get the phone number from input

        if not username or not password or not phone:
            self.login_status_label.setText("Username, password, and phone cannot be empty")
            return

        if self.db.user_exists(username):
            self.login_status_label.setText("Username already exists")
            return

        if self.db.add_user(username, password, phone):
            self.login_status_label.setText("Registration successful")
            self.send_sms_notification(phone)  # Send SMS notification
            self.clearInputs()

    def send_sms_notification(self, user_phone):
        account_sid = 'AC2afec9f9ff38eea3ffa8597b817d7c6f'
        auth_token = 'fcfb74b91442d8365c784843f1d827a2'
        client = Client(account_sid, auth_token)
        twilio_number = '+18775632287'  # Ensure the number is in E.164 format
        message_body = 'Welcome! Thank you for registering with FindMySpot.'

        try:
            message = client.messages.create(
                body=message_body,
                from_=twilio_number,
                to=user_phone
            )
            print(f"Message sent: {message.sid}")
        except Exception as e:
            print(f"Failed to send SMS: {e}")

    def clearInputs(self):
        self.username_input.clear()
        self.password_input.clear()
        self.phone_number_input.clear()

# The following should be outside of the class definition
# and typically included only if this script is the main entry point for the application.
if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    # Replace None with actual instances if necessary
    login_screen = LoginScreen(None, None)  # Replace with the actual stacked_widget and db
    login_screen.show()
    app.exec_()
