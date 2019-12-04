from project import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return Farmer1.query.get(int(id))

class Farmer1(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    Aadhaar = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.Aadhaar}')"


class Admin1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Admin('{self.username}')"


class Tools1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(20), nullable=False)
    count = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return f"Tools('{self.tool_name}','{self.count}')"

class Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= username = db.Column(db.String(20), unique=True, nullable=False)
    door_no=db.Column(db.String(5))
    Area=db.Column(db.String(10))

    def __repr__(self):
        return f"Details('{self.username}','{self.door_no}','{self.Area}')"

class Suggestions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tool_name= db.Column(db.String(20), unique=True, nullable=False)
    size=db.Column(db.String(5))

    def __repr__(self):
        return f"Suggestions('{self.tool_name}','{self.size}')"

class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),nullable=False)
    tool=db.Column(db.String(20),nullable=False)
    duration=db.Column(db.String(2),nullable=False)

    def __repr__(self):
        return f"Order('{self.username}','{self.tool}','{self.duration}')"

class Extend(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),nullable=False)
    duration=db.Column(db.String(2),nullable=False)

    def __repr__(self):
        return f"Order('{self.username}','{self.duration}')"