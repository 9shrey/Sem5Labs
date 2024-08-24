import cv2
import numpy as np

def gradient(img):
    fx = np.array([[-1, -2, -1],
                   [0,  0,  0],
                   [1,  2,  1]])

    fy = np.array([[-1,  0,  1],
                   [-2,  0,  2],
                   [-1,  0,  1]])

    gradx = cv2.filter2D(img, -1, fx)
    grady = cv2.filter2D(img, -1, fy)
    D = np.arctan2(grady, gradx)  # Gradient direction in radians
    gradxy = np.sqrt(gradx**2 + grady**2)
    gradxy = np.clip(gradxy, 0, 255).astype(np.uint8)
    return gradxy, D

def non_max_suppression(img, D):
    M, N = img.shape
    Z = np.zeros((M, N), dtype=np.uint8)
    angle = D * 180. / np.pi
    angle[angle < 0] += 180

    # Define the gradient direction bins
    angle_bin = np.floor((angle + 22.5) / 45) % 4

    for i in range(1, M-1):
        for j in range(1, N-1):
            if angle_bin[i, j] == 0:  # 0 degrees
                q = img[i, j + 1]
                r = img[i, j - 1]
            elif angle_bin[i, j] == 1:  # 45 degrees
                q = img[i + 1, j - 1]
                r = img[i - 1, j + 1]
            elif angle_bin[i, j] == 2:  # 90 degrees
                q = img[i + 1, j]
                r = img[i - 1, j]
            elif angle_bin[i, j] == 3:  # 135 degrees
                q = img[i - 1, j - 1]
                r = img[i + 1, j + 1]

            if img[i, j] >= q and img[i, j] >= r:
                Z[i, j] = img[i, j]
            else:
                Z[i, j] = 0

    return Z

def threshold(img, lowThresholdRatio=0.05, highThresholdRatio=0.09):
    highThreshold = img.max() * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio

    M, N = img.shape
    res = np.zeros((M, N), dtype=np.uint8)

    weak = 25
    strong = 255

    strong_i, strong_j = np.where(img >= highThreshold)
    weak_i, weak_j = np.where((img >= lowThreshold) & (img < highThreshold))

    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak

    return res

def hysteresis(img, weak=25, strong=255):
    M, N = img.shape

    for i in range(1, M-1):
        for j in range(1, N-1):
            if img[i, j] == weak:
                if (
                    (img[i+1, j-1] == strong) or (img[i+1, j] == strong) or
                    (img[i+1, j+1] == strong) or (img[i, j-1] == strong) or
                    (img[i, j+1] == strong) or (img[i-1, j-1] == strong) or
                    (img[i-1, j] == strong) or (img[i-1, j+1] == strong)
                ):
                    img[i, j] = strong
                else:
                    img[i, j] = 0

    return img

def canny_edge(img):
    # Gaussian Blurring
    gb_img = cv2.GaussianBlur(src=img, ksize=(5, 5), sigmaX=3)
    cv2.imshow("1. Gaussian Blur", gb_img)

    # Gradient computation
    g_img, D = gradient(gb_img)
    cv2.imshow("2. Gradient", g_img)

    # Non-maximum suppression
    nms_img = non_max_suppression(g_img, D)
    cv2.imshow("3. Non-Maximum Suppression", nms_img)

    # Double thresholding
    t_img = threshold(nms_img)
    cv2.imshow("4. Double Thresholding", t_img)

    # Hysteresis
    hys_img = hysteresis(t_img)
    cv2.imshow("5. Hysteresis", hys_img)

    return hys_img

if __name__ == "__main__":
    img = cv2.imread("/home/student/Documents/220962101/Week4/ref_pic.jpg",0)
    gb_img = cv2.GaussianBlur(src=img, ksize=(5, 5), sigmaX=3)
    canny_img = canny_edge(img)
    cv2.imshow("Canny Edge Detection", canny_img)

    imgCanny = cv2.Canny(gb_img, 50, 50)
    cv2.imshow("Canny Edge Detection via OpenCV",imgCanny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
