from flask import url_for, flash, redirect
from system import app, db
from system.models import Vehicle, Bill, Slot
from flask_login import current_user, logout_user, login_required
from datetime import datetime

# Logout user
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# Park Vehicle
@app.route("/profile/park-vehicle<int:vehicle_id>", methods=['POST'])
@login_required
def park_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    slot = Slot(id=current_user.id,vehicle_id=vehicle.vehicle_id)
    
    db.session.add(slot)
    db.session.commit()
    flash('vehicle parked!', 'success')
    return redirect(url_for('home'))

# Delete Vehicle
@app.route("/profile/remove-vehicle<int:vehicle_id>", methods=['POST'])
@login_required
def remove_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)

    db.session.delete(vehicle)
    db.session.commit()
    flash('Vehicle has been removed!', 'success')
    return redirect(url_for('profile'))

# Take Vehicle
@app.route("/home/take/<int:slot_id>", methods=['POST'])
@login_required
def take(slot_id):
    slot = Slot.query.get(slot_id)
    st_H = int(slot.time.strftime("%H"))
    st_M = int(slot.time.strftime("%M"))
    end_time = datetime.now()
    et_H = int(end_time.strftime("%H"))
    et_M = int(end_time.strftime("%M"))
    et_H, et_M = abs(st_H - et_H), abs(st_M - et_M)
    total_time = et_M + (et_H * 60)
    if slot.vehicle.type == 2:
        pay = float(total_time * .2)
    elif slot.vehicle.type == 4:
        pay = float(total_time * .4)
    else: 
        pay = float(total_time * .8)
        
    bill = Bill(
        id=current_user.id,
        vehicle_id=slot.vehicle_id,
        bill_date=datetime.now(),
        bill_time= int(total_time),
        bill_amount=pay
        )
    db.session.add(bill)
    db.session.delete(slot)
    db.session.commit()
    flash('Vehicle has been taken!', 'success')
    return redirect(url_for('home'))

# Pay bill User
@app.route("/profile/pay/<int:bill_id>", methods=['POST'])
@login_required
def pay(bill_id):
    bill = Bill.query.get(bill_id)
    if current_user.isAdmin:
        bill.bill_status = "Payed"
        db.session.commit()
        flash('Payed!', 'success')
        return redirect(url_for('bills'))
    else:
        bill.bill_status = "Unapproved"
        db.session.commit()
        flash('Contact Admin, Under Admins Approval!', 'success')
        return redirect(url_for('user_bill'))