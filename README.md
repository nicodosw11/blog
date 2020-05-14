## Requirements
- Python 3.6.8
- Flask 1.1.2
- Flask-FlatPages 0.7.2

```pip install flask```    
```pip install Flask-FlatPages```

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
└── templates
    ├── base.html
    ├── index.html
    ├── page.html
    ├── partials
    │   └── _list.html
    └── tag.html

```

## Usage

Running ```python main.py```, navigate to the below address in browser:
```
http://localhost:5000
http://localhost:5000/example-text/
```