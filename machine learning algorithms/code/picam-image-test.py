from picamera2 import Picamera2, Preview
from PIL import Image
import time

# Load an image for object detection
# Initialize the PiCamera
camera = Picamera2()
camera_config = camera.create_preview_configuration()
camera.start()
image = camera.capture_image("main")
image.save('new_image.png')
exit()
