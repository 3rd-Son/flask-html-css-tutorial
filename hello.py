from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/page2")
def content():
    return "<h1>This is my first flask app and I hope to do something better next time</h1>"


@app.route("/index/<int:num>")
def table(num):
    return render_template("index.html", n=num)


if __name__ == "__main__":
    app.run(debug=True)
