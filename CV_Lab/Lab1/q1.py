import cv2
img = cv2.imread("image.jpeg",0)
cv2.imshow('Image', img)
cv2.imwrite('output_image.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
