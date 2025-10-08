import cv2
import numpy as np

def apply_filter(image, filter_type):
    # Convert to RGB for edge detection filters
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if filter_type == 'r':
        filtered = image.copy()
        filtered[:, :, 0] = 0  # Zero Blue
        filtered[:, :, 1] = 0  # Zero Green
        return filtered
    elif filter_type == 'g':
        filtered = image.copy()
        filtered[:, :, 0] = 0  # Zero Blue
        filtered[:, :, 2] = 0  # Zero Red
        return filtered
    elif filter_type == 'b':
        filtered = image.copy()
        filtered[:, :, 1] = 0  # Zero Green
        filtered[:, :, 2] = 0  # Zero Red
        return filtered
    elif filter_type == 's':
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sobel_combined = cv2.magnitude(sobelx, sobely)
        sobel_norm = cv2.normalize(sobel_combined, None, 0, 255, cv2.NORM_MINMAX)
        sobel_img = cv2.convertScaleAbs(sobel_norm)
        return cv2.cvtColor(sobel_img, cv2.COLOR_GRAY2BGR)
    elif filter_type == 'c':
        canny_edges = cv2.Canny(gray, 100, 200)
        return cv2.cvtColor(canny_edges, cv2.COLOR_GRAY2BGR)
    else:
        return image

def main():
    image_path = 'python/WIN_20250519_22_26_04_Pro.jpg'
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not load image.")
        return

    print("PRESS KEY TO APPLY FILTERS:")
    print("r - Red tint, g - Green tint, b - Blue tint, s - Sobel Edge Detection, c - Canny Edge Detection, o - Original, q - Quit")

    filter_type = 'o'

    while True:
        filtered = apply_filter(image, filter_type)
        cv2.imshow('Filtered Image', filtered)

        key = cv2.waitKey(0) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):
            filter_type = 'r'
        elif key == ord('g'):
            filter_type = 'g'
        elif key == ord('b'):
            filter_type = 'b'
        elif key == ord('s'):
            filter_type = 's'
        elif key == ord('c'):
            filter_type = 'c'
        elif key == ord('o'):
            filter_type = 'o'
        else:
            print("Invalid key. Please press r, g, b, s, c, o, or q.")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()