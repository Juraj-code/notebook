from app import db
from flask_login import UserMixin

class Person(db.Model):
    __tablename__ = 'people'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, index = True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    birthdate = db.Column(db.String(120), unique=True, nullable=True)

    #   Po zmene v medeli
    #   alembic revision --autogenerate -m ""
    #   alembic upgrade head
    def __repr__(self):
        return f'<It is {self.name}>'
    
    
    
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20))
    description = db.Column(db.String(300))
    
    
    def __repr__(self):
        return f'<User: {self.username}, Role: {self.role}>'
    
    def get_id(self):
        return self.id