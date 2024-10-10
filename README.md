cd flask-crud/
python -m venv venv
 venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
export FLASK_APP=crudapp.py
flask db init
flask db migrate -m "entries table"
flask db upgrade
flask run