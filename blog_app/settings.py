import os

REPO_NAME = "blog"  # Used for FREEZER_BASE_URL
DEBUG = True

# Assumes the app is located in the same directory
# where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__)) # blog_app

def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, you must build the static files to
# the project root
# build the static content to the project root instead of the default build/ directory
FREEZER_DESTINATION = PROJECT_ROOT # alternatively FREEZER_DESTINATION = os.path.join(PROJECT_ROOT, 'build')
FREEZER_DESTINATION_IGNORE = ['.git*']

# Since this is a repo page (not a Github user page),
# we need to set the BASE_URL to the correct url as per GH Pages' standards
# http://username.github.com/your-reponame or explicitly set FREEZER_BASE_URL
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME) # defaults to 'http://localhost/'
# FREEZER_RELATIVE_URLS = False # defaults
FREEZER_REMOVE_EXTRA_FILES = True  # IMPORTANT: If this is True (the default), all app files
                                    # will be deleted when you run the freezer
# FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite'] # defaults
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages') # or FLATPAGES_ROOT = os.path.join(PROJECT_ROOT, 'pages')
# FLATPAGES_AUTO_RELOAD = DEBUG # defaults
FLATPAGES_EXTENSION = ".md"