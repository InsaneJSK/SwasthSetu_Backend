from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from app.models import db
from app.routes.auth import auth
from app.routes.rides import rides
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    JWTManager(app)
    Migrate(app, db)
    CORS(app)
    
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(rides, url_prefix="/rides")
    
    return app
