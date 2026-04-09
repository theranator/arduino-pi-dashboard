# app.py

import serial
import threading
from flask import Flask, jsonify, render_template
from collections import deque
import time

PORT = "/dev/ttyACM0"
BAUD = 9600
MAX_READINGS = 60

app = Flask(__name__)
readings = deque(maxlen=MAX_READINGS)
lock = threading.Lock()

def read_serial():
    print(f"Connecting to Arduino on {PORT} at {BAUD} baud...")
    while True:
        try:
            with serial.Serial(PORT, BAUD, timeout=1) as ser:
                ser.reset_input_buffer()
                for _ in range(3):
                    ser.readline()
                while True:
                    line = ser.readline().decode("utf-8", errors="replace").strip()
                    if line:
                        try:
                            temp = float(line)
                            timestamp = time.strftime("%H:%M:%S")
                            with lock:
                                readings.append({"time": timestamp, "temp": temp})
                            print(f"[{timestamp}] {temp}°C")
                        except ValueError:
                            pass
        except serial.SerialException as e:
            print(f"Serial error: {e} — retrying in 3 seconds...")
            time.sleep(3)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    with lock:
        return jsonify(list(readings))

if __name__ == "__main__":
    t = threading.Thread(target=read_serial, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=5000, debug=False)
