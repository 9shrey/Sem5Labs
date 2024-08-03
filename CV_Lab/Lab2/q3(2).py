import cv2

img=cv2.imread('sample.jpeg')
re_img=cv2.resize(img,(200,800))
crop_img=img[50:300,100:300,:]
cv2.imshow("Original",img)
cv2.imshow("Resized",re_img)
cv2.imshow("Cropped",crop_img)
cv2.waitKey(0)
