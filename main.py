from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/welcome/")
def welcome():
    return "Welcome to my webpage!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
