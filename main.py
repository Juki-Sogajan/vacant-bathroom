import serial
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer


# Config
device_serial_path = "/dev/tty.usbmodem101"
device_serial_rate = 9600
server_address = ("", 80) # HOST, PORT


class serial_device:
    def __init__(self, name: str, device: str, rate: int):
        self.name = name
        self.devpath = device
        self.rate = rate
    
    def read(self):
        with serial.Serial(self.devpath, self.rate) as instance:
            return instance.readline()
    
    def list(self):
        return self.name + ":\t" + self.read().decode()
        

class MainHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """GETリクエストの処理"""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(value.encode())

value = ""
RestroomSensor1 = serial_device("4F", device_serial_path, device_serial_rate)
httpd = HTTPServer(server_address, MainHTTPHandler)

def start_server():
    httpd.serve_forever()

thread = threading.Thread(target=start_server)
thread.daemon = True
thread.start()

while True:
    value = RestroomSensor1.list()