image matching
1. full pixel matching
2. part pixel matching
3. object information matching using YOLOv3 - tiny

--------------al clear

time information

Now logic is using frame
    -> searching time section
    how?



#fps->초당 보여지는 사진의 수라고 생각하면 됨
#현재 영상은 드롭 프레임 인 것을 알 수 있다. -> 59.98
#드롭 프레임이란 10분, 20분 같은 시간을 제외하고 매분 2프레임씩 삭제 시키는 것을 의미한다.
#fps = allframe/ 실제 시간(sec)



# 현재 프레임 수 연산 (video_name).get(cv.CAP_PROP_POS_FRAMES)->+1
#print("frame shape & count info \n", "frame info: " ,frame.shape,"count info: ",count)