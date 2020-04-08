'''
All rights about the program by GIGA Genie AI Service Team, korea Telecom Data System.
@author : S.C CHOI
'''

import cv2 as cv
from load_video import *
from matching_img import *
from cul_time import *


if __name__ == '__main__':
    '''
    비디오 경로 읽는 코드
    현 코드는 예제로 진행하였습니다.
    '''

    video_path = '/Users/sechan/Desktop/v.data-ds/realv/teat2.mpg'
    clip_path = '/Users/sechan/Desktop/v.data-ds/realv/clip.mp4'

    vid = cv.VideoCapture(video_path)
    clip = cv.VideoCapture(clip_path)

    ret , img = clip.read()

    frame_num = video_open(vid,img)


   # print(times)
