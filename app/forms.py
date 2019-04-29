from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()],render_kw={"placeholder": "Username..."})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "Password..."})
    submit = SubmitField('Sign In')
