from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST" and request.form['pass'] == "pass":
        return redirect(url_for("buy"))
    return render_template("home.html")


@app.route("/buy")
def buy():
    return render_template("buy.html")


if __name__ == "__main__":
    app.run(debug=True)
