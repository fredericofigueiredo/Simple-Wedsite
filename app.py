from flask import Flask, render_template
import requests

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

# Random pages


@app.route('/whoop/')
def whoop():
    return render_template('whoop.html')


# Callback for API requests
# WHOOP
CLIENT_ID = 'e3e04efa-6588-40a9-a883-d6868dc31a6f'
CLIENT_SECRET = 'e9c1d09f752c2d17ccb596b8edc0e755a6b8610d7f7e83d86f3cad268161608c'
# Replace with the API's token URL
TOKEN_URL = 'https://api.example.com/oauth/token'


@app.route('/whoop-callback')
def callback():
    code = request.args.get('code')

    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        # Replace with your actual redirect URI
        'redirect_uri': 'http://localhost:3000/whoop-callback',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(TOKEN_URL, data=payload)

    if response.status_code == 200:
        access_token = response.json().get('access_token')
        # Now you can use the access token to make authenticated requests to the API
        return "Access token received"
    else:
        return "Error getting access token", 400


if __name__ == '__main__':
    app.run(debug=True)
