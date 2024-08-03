import cv2
import numpy as np

def manual_histogram_equalization(image):

        if len(image.shape) != 2:
            raise ValueError("The input image must be grayscale")


        hist = np.zeros(256, dtype=int)
        for pixel_value in image.ravel():
            hist[pixel_value] += 1


        cdf = np.cumsum(hist)
        cdf_normalized = cdf * 255 / cdf[-1]


        lookup_table = np.floor(cdf_normalized).astype(np.uint8)


        equalized_image = lookup_table[image]

        return equalized_image

image = cv2.imread('sample.jpeg', cv2.IMREAD_GRAYSCALE)


equalized_image = manual_histogram_equalization(image)


cv2.imshow('Original Grayscale Image', image)
cv2.imshow('Equalized Image', equalized_image)


cv2.waitKey(0)
cv2.destroyAllWindows()

