import cv2 as cv
import argparse
import sys
import numpy as np
import os.path
import time

st = time.time()
video_path = '/Users/sechan/Desktop/v.data-ds/testv.mov'
pic_top_path = '/Users/sechan/Desktop/v.data-ds/test3.png'
pic_sam_path = '/Users/sechan/Desktop/v.data-ds/test2.png'
pic_dif_path = '/Users/sechan/Desktop/v.data-ds/test1.png'
pic_sim = '/Users/sechan/Desktop/v.data-ds/check_sim.png'
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

def getOutputsNames(net):
    layersNames = net.getLayerNames()
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]


count = 0
pre_confi =0
def drawPred(classId, conf, left, top, right, bottom,con):
    cv.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)
    label = '%.2f' % conf
    if classes:
        assert (classId < len(classes))
        label = '%s:%s' % (classes[classId], label)
    labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, labelSize[1])
    cv.rectangle(frame, (left, top - round(1.5 * labelSize[1])), (left + round(1.5 * labelSize[0]), top + baseLine),
                 (255, 255, 255), cv.FILLED)
    cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1)
    print("object information\ntop: ",top,"\nbottm: ",bottom,"\nright: ",right, "\nleft: ",left,"\nconfidence_score: ",con )
    if con !=0:
        pre_confi =con



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
    indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        con = confidences[i]
        drawPred(classIds[i], confidences[i], left, top, left + width, top + height,con)
    if len(boxes) >= 1:
        print("detection_object_count: " ,len(boxes))
    if pre_confi !=0 and pre_confi == con:
        count+=1




vide =cv.VideoCapture(video_path)
winName = 'test_result'
#vide = cv.VideoCapture(0)
print("start_count: ",count)
while vide.isOpened():

    hasFrame, frame = vide.read()
    if hasFrame == False:
        break

    blob = cv.dnn.blobFromImage(frame, 1 / 256, (inpWidth, inpHeight), [0, 0, 0], 1, crop=False)
    net.setInput(blob)
    outs = net.forward(getOutputsNames(net))
    postprocess(frame, outs)
    t, _ = net.getPerfProfile()
    label = 'Inference time: %.2f ms' % (t * 1000 / cv.getTickFrequency())
    cv.putText(frame, label, (0, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    frame = cv.resize(frame, dsize=(640, 1000), interpolation=cv.INTER_AREA)
    cv.imshow(winName, frame)

    if cv.waitKey(1) == 27:
        break


cv.waitKey(0)
vide.release()
cv.destroyAllWindows()
print("final_count: ",count)
print(time.time()-st)


#time - 90s -> 775s