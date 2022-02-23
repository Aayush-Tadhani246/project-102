import cv2
import dropbox 
import time
import random

start_time=time.time()

def takeSnap():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name='img'+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
    return img_name
    print('snapshot taken')
    videoCaptureObject.release()
    cv2.destoryAllWindows()

def uploadFile(img_name):
    access_token='y3ZyP-GsnM4AAAAAAAAAAYpdT4VU3VN8fFeGWI7tsHlBhgGFYG-VfJT2qQtKgv-R'
    file = img_name
    file_from = file
    file_to = '/newfolder1/'+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded')

def main():
    while(True):
        if ((time.time()-start_time) >= 300):
            name = takeSnap()
            uploadFile(name)
main()

