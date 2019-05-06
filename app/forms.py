from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  SubmitField, SelectMultipleField,widgets,RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models import User,Poll,Option,Behaviour
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
    submit = SubmitField('Delete User')
    def validate_example(self,example):
        if(len(self.example.data)<1):
            raise ValidationError('You are not deleting any user!')

class ShowPollForm(FlaskForm):
    list_of_polls = [p.poll_name for p in Poll.query.all()]
    polls = [(x, x) for x in list_of_polls]
    example = MultiCheckboxField('Label', choices=polls)
    submit = SubmitField('Delete Form')
    def validate_example(self,example):
        if(len(self.example.data)<1):
            raise ValidationError('You are not deleting any poll!')

class ShowOptionForm(FlaskForm):
    list_of_options = [o.option for o in Option.query.all()]
    options = [(x, x) for x in list_of_options]
    example = RadioField('Label',choices=options)
    submit = SubmitField('Submit Your Vote')

    def validate_example(self,example):
        if(self.example.data==""):
            raise ValidationError('You are not voting any option!')

class ShowResponseForm(FlaskForm):
    list_of_poll_id = [b.poll_id for b in Behaviour.query.all()]
    list_of_user_id = [b.user_id for b in Behaviour.query.all()]
    list_of_poll = []
    list_of_user = []
    list_of_response=[]
    for poll_id in list_of_poll_id:
        poll_name = db.session.query(Poll).filter_by(id=poll_id).first().poll_name
        list_of_poll.append(poll_name)
    for user_id in list_of_user_id:
        user_name = db.session.query(User).filter_by(id=user_id).first().username
        list_of_user.append(user_name)

    for i in range(len(list_of_user)):
        str = list_of_user[i] + ":" +list_of_poll[i]
        list_of_response.append(str)

    responses = [(x, x) for x in list_of_response]
    example = MultiCheckboxField('Label', choices=responses)
    submit = SubmitField('Delete Response')
    def validate_example(self,example):
        if(len(self.example.data)<1):
            raise ValidationError('You are not deleting any response!')
