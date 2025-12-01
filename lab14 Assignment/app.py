from flask import Flask, render_template, request

# Create a Flask web application instance
app = Flask(__name__)

# Route for the home page, which serves the login form
@app.route('/')
def index():
    """
    Serves the login form.
    This function renders the 'task-3.html' template.
    """
    return render_template('task-3.html')

# Route to handle the form submission from '/login'
@app.route('/login', methods=['POST'])
def login():
    """
    Handles the login form submission.
    It retrieves the username from the form data, prints it to the console,
    and returns a success message to the user.
    """
    username = request.form.get('username')
    print(f"Login attempt from username: {username}")
    return f"<h1>Login Successful!</h1><p>Welcome, {username}!</p>"

# Run the app
if __name__ == '__main__':
    # Runs the Flask app on the local development server
    app.run(debug=True)