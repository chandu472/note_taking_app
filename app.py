from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note and note.strip():
            # Get notes from user's session
            notes = session.get('notes', [])
            # Append new note to the list
            notes.append(note)
            # Store updated notes list in user's session
            session['notes'] = notes
    # Retrieve notes from user's session
    notes = session.get('notes', [])
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
