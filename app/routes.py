from flask import render_template, flash, redirect,request,json
from app import app,db
from app.forms import LoginForm,RegistrationForm,ShowUserForm,MultiCheckboxField,ShowPollForm,ShowOptionForm,ShowResponseForm
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User,Poll,Option,Behaviour
from flask_login import login_required
from werkzeug.urls import url_parse
from flask import url_for


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
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data) or not login_user(user, remember=form.remember.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        print("next page is ",next_page)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
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

@app.route('/delete_response',methods=['GET','POST'])
def delete_response():
    if (not current_user.administrator or current_user.is_anonymous):
        return redirect(url_for('index'))
    response_form = ShowResponseForm()
    list_of_poll_id = [b.poll_id for b in Behaviour.query.all()]
    list_of_user_id = [b.user_id for b in Behaviour.query.all()]
    list_of_options = [b.option for b in Behaviour.query.all()]
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
        str = list_of_user[i] + ":" +list_of_poll[i] + ":" + list_of_options[i]
        list_of_response.append(str)

    responses = [(x, x) for x in list_of_response]
    response_form.example.choices = responses

    if response_form.validate_on_submit():
        for response_str in response_form.example.data:
            user_name = response_str.split(':')[0]
            poll_name = response_str.split(':')[1]
            user_id = db.session.query(User).filter_by(username=user_name).first().id
            poll_id = db.session.query(Poll).filter_by(poll_name=poll_name).first().id
            db.session.query(Behaviour).filter_by(poll_id=poll_id,user_id=user_id).delete()
            db.session.commit()
        return redirect(url_for('index'))
    return render_template('delete_response.html',title='Delete Response',response_form=response_form)

@app.route('/create_poll',methods=['GET', 'POST'])
def create_poll():
    return render_template("create_poll.html",title='Create Poll')

@app.route('/create_poll_submit',methods=['GET', 'POST'])
def create_poll_submit():
    print("hi")
    poll_name = request.values.get('poll_name')
    options = request.values.get('options')
    category = request.values.get('category')
    description = request.values.get('description')
    print(poll_name)
    print(options)
    print(category)
    print(description)
    #validation part
    categories = ['Romantic Movie','Horror Movie','Fiction Movie','Documentary Movie','Comedy Movie','Action Movie']
    if (poll_name=="" or len(options.split(','))<2 or len(options.split(','))>10 or len(description)>200 or category not in categories):
        return redirect(url_for('index'))
    # In case duplicate options

    options = options.split(',')
    print(len(options))
    print(options)
    print(list(set(options)))
    if(len(options)!=len(list(set(options)))):
        return redirect(url_for('index'))



    if(db.session.query(Poll).filter_by(poll_name=poll_name).first()):
        return redirect(url_for('index'))
    print("Before submit, the description is ",description)
    poll = Poll(poll_name=poll_name,category=category,description=description)
    db.session.add(poll)
    db.session.commit()
    poll_id = Poll.query.filter_by(poll_name=poll_name).first().id
    for option in options:
        insert_option = Option(poll_id=poll_id,option=option)
        db.session.add(insert_option)
        db.session.commit()

    return redirect(url_for('index'))



@app.route('/template/<id>', methods=['GET', 'POST'])
@login_required
def template(id):
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    option_form = ShowOptionForm()
    poll_name = db.session.query(Poll).filter_by(id=id).first().poll_name
    description = db.session.query(Poll).filter_by(id=id).first().description
    list_of_options = [o.option for o in Option.query.filter_by(poll_id=id)]
    list_of_votes = [o.votes for o in Option.query.filter_by(poll_id=id)]
    options_str = (",").join(list_of_options)
    votes_str = ','.join(str(v) for v in list_of_votes)

    options = [(x, x) for x in list_of_options]

    option_form.example.choices = options
    behaviour_existance = db.session.query(Behaviour).filter_by(poll_id=id, user_id = current_user.id).first()

    behaviour = False
    if(behaviour_existance):
        behaviour = True

    if option_form.validate_on_submit():
        if(behaviour==False):
            option_object = Option.query.filter_by(option=option_form.example.data).first()
            option_object.votes +=1
            behaviour_object = Behaviour(poll_id=id,user_id=current_user.id,option=option_form.example.data)
            db.session.add(behaviour_object)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('template.html',title='Vote Here',description=description,labels=options_str,values=votes_str,option_form=option_form,behaviour=behaviour,poll_name=poll_name)
