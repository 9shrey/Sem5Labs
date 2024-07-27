import cv2
src = cv2.imread('image.jpeg')
image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('img', image)
cv2.waitKey(0)