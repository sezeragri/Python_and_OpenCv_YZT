import cv2 as cv
import numpy as np
from collections import deque
# deque   -> tespit ettiğğmiz objenin merkezini depolamak için deque kullanırız

# belirli renklerde bulunan nesnelerin tespitinin nasıl yapılacağını kontur bulmma yöntemi ile öğreneceğiz

# konturlar basitçe, aynı renk veya yoğunluğa sahip tüm sürekli noktaları birlesştiren bir eğri olarak açıklanabilir
# Konturlar , şekil analizi ve nesne algılama ve tanıma içn kullanışlı bir araçtır


buffer_size = 16 # deque nin sizesi olsun diyorum aslında
pts =deque(maxlen= buffer_size)


# örnek olarak mavi rengini kullanalım bunun için mavş rennk aralığı oluşturmammız gerekiyor bunu HSV formatında belirleyeceğiz


blueLover =(84 , 98 , 0)
blueUpper =(179 , 255 , 255)

# capture

cap = cv.VideoCapture(0)
cap.set(3,960)
cap.set(4,480)

while True :

    success , imgOriginal = cap.read()

    if success :

      # blur
      blurred = cv.GaussianBlur(imgOriginal, (11,11), 0 )

      # hsv
      hsv = cv.cvtColor(blurred , cv.COLOR_BGR2HSV)

      cv.imshow("HSV Image ", hsv)

      # mavi için maske oluştur
      mask =  cv.inRange(hsv , blueLover , blueUpper)
      cv.imshow("HSV Image",mask)

    if cv.waitKey(1) & 0xFF == ord("q") : break







