
import cv2 as cv
import time

video_path = '/Users/sechan/Desktop/v.data-ds/testv.mov'
video_path = '/Users/sechan/Desktop/v.data-ds/tests.mp4'
video_path = '/Users/sechan/Desktop/v.data-ds/realv/test1.mpg'

vide =cv.VideoCapture(video_path)
'''
while (vide.isOpened):
    sta = time.time()
    ret, frame = vide.read()
    if ret != True :
        break
    frame_number+=1
'''
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
        total_frame = vide.get(cv.CAP_PROP_FRAME_COUNT)
        sec_time =   total_frame/fps
        hour, miniute, sec = chang_value_time(sec_time)

        print("video_information")
        print("----------------------------------------------------")
        print("fps: ", fps)
        print("frame: ", total_frame)
        print("video time(sec): ", sec_time)
        print("video time(h,m,s): ",hour, "h ",miniute, "m ",sec, "s")

