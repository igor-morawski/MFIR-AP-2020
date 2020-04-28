import numpy as np
import cv2
IMG_N = 10

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 680)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 460)

for idx in range(IMG_N):
    ret, frame = cam.read()
    assert ret
    cv2.imwrite("{}.jpg".format(str(idx)), frame)
    print("{}/{} photos taken. Press SPACE continue...".format(idx+1, IMG_N))
    while (cv2.waitKey(30) & 0xFF != ord(' ')):
        ret, frame = cam.read()
        assert ret
        cv2.imshow('frame', frame)
    

cam.release()
cv2.destroyAllWindows()