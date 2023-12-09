from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFormLayout

class PaymentInformationScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Title Label
        title_label = QLabel("Payment Information")
        layout.addWidget(title_label)

        # Form layout for payment details
        form_layout = QFormLayout()

        # Cardholder name
        self.cardholder_name_input = QLineEdit(self)
        self.cardholder_name_input.setPlaceholderText("Cardholder Name")
        form_layout.addRow("Cardholder Name:", self.cardholder_name_input)

        # Card Number
        self.card_number_input = QLineEdit(self)
        self.card_number_input.setPlaceholderText("1234 5678 9101 1121")
        form_layout.addRow("Card Number:", self.card_number_input)

        # Expiry Date
        self.expiry_date_input = QLineEdit(self)
        self.expiry_date_input.setPlaceholderText("MM/YY")
        form_layout.addRow("Expiry Date:", self.expiry_date_input)

        # CVV
        self.cvv_input = QLineEdit(self)
        self.cvv_input.setPlaceholderText("123")
        form_layout.addRow("CVV:", self.cvv_input)

        layout.addLayout(form_layout)

        # Save Button
        self.save_button = QPushButton('Save Payment Information', self)
        self.save_button.clicked.connect(self.savePaymentInformation)
        layout.addWidget(self.save_button)

        # Back to Settings Button
        self.back_button = QPushButton('Back to Settings', self)
        self.back_button.clicked.connect(self.gotoSettingsScreen)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def savePaymentInformation(self):
        # Here you would collect the payment information and process it (e.g. send to a server)
        cardholder_name = self.cardholder_name_input.text()
        card_number = self.card_number_input.text()
        expiry_date = self.expiry_date_input.text()
        cvv = self.cvv_input.text()
        # Process payment information here
        print("Payment information saved.")

    def gotoSettingsScreen(self):
        # Delayed import to resolve circular dependency
        from settings_screen import SettingsScreen

        for index in range(self.stacked_widget.count()):
            widget = self.stacked_widget.widget(index)
            if isinstance(widget, SettingsScreen):
                self.stacked_widget.setCurrentIndex(index)
                break
