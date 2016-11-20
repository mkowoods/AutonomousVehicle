from flask import Flask, render_template, Response
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
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/post_data')
def send_data():
    pass

if __name__ == "__main__":
    app.run(debug=True)

