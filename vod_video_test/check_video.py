import cv2 as cv
import time
import numpy as np
import pixel_matching as p
st_time = time.time()
video_path = "/Users/sechan/Desktop/v.data-ds/realv/test1.mpg"
videos_path = "/Users/sechan/Desktop/v.data-ds/testv.mov"
pic_path = "/Users/sechan/Desktop/v.data-ds/time.png"

#video = cv.VideoCapture(video_path)
video = cv.VideoCapture(videos_path)
pic = cv.imread(pic_path)

count = 0
while video.isOpened():
    ret , frame = video.read()
    #if p p(frame, pic):
     #   print("matching")
    if ret == False:
        break
    cv.imshow("test_img", frame)
    if count == 100:
        break


    count+=1


print(time.time()-st_time)
#cv.waitKey(0)
#video.release()
#cv.destroyAllWindows()
