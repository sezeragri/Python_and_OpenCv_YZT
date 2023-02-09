import cv2 as cv
import numpy as np
# resimi ice aktar
img = cv.imread("yeni_kart.jpg")
cv.imshow("Orijinal",img)

width = 400
height = 500
# burada poiterlar oluşturuyoruz 4 köşesinin değerlerini giriyoruz
# yani çevirmek istediğm resmin köşelerini giriyorum yani dört köşe

cv.waitKey(0)


