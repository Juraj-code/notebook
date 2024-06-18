from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
import os

# import logging
# from logging import RotationgFileHandler, SMTPHandler

# TODO: Implementuj logovanie

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

## Globálna premenná na sledovanie inicializácie
initialization_done = False
    
## Inicializacia databazy 
@app.before_request
def create_tables():
    global initialization_done
    if not initialization_done:
        db.create_all()
        initialization_done = True    


from app import routes