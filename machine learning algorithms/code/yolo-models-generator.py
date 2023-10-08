from ultralytics import YOLO
 
# Load the model.
model_name = 'yolov8n'
model = YOLO(model_name+'.pt')
# model = YOLO('yolov8s.pt')
# model = YOLO('yolov8m.pt')
 
# Training.
results = model.train(
   data='C:\\Users\\cchan\\computer-vision\\machine learning algorithms\\dataset\\data.yaml',
   imgsz=640,
   epochs=100,
   batch=16,
   name='{}_custom'.format(model_name)
)
#saving the model
# Export the model
model.export(format='onnx')