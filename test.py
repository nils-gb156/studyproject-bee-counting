from ultralytics import YOLO

# Modell laden
model = YOLO("runs/detect/train/weights/best.pt")

# Inferenz auf einem Testbild
results = model.predict(
    source="data/images/test/bee1.jpg",  # Pfad zum Testbild
    conf=0.3,   # Confidence Threshold, z.B. 0.3
    save=True,  # speichert Bild mit Bounding Boxes
    show=True   # öffnet das Bild im Fenster
)

# Ergebnisse ausgeben
for r in results:
    print("Gefundene Bienen:", len(r.boxes))
    print("Koordinaten:", r.boxes.xyxy)  # xmin, ymin, xmax, ymax
