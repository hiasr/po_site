from flask import Flask, render_template, request, redirect, url_for, jsonify
import time
import serial

app = Flask(__name__)
angle = 0
speed = "slow"
motor = 'false'

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


@app.route("/stream", methods=["GET", "POST"])
def stream():
    if request.method == "POST":
        bluetoothSerial = serial.Serial("/dev/rfcomm0", baudrate=9600)
        global angle, speed, motor
        if request.form["angle"] != angle:
            angle = request.form["angle"]
            bluetoothSerial.write('B{}'.format(angle))
            time.sleep(0.01)

        if request.form["speed"] != speed or request.form["motor"] != motor:
            speed = request.form["speed"]
            motor = request.form["motor"]
            if motor == 'true':
                motor_nb = 1
            else:
                motor_nb = 0
            if speed == 'slow':
                speed_nb = 40
            elif speed == 'medium':
                speed_nb = 100
            else:
                speed_nb = 255
            bluetoothSerial.write('A{0}{1}'.format(motor_nb, speed_nb))

        return ""
    else:
        return render_template("stream.html")




if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

