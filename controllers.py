from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm, ShowUserForm, MultiCheckboxField, ShowPollForm, ShowOptionForm, ShowResponseForm
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User,Poll,Option,Behaviour
from flask import request
from werkzeug.urls import url_parse

class UserController():

 def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
          flash('Invalid username or password')
        return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        print("next page is ",next_page)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(redirect(next_page))
    return render_template('login.html', title='Sign In', form=form)


class PollController():

    def poll_list():
        polls= PollController.get_all_polls()
        return render_template('index.html', polls=polls)

    def get_all_polls():
            polls = [p.poll_name for p in Poll.query.all()]
            poll_id = [p.id for p in Poll.query.all()]
            poll_categories = [p.category for p in Poll.query.all()]
            user_preference=[]
