from flask import Flask
from flask_flatpages import FlatPages
# from flask_frozen import Freezer
from flask_assets import Environment, Bundle
from .util.assets import bundles

pages = FlatPages()
# freezer = Freezer()

def create_app(config='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config)

    pages.init_app(app)
    # freezer.init_app(app)

    assets = Environment(app)
    assets.register(bundles)

    from blog_app.posts.routes import posts

    app.register_blueprint(posts)

    return app
