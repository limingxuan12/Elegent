import cv2
import numpy as np 
vc = cv2.VideoCapture(0)
cv2.namedWindow('window',cv2.WINDOW_NORMAL)
cv2.resizeWindow('window',(640, 480))

while vc.isOpened():
    ret, frame = vc.read()
    if not ret:
        break
    cv2.putText(frame, "FPS:60", (20, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
    cv2.circle(frame, (320,240), 5, (0, 0, 255), -1)
    cv2.rectangle(frame, (305, 225), (335, 255), (0, 0, 255), 4)
    cv2.imshow('window', frame)
    key = cv2.waitKey(1000//60)

    if key == ord('q'):
        break

vc.release()
cv2.destroyAllWindows()

