from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Ride, User

rides = Blueprint("rides", __name__)

@rides.route("/request", methods=["POST"])
@jwt_required()
def request_ride():
    data = request.json
    patient_id = get_jwt_identity()

    ride = Ride(
        patient_id=patient_id,
        pickup_location=data["pickup_location"],
        drop_location=data["drop_location"],
    )

    db.session.add(ride)
    db.session.commit()
    return jsonify({"message": "Ride request created", "ride_id": ride.id}), 201

@rides.route("/status/<int:ride_id>", methods=["GET"])
@jwt_required()
def get_ride_status(ride_id):
    ride = Ride.query.get(ride_id)
    if ride:
        return jsonify({"ride_id": ride.id, "status": ride.status})
    return jsonify({"message": "Ride not found"}), 404
