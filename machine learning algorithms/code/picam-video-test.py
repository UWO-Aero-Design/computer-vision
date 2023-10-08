from picamera2 import Picamera2, Preview
import time

# Load an image for object detection
# Initialize the PiCamera
camera = Picamera2()
camera_config = camera.create_preview_configuration()
camera.configure(camera_config)
camera.start_preview(Preview.DRM)
camera.start()
time.sleep(2)
exit()
