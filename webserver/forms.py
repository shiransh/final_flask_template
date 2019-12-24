from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from webserver.models import User


class LoginForm(Form):
    username = StringField('Your Username:', validators=[DataRequired()])
    password = PasswordField('Your Password:', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class SignUpForm(Form):
    username = StringField('Username:', validators=[DataRequired(), Length(3,80)])
    password = PasswordField('Password:', validators=[DataRequired(),
                                                      EqualTo('password2', message='passwords must match')])
    password2 = PasswordField('Confirm Password:', validators=[DataRequired()])

    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('This username is already taken')
