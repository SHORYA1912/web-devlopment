import cv2
import numpy as np

def apply_filter(img,mode):
    filtered = img.copy()
    if mode == "red_tint":
        filtered  [:,:,0:2]=0
    if mode == "green_tint":
        filtered[:,:, [0,2]] = 0
    if mode == "blue_tint":
        filtered[:,:,1:3] = 0
    if mode == "yellow_tint":
        filtered[:,:,0] = 0
    if mode == "purple_tint":
        filtered[:,:,1] = 0
    if mode == "cyan_tint":
        filtered[:,:,2] = 0
    if mode == "increased_red":
        filtered[:,:,2] = np.clip(filtered[:,:,2]+ 100,0,255)
    if mode == "decreased_blue":
        filtered[:,:,0] = np.clip(filtered[:,:,0]-100,0,255)
    return filtered

img = cv2.imread("python/example.jpeg")
if img is None:
     print("❌ Not found");
     exit()

filters = {
    ord("r"): "red_tint",
    ord("g"): "green_tint",
    ord("b"): "blue_tint",
    ord("i"): "increased_red",
    ord("d"): "decreased_blue",
    ord("y"): "yellow_tint",
    ord("p"): "purple_tint",
    ord("c"): "cyan_tint",
    ord("o"): "original"
}
print("PRESS: r=red, g=green, b=blue, i=increased red, d=decreased blue, y=yellow, p=purple, c=cyan, o=original, q=quit")
while True:
    cv2.imshow("Image", img)
    key = cv2.waitKey(0) & 0xFF
    if key == ord("q"):
        break
    elif key in filters:
        img = apply_filter(cv2.imread("python/example.jpeg"), filters[key])
    else:
        print("⚠️ Invalid key")

