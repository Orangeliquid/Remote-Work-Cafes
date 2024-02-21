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
    pass
    # return render_template("osu.html")


@app.route("/north")
def north():
    pass
    # return render_template("osu.html") if __name__ == "__main__":
    app.run(debug=True, port=5002)


if __name__ == "__main__":
    app.run(debug=True, port=5002)