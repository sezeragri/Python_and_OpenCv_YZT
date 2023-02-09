import cv2 as cv
img = cv.imread("uu_logo.png",1) # buradaki 0 gri formatına çeviriyor
print("Resim  boyutu : ",img.shape)
cv.imshow("Orijinal",img)


imgResize = cv.resize(img,(800,800))
print("Resized Img Shape : " , imgResize.shape)

cv.imshow("img Resized",imgResize)


# kırpma işşlemi
imgCropped = img[:500,0:300]
cv.imshow("img cropped",imgCropped)


cv.waitKey(0)

