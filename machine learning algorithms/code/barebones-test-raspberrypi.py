#saving the model
from ultralytics import YOLO
from PIL import Image
import time, subprocess
from memory_profiler import profile

@profile
def inference_with_memory_profile():
    # Load the pre-trained YOLO model
    print('*************START**************')
    command = f'free -h'
    subprocess.call(command, shell=True)

    model = YOLO('yolov8n.pt')  

    # # Capture an image and save it
    image_file = "test_red.jpg"

    image = Image.open('test_red.jpg')

    print('*************AFTER MODEL LOAD**************')
    command = f'free -h'
    subprocess.call(command, shell=True)

    inference_start_time = time.time()
    
    results = model(image)
    inference_end_time = time.time()

    print('*************AFTER INFERENCE**************')
    command = f'free -h'
    subprocess.call(command, shell=True)

    inference_time = inference_end_time - inference_start_time
    print('the total inference time is: ', str(inference_time))

if __name__ == "__main__":
    inference_with_memory_profile()