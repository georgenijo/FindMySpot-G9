from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class MapSettingsScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Add content for the Map Settings screen here
        label = QLabel("Map Settings Screen")
        layout.addWidget(label)

        # Back to Settings button
        self.back_button = QPushButton('Back to Settings', self)
        self.back_button.clicked.connect(self.gotoSettingsScreen)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def gotoSettingsScreen(self):
        # Delayed import to resolve circular dependency
        from settings_screen import SettingsScreen

        for index in range(self.stacked_widget.count()):
            widget = self.stacked_widget.widget(index)
            if isinstance(widget, SettingsScreen):
                self.stacked_widget.setCurrentIndex(index)
                break
