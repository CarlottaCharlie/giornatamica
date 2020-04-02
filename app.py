from flask_table import Table, Col, LinkCol
from flask import Flask, Markup, request, url_for, session
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_login import current_user
from flask_session import Session
#from flask.ext.session import Session

import json
import os
import time
import numpy as np
basedir = os.path.abspath(os.path.dirname(__file__))
# general settings, TOOD will be replaced by file reading
SECRET_KEY = 'B1Zr548j/3yX M~XEH!1mN]LWX/,?NT'
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'reference_database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSIONS_PER_PAGE = 20
    MAX_SEARCH_RESULTS = 20
    SECRET_KEY = SECRET_KEY
    DEBUG = False
    FLASK_APP = "GPU_SDR"


app = Flask(__name__)
app.secret_key =SECRET_KEY
app.config.from_object(Config)
app.config['SESSION_TYPE'] = 'filesystem'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
socketio = SocketIO(app)
Session(app)

# MUST be after app init
from routes import *

if __name__ == '__main__':
    socketio.run(app, host= "0.0.0.0", port = "5000")
