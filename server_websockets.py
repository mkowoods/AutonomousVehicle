
from flask import Flask, session, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
import config
import logging
import time

logging.basicConfig(level=logging.WARNING)

#socketio = SocketIO()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if config.PRODUCTION:
    #import gopigo
    from camera import RaspberryPiCamera as Camera
else:
    from camera import TestCamera as Camera

counter = 0

@app.route('/')
def index():
    return render_template('index_socketio.html')

@socketio.on('my_event', namespace='/test')
def test_message(message):
    print "in my_event"
    emit('my_response', {'data': message['data']})

@socketio.on('my_broadcast_event', namespace='/test')
def test_message(message):
    emit('my_response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my_response', {'data': 'Connected', 'count': counter})
    get_image()

@socketio.on('get_image_ping', namespace='/test')
def img_ping(msg):
    logging.warning('get_image_ping')
    get_image()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

from camera import TestCamera
import base64
cam = TestCamera()

stop_stream = False

def get_image():
    print "In start stream"
    header =  "data:image/gif;base64,"
    #while True:
    print "sending data"
    time.sleep(0.5)
    frame = cam.get_frame()
    b64_data = base64.b64encode(frame)
    emit('get_image_event', {'data': header + b64_data})
    #stop_stream = True
    #update stop_stream using sockets
    #if stop_stream:
    #    break

#start_stream()





if __name__ == '__main__':
    socketio.run(app, debug=True)
