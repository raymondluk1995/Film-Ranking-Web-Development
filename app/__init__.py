from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_login import LoginManager

from config import Config
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
login = LoginManager(app)
login.login_view = 'login'

from app import routes,models
# from app import models
