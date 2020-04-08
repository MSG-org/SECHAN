
import cv2 as cv

import time

video_path = '/Users/sechan/Desktop/v.data-ds/realv/test2.mpg'
clip_path = '/Users/sechan/Desktop/v.data-ds/realv/testclip.mp4'

vide =cv.VideoCapture(video_path)
clip = cv.VideoCapture(clip_path)
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
        ret , frame = data.read()
        fps = data.get(cv.CAP_PROP_FPS)
        total_frame = vide.get(cv.CAP_PROP_FRAME_COUNT)
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

            if data1[row][low] != data2[row][low]:
                check = True
                print("differ -> info ---- data2_pixel : " ,data2[row][low], "data1_pixel: ",data1[row][low])
                return False
    return True

check_video_info(clip)

ret , clipframe = clip.read()

print(part_check_pixel(vide,clipframe))


#pixel frame 이 안 맞음
#짧은 동영상으로 확인 불가한가?