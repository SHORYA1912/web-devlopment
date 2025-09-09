import cv2
import matplotlib.pyplot as plt

image = cv2.imread('python/example.jpeg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

h,w,_=img.shape
rects = [((20, 20), 150, 150, (0, 255, 255)),

((w - 200, h - 200), 200, 150, (255, 0, 255))]
centers = []
for (x, y), rw, rh, color in rects:
    cv2.rectangle(img, (x, y), (x + rw, y + rh), color, 3)
    cx, cy = x + rw // 2, y + rh // 2
    centers.append((cx, cy))
    cv2.circle(img, (cx, cy), 5, (255, 255, 0), -1)

cv2.line(img, (cx, cy), (cx + 50, cy + 50), (255, 0, 0), 2)
font = cv2.FONT_HERSHEY_SIMPLEX
label =[('Rect 1',rects[0][0]),('Rect 2',rects[1][0]),
        ('center-1',(centers[0][0]- 40,centers[0][1]-40)),
        ('center-2',(centers[1][0]+ 20,centers[1][1]+20))]

for text,pos in label:
    cv2.putText(img, text, pos, font, 0.7, (0, 255, 0), 2)

arrow_start = (centers[0][0] + 20, centers[0][1] + 20)
arrow_end = (centers[1][0] - 20, centers[1][1] - 20)
cv2.arrowedLine(img, arrow_start, arrow_end, (0, 0, 255), 2)

midarrow = ((arrow_start[0] + arrow_end[0]) // 2, (arrow_start[1] + arrow_end[1]) // 2)
cv2.circle(img, midarrow, 5, (0, 255, 255), -1)

plt.imshow(img)
plt.title('Image with Annotations')
plt.axis('off')
plt.show()