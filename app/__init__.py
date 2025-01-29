from flask import Flask
from app.routes.home_routes import home_bp
from app.routes.ride_routes import ride_bp
from app.routes.volunteer_routes import volunteer_bp
from app.routes.ambulance_routes import ambulance_bp
from app.routes.leaderboard_routes import leaderboard_bp

def create_app():
    app = Flask(__name__)
    
    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(ride_bp, url_prefix='/rides')
    app.register_blueprint(volunteer_bp, url_prefix='/volunteers')
    app.register_blueprint(ambulance_bp, url_prefix='/ambulance')
    app.register_blueprint(leaderboard_bp, url_prefix='/leaderboard')

    return app
