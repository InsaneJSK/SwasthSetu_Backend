from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import db, User

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    data = request.json
    hashed_password = generate_password_hash(data["password"])
    user = User(name=data["name"], email=data["email"], password=hashed_password, role=data["role"], gender=data.get("gender"))
    
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    
    if user and check_password_hash(user.password, data["password"]):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token, "user_id": user.id})
    
    return jsonify({"message": "Invalid credentials"}), 401
