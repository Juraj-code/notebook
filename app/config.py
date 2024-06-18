import os
from dotenv import load_dotenv

## Configuracia databazy
basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(basedir, '.env'))

# Výpis SQLALCHEMY_DATABASE_URI
# TODO: Vymazat print
print("Environment DATABASE_URL: ", os.getenv('SQLALCHEMY_DATABASE_URI'))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
#    LOG_TO_STDOUT = os.getenv('LOG_TO_STDOUT')