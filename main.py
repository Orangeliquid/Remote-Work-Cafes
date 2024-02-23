from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


# Index app route creation
@app.route("/")
def home():
    return render_template("index.html")


# six geographic Columbus app route creations
@app.route("/osu")
def osu():
    return render_template("osu.html")


@app.route("/downtown")
def downtown():
    return render_template("downtown.html")


@app.route("/north")
def north():
    return render_template("north.html")


@app.route("/east")
def east():
    return render_template("east.html")


@app.route("/south")
def south():
    return render_template("south.html")


@app.route("/west")
def west():
    return render_template("west.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)