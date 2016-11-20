from flask import Flask, render_template, Response
import config
import logging

logging.basicConfig(level=logging.INFO)


if config.PRODUCTION:
    from camera import RaspberryPiCamera as Camera
else:
    from camera import TestCamera as Camera


def gen(camera):
    while True:
        frame =  camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def feed():
    logging.info("connect to /video_feed")
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/post_data')
def send_data():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)

