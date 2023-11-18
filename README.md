# FindMySpot Application

## Description
FindMySpot is a desktop application built using PyQt5, designed to streamline parking spot searches and management. It features a user-friendly interface, allowing users to log in, manage their settings, and access dashboard functionalities.

## Features
- User authentication (login and registration)
- Dashboard with main app functionalities
- Settings management
- Logout functionality

## Installation

### Prerequisites
- Python 3.x
- PyQt5
- MongoDB
- bcrypt

## Setup

### Prerequisites
Before running the application, ensure you have the following installed (This was built using Python 3.12):
- Python 3.x
- PyQt5
- MongoDB
- bcrypt

You can install PyQt5, MongoDB, and bcrypt using pip:

pip install PyQt5 pymongo bcrypt

git clone https://github.com/yourusername/findmyspot.git

cd findmyspot

## Usage
After launching the application, users can:

- **Login/Register**: Access the application by entering their credentials.
- **Dashboard**: Navigate through the app's main functionalities.
- **Settings**: Customize user settings like notifications, payment information, etc.
- **Logout**: Safely exit their session.

## File Structure

- `main.py`: Main application file. This is the entry point of the application.
- `login_screen.py`: Contains the `LoginScreen` class, responsible for the user login interface and functionality.
- `dashboard_screen.py`: Contains the `DashboardScreen` class, which is the main interface after login.
- `settings_screen.py`: Contains the `SettingsScreen` class, allowing users to modify their application settings.
- `db_module.py`: Manages database connections and user authentication logic.
- `style.qss`: Contains the CSS styling for the application's UI.
