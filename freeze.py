import sys

from flask_frozen import Freezer
from blog_app import create_app

app = create_app()

freezer = Freezer(app)

@freezer.register_generator
def page_url_generator():  # Some other function name
    # `(endpoint, values)` tuples
    yield 'posts.per_page', {'num': '1'}
    yield 'posts.per_page', {'num': '2'}
    yield 'posts.per_page', {'num': '3'}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze() # freezer.run(debug=True)

