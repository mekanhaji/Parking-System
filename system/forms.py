# Imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from system.models import User, Vehicle

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already Teken')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email already Teken')

class VehicleFrom(FlaskForm):
    valicle_name = StringField('Vahicle Name', validators=[DataRequired()])
    valicle_number = IntegerField('Vahicle Number', validators=[DataRequired()])
    valicle_type = SelectField('Velicle Type', choices=[(2, 'Two wheeler'), (4, 'Four wheeler'), (6, 'Large Vehicle')])
    submit = SubmitField('Add Vehicle')

    def validate_vahicle(self, valicle_number):
        vehicle = Vehicle.query.filter_by(vehicle_number=int(valicle_number.data)).first()
        if vehicle:
            raise ValidationError('Vahicle With Same Number Already Exist!')


class UpdateUserForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Update')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already Teken')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email already Teken')

class UpdateVehicleFrom(FlaskForm):
    valicle_name = StringField('Vahicle Name', validators=[DataRequired()])
    valicle_number = IntegerField('Vahicle Number', validators=[DataRequired()])
    valicle_type = SelectField('Velicle Type', choices=[(2, 'Two wheeler'), (4, 'Four wheeler'), (6, 'Large Vehicle')])
    submit = SubmitField('Update Vehicle')

    def validate_vahicle(self, valicle_number):
        vehicle = Vehicle.query.filter_by(vehicle_number=valicle_number.data).first()
        if vehicle:
            raise ValidationError('Vahicle With Same Number Already Exist!')