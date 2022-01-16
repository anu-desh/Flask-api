from space import db

class User(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(length = 20), nullable = False)
    email = db.Column(db.String(length = 30), nullable = False, unique = True)

    def __init__(self,name,email):
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return "Name : "+ self.name
    
    @property
    def serialize(self):
        return {"id":self.id, "name": self.name, "email": self.email}
