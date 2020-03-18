import cv2 as cv
import argparse
import numpy as np
import time
import copy
st = time.time()

pic_top_path = '/Users/sechan/Desktop/v.data-ds/test3.png'
pic_sam_path = '/Users/sechan/Desktop/v.data-ds/test2.png'
pic_dif_path = '/Users/sechan/Desktop/v.data-ds/test1.png'
pic_sim_path = '/Users/sechan/Desktop/v.data-ds/check_sim.png'
pic_time_path ='/Users/sechan/Desktop/v.data-ds/time.png'


kernel_sharpen_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
confThreshold = 0.5
nmsThreshold = 0.6
inpWidth = 416
inpHeight = 416

parser = argparse.ArgumentParser(description='Object Detection using YOLO in OPENCV')
args = parser.parse_args()

classesFile = "YOLO_module_file/coco.names"
classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

modelConfiguration = "YOLO_module_file/yolov3-tiny.cfg"
modelWeights = "YOLO_module_file/yolov3-tiny.weights"

net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)
check_list1 =[]
check_list2 = []
count = 0
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
def print_check_lists():
    print("first img detection info\n\n-----------------------")
    for list in check_list1:
        print(list)

    print("second img detection info\n\n-----------------------")

    for list in check_list2:
        print(list)
    print("\n")
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





pic_top = cv.imread(pic_top_path)
pic_sam = cv.imread(pic_sam_path)
pic_dif = cv.imread(pic_dif_path)
pic_check_sim = cv.imread(pic_time_path)
pic_sim = cv.imread(pic_sim_path)


detection(pic_check_sim)
count += 1
detection(pic_sim)
print("\n\n")
print_check_lists()
matching_detection_information()
print(time.time()-st)


