from flask import render_template, url_for, flash, redirect, request
from system import app, db
from system.models import User, Vehicle
from system.forms import LoginForm, RegistrationForm, VehicleFrom, UpdateUserForm, UpdateVehicleFrom
from flask_login import login_user, current_user, login_required

# Registration Page
@app.route("/Registration", methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data
                )
        db.session.add(user)
        db.session.commit()
        flash(f'Account created!', 'success')
        return redirect(url_for('login'))
    return render_template("forms/registration.html", title = "Registration", form=form, lagend="Register")

# Login Page
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # admin = Admin.query.filter_by(email=form.email.data).first()
        if (user and user.password == form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('profile'))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("forms/login.html", title = "login", form=form)


# Add Vehicle
@app.route("/profile/Add-vehicle", methods=['GET', 'POST'])
@login_required
def vehicle():
    form = VehicleFrom()
    if form.validate_on_submit():
        vehicle = Vehicle(
                    id=current_user.id,
                    name=form.valicle_name.data,
                    vehicle_number=form.valicle_number.data,
                    type=form.valicle_type.data
                )
        db.session.add(vehicle)
        db.session.commit()
        flash(f'Vahicle is added to your profile!', 'success')
        return redirect(url_for('login'))
    return render_template("forms/vehicle.html", title = "Add Vehicle", form=form)

# Update User
@app.route("/profile/Update", methods=['GET', 'POST'])
@login_required
def update_user():
    form = UpdateUserForm()
    if form.validate_on_submit() :
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.password = form.password.data

        db.session.commit()
        flash('Profile Updated!', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template("forms/registration.html", title = "Update", form=form, lagend="Update")

# Update Vehicle
@app.route("/profile/update-vehicle<int:vehicle_id>", methods=['POST'])
@login_required
def update_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    form = UpdateVehicleFrom()
    if form.validate_on_submit():
        vehicle.name = form.valicle_name.data
        vehicle.vehicle_number = form.valicle_number.data
        vehicle.type = form.valicle_type.data
        
        db.session.commit()
        flash('Vehicle Updated!', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'POST':
        form.valicle_name.data = vehicle.name
        form.valicle_number.data = vehicle.vehicle_number
        form.valicle_type.data = vehicle.type
    return render_template("forms/vehicle.html", title = "Update Vehicle", form=form)
