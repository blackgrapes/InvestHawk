from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory('media', filename)
    


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/register.html')
def login():
    return render_template('register.html')

@app.route('/features.html')
def features():
    return render_template('features.html')
    
    
    
@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
