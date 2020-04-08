
import cv2 as cv

import time

video_path = '/Users/sechan/Desktop/v.data-ds/testv.mov'
pic_path = '/Users/sechan/Desktop/v.data-ds/size_test.png'# 1200


vide =cv.VideoCapture(video_path)
pic = cv.imread(pic_path)
def calculate_time_from_frame(data,frame_data):
    return frame_data/data.get(cv.CAP_PROP_FPS)
def chang_value_time(times):
    change_time_h = times // 3600
    change_time_m = times // 60 - change_time_h * 60
    change_time_sec = times % 3600 - change_time_m * 60

    return change_time_h,change_time_m,change_time_sec
def check_video_info(data):

    if data.isOpened() == False:
        print("video is not open")

    else:
        fps = data.get(cv.CAP_PROP_FPS)
        total_frame = data.get(cv.CAP_PROP_FRAME_COUNT)
        sec_time =   total_frame/fps
        hour, miniute, sec = chang_value_time(sec_time)



        print("video_information")
        print("----------------------------------------------------")
        print("fps: ", fps)
        print("frame: ", total_frame)
        print("video time(sec): ", sec_time)
        print("video time(h,m,s): ",hour, "h ",miniute, "m ",sec, "s")
        print("video frame shape",frame.shape)

def part_check_pixel(data1, data2):

    rowcount = 300
    lcount = 600

    check = False

    for row in range(rowcount, rowcount+300):
        for low in range(lcount , lcount + 500):
            '''
            if data1[row][low][0] != data2[row][low][0]:
                check = True
                print("differ -> info ---- data2_pixel : " ,data2[row][low], "data1_pixel: ",data1[row][low])
                return False
                '''
            if data1[row][low][0]-data2[row][low][0] >=10 or data1[row][low][1]-data2[row][low][1] >=10 or data1[row][low][2]-data2[row][low][2] >=10:
                print("differ -> info ---- data2_pixel : ", data2[row][low], "data1_pixel: ", data1[row][low])
                return False
    return True
ret ,frame = vide.read()
#pic = cv.resize(pic,dsize = (frame.shape[1],frame.shape[0]))

check_video_info(vide)

count = 0
'''
while vide.isOpened():
    ret ,frame = vide.read()

    if(ret == False):
        break
    if count == 1200:
        cv.imshow('asd',frame)
        cv.waitKey(0)
        break
    count +=1
    print(count)'
'''


video_paths = '/Users/sechan/Desktop/v.data-ds/realv/test2.mpg'

re = cv.VideoCapture(video_paths)

check_video_info(re)