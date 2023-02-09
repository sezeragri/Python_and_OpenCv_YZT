import cv2 as cv
import matplotlib.pyplot as plt
# karıstırma
img1 = cv.imread("uu_logo.png")
img2 = cv.imread("van_gogh.jpg")

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# karıltırma işlemi yapabilmek için ilk önce iki resmin aynı boyutta olduğuna emin olmam lazım değilde aynı boyuta indirgrmrm lazım
print(img1.shape)
print(img2.shape)  # burada farklı boyutta oldukarını öğrenmiş oldum

img1 = cv.resize(img1,(600,600))
img2 = cv.resize(img2,(600,600))
print(img1.shape)
print(img2.shape)   # bu şekilde aynı boyut yapmış oldum

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)


# karıştırılmış resim = alpha*img1 + beta*img2
blended = cv.addWeighted(src1 = img1, alpha = 0.3, src2 = img2 , beta  = 0.7, gamma = 0)

plt.figure

plt.imshow(blended)



cv.imshow("blended",blended)

cv.waitKey(0)



