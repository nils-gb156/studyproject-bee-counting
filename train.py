from ultralytics import YOLO

# Modell laden
model = YOLO('yolov8n.pt')

# Training starten
model.train(
    data='yolov8_bee.yaml',
    imgsz=[1920, 1080],
    epochs=100,
    batch=16,
    cache=True
)
