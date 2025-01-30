from main import app as a
from app import db
from app.models import HelpRequest, Volunteer
from sqlalchemy import text

# Query the HelpRequest table and get all entries
with a.app_context():
    requests = HelpRequest.query.all()
    for col in HelpRequest.__table__.columns:
        print(col)
    requests = Volunteer.query.all()
    for col in Volunteer.__table__.columns:
        print(col)

    result = db.session.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
    tables = result.fetchall()



# Check if there is data
if requests:
    for request in requests:
        print(f"ID: {request.id}, Name: {request.name}, Age: {request.age}, Gender: {request.gender}, Contact: {request.contact}, Location: {request.location}, Injury: {request.injury}, Transport: {request.transport}")
else:
    print("No data found in the HelpRequest table.")



print("Tables in the database:")
for table in tables:
    print(table[0])  # This will print the names of the tables in the public schema

