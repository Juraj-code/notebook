from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, index = True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    birthdate = db.Column(db.String(120), unique=True, nullable=True)

    #   Po zmene v medeli
    #   alembic revision --autogenerate -m ""
    #   alembic upgrade head
    def __repr__(self):
        return f'<It is {self.name}>'