import cv2
import numpy as np

video = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(300,200,True)

a = 0
first_frame = None
tmp = False
moving = 0

while True:
    a = a+1
    check, frame = video.read()

    fgmask = fgbg.apply(frame)
    
    count = np.count_nonzero(fgmask)

    if a > 1 and count > 3000:
        print(a)
        moving += 1
        if tmp == False and moving>10:
            tmp = True
            cv2.imwrite("slika.jpg", frame)

    cv2.imshow('capturef',frame)
    cv2.imshow('capture',fgmask)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()