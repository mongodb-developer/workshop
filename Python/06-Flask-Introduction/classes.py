from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField

class CreateEmployee(FlaskForm):
    name = TextField('Employee Name')
    age = IntegerField('Age')
    email = TextField('Email Address')
    country = TextField('Country')
    create = SubmitField('Create')

class DeleteEmployee(FlaskForm):
    key = TextField('Employee ID')
    name = TextField('Name')
    delete = SubmitField('Delete')

class UpdateEmployee(FlaskForm):
    key = TextField('Employee ID')
    name = TextField('Name')
    update = SubmitField('Update')

class ResetEmployee(FlaskForm):
    reset = SubmitField('Reset')
