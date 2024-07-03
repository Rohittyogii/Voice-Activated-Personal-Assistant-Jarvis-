import cv2

def open_webcam():
    cam = cv2.VideoCapture(0)

    while True:
        ret, img = cam.read()
        cv2.imshow('webcam', img)
        k = cv2.waitKey(10)
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


