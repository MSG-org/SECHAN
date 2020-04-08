'''
All rights about the program by GIGA Genie AI Service Team, korea Telecom Data System.
@author : S.C CHOI
'''
import numpy as np
import cv2 as cv
from matching_img import *
from cul_time import *


if __name__ == '__main__':
    '''
    비디오 경로 읽는 코드
    현 코드는 예제로 진행하였습니다.
    '''

    video_path = '/Users/sechan/Desktop/v.data-ds/testv.mov'
    pic = '/Users/sechan/Desktop/v.data-ds/test1.png'


    vid = cv.VideoCapture(video_path)
    img = cv.imread(pic)


    st, frame_num = video_open(vid,img)
    time =calculate_time_from_frame(vid,frame_num)
    h,m,s = chang_value_time(time)
    print("Start time " ,h, "h ",m, "m ",int(s), "s")
