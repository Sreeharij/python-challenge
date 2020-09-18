#rearrange pink lines to the left (left shift row from occurance of pink line.)

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import collections

# def non():
    # global arr,img
gif = cv2.VideoCapture('mozart.gif')
ret,frame = gif.read()

img = Image.fromarray(frame)
img = img.convert('RGB')
arr = np.array(img)
obj = collections.Counter(arr.ravel())

freq = {}
for i in range(480):
    for j in arr[i]:
        if tuple(j) in freq:
            freq[tuple(j)] += 1
        else:
            freq[tuple(j)] = 1
for number in freq:
    if freq[number]%480==0 and freq[number]!=0:
        print(number,":",freq[number],sep="")
new=[]
# print(arr.shape)
for row in range(480):
    cnt = 0
    for li in arr[row]:
        cnt += 1
        if li[0]==[255] and li[1]==[0] and li[2] == [255]:
            break
    idx = cnt

    for j in range(idx,640):
        new.append(arr[row][j])
    for j in range(idx):
        new.append(arr[row][j])
new = np.array(new)
new = np.reshape(new,(480,640,3))
print(new.shape)
cv2.imwrite('correct.jpg',new)

#answer = romance
