
import numpy as np
import cv2

def equalizeHistogram(img):
    img_height = img.shape[0]
    img_width = img.shape[1]
    histogram = np.zeros([256], np.int32)

    for i in range(0, img_height):
        for j in range(0, img_width):
            histogram[img[i, j]] += 1

    pdf_img = histogram / histogram.sum()
    cdf = np.zeros([256], float)

    for i in range(0, 256):
        for j in range(0, i + 1):
            cdf[i] += pdf_img[j]

    cdf = np.zeros(256, float)
    cdf[0] = pdf_img[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + pdf_img[i]

    cdf_eq = np.round(cdf * 255, 0)  # mapping, transformation function T(x)
    imgEqualized = np.zeros((img_height, img_width))

    for i in range(0, img_height):
        for j in range(0, img_width):
            r = img[i, j]
            s = cdf_eq[r]
            imgEqualized[i, j] = s

    return imgEqualized

img = cv2.imread('sample.jpeg',0)
img_eq = equalizeHistogram(img)
img_eq = img_eq.astype('uint8')
cv2.imshow('Equalized', img_eq)
cv2.waitKey()