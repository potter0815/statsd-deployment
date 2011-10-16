from datetime import datetime

from middleware import ReverseProxied

from flask import Flask, render_template
app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)


# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard/<name>/")
def dashboard(name):
    return render_template("dashboards/%s.html" % name)


# Template tags
@app.template_filter("date")
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)

@app.context_processor
def now():
    return dict(now=datetime.now())


if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0")
