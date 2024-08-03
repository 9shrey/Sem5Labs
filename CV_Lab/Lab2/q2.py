import cv2
import numpy as np

def compute_histogram_and_cdf(image):
    hist = np.zeros(256, dtype=int)
    for pixel_value in image.ravel():
        hist[pixel_value] += 1
    cdf = np.cumsum(hist)
    cdf_normalized = cdf * hist.max() / cdf.max()
    return hist, cdf, cdf_normalized

def histogram_specification(input_image, reference_image):
    input_hist, input_cdf, input_cdf_normalized = compute_histogram_and_cdf(input_image)
    ref_hist, ref_cdf, ref_cdf_normalized = compute_histogram_and_cdf(reference_image)
    input_cdf_normalized = input_cdf_normalized / input_cdf_normalized[-1]
    ref_cdf_normalized = ref_cdf_normalized / ref_cdf_normalized[-1]
    mapping = np.interp(input_cdf_normalized, ref_cdf_normalized, np.arange(256))
    output_image = np.interp(input_image, np.arange(256), mapping).astype(np.uint8)
    return output_image

def main(input_image_path, reference_image_path, output_image_path):
    input_image = cv2.imread(input_image_path)
    reference_image = cv2.imread(reference_image_path)
    specified_image = histogram_specification(input_image, reference_image)
    cv2.imwrite(output_image_path, specified_image)
    cv2.imshow('Input Image', input_image)
    cv2.imshow('Reference Image', reference_image)
    cv2.imshow('Specified Image', specified_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image_path = 'sample.jpeg'
    reference_image_path = 'sample2.jpeg'
    output_image_path = 'output_image.png'
    main(input_image_path, reference_image_path, output_image_path)
