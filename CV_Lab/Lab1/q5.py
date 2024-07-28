import cv2
image = cv2.imread('image.jpeg')
width, height = 800, 600
resized_image = cv2.resize(image, (width, height))
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)