# Beecounting Project

Dieses Projekt implementiert ein **zone-based Bee-Counting System** mit der **senseBox Eye (ESP32-S3 + Kamera)**.  
Das Ziel ist es, Ein- und Ausflüge von Bienen zu erkennen, zählen und die Ergebnisse später in einem Dashboard darzustellen.

---

## 1. Projektübersicht

### Komponenten
- **Modelltraining**: YOLOv8 Nano (YOLOv8n) für Bienen-Detection
- **Datensatz**: Gelabelte Bilder von Bienen am Einflugloch (Train / Val)
- **Deployment**: Auf dem PC zunächst Tests, später auf ESP32-S3
- **Tracking**: BoTSORT für Video-Tracking und Zählung

### Verzeichnisstruktur

```
studyproject-bee-counting/
│
├── data/
│ ├── images/test/
│ ├── images/train/
│ ├── images/val/
│ ├── labels/train/
│ ├── labels/val/
│ └── videos/bee_video.mp4
│
├── runs/ # YOLO Outputs (Weights, Predictions)
│
├── train.py # Trainingsskript
├── test.py # Testskript für Einzelbilder
└── yolov8_bee.yaml # Dataset-Konfiguration für YOLO
```

---

## 2. Training

Trainiere das Modell mit YOLOv8n:

```python
python train.py
```

Nach dem Training findest du die Gewichte in: `runs/detect/train/weights/best.pt`

---

## 3. Testen

### 3.1 Einzelbild

Du kannst ein Testbild mit `test.py` prüfen:

- Passe den Pfad zum Testbild an.
- Annotierte Bilder werden in `runs/detect/predict/` gespeichert.
- `conf` = Confidence Threshold, kann angepasst werden (z.B. 0.2–0.5).

### 3.2 Video mit Tracking

Für ein Video mit Tracking (BoTSORT):

```
yolo track model=runs/detect/train/weights/best.pt source=data/videos/bee_video.mp4 tracker=botsort.yaml conf=0.3 save=True
```

- Jede Biene erhält eine ID, die über Frames verfolgt wird
- Perfekt für Zone-based Counting
- Output-Video wird automatisch in `runs/track/` gespeichert

---

## 4. Weiteres Vorgehen

- Nach erfolgreichem Test auf PC kannst du das Modell quantisieren und auf ESP32-S3 deployen
- Zone-based Counting implementieren:
  - Zonen definieren (z.B. Ein- / Ausflug)
  - Tracker-ID nutzen, um einzelne Bienen zu zählen
- Ergebnisse über MQTT / SD-Karte speichern und Dashboard darstellen

---

## 5. Quelle der Trainingsdaten
https://data.mendeley.com/datasets/8gb9r2yhfc/6
