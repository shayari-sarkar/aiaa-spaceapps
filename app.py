# general flask libraries
from flask import Flask, render_template, request

# get reCAPTCHA keys
from config import Config

# create the app
app = Flask(__name__)
app.config.from_object(Config)

# login/register
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("home.html")
    else:
        return render_template("index.html")

# about us
@app.route('/about-us', methods=['GET', 'POST'])
def about():
    return render_template("about-us.html")


if __name__ == '__main__':
   app.run(debug=True)