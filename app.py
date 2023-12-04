from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Route to render the HTML form


@app.route('/')
def index():
    return render_template('index.html')


# Route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save the form data to a database or file
        print(f"Name: {name}, Email: {email}, Message: {message}")

        # Return a success message
        response_message ='Form submitted successfully!'

        meme_url = generate_meme(message)
        
        return jsonify({"message": response_message, "meme_url": meme_url})


def generate_meme(text):
    
    url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"

    querystring = {"meme":"TBD","bottom":"TBD","top":"TBD","font":"Impact","font_size":"50"}

    headers = {
        "X-RapidAPI-Key": "0ada951614mshebf9bd422035583p1eb42djsn394e9bfa58d0",
        "X-RapidAPI-Host": "ronreiter-meme-generator.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)


    return response.json()


if __name__ == '__main__':
    app.run(debug=True)