import cv2
import numpy as np

def apply_filter(image, filter_type):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if filter_type in ['r', 'g', 'b']:
        color_map = {'r': (0, 1), 'g': (0,2), 'b': (1,2)}[filter_type]
        image[:, :, color_map[0]] = 0
        image[:, :, color_map[1]] = 0
    elif filter_type == 's':
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sobel_combined = cv2.magnitude(sobelx, sobely)
        image = cv2.convertScaleAbs(sobel_combined)

    elif filter_type == 'c':
        canny_edges = cv2.Canny(gray, 100, 200)
        image = cv2.cvtColor(canny_edges, cv2.COLOR_GRAY2BGR)

    return image

image_path = 'python/example.jpeg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
    exit()

print("PRESS KEY TO APPLY FILTERS:")

print("r - Red tint/ing , g - Green tint/ing , b - Blue tint/ing , q - Quit, s - Sobel Edge Detection , c - Canny Edge Detection ")
filter_type = 'original'

while True:

    filtered = apply_filter(image.copy(), filter_type)
    cv2.imshow('Filtered Image', filtered)

    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        break
    elif key in [ord('r'), ord('g'), ord('b'), ord('s'), ord('c')]:
        filter_type = chr(key)
    else:
        print("Invalid key. Please press r, g, b, s, c, or q.")

cv2.destroyAllWindows()