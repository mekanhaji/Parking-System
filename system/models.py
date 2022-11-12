from datetime import datetime
from system import db , login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    # identity
    id = db.Column(db.Integer, primary_key=True)
    # detail
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    isAdmin = db.Column(db.Integer, default=0)
    # relationship
    vehicles = db.relationship('Vehicle', backref='user', lazy=True)
    bills = db.relationship('Bill', backref='user', lazy=True)
    slot = db.relationship('Slot', backref='user', lazy=True)

    def __repr__(self):
        return f"<User('{self.id}, {self.username}', '{self.email}')>"

class Vehicle(db.Model):
    # identity
    vehicle_id = db.Column(db.Integer, nullable=False, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # detail
    vehicle_number = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(20), default="ungiven")
    type = db.Column(db.Integer, nullable=False)
    # relationship
    slot = db.relationship('Slot', backref='vehicle', lazy=True)
    bill = db.relationship('Bill', backref='vehicle', lazy=True)

    def __repr__(self):
        return f"(<Vehicle('{self.vehicle_id}, {self.vehicle_number}'> <'{self.name}'> <'{self.type}'> <'{self.id}'> <'{self.slot}'>)"

class Bill(db.Model):
    # identity
    bill_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.vehicle_id'), nullable=False)
    # detail's
    bill_date = db.Column(db.DateTime, nullable=False, default=datetime.date)
    bill_time = db.Column(db.Integer, nullable=False)
    bill_amount = db.Column(db.Integer, default=0.0)
    bill_status=db.Column(db.String(20), default="Pending")
    
    def __repr__(self):
        return f"<Admin('{self.bill_id}, {self.bill_date}'> <'{self.id}')>"

class Slot(db.Model):
    slot_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.vehicle_id'), nullable=False)
    
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)
