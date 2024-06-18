import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(basedir, '.env'))
print('basedir is : '+basedir)
# Výpis SQLALCHEMY_DATABASE_URI
# TODO: Vymazat 
print("Environment DATABASE_URL: ", os.getenv('SQLALCHEMY_DATABASE_URI'))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False    