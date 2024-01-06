from flask import Flask, render_template

app = Flask(__name__)


# Base URL
@app.route('/')
def home():
    return render_template('index.html')


# Subpages
@app.route('/home/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/projects/')
def projects():
    return render_template('projects.html')


@app.route('/resume/')
def resume():
    return render_template('resume.html')


@app.route('/content/')
def content():
    return render_template('content.html')


@app.route('/motd/')
def meme():
    return render_template('meme.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
