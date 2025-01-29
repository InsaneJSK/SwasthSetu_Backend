from flask import Blueprint, jsonify, request
from app.models import db, Leaderboard, User

leaderboard_bp = Blueprint("leaderboard", __name__)

# 🏆 **Get Top N Users on the Leaderboard**
@leaderboard_bp.route("/leaderboard", methods=["GET"])
def get_leaderboard():
    top_n = request.args.get("top_n", default=10, type=int)
    
    leaderboard_data = (
        db.session.query(Leaderboard, User.name)
        .join(User, Leaderboard.user_id == User.id)
        .order_by(Leaderboard.points.desc())
        .limit(top_n)
        .all()
    )

    result = [
        {"rank": idx + 1, "user_id": lb.user_id, "name": user_name, "points": lb.points}
        for idx, (lb, user_name) in enumerate(leaderboard_data)
    ]

    return jsonify({"leaderboard": result}), 200

# 🎖 **Increase User's Points**
@leaderboard_bp.route("/leaderboard/update_points", methods=["POST"])
def update_points():
    data = request.get_json()
    user_id = data.get("user_id")
    points = data.get("points")

    if not user_id or points is None:
        return jsonify({"error": "Missing user_id or points"}), 400

    leaderboard_entry = Leaderboard.query.filter_by(user_id=user_id).first()
    
    if not leaderboard_entry:
        leaderboard_entry = Leaderboard(user_id=user_id, points=0)
        db.session.add(leaderboard_entry)

    leaderboard_entry.points += points
    db.session.commit()

    return jsonify({"message": f"User {user_id} awarded {points} points!"}), 200
