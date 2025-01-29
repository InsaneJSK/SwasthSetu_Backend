from flask import Blueprint, request, jsonify
from app.models import db, RideRequest
from datetime import datetime

ambulance_bp = Blueprint("ambulance", __name__)

# Sample ambulance data (Replace with actual database queries if needed)
ambulances = [
    {"id": 1, "lat": 28.7041, "lng": 77.1025, "status": "Available"},  # Example coordinates (Delhi)
    {"id": 2, "lat": 19.0760, "lng": 72.8777, "status": "On Duty"},    # Example coordinates (Mumbai)
]

# 🚑 **Get List of Available Ambulances**
@ambulance_bp.route("/ambulances", methods=["GET"])
def get_ambulances():
    available_ambulances = [amb for amb in ambulances if amb["status"] == "Available"]
    return jsonify({"ambulances": available_ambulances}), 200

# 📍 **Request an Ambulance**
@ambulance_bp.route("/request_ambulance", methods=["POST"])
def request_ambulance():
    data = request.get_json()

    if "user_id" not in data or "location" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    ride_request = RideRequest(
        user_id=data["user_id"],
        location=data["location"],
        emergency=True,  # Ambulance requests are always emergencies
        status="Requested",
        created_at=datetime.utcnow(),
    )
    db.session.add(ride_request)
    db.session.commit()

    return jsonify({"message": "Ambulance requested successfully!", "request_id": ride_request.id}), 201

# 🚑 **Update Ambulance Status (Admin Use)**
@ambulance_bp.route("/update_ambulance_status/<int:ambulance_id>", methods=["PUT"])
def update_ambulance_status(ambulance_id):
    data = request.get_json()
    new_status = data.get("status", "").capitalize()

    for ambulance in ambulances:
        if ambulance["id"] == ambulance_id:
            ambulance["status"] = new_status
            return jsonify({"message": f"Ambulance {ambulance_id} status updated to {new_status}"}), 200

    return jsonify({"error": "Ambulance not found"}), 404
