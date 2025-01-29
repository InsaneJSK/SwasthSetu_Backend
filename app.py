from flask import Flask, render_template, request

app = Flask(__name__)

# Home Route (Can be updated later)
@app.route('/')
def home():
    return "Welcome to SwasthSetu Backend"

# Serve Volunteer Form
@app.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'POST':
        volunteer_data = request.form  # Process form data here
        print("Received Volunteer Data:", volunteer_data)
        return "Thank you for registering!"
    return render_template('BecomeAVolunteerForm.html')

# Serve Emergency Page
@app.route('/emergency')
def emergency():
    return render_template('Emergency.html')

# Serve Leaderboard
@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

# Serve Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"Login Attempt: {email}, {password}")
        return "Login Successful!"  # You can integrate authentication later
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
