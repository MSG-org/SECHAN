import cv2
import random
pic_top_path = '/Users/sechan/Desktop/v.data-ds/test3.png'
pic_sam_path = '/Users/sechan/Desktop/v.data-ds/test2.png'
pic_dif_path = '/Users/sechan/Desktop/v.data-ds/test1.png'
imageNDArray = cv2.imread(pic_sam_path)
rotateImageNDArray = cv2.imread(pic_top_path)

grayscaleImageNDArray = cv2.cvtColor(imageNDArray, cv2.COLOR_BGR2GRAY)
rotateGrayscaleImagenDArray = cv2.cvtColor(rotateImageNDArray, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

keyPointList, keyPointDescriptor = sift.detectAndCompute(grayscaleImageNDArray, None)
rotateKeyPointList, rotateKeyPointDescriptor = sift.detectAndCompute(rotateGrayscaleImagenDArray, None)

bfMatcher = cv2.BFMatcher()

matchList = bfMatcher.knnMatch(keyPointDescriptor, rotateKeyPointDescriptor, k=2)

goodList = []

for m, n in matchList:
    if m.distance < 0.7 * n.distance:
        goodList.append([m])

random.shuffle(goodList)  # 비교한 특징점들 중에서 일부만 골고루 표시하기 위해 섞는다.

matchImageNDArray = cv2.drawMatchesKnn(imageNDArray, keyPointList, rotateImageNDArray, rotateKeyPointList, \
                                       goodList[:50], flags=2, outImg=None)

cv2.imwrite("target.jpg", matchImageNDArray)
matchImageNDArray = cv2.resize(matchImageNDArray,dsize = (960,800),interpolation=cv2.INTER_AREA)
cv2.imshow("image", matchImageNDArray)

cv2.waitKey(0)
cv2.destroyAllWindows()
