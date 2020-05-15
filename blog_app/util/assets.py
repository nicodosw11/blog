from flask_assets import Bundle

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