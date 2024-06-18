from app import db

class Person(db.Model):
    __tablename__ = 'people'
    
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    ## TODO: add more
    
    def __repr__(self) -> str:
        return f'Person with name {self.name}'