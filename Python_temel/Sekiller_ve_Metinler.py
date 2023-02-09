import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)  # siyah bir resim

print(img.shape)

cv.imshow("Siyah",img)
# (resim ,baslangıc noktası,bitis noktası,renk,kalınlık)
cv.line(img,(100,100),(200,200),(0,255,0),3)  # RGB =(255,0,0) -> kırmızı , (0,0,255)   burada cv de BGR ye göre alınır
cv.imshow("Cizgi",img)

# dikdörtgen
#(resim,başlangıc,bitiş,renk,kalınlık,icini doldurma)
cv.rectangle(img,(50,50),(256,256),(255,0,0),cv.FILLED)
cv.imshow("Dikdotgen",img)

# cember
# (resim,merkez,yarı cap ,renk )
cv.circle(img,(300,300),100,(0,0,255),cv.FILLED)
cv.imshow("Cember",img)

# METİN
#(resim,baslangıc noktası,font,kalınlık,renk)
cv.putText(img,"Resim",(350,350),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv.imshow("Metin",img)
cv.waitKey(0)
