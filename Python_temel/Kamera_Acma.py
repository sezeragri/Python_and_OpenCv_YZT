import cv2 as cv
#capture

cap = cv.VideoCapture(0)
# kameranın yuksekliini ve genişliğni alalım
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

print(f"{width},{height}")

# video kaydedici

writer = cv.VideoWriter("video_kaydim.mp4",cv.VideoWriter_fourcc(*"DIVX"),20,(width,height))
# fourcc çerçeveleri sıkıştırmak için kullandığımız codec codu

while True :
    ret , frame  = cap.read()
    cv.imshow("Video",frame)

    # save
    writer.write(frame)
    if cv.waitKey(1) & 0xFF == ord("q"): break

cap.release()
writer.release()
cv.destroyAllWindows


