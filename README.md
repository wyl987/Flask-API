# Flask REST API Application

This is a simple REST API built using Flask, Flask-RESTful, and Flask-SQLAlchemy. The app allows for creating, reading, updating, and deleting (CRUD) user data, such as usernames and emails, stored in an SQLite database.

The project was built with reference to the tutorial:  
**[Python REST API Tutorial for Beginners | How to Build a Flask REST API](https://www.youtube.com/watch?v=z3YMz-Gocmw)**

## Features

- **Create Users**: Add new users with a username and email.
- **Retrieve Users**: Fetch all users or a specific user by ID.
- **Update Users**: Partially update a user’s information using their ID.
- **Delete Users**: Remove a user from the database.

## Tech Stack

- **Python**: Programming language used to build the API.
- **Flask**: Web framework to build the REST API.
- **Flask-RESTful**: Flask extension to simplify building REST APIs.
- **Flask-SQLAlchemy**: Flask extension to handle SQL database operations with ease.
- **SQLite**: Database used for storing user data.

## Running the Application

1. Set up a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   .\venv\Scripts\activate   # Windows
2. Install dependencies:
   ```bash
   pip install -r requirements.txt


