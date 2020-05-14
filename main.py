from flask import Flask, render_template
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)


@app.route("/")
@app.route("/welcome/")
def welcome():
    return "Welcome to my webpage!"


@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)  # return pages.get_or_404(path).html


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
