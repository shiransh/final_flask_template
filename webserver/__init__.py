import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))
db_file_path = os.path.join(basedir, 'app.db')

app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file_path
app.config['DEBUG'] = True

#configure authentication:
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.session_protection = "login"
login_manager.login_view = "login"
login_manager.init_app(app=app)

db = SQLAlchemy(app)

print('db file located at: {}'.format(db_file_path))