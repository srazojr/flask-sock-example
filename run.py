from flask import Flask, render_template
from flask_sock import Sock
import time
app = Flask(__name__)
sock = Sock(app)


@app.route("/")
def index():
    return render_template("index.html")


@sock.route("/echo")
def echo(sock):
    last_time=time.time()
    count=0
    while True:
        data = sock.receive(timeout=.1)
        if data:
            sock.send(data)
        if (time.time()>(last_time+2.00)):
            count+=1
            sock.send(count)
            last_time=time.time()
            
