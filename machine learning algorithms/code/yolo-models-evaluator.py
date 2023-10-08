#saving the model
from ultralytics import YOLO
from picamera2 import Picamera2
from PIL import Image
import cv2, os, time, subprocess
from time import sleep

# Load the pre-trained YOLO model
model = YOLO('yolov8n.pt')  

# Load an image for object detection
# Initialize the PiCamera
camera = Picamera2()
camera.start()

# Capture an image and save it
image_file = "captured_image.png"

start_time = time.time()

for i in range(10):
    lap_start_time = time.time()
    image = camera.capture_image("main")
    print('type of image: ', str(type(image)))
    cam_capture_time = time.time() - lap_start_time
    results = model(image)
    # Show the results
    # for r in results:
    #     im_array = r.plot()  # plot a BGR numpy array of predictions
    #     im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    total_lap_time = time.time() - lap_start_time #this is the logging for elapsed time.
    print('camera capture time: ' + str(cam_capture_time))
    print('total lap time: ' + str(total_lap_time))

    # Display final output for multiple color detection opencv python
    image_path = 'output_image{}.png'.format(i)
    print('type', str(type(image)))
    image.save(image_path)
    # Use the 'fbi' command to display the image
    command = f'fbi -a {image_path}'
    subprocess.call(command, shell=True)

elapsed_time = time.time() - start_time
print('the total time elapsed is: ' + str(elapsed_time))