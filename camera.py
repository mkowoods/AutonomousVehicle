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
        logging.info( "new frame" )
        time.sleep(0.2)
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
            logging.info("Initialized  Camera Thread waiting for frame to be set")
            while self.frame is None:
                pass

            logging.info("first frame received")

    @classmethod
    def _camera_stream_thread(cls):
        with picamera.PiCamera() as cam:
            logging.info("initializing connection to cam")
            cam.resolution = (320, 240)
            #cam.hflip = True
            #cam.vflip = True

            logging.info("Starting Camera Preview")
            cam.start_preview()
            time.sleep(0.5)
            logging.info("Completed Preview")

            stream = io.BytesIO()
            for _ in cam.capture_continuous(stream, 'jpeg', use_video_port = True):

                stream.seek(0)
                cls.frame = stream.read()

                stream.seek(0)
                stream.truncate()
                now = time.time()
                if (now - cls.last_access) > cls.timeout:
                    logging.info("Hit Time Out time: %.2f, last_access: %.2f, timeout: %.2f"%(now, cls.last_access, cls.timeout))
                    break
        cls.thread = None

    def get_frame(self):

        RaspberryPiCamera.last_access = time.time()
        self.start_streaming()
        return self.frame




