from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


# import logging
# from logging import RotationgFileHandler, SMTPHandler

# TODO: Implementuj logovanie
# TODO: Prerob na Factory

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
app.secret_key = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)

from app.models import User

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

bcrypt = Bcrypt(app)


## Globálna premenná na sledovanie inicializácie databazy
initialization_done = False
    
## Inicializacia databazy 
@app.before_request
def create_tables():
    global initialization_done
    if not initialization_done:
        db.create_all()
        initialization_done = True    


from app import routes