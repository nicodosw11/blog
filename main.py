import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask_assets import Environment, Bundle

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

bundles = {
    "home_js": Bundle(
        "js/custom.js", "js/log.js", filters="jsmin", output="dist/js/main.min.js"
    ),
    "home_css": Bundle(
        "css/main.scss",
        depends=["css/*.scss"],
        filters="libsass",
        output="dist/css/style.css",
    ),
}
assets = Environment(app)
assets.register(bundles)


@app.route("/")
def index():
    # all_pages = [p for p in pages] #all_pages = [type(p) for p in pages] #all_pages = [p.__dict__ for p in pages]
    all_pages = [p.meta.get("date", []) for p in pages]  # all_pages.sort()
    return render_template("index.html", pages=pages, all=all_pages)


@app.route("/welcome/")
def welcome():
    return "Welcome to my webpage!"


@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)  # return pages.get_or_404(path).html


@app.route("/tag/<string:tag>/")
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get("tags", [])]
    return render_template("tag.html", pages=tagged, tag=tag)


@app.route("/new/")
def latest():
    # Articles are pages with a date
    articles = (p for p in pages if "date" in p.meta)
    # Show the 3 most recent articles, most recent first.
    latest = sorted(articles, reverse=True, key=lambda p: p.meta["date"])
    return render_template("index.html", pages=latest[:3], all=articles)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True, host="0.0.0.0")
