import os
import cv2
from tqdm import tqdm

# ==============================
# 🔧 Einstellungen
# ==============================
input_dir = "data_raw/images/val"   # Eingangsordner (train)
output_dir = "data/images/val"      # Zielordner
target_width = 320                  # Zielbreite in Pixeln

# Ordnerstruktur automatisch erstellen
os.makedirs(output_dir, exist_ok=True)

# ==============================
# ⚙️ Bilder skalieren
# ==============================
for filename in tqdm(os.listdir(input_dir), desc="Resizing images"):
    if not (filename.endswith(".jpg") or filename.endswith(".png")):
        continue

    # Bild laden
    img_path = os.path.join(input_dir, filename)
    img = cv2.imread(img_path)

    if img is None:
        print(f"⚠️ Konnte {filename} nicht lesen, überspringe...")
        continue

    # Seitenverhältnis beibehalten
    h, w = img.shape[:2]
    scale = target_width / w
    new_h = int(h * scale)
    resized = cv2.resize(img, (target_width, new_h))

    # Neues Bild speichern
    out_path = os.path.join(output_dir, filename)
    cv2.imwrite(out_path, resized)

print("✅ Alle Bilder erfolgreich skaliert.")
