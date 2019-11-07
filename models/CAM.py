import cv2
import os
from time import sleep
cam =  cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080,format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")

class From_cam():
    
    def rescale_frame(self,frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)


    def cam(self):

        cv2.namedWindow("test")
        directory = 'pic_cv2/'

        img_counter = 0
        os.chdir(directory)
        while True:

            ret, frame = cam.read()
            frame75 = self.rescale_frame(frame, percent=45)
            cv2.imshow("test", frame75)
            if not ret:
                break
            k = cv2.waitKey(33)

            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k == ord('a'):
                print('Pressed a')
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter +=1
                break
             
#             cam.release()
#             cv2.destroyAllWindows()
#             sleep(2)
                
                

        cam.release()

        cv2.destroyAllWindows()
        sleep(2)
        
