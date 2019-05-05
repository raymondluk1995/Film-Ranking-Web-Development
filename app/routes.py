from flask import render_template, flash, redirect,request
from app import app,db
from app.forms import LoginForm,RegistrationForm,ShowUserForm,MultiCheckboxField
from flask_login import current_user,login_user,logout_user
from app.models import User
from flask_login import login_required
from werkzeug.urls import url_parse
from flask import url_for


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # username = request.form.get('form-username')
    # password = request.form.get('form-password')
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        preference_string = ",".join(form.example.data)
        user = User(username=form.username.data, email=form.email.data,preference=preference_string)
        print(form.example.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/delete_user',methods=['GET','POST'])
def delete_user():
    if (not current_user.administrator or current_user.is_anonymous):
        return redirect(url_for('index'))
    user_form = ShowUserForm()
    # user_form.update()
    list_of_users = [u.username for u in User.query.filter_by(administrator=0)]
    users = [(x, x) for x in list_of_users]
    # user_form.example = MultiCheckboxField('Label', choices=users)
    user_form.example.choices = users
    # print(users)
    # print("\n\n\n")
    # print(MultiCheckboxField('Label', choices=users))
    if user_form.validate_on_submit():
        # print(user_form.example.data)
        for user_name in user_form.example.data:
            # user = User.query.filter_by(username=user_name).delete()
            db.session.query(User).filter_by(username=user_name).delete()
            # db.session.delete(user)
            db.session.commit()

        # list_of_users = [u.username for u in User.query.filter_by(administrator=0)]
        # users = [(x, x) for x in list_of_users]
        # print(users)
        return redirect(url_for('index'))
    return render_template('delete_user.html',title='Delete User',user_form=user_form)

@app.route('/create_poll',methods=['GET', 'POST'])
def create_poll():
    return render_template("create_poll.html",title='Create Poll')

@app.route('/create_poll_submit',methods=['GET', 'POST'])
def create_poll_submit():
    poll_name = request.values.get('poll_name')
    options = request.values.get('options')
    category = request.values.get('category')
    print(poll_name)
    print(options)
    print(category)
    return redirect(url_for('index'))
