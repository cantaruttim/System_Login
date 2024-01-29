from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from Homepage.models import User


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    button_submit = SubmitField("Login")


class FormCreateAccount(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('User name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6,8)])
    pass_submit = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    button_submit = SubmitField('Submit')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            return ValidationError("E-mail alredy register. Do login to continue!")