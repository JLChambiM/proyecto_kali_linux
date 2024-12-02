from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/processes')
def processes():
    return render_template('pages/processes.html')

@app.route('/memory')
def memory():
    return render_template('pages/memory.html')

@app.route('/distributed')
def distributed():
    return render_template('pages/distributed.html')

@app.route('/servers')
def servers():
    return render_template('pages/servers.html')

if __name__ == '__main__':
    app.run(debug=True)