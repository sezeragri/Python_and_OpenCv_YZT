import cv2 as cv
import numpy as np
# Kontur algılama
# aynı renk veya yoğunluğa sahip tüm kesintisiz noktaları birleştirmeye yarayan yöntemdir
# Konturlar  şekil analizi ile nesne algılama ve tanıma için kullanılır

# resmi içe aktar
img = cv.imread("konturr.png",0)
imgResize = cv.resize(img,(400,400))

cv.imshow("orijinal",imgResize)

image , contours , hierarch = cv.findContours(imgResize , cv.RETR_CCOMP , cv.CHAIN_APPROX_SIMPLE)

external_countur = np.zeros(imgResize.shape)
internal_countur = np.zeros(imgResize.shape)


for i in range(len(contours)):
    if hierarch[0][i][3] == -1:
        cv.drawContours(external_countur ,contours , i  , 255 , -1 )

    else : #internal
        cv.drawContours(internal_countur, contours, i, 255, -1)


cv.imshow("external", external_countur)
cv.imshow("internal", internal_countur)
cv.waitKey(0)







