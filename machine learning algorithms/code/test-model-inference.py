#saving the model
from ultralytics import YOLO
from memory_profiler import profile
from PIL import Image

@profile
def inference_with_memory_profile():
    # Load the pre-trained YOLO model
    model = YOLO('yolov8s.pt')  

    # Capture an image and save it
    image_file = "test_red.jpg"

    image = Image.open('test_red.jpg')
    print('type of image: ', str(type(image)))
    results = model(image)
    # Show the results
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image

    # Display final output for multiple color detection opencv python
    image_path = 'output_image.png'
    print('type', str(type(image)))
    image.save(image_path)

if __name__ == "__main__":
    inference_with_memory_profile()