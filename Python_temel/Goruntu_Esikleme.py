import cv2 as cv
# resmi içe aktarma

img = cv.imread("van_gogh.jpg",0)
img1 = cv.resize(img,(600,600))
cv.imshow("van gogh",img1)



# eşikleme
_,thresh_img = cv.threshold(img1,thresh = 60 , maxval = 255 , type = cv.THRESH_BINARY) # 60 ile 255 arasını beyazlaştıracak

cv.imshow("_,thresh",thresh_img)


# uyarlamalı eşik değeri

thresh_img2 = cv.adaptiveThreshold(img1,255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,8)
cv.imshow("_,thresh",thresh_img2)







cv.waitKey(0)