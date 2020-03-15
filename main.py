from flask import Flask, render_template, request, redirect, url_for, jsonify
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
        linzen = request.form["linzen"]
        rijst = request.form["rijst"]
        mais = request.form["mais"]
        print((rijst, linzen, mais))
        return ""
    if request.method == "GET":
        return render_template("buy.html", connected=server.connected)


@app.route("/process", methods=["POST"])
def process():
    linzen = request.form["linzen"]
    rijst = request.form["rijst"]
    mais = request.form["mais"]
    print((linzen, rijst, mais))
    return ""



class Server:
    def __init__(self):
        self.conn = None
        self.connected = ""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(("192.168.0.144", 1122))
        x = threading.Thread(target=self.server_daemon, daemon=True)
        x.start()

    def server_daemon(self):
        while 1:
            self.connected = ""
            self.s.listen()
            print('Server listening')
            self.conn, addr = self.s.accept()
            with self.conn:
                self.conn.send(b'Yeet')
                self.connected = "Connected!"

    def send_message(self, msg):
        self.conn.send(msg.encode("utf-8"))

    def get_connected(self):
        return self.connected



def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("192.168.0.144", 1122))
        while 1:
            s.listen()
            conn, addr = s.accept()
            render_template("buy.html", connected="Connected!")
            with conn:
                print('Connected')
                time.sleep(10)
                s.close()
                break


if __name__ == "__main__":
    server = Server()
    app.run(debug=True, use_reloader=False)
