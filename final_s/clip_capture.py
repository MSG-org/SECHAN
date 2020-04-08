'''
All rights about the program by GIGA Genie AI Service Team, korea Telecom Data System.
@author : S.C CHOI
'''

import cv2 as cv


def capture(path):
    clip = cv.VideoCapture(path)
    ret , frame = clip.imread()
    cv.imwrite("저장 경로" , frame)
