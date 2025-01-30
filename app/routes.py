from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, HelpRequest, Volunteer
from .forms import HelpRequestForm, VolunteerForm

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/login")
def login():
    return render_template("login.html")

@main.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")

@main.route("/emergency")
def emergency():
    return render_template("emergency.html")

@main.route("/form", methods=["GET", "POST"])
def form():
    form = HelpRequestForm()

    if form.validate_on_submit():
        # Form is valid, now save to the database
        new_request = HelpRequest(
            name=form.name.data,
            age=form.age.data,
            gender=form.gender.data,
            contact=form.contact.data,
            location=form.location.data,
            injury=form.injury.data,
            transport=form.transport.data,
        )
        try:
            db.session.add(new_request)
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            print(f"Error: {e}")
            flash("There was an error saving your request. Please try again.", "danger")

        flash("Form submitted successfully!", "success")
        return redirect(url_for("main.home"))
    
    return render_template("AskForHelpForm.html", form=form)

@main.route("/volunteer", methods=["GET", "POST"])
def volunteer():
    form = VolunteerForm()

    if form.validate_on_submit():
        # Form is valid, now save to the database
        new_volunteer = Volunteer(
            volunteer_id=form.volunteer_id.data,
            name=form.name.data,
            gender=form.gender.data,
            contact=form.contact.data,
            location=form.location.data,
            father_name=form.father_name.data,
            education=form.education.data,
            vehicle=form.vehicle.data
        )
        try:
            db.session.add(new_volunteer)
            db.session.commit()
            flash("Volunteer registered successfully!", "success")
            return redirect(url_for("main.home"))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash("There was an error registering the volunteer. Please try again.", "danger")
            print(e)

    return render_template("BecomeAVolunteerForm.html", form=form)