import cv2 as cv
import numpy as np
import warnings
warnings.filterwarnings("ignore")



# goruntu bulanıklastırma goruntunun düşük geçişli bibr filtre uygulanmasıyla elde edilir
# open cv üç ana bulanıklastırma tekniği sağlar
# 1) ortalama bulanıklaştırma
# 2) Gauss bulanıklaiştırma
# 3) Medyan bulanıklaştırma


# Ortalama Bulanıklaştırma
# bluring = detayı azaltır vev  gürültüyü engeller

img = cv.imread("van_gogh.jpg")
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("Gorsel",img)


dst2 = cv.blur(img,ksize = (10,10))  # ksize kutucugun boyutu o kutucukların ortalamasını alacağım
cv.imshow("blur",dst2)




"""
Gaussian Bluring  
"""

gb = cv.GaussianBlur(img,ksize = (3,3), sigmaX = 7)

cv.imshow("Gaussian ", gb)



"""
Medyan Blur 
"""
"""
mb = cv.medianBlur(img,kszie = 3)
cv.imshow("Media Blur ", mb)

"""









cv.waitKey(0)