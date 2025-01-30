from . import db

class HelpRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    injury = db.Column(db.String(200), nullable=False)
    transport = db.Column(db.String(50), nullable=False)
class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    volunteer_id = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    education = db.Column(db.String(255), nullable=False)
    vehicle = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Volunteer {self.name}>"
