from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory('media', filename)
    


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
