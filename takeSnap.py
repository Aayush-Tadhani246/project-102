import cv2

def takeSnap():
    videoCaptureObject=cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame=videoCaptureObject.read()
        cv2.imwrite('newpicture.jpg',frame)
    videoCaptureObject.release()
    cv2.destoryAllWindows()

takeSnap()