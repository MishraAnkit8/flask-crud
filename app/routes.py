from flask import render_template, request, redirect
from app import app, db
from app.models import Entry

# Debug message to check if the module loads correctly
print("Flask application loaded successfully!")

# Global variable for testing responses
jedi = "of the jedi"

@app.route('/')
@app.route('/index')
def index():
    """
    Renders the index page with a list of all entries.
    """
    try:
        # Fetch all entries from the database
        entries = Entry.query.all()
        return render_template('index.html', entries=entries)
    except Exception as e:
        # Print error for debugging
        print(f"Error fetching entries: {e}")
        return jedi

@app.route('/add', methods=['POST'])
def add():
    """
    Adds a new entry to the database.
    """
    try:
        form = request.form
        title = form.get('title')
        description = form.get('description')

        # Check if title and description are provided
        if title and description:
            entry = Entry(title=title, description=description)
            db.session.add(entry)
            db.session.commit()
            print("New entry added successfully!")
            return redirect('/')
        else:
            print("Title or description missing!")
    except Exception as e:
        # Print error for debugging
        print(f"Error adding entry: {e}")
    
    return jedi

@app.route('/update/<int:id>')
def updateRoute(id):
    """
    Renders the update page for a specific entry.
    """
    try:
        entry = Entry.query.get(id)
        if entry:
            return render_template('update.html', entry=entry)
        else:
            print(f"No entry found with id: {id}")
    except Exception as e:
        # Print error for debugging
        print(f"Error fetching entry for update: {e}")

    return jedi

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    """
    Updates an existing entry in the database.
    """
    try:
        entry = Entry.query.get(id)
        if entry:
            form = request.form
            title = form.get('title')
            description = form.get('description')

            if title and description:
                entry.title = title
                entry.description = description
                db.session.commit()
                print(f"Entry with id {id} updated successfully!")
                return redirect('/')
            else:
                print("Title or description missing for update!")
        else:
            print(f"No entry found with id: {id} for update")
    except Exception as e:
        # Print error for debugging
        print(f"Error updating entry: {e}")

    return jedi

@app.route('/delete/<int:id>')
def delete(id):
    """
    Deletes an entry from the database.
    """
    try:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
            print(f"Entry with id {id} deleted successfully!")
            return redirect('/')
        else:
            print(f"No entry found with id: {id} for deletion")
    except Exception as e:
        # Print error for debugging
        print(f"Error deleting entry: {e}")

    return jedi

@app.route('/turn/<int:id>')
def turn(id):
    """
    Toggles the status of an entry in the database.
    """
    try:
        entry = Entry.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
            print(f"Status for entry with id {id} toggled successfully!")
            return redirect('/')
        else:
            print(f"No entry found with id: {id} for status toggle")
    except Exception as e:
        # Print error for debugging
        print(f"Error toggling status: {e}")

    return jedi

@app.errorhandler(Exception)
def error_page(e):
    """
    Handles general exceptions and displays an error message.
    """
    print(f"An error occurred: {e}")
    return jedi
