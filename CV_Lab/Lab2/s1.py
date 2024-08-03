import cv2
import numpy as np

img = cv2.imread('sample.jpeg',0)
cv2.imwrite('sample2.jpeg',img)

if img is None:
    raise ValueError("Image not loaded. Please check the file path.")

img_float = img.astype(np.float32)

c = 255 / (np.log(1 + np.max(img_float)))

log_transformed = c * np.log(1 + img_float)
log_transformed = np.array(log_transformed, dtype=np.uint8)

cv2.imwrite('log_transformed.jpg', log_transformed)
cv2.waitKey(0)