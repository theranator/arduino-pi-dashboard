# Arduino Pi Dashboard

A live temperature monitoring dashboard built with an Arduino Uno, Raspberry Pi 3, and Python Flask.

## How It Works

- Arduino Uno reads temperature from a TMP36 analog sensor
- Sends readings over USB serial in the format `Temp: 24.78 C | 76.60 F`
- Raspberry Pi runs a Python Flask web server that reads the serial data
- A browser-based dashboard at `http://<pi-ip>:5000` displays a live updating graph

## Hardware

- Arduino Uno
- TMP36 temperature sensor
- Raspberry Pi 3
- USB cable (Arduino → Pi)

## Software

- Python 3
- Flask
- pyserial
- Chart.js (via CDN)

## Setup

1. Upload the Arduino sketch (see [serial-logger](https://github.com/theranator/serial-logger))
2. Clone this repo onto your Raspberry Pi
3. Install dependencies: `pip install flask pyserial`
4. Run: `python3 app.py`
5. Open `http://<your-pi-ip>:5000` in any browser on your network

## Project Status

✅ Complete and running
