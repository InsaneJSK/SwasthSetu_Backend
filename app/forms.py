from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange

class HelpRequestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1, max=130)])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], validators=[DataRequired()])
    contact = StringField('Contact', validators=[DataRequired(), Regexp(r'^\+?1?\d{9,15}$', message="Invalid contact number")])
    location = StringField('Location', validators=[DataRequired(), Length(min=1, max=100)])
    injury = StringField('Injury Description', validators=[DataRequired(), Length(min=1, max=200)])
    transport = SelectField('Transport Needed', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class VolunteerForm(FlaskForm):
    volunteer_id = StringField(
        'Volunteer ID',
        validators=[
            DataRequired(),
            Length(min=16, max=16, message="Aadhar number must be exactly 16 digits."),
            Regexp(r'^\d{16}$', message="Aadhar number must contain only digits.")
        ]
    )
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], validators=[DataRequired()])
    contact = StringField('Contact Number', validators=[DataRequired(), Regexp(r'^\+?1?\d{9,15}$', message="Invalid contact number.")])
    location = StringField('Location', validators=[DataRequired(), Length(min=1, max=100)])
    father_name = StringField('Father\'s Name', validators=[DataRequired()])
    education = StringField('Educational Qualifications', validators=[DataRequired()])
    vehicle = SelectField('Mode of Vehicle Owned', choices=[('Car', 'Car'), ('Bike', 'Bike'), ('Cycle', 'Cycle'), ('None', 'None')], validators=[DataRequired()])
    submit = SubmitField('Submit')
