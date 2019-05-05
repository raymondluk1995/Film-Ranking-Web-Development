from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  SubmitField, SelectMultipleField,widgets
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models import User
from app import db
from wtforms_sqlalchemy.fields import QuerySelectField



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()],render_kw={"placeholder": "Username..."})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "Password..."})
    submit = SubmitField('Sign In')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class RegistrationForm(FlaskForm):
    username = StringField('Username (at least 4 characters and maximum 10 characters)', validators=[DataRequired(),Length(min=4,max=10)],render_kw={"placeholder": "Username..."})
    email = StringField('Email', validators=[DataRequired(), Email()],render_kw={"placeholder": "Email..."})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "Password..."})
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')],render_kw={"placeholder": "Repeat Password..."})
    submit = SubmitField('Register')

    string_of_preference = ['Romantic Movie,Horror Movie,Fiction Movie,Documentary Movie,Comedy Movie,Action Movie']
    list_of_preference = string_of_preference[0].split(',')
    preference = [(x, x) for x in list_of_preference]
    example = MultiCheckboxField('Label', choices=preference)

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

    def validate_example(self,example):
        if(len(self.example.data)<1):
            raise ValidationError('Please choose at least one preference')

class ShowUserForm(FlaskForm):
    list_of_users = [u.username for u in User.query.filter_by(administrator=0)]
    users = [(x, x) for x in list_of_users]
    example = MultiCheckboxField('Label', choices=users)
    # print(example)

    submit = SubmitField('Delete User')

    # def update(self):
    #     list_of_users = [u.username for u in User.query.filter_by(administrator=0)]
    #     users = [(x, x) for x in list_of_users]
    #     # print(self.users)
    #     self.example = MultiCheckboxField('Label',choices=users)
    #     print(self.example)

    def validate_example(self,example):
        if(len(self.example.data)<1):
            raise ValidationError('You are not deleting any user!')


# class CreatePollForm(FlaskForm):
#     pollname = StringField('Pollname', validators=[DataRequired(),Length(max=40)]],render_kw={"placeholder": "Poll Name..."})
