from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length,EqualTo, ValidationError
from project.models import Farmer1
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    Aadhaar = StringField('Aadhaar',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = Farmer1.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    Aadhaar = StringField('Aadhaar',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class LoginAdm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    
class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    Area = StringField('Area',
                           validators=[DataRequired()])
    door_no = StringField('door_no',
                        validators=[DataRequired()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = Farmer1.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

class SuggestForm(FlaskForm):
    tool_name = StringField('tool_name',
                        validators=[DataRequired()])
    size = StringField('size', validators=[DataRequired()])
    submit = SubmitField('suggest')

class OrderForm(FlaskForm):
    username=StringField('username',
                        validators=[DataRequired()])
    tool= StringField('tool', validators=[DataRequired()])
    duration =  StringField('duration', validators=[DataRequired()])
    submit = SubmitField('Add')

class ExtendForm(FlaskForm):
      
    username=StringField('username',
                        validators=[DataRequired()])
    duration=StringField('duration',validators=[DataRequired()]) 
    submit=SubmitField('extend')  

class ListForm(FlaskForm):
    username=StringField('username',validators=[DataRequired()])
