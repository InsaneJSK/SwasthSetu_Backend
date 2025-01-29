from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # "patient" or "volunteer"
    gender = db.Column(db.String(10))
    location = db.Column(db.String(100))
    points = db.Column(db.Integer, default=0)

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    volunteer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    status = db.Column(db.String(20), default="pending")  # "pending", "accepted", "completed"
    pickup_location = db.Column(db.String(255), nullable=False)
    drop_location = db.Column(db.String(255), nullable=False)
    request_time = db.Column(db.DateTime, default=datetime.utcnow)
