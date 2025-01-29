from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')

@home_bp.route('/login')
def login():
    return render_template('login.html')

@home_bp.route('/ask-for-help')
def ask_for_help():
    return render_template('AskForHelpForm.html')

@home_bp.route('/become-a-volunteer')
def become_volunteer():
    return render_template('BecomeAvolunteerForm.html')
