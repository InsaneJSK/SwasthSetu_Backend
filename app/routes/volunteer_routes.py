from flask import Blueprint, request, jsonify
from app import db
from app.models import Volunteer, User

volunteer_bp = Blueprint("volunteers", __name__)

@volunteer_bp.route("/", methods=["GET"])
def get_volunteers():
    volunteers = Volunteer.query.all()
    return jsonify([{"id": v.id, "user_id": v.user_id, "city": v.city, "rating": v.rating} for v in volunteers])

@volunteer_bp.route("/register", methods=["POST"])
def register_volunteer():
    data = request.get_json()
    user = User.query.get(data["user_id"])

    if not user:
        return jsonify({"error": "User not found"}), 404

    new_volunteer = Volunteer(user_id=user.id, city=data["city"])
    db.session.add(new_volunteer)
    db.session.commit()

    return jsonify({"message": "Volunteer registered!"}), 201
