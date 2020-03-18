import time
import cv2 as cv
import numpy as np

video_path = '/Users/sechan/Desktop/v.data-ds/realv/test1.mpg'

vide =cv.VideoCapture(video_path)




def check_shape(data):
    count = 0

    while(vide.isOpened):
        ret, frame = data.read()
        if count == 200:
            print(frame.shape)
            break
        count +=1



check_shape(vide)
