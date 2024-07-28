import cv2

image = cv2.imread('image.jpeg')

x, y = 100, 150

pixel = image[y, x]
blue, green, red = pixel

print(f'RGB values at ({x}, {y}): R={red}, G={green}, B={blue}')
