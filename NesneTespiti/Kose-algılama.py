import cv2 as cv
import numpy as np
img = cv.imread("sudoku_copyy.png",0)
#img = np.float32(img)
print(img.shape)
imgResize = cv.resize(img,(400,400))
cv.imshow("orijinal",img)



# harris corner detection
dst = cv.cornerHarris(imgResize, blockSize = 3 , ksize = 3 , k = 0.04)  # blocksize oradaki komşuluk değeri
cv.imshow("harris", dst)

dst = cv.dilate(dst, None) # genişletme yöntemi
imgResize[dst>0.2*dst.max()] = 1
cv.imshow("dilate", dst)


# shi tomasi detection

imgResize = cv.imread("sudoku_copyy.png", 0 )
imgResize = np.float32(img)


corners = cv.goodFeaturesToTrack(imgResize, 200, 0.01, 10)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv.circle(imgResize, (x,y) ,3 , (125,125,125), cv.FILLED)

cv.imshow("sezer", imgResize)







cv.waitKey(0)