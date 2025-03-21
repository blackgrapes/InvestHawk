from flask import Flask, render_template, send_from_directory, redirect, url_for

app = Flask(__name__)


@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory('media', filename)
    


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home.html')
def home2():
            return redirect(url_for("home"))


@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/features.html')
def features():
    return render_template('features.html')
    
    
    
@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
