import time
import cv2 as cv
import numpy as np

video_path = '/Users/sechan/Desktop/v.data-ds/testv.mov'
pic_top_path = '/Users/sechan/Desktop/v.data-ds/test3.png'
pic_sam_path = '/Users/sechan/Desktop/v.data-ds/test2.png'
pic_dif_path = '/Users/sechan/Desktop/v.data-ds/test1.png'
pic_sim = '/Users/sechan/Desktop/v.data-ds/check_sim.png'
pic_time_path ='/Users/sechan/Desktop/v.data-ds/time.png'


st = time.time()

vide =cv.VideoCapture(video_path)
pic = cv.imread(pic_top_path)
dif = cv.imread(pic_dif_path)
sam = cv.imread(pic_sam_path)
for_time_check = cv.imread(pic_time_path)
pic_sim = cv.imread(pic_sim)

gray_pic = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)
gray_dif = cv.cvtColor(dif, cv.COLOR_BGR2GRAY)
gray_sam = cv.cvtColor(sam, cv.COLOR_BGR2GRAY)
gray_time = cv.cvtColor(for_time_check,cv.COLOR_BGR2GRAY)
gray_sim = cv.cvtColor(pic_sim,cv.COLOR_BGR2GRAY)
#to gray image value

def check_pixel(data1, data2):
    rowcount = 0
    lcount = 0
    check = False
    for i in data1:
        for j in i:

            if j != data2[rowcount][lcount]:
                check = True
                print("differ -> info ---- data2_pixel : " ,data2[rowcount][lcount], "data1_pixel: ",j)
                print("count info -> lcoint: ", lcount, " rowcount: ",rowcount)
                return False
            lcount+=1
        if check == True:
            print(lcount)
            break
        rowcount+=1
        lcount =0

    return True
#full pixel matching function

def part_check_pixel(data1, data2):
    rowcount = 300
    lcount = 600

    check = False

    for row in range(rowcount, rowcount + 300):
        for low in range(lcount, lcount + 500):

            if data1[row][low][0] != data2[row][low][0]:
                check = True
                print("differ -> info ---- data2_pixel : ", data2[row][low], "data1_pixel: ", data1[row][low])
                return False
    return True
# for part_img_matching function
def check_sim(data1,data2):
    count =0
    Rsim =0
    Gsim =0
    Bsim =0

    for i in range(0,900):
        for j in range(0,1440):
            count+=1
            if data1[i][j][0] == data2[i][j][0]:
                Rsim +=1
            if data1[i][j][1] == data2[i][j][1]:
                Gsim +=1
            if data1[i][j][2] == data2[i][j][2]:
                Bsim +=1

    print("rate of image RGB rate")
    print("R rate: ",(Rsim/count)*100)
    print("G rate: ",(Gsim/count)*100)
    print("B rate: ",(Bsim/count)*100)
#check simility_rate of pic - color

def gray_check_sim(data1, data2):
    count = 0
    sim = 0


    for i in range(0, 900):
        for j in range(0, 1440):
            count += 1
            if data1[i][j] == data2[i][j]:
                sim+=1

    print("rate of image RGB rate")
    print("R rate: ", (sim / count) * 100)
# check simility_rate of pic - gray


'''
while (vide.isOpened):
    ret, frame = vide.read()
    if ret != True :
        break
   # print(count)
    #gray_vid=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("testing ",frame)
    if  part_check_pixel(frame,for_time_check):
        #print("frame number: ",count)
        break
    #count +=1

 # about video code
 '''
'''
testim = for_time_check[300:600,600:1100]

print(for_time_check)
print(testim)

cv.imshow("real",for_time_check)
cv.imshow("part",pic_sim)

cv.waitKey(0)
cv.destroyAllWindows()
''' # show img example


print("sim pic result of rate RGB pixel")
check_sim(for_time_check,pic_sim)

print("\n\n")
print("same pic result of rate RGB pixel")
check_sim(for_time_check,for_time_check)
print(pic.shape)



print("time information to full pixel matching: ", time.time()-st)