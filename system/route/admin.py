from flask import render_template, url_for, flash, redirect
from system import app, db
from system.models import User, Vehicle, Bill
from flask_login import current_user, login_required

# ------------------------------ Admin ------------------------------ #
# Admin Page
@app.route("/admin")
@login_required
def admin():
    if not current_user.isAdmin: return redirect(url_for('profile'))
    return render_template("layouts/admin.html", title = "Admin", admin=current_user)

# Admin -> View Users
@app.route("/admin/users")
@login_required
def users():
    if not current_user.isAdmin: return redirect(url_for('profile'))
    users = User.query.all()
    page = 'users'
    return render_template("admin/users.html", title = "View Users", users=users, page=page)

# Admin -> View bills
@app.route("/admin/bills")
@login_required
def bills():
    if not current_user.isAdmin: return redirect(url_for('profile'))
    bills = Bill.query.all()
    page = 'bills'
    return render_template("admin/bills.html", title = "View bills", bills=bills, page=page)

# Admin -> View bills
@app.route("/admin/bills-history")
@login_required
def bill_history():
    if not current_user.isAdmin: return redirect(url_for('profile'))
    bills = Bill.query.all()
    page = 'history'
    return render_template("admin/history.html", title = "View bills", bills=bills, page=page)

# Admin -> View Vehicles
@app.route("/admin/vehicles")
@login_required
def vehicles():
    if not current_user.isAdmin: return redirect(url_for('profile'))
    vehicles = Vehicle.query.all()
    page = 'vehicles'
    return render_template("admin/vehicles.html", title = "View Bills",  vehicles=vehicles, page=page)

# Remove User
@app.route("/admin/remove/<int:id>", methods=['GET', 'POST'])
@login_required
def remove(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash('User has been removed!', 'success')
    return redirect(url_for("users"))

# Add Admin
@app.route("/admin/add-admin/<int:id>/<int:req>", methods=['GET', 'POST'])
@login_required
def add_admin(id, req):
    user = User.query.get(id)
    if req:
        user.isAdmin = 1
        db.session.commit()
        flash('User has been promoted to admin!', 'success')
    else:
        user.isAdmin = 0
        db.session.commit()
        flash('User has been demoted to admin!', 'success')
    return redirect(url_for("users"))
