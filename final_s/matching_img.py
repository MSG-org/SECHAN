'''
All rights about the program by GIGA Genie AI Service Team, korea Telecom Data System.
@author : S.C CHOI
'''



import cv2 as cv
import argparse
import numpy as np
from cul_time import *

kernel_sharpen_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
confThreshold = 0.5
nmsThreshold = 0.6
inpWidth = 416
inpHeight = 416
parser = argparse.ArgumentParser(description='Object Detection using YOLO in OPENCV')
args = parser.parse_args()

#모델 경로만 수정 요
classesFile = "/Users/sechan/PycharmProjects/SECHAN/YOLO_module_file/coco.names"
modelConfiguration = "/Users/sechan/PycharmProjects/SECHAN/YOLO_module_file/yolov3-tiny.cfg"
modelWeights = "/Users/sechan/PycharmProjects/SECHAN/YOLO_module_file/yolov3-tiny.weights"

classes = None
net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)
check_list1 =[]
check_list2 = []
count = 0


with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

def part_check_pixel(data1, data2):

    # These variable values can change fluidly.
    rowcount = 300
    lcount = 600

    for row in range(rowcount, rowcount+300):
        for low in range(lcount , lcount + 500):
            if data1[row][low][0] != data2[row][low][0]:
                return False
    return True
def getOutputsNames(net):
    layersNames = net.getLayerNames()
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
def postprocess(frame, outs):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    classIds = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:] * 100
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                center_x = int(detection[0] * frameWidth)
                center_y = int(detection[1] * frameHeight)
                width = int(detection[2] * frameWidth)
                height = int(detection[3] * frameHeight)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

                if count ==0:
                    check_list1.append([left, top, width, height,confidence,classIds])
                else :
                    check_list2.append([left, top, width, height, confidence,classIds])
    indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        con = confidences[i]
    if len(boxes) >= 1:
        print("detection_object_count: " ,len(boxes))
def detection(data):
    blob = cv.dnn.blobFromImage(data, 1 / 256, (inpWidth, inpHeight), [0, 0, 0], 1, crop=False)
    net.setInput(blob)
    outs = net.forward(getOutputsNames(net))
    postprocess(data, outs)
def matching_detection_information():
    if len(check_list1) != len(check_list2):
        print("not matching img ------ detection object count is different")
        return False

    for column in range(0,len(check_list1)):
        for row in range(0,5):
            if check_list1[column][row] != check_list2[column][row]:
                print("not matching img ------ information is not matching")
                return False
    print("img is matching")
    return True
def match(data1,data2,fr):
    check = part_check_pixel(data1,data2)

    if check == True:
        print("match!")
        print("start detection matching......")
        detection(data1)
        global count
        count += 1
        detection(data2)
        matching_detection_information()
        return True
    else:
        print(fr,"frame is Not matching")
        return False

def video_open(vod_data,pic_data):
    c = 0
    while vod_data.isOpened:
        ret, frame = vod_data.read()

        if ret ==False:
            break

        if match(frame,pic_data,c) == True:
            return "finish",vod_data.get(cv.CAP_PROP_POS_FRAMES)
        c+=1



