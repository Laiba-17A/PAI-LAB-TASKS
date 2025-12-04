import cv2 
import numpy as np 

image1 = cv2.imread("images.jpeg") 
image2 = cv2.imread("img2.jpg") 

image1 = cv2.resize(image1,(image2.shape[1],image2.shape[0]))

alpha = 0.5
beta = 1 - alpha
blended_image = cv2.addWeighted(image1, alpha, image2, beta, 0)

cv2.imwrite("blended_image.jpg", blended_image)
cv2.imshow("Blended  and equalized Image", blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()