import sys

from flask_frozen import Freezer
from blog_app import create_app

app = create_app()

freezer = Freezer(app)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()

