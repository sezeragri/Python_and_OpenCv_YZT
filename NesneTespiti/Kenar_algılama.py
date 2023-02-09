import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv.imread("saat_kulesi.jpg",0)
cv.imshow("orijinal",img)


edges = cv.Canny(image = img , threshold1 = 0 , threshold2 = 255)
cv.imshow("kenar",edges)

med_val = np.median(img)
print(med_val)

low = int(max(0,(1-0.33)*med_val))
high = int(min(255, (1 + 0.33)*med_val))


print(low)
print(high)

edges2 = cv.Canny(image = img , threshold1 = low, threshold2 = high)
cv.imshow("kenar_edges2",edges2)


#bluring
blured_img = cv.blur(img , ksize = (4,4))
cv.imshow("blured_img",blured_img)

med_val = np.median(blured_img)
print(med_val)

low = int(max(0,(1-0.33)*med_val))
high = int(min(255, (1 + 0.33)*med_val))


print(low)
print(high)


edges3 = cv.Canny(image = blured_img , threshold1 = low, threshold2 = high)
cv.imshow("kenar_edges3",edges3)




cv.waitKey(0)