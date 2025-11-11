from ultralytics import YOLO

# Modell laden
model = YOLO('runs/detect/train/weights/best.pt')

# Inferenz auf einem Bild
results = model.predict(
    source='data/images/test/20230609a48.jpg',  # Pfad zu deinem Testbild
    conf=0.3,    # Confidence Threshold
    save=True,   # speichert das Bild mit Bounding Boxes
    show=True    # öffnet Fenster (funktioniert nicht in Colab)
)

# Ergebnisse inspizieren (optional)
for r in results:
    print(r.boxes.xyxy)   # Koordinaten
    print(r.boxes.conf)   # Confidence
    print(r.boxes.cls)    # Klassen-ID (bei dir nur "bee")
