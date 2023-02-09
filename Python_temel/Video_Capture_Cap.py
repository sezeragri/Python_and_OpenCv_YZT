
import cv2 as cv
import time

# video ismi

video_name = "video.mp4"

# video içe aktarma  video capture

cap = cv.VideoCapture(video_name)
print("genislik",cap.get(3))
print("yukseklik",cap.get(4))

if cap.isOpened() == False :
    print("Error")
while True:
    ret, frame = cap.read()
    if ret == True:
        time.sleep(0.01)  # uyarı : kullanmazsak cok hızlı akar
        cv.imshow("Video", frame)
    else : break

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv.destroyAllWindows()


