from flask import render_template
from system import app
from system.models import Slot

# Home Page
@app.route("/home")
@app.route("/home/")
@app.route("/")
def home():
    slots = Slot.query.all()
    return render_template("pages/home.html", title = "Home", slots=slots)
