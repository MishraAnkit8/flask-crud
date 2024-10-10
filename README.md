# Navigate to your project directory
cd flask-crud/

# Create a virtual environment in the project directory
python -m venv venv

# Activate the virtual environment
# Use the correct command depending on your operating system:
# For Windows:
venv\Scripts\activate
# For Unix or MacOS:
source venv/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install the required dependencies from the requirements.txt file
pip install -r requirements.txt

# Set the Flask app environment variable
# On Windows (CMD):
set FLASK_APP=crudapp.py
# On Windows (PowerShell):
$env:FLASK_APP = "crudapp.py"
# On Unix or MacOS:
export FLASK_APP=crudapp.py

# Initialize the database migrations directory
flask db init

# Generate a migration for the 'entries' table
flask db migrate -m "entries table"

# Apply the migration to update the database schema
flask db upgrade

# Run the Flask application
flask run








# Flask CRUD Application

## Project Structure

| Path                 | Description                          |
|----------------------|--------------------------------------|
| `flask-crud/`        | Root directory of the project.      |
| ├── `app/`           | Contains the main application files.|
| │   ├── `__init__.py`| Initializes the Flask application.  |
| │   ├── `models.py`  | Defines the database models.        |
| │   ├── `routes.py`  | Contains the application routes.    |
| │   ├── `templates/` | Holds HTML templates for the app.   |
| │   ├── `static/`    | Contains static files (CSS, JS, etc.).|
| ├── `migrations/`    | Directory for database migrations.  |
| ├── `venv/`          | Virtual environment for dependencies.|
| ├── `crudapp.py`     | Main application entry point.       |
| ├── `requirements.txt` | Lists project dependencies.        |
| ├── `config.py`      | Configuration settings for the app. |
| ├── `README.md`      | Documentation for the project.      |
| ├── `.gitignore`     | Specifies files to ignore in Git.   |
| ├── `.flaskenv`      | Environment variables for Flask.    |


