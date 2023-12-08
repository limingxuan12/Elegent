import cv2
import numpy as np 
from datetime import datetime
import time

vc = cv2.VideoCapture(0)
cv2.namedWindow('window',cv2.WINDOW_NORMAL)
cv2.resizeWindow('window',(640, 480))
t2 = time.perf_counter()
while vc.isOpened():
    ret, frame = vc.read()
    if not ret:
        break
    t1 = time.perf_counter()
    fps = int(1/(t1 - t2))
    t2 = time.perf_counter()
    FPS = "FPS" + str(fps)
    cv2.putText(frame, FPS, (20, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
    cv2.circle(frame, (320,240), 5, (0, 0, 255), -1)
    cv2.rectangle(frame, (305, 225), (335, 255), (0, 0, 255), 4)
    cv2.imshow('window', frame)
    key = cv2.waitKey(1000//60)

    if key == ord('q'):
        break

vc.release()
cv2.destroyAllWindows()

