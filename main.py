from flask import Flask, render_template, request, redirect, url_for
import threading
import socket
import time

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST" and request.form['pass'] == "pass":
        return redirect(url_for("buy"))
    return render_template("home.html")


@app.route("/buy", methods=["POST", "GET"])
def buy():
    if request.method == "POST":
        pass
    return render_template("buy.html")


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("192.168.0.144", 9999))
        while 1:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected')
                time.sleep(10)
                conn.sendall("YEET")
                s.close()
                break


if __name__ == "__main__":
    x = threading.Thread(target=server, daemon=True)
    x.start()
    app.run(debug=True)
