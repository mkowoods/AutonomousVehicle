import time
import config
import threading
import io
import logging

if config.PRODUCTION:
    import picamera


class TestCamera:
    def __init__(self):
        self.img_path_template = './sample_images/video-streaming-%d.jpg'
        self.frames = [open(self.img_path_template%i, 'rb').read() for i in range(1, 4)]

    def get_frame(self):
        return self.frames[int(time.time()) % 3]


class RaspberryPiCamera:

    timeout = 10.0
    thread = None
    frame = None
    last_access = 0

    def start_streaming(self):
        cls = RaspberryPiCamera
        if cls.thread is None:
            cls.thread = threading.Thread(target=self._camera_stream_thread)
            cls.thread.start()

            while self.frame is None:
                pass

            print "received first frame"

    @classmethod
    def _camera_stream_thread(cls):
        with picamera.PiCamera() as cam:
            cam.resolution = (320, 240)
            cam.hflip = True
            cam.vflip = True

            cam.start_preview()
            time.sleep(2)

            stream = io.BytesIO()

            for _ in cam.capture_continuous(stream, 'jpeg', use_video_port = True):

                stream.seek(0)
                cls.frame = stream.read()

                stream.seek(0)
                stream.truncate()

                if (time.time() - cls.last_access) > cls.timeout:
                    break
        cls.thread = None

    def get_frame(self):

        self.last_access = time.time()
        self.start_streaming()
        return self.frame




