import numpy as np
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import cv2
import os

confidence_threshold = 0.5

classes = [
    "person", "bicycle", "car", "cycle", "bus", "train",
    "backhground", "dog", "cat", "horse","sheep", "tvmoniter", "sofa"
    , "diningtable","bottle" ]

emoji = {
    "person": "🚶", "bicycle": "🚲", "car": "🚗", "cycle": "🚴", 
     "bus": "🚌", "train": "🚆", "dog": "🐕", "horse": "🐎",
      "cat": "🐈", "sheep": "🐑", "tvmoniter": "📺", "sofa": "🛋️",
       "diningtable": "🍽️", "bottle": "🍾"}

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

image_path = input("Enter image path: ").strip()

if not os.path.isfile(image_path):
    print("Invalid image path.")
    exit()
    
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

boxes, weights = hog.detectMultiScale(gray, winStride=(8,8))
draw = ImageDraw.Draw(pil_image)

counts = {}

for (x, y, w, h).conf in zip(boxes, weights):
    if conf <confidence_threshold:
        continue

    x1 ,y1 ,x2 ,y2 = x, y, x + w , y + h 

    draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
    label = "person"
    emoji_symbol = emoji.get(label, "")
    text = f"{emoji_symbol} {label}: {conf:.2f}"
    draw.text((x1, y1 - 10), text, fill="red")

    counts[label] = counts.get(label, 0) + 1

    out = f"{datetime.now().isoformat()} - Detected {label} with confidence {conf:.2f} at [{x1}, {y1}, {x2}, {y2}]"
    pil_image = image.save(out)

    print (f"/n saved: {out}")

    if counts:
    print("Detection Summary:")
    for label, count in counts.items():
        print(f"{label}: {count}")
