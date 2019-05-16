from flask import render_template, flash, redirect,request,json
from app import app,db
from app.forms import LoginForm,RegistrationForm,ShowUserForm,MultiCheckboxField,ShowPollForm,ShowOptionForm,ShowResponseForm
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User,Poll,Option,Behaviour
from flask_login import login_required
from werkzeug.urls import url_parse
from flask import url_for
from app.controllers import UserController, PollController


@app.route('/')
@app.route('/index')
def index():
    polls = [p.poll_name for p in Poll.query.all()]
    poll_id = [p.id for p in Poll.query.all()]
    poll_categories = [p.category for p in Poll.query.all()]
    user_preference=[]
    if current_user.is_authenticated:
        user_preference = current_user.preference.split(',')
    return render_template("index.html",title='Home',polls=polls,user_preference=user_preference,poll_categories=poll_categories,poll_id=poll_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    return UserController.login()
@app.route('/logout')
def logout():
    # logout_user()
    # return redirect(url_for('index'))
  return UserController.logout()



@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    return UserController.register()

@app.route('/delete_user',methods=['GET','POST'])
def delete_user():
    if (not current_user.administrator or current_user.is_anonymous):
        return redirect(url_for('index'))

    return UserController.delete_user()

@app.route('/delete_poll',methods=['GET','POST'])
def delete_poll():
    if (not current_user.administrator or current_user.is_anonymous):
        return redirect(url_for('index'))

    return PollController.delete_poll()


@app.route('/delete_response',methods=['GET','POST'])
def delete_response():
    if (not current_user.administrator or current_user.is_anonymous):
        return redirect(url_for('index'))
    return PollController.delete_response()

@app.route('/create_poll',methods=['GET', 'POST'])
def create_poll():
    return render_template("create_poll.html",title='Create Poll')

@app.route('/create_poll_submit',methods=['GET', 'POST'])
def create_poll_submit():
    return PollController.create_poll_submit()




@app.route('/template/<id>', methods=['GET', 'POST'])
@login_required
def template(id):
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    return PollController.template(id)
    
