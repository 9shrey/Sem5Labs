import cv2
image = cv2.imread('image.jpeg')
start_point = (50, 50)
end_point = (200, 200)
color = (0, 255, 0)
thickness = 2
cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow('Image with Rectangle', image)
cv2.waitKey(0)