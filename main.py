from flask import Flask, render_template
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)


@app.route("/")
def index():
    # all_pages = [p for p in pages] #all_pages = [type(p) for p in pages] #all_pages = [p.__dict__ for p in pages]
    all_pages = [p.meta.get('date', []) for p in pages] #all_pages.sort()
    return render_template("index.html", pages=pages, all=all_pages)


@app.route("/welcome/")
def welcome():
    return "Welcome to my webpage!"


@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)  # return pages.get_or_404(path).html


@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
