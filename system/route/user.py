from flask import render_template, url_for, redirect
from system import app
from system.models import Vehicle, Bill, Slot
from flask_login import current_user, login_required

# ------------------------------ User ------------------------------ #
# User > Profile Page
@app.route("/profile")
@app.route("/profile/")
@login_required
def profile():
    if current_user.isAdmin : return redirect(url_for('admin'))
    return render_template("layouts/profile.html", title = "profile")

# User > Vehicle Page
@app.route("/profile/vehicle")
@app.route("/profile/vehicle/")
@login_required
def user_vehicle():
    if current_user.isAdmin : return redirect(url_for('admin'))
    vehicles = Vehicle.query.filter_by(id=current_user.id)
    slots = Slot.query.all()
    page = 'vehicle'
    return render_template("user/vehicle.html", title = "Vehicle", vehicles=vehicles, page=page, slots=slots)

# User > Bill Page
@app.route("/profile/bill")
@app.route("/profile/bill/")
@login_required
def user_bill():
    if current_user.isAdmin : return redirect(url_for('admin'))
    bills = Bill.query.filter_by(id=current_user.id)
    page = 'bill'
    return render_template("user/bill.html", title = "Bill", bills=bills, page=page)

# User > Bill History Page
@app.route("/profile/bill-history")
@app.route("/profile/bill-history/")
@login_required
def user_bill_history():
    if current_user.isAdmin : return redirect(url_for('admin'))
    bills = Bill.query.filter_by(id=current_user.id)
    page = 'bill history'
    return render_template("user/history.html", title = "Bill", bills=bills, page=page)