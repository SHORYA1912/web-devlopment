import cv2
image = cv2.imread('python/example.jpeg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resize_image = cv2.resize(gray_image,(224,224))

cv2.imshow("processed image", resize_image)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite("gray_resize_image.jpg",resize_image)
    print("image saved as gray_resize_image.jpg")
else:
    print("image not saved")

cv2.destroyAllWindows()
print("processed image dimensions:{resized_image.shape}")