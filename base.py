import cv2
import numpy as np

video = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(300,200,True)

a = 0
first_frame = None

while True:
    a = a+1
    check, frame = video.read()

    fgmask = fgbg.apply(frame)
    
    count = np.count_nonzero(fgmask)

    if a > 1 and count > 3000:
        print(a)

    cv2.imshow('capturef',frame)
    cv2.imshow('capture',fgmask)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()