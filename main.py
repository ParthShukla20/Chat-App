from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

users ={}

@socketio.on("connect")
def handle_connect():
    print("user connected")
    


@app.route('/')
def index():
    return render_template('index.html')

if __name__ =='__main__':
    socketio.run(app, port=4050, debug = True)