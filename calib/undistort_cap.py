import numpy as np
import cv2
import pickle

if __name__ == "__main__":
    pkl = None
    with open('calib.pkl', 'rb') as f:
        pkl = pickle.load(f)
    assert pkl
    
    #UNDISTORTING STEP 1
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(pkl['mtx'],pkl['dist'],(pkl['width'],pkl['height']),1,(pkl['width'],pkl['height']))

    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 680)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 460)

    ret, frame = cam.read()
    assert ret
    print("Press SPACE to quit...")
    while (cv2.waitKey(20) & 0xFF != ord(' ')):
        ret, frame = cam.read()
        #UNDISTORTING STEP 2
        frame = cv2.undistort(frame, pkl['mtx'], pkl['dist'], None, newcameramtx)
        cv2.imshow('frame', frame)
        
    cam.release()
    cv2.destroyAllWindows()

