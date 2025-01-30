from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure the database (update with your actual database URI)
    app.config['SECRET_KEY'] = '3fcd98008c88147bfd0bec3a'
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost/swasthsetu"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app
