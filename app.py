from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import os
import bcrypt

# ✅ Initialize Flask App
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# ✅ MySQL Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:772002@localhost/investhawk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ✅ Initialize Database
db = SQLAlchemy(app)

# ✅ Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Redirects to login page if unauthorized

# ✅ User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    
    def __init__(self, fullname, email, username, password):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# ✅ Create Tables (Ensure tables exist before running)
with app.app_context():
    db.create_all()

# ✅ User Loader (Required for Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ✅ Serve Media Files
@app.route('/media/<path:filename>')
def media(filename):
    media_folder = os.path.join(app.root_path, 'media')
    return send_from_directory(media_folder, filename)

# ✅ Home Route
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/home.html")
def home2():
    return redirect (url_for("home"))


# ✅ Login Route
@app.route("/login.html", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)  # Login the user
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password", "danger")
    
    return render_template('login.html')

# ✅ Register Route


@app.route("/register.html", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        fullname = request.form.get("fullname")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        # Debugging print statement
        print(f"Received data: {fullname}, {email}, {username}, {password}")

        if not (fullname and email and username and password):
            flash("All fields are required!", "danger")
            return redirect(url_for("register"))

        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("register"))

        # Check if user already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash("Username or Email already exists!", "danger")
            return redirect(url_for("register"))

        # Hash password before saving
        hashed_password = generate_password_hash(password)

        # Create new user
        new_user = User(fullname=fullname, email=email, username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


# ✅ Features Route
@app.route('/features.html')
def features():
    return render_template('features.html')

# ✅ Dashboard Route (Protected)
@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html', user=current_user)

# ✅ Logout Route (Protected)
@app.route('/logout.html')
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('login.html'))

# ✅ Run Flask App
if __name__ == '__main__':
    app.run(debug=True, port=5000)
