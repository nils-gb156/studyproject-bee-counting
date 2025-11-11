from ultralytics import YOLO

# Modell laden
model = YOLO('yolov8n.pt')

# Training starten
model.train(
    data='yolov8_bee.yaml',
    imgsz=[320, 180],
    epochs=50,
    batch=16,
    cache=True
)
