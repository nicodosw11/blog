## Requirements
- Python 3.6.8
- Flask 1.1.2
- Flask-FlatPages 0.7.2
- Frozen-Flask 0.15
- Flask-Assets 2.0
- cssmin 0.2.0
- jsmin 2.2.2
- libsass 0.20.0

```pip install flask```    
```pip install Flask-FlatPages```
```pip install Frozen-Flask```  
```pip install Flask-Assets```  
```pip install jsmin```  
```pip install cssmin```  
```pip install libsass```

## Project Structure

```
.
├── main.py
├── pages
│   ├── article-1.md
│   ├── article-2.md
│   ├── article-3.md
│   ├── article-4.md
│   ├── article-5.md
│   └── example-text.md
├── static
│   ├── css
│   │   ├── _base.scss
│   │   ├── _homepage.scss
│   │   ├── _variables.scss
│   │   └── main.scss
│   ├── dist
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.min.js
│   └── js
│       ├── custom.js
│       └── log.js
└── templates
    ├── base.html
    ├── index.html
    ├── page.html
    ├── partials
    │   └── _list.html
    └── tag.html

```

Blueprints

```

.
├── blog_app
│   ├── __init__.py
│   ├── models.py
│   ├── pages
│   │   ├── article-1.md
│   │   ├── article-2.md
│   │   ├── article-3.md
│   │   ├── article-4.md
│   │   ├── article-5.md
│   │   └── example-text.md
│   ├── posts
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── static
│   │   ├── css
│   │   │   ├── _articles.scss
│   │   │   ├── _test.scss
│   │   │   ├── abstracts
│   │   │   │   ├── _mixins.scss
│   │   │   │   └── _variables.scss
│   │   │   ├── base
│   │   │   │   ├── _animations.scss
│   │   │   │   ├── _base.scss
│   │   │   │   └── _typography.scss
│   │   │   ├── components
│   │   │   │   ├── _avatar.scss
│   │   │   │   ├── _spinner.scss
│   │   │   │   └── _up.scss
│   │   │   └── main.scss
│   │   ├── dist
│   │   │   ├── css
│   │   │   │   └── style.css
│   │   │   └── js
│   │   │       └── main.min.js
│   │   ├── fonts
│   │   │   ├── icomoon.eot
│   │   │   ├── icomoon.svg
│   │   │   ├── icomoon.ttf
│   │   │   └── icomoon.woff
│   │   ├── img
│   │   │   ├── avatar.jpeg
│   │   │   ├── clapham.jpg
│   │   │   ├── parisquai-panorama.jpg
│   │   │   ├── programmer.jpeg
│   │   │   ├── python.jpg
│   │   │   ├── reuters.jpeg
│   │   │   └── top-view-of-paris.jpg
│   │   └── js
│   │       ├── custom.js
│   │       └── log.js
│   ├── templates
│   │   ├── base-articles.html
│   │   ├── base.html
│   │   ├── index-all.html
│   │   ├── index-articles.html
│   │   ├── index.html
│   │   ├── page.html
│   │   ├── partials
│   │   │   ├── _articles.html
│   │   │   ├── _avatar.html
│   │   │   └── _list.html
│   │   └── tag.html
│   └── util
│       └── assets.py
├── freeze.py
└── main.py

```

## Usage

Running ```python main.py```, navigate to the below address in browser:
```
http://localhost:5000
http://localhost:5000/example-text/
```

## Build static set of files and assets

```python freeze.py build```

```

.
├── article-1
│   └── index.html
├── article-2
│   └── index.html
├── article-3
│   └── index.html
├── article-4
│   └── index.html
├── article-5
│   └── index.html
├── articles
│   └── index.html
├── example-text
│   └── index.html
├── index.html
├── new
│   └── index.html
├── page
│   ├── 1
│   │   └── index.html
│   ├── 2
│   │   └── index.html
│   └── 3
│       └── index.html
├── static
│   ├── css
│   │   ├── _articles.scss
│   │   ├── _test.scss
│   │   ├── abstracts
│   │   │   ├── _mixins.scss
│   │   │   └── _variables.scss
│   │   ├── base
│   │   │   ├── _animations.scss
│   │   │   ├── _base.scss
│   │   │   └── _typography.scss
│   │   ├── components
│   │   │   ├── _avatar.scss
│   │   │   ├── _spinner.scss
│   │   │   └── _up.scss
│   │   └── main.scss
│   ├── dist
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.min.js
│   ├── fonts
│   │   ├── icomoon.eot
│   │   ├── icomoon.svg
│   │   ├── icomoon.ttf
│   │   └── icomoon.woff
│   ├── img
│   │   ├── avatar.jpeg
│   │   ├── clapham.jpg
│   │   ├── parisquai-panorama.jpg
│   │   ├── programmer.jpeg
│   │   ├── python.jpg
│   │   ├── reuters.jpeg
│   │   └── top-view-of-paris.jpg
│   └── js
│       ├── custom.js
│       └── log.js
├── tag
│   ├── awesome
│   │   └── index.html
│   ├── general
│   │   └── index.html
│   └── stuff
│       └── index.html
└── welcome
    └── index.html

```