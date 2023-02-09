import cv2 as cv
import numpy as np

# resmi içe aktar
img = cv.imread("uu_logo.png")
cv.imshow("Orijinal",img)
# yatay
horizontal  =  np.hstack((img,img))

cv.imshow("horizontal",horizontal)

# dikey
imgResize = cv.resize(img,(200,200))
vertical = np.vstack((img,img))
cv.imshow("vertical",vertical)
print(img.shape)





cv.waitKey(0)