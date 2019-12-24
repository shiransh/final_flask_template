from flask import render_template, flash, redirect, url_for, request, Response
from flask_login import login_required, login_user, logout_user
from webserver import app, db, login_manager
from webserver.forms import LoginForm, SignUpForm
from webserver.models import User
from webserver import webinfra
import random


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user:
        user = User.get_by_username(username=form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user=user, remember=form.remember_me.data)
            flash('Logged in successfully as {}'.format(user.username))
            return redirect(request.args.get('next') or url_for('index'))
        flash('Incorrect username or password')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcome {}, Please login'.format(user.username))
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/example_stream/', methods=['GET', 'POST'])
@login_required
def example_stream():
    # this is an example for javascript stream to the client
    my_string = 'Random int is: {}'.format(random.randint(0,100000))
    # this function converts the text to the expected format:
    my_string = webinfra.get_js_data(my_string)
    return Response(my_string, content_type='text/event-stream')


@app.route('/example_jinja2_usage/')
@login_required
def example_jinja2_usage():
    # jinja2 is an easy way to send object from server to client
    # This example describes simple usage of transfer items from db model from server to client and display it
    user = User.get_by_username('admin')
    return render_template('example_jinja.html', jinja_object=user)


@app.route('/example_javascript_stream_page/', methods=['GET', 'POST'])
@login_required
def example_javascript_stream_page():
    return render_template('example_javascript_stream.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
