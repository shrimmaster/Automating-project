import cv2
import time
import random
import dropbox
start_time=time.time()    
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject= cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token = 'sl.A0xi795yoBBwX1xcFaQz-RE3cDVTgsDx8xnbKN9IpLRBoHI87MI3l_ugEheEU-KxykOe1wCdyD0OmrTa0inEvCe4Q6wcsUY_sIGHQ5QcsKqI9cNmhpfhmMcQ341FFtLThoEI-GM'
    file=img_counter
    file_from=file
    file_to="/newFolder1/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
def main():
    while(True):
        if((time.time() - start_time)>=300):
            name=take_snapshot()
            upload_file(name)

main()
            
     
        
    
