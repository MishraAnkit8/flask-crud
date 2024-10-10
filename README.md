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








flask-crud/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   ├── static/
├── migrations/
├── venv/
├── crudapp.py
├── requirements.txt
├── config.py
├── README.md
├── .gitignore
├── .flaskenv
