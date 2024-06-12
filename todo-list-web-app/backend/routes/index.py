from flask import Flask, Blueprint, render_template

# Define the blueprint for the index route
index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html', current_route='index')

# Create the Flask application
app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html', current_route='login')

# Register the blueprint
app.register_blueprint(index_bp)

if __name__ == '__main__':
    app.run(debug=True)
