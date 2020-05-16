from flask import render_template, Blueprint
from blog_app import pages
from blog_app.models import Paginate as Paginate

posts = Blueprint("posts", __name__)


@posts.route("/")
def index():
    # all_pages = [p for p in pages] #all_pages = [type(p) for p in pages] #all_pages = [p.__dict__ for p in pages]
    all_pages = [p.meta.get("date", []) for p in pages]  # all_pages.sort()
    posts = [page for page in pages if "date" in page.meta]
    sorted_pages = sorted(posts, reverse=True, key=lambda page: page.meta["date"])
    return render_template("index.html", pages=sorted_pages[:2], all=all_pages)

@posts.route("/articles/")
def articles():
    posts = [page for page in pages if "date" in page.meta]
    sorted_pages = sorted(posts, reverse=True, key=lambda page: page.meta["date"])
    PER_PAGE_NUMBER = 2
    page_paginate = Paginate(PER_PAGE_NUMBER, sorted_pages)
    return render_template(
        "index-articles.html",
        pages=sorted_pages[:2],
        paginated=page_paginate.paginated,
        current_per_page_number=PER_PAGE_NUMBER,
        total_num=page_paginate.get_total_number())


@posts.route("/page/<string:num>/")
def per_page(num):
    num = int(num)
    posts = [page for page in pages if "date" in page.meta]
    sorted_pages = sorted(posts, reverse=True, key=lambda page: page.meta["date"])
    PER_PAGE_NUMBER = 2
    page_paginate = Paginate(PER_PAGE_NUMBER, sorted_pages)
    return render_template(
        "index-articles.html",
        pages=page_paginate.get_number_pages(num),
        paginated=page_paginate.paginated,
        current_page_articles=page_paginate.get_number_pages(num),
        current_per_page_number=PER_PAGE_NUMBER,
        total_num=page_paginate.get_total_number()
    )


@posts.route("/welcome/")
def welcome():
    return "Welcome to my webpage!"


@posts.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)  # return pages.get_or_404(path).html


@posts.route("/tag/<string:tag>/")
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get("tags", [])]
    return render_template("tag.html", pages=tagged, tag=tag)


@posts.route("/new/")
def latest():
    # Articles are pages with a date
    articles = (p for p in pages if "date" in p.meta)
    # Show the 3 most recent articles, most recent first.
    latest = sorted(articles, reverse=True, key=lambda p: p.meta["date"])
    return render_template("index.html", pages=latest[:3], all=articles)