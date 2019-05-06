from flask import render_template, flash, redirect,request
from app import app,db
from app.forms import LoginForm,RegistrationForm,ShowUserForm,MultiCheckboxField,ShowPollForm
from flask_login import current_user,login_user,logout_user
from app.models import User,Poll,Option,Behaviour
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
    list_of_users = [u.username for u in User.query.filter_by(administrator=0)]
    users = [(x, x) for x in list_of_users]
    user_form.example.choices = users

    if user_form.validate_on_submit():
        for user_name in user_form.example.data:
            db.session.query(User).filter_by(username=user_name).delete()
            db.session.commit()
        return redirect(url_for('index'))
    return render_template('delete_user.html',title='Delete User',user_form=user_form)

@app.route('/delete_poll',methods=['GET','POST'])
def delete_poll():
    if (not current_user.administrator or current_user.is_anonymous):
        return redirect(url_for('index'))
    poll_form = ShowPollForm()
    list_of_polls = [p.poll_name for p in Poll.query.all()]
    polls = [(x, x) for x in list_of_polls]
    poll_form.example.choices = polls

    if poll_form.validate_on_submit():
        for poll_name in poll_form.example.data:
            poll_object = db.session.query(Poll).filter_by(poll_name=poll_name).first()
            poll_id = poll_object.id
            print(poll_id)
            db.session.query(Option).filter_by(poll_id=poll_id).delete()
            db.session.query(Behaviour).filter_by(poll_id=poll_id).delete()
            db.session.query(Poll).filter_by(id=poll_id).delete()
            db.session.commit()
        return redirect(url_for('index'))
    return render_template('delete_poll.html',title='Delete Poll',poll_form=poll_form)

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
    #validation part
    categories = ['Romantic Movie','Horror Movie','Fiction Movie','Documentary Movie','Comedy Movie','Action Movie']
    if (poll_name=="" or len(options.split(','))<2 or len(options.split(','))>10  or category not in categories):
        return redirect(url_for('index'))
    poll = Poll(poll_name=poll_name,category=category)
    db.session.add(poll)
    db.session.commit()
    poll_id = Poll.query.filter_by(poll_name=poll_name).first().id
    options = options.split(',')
    for option in options:
        insert_option = Option(poll_id=poll_id,option=option)
        db.session.add(insert_option)
        db.session.commit()

    return redirect(url_for('index'))
