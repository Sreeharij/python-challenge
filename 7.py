#download image and save it as 'oxygen.jpg'
#pixels at the centre are in grey scale.
#convert the obtained ascii values.

import cv2
import numpy as np

img = cv2.imread('oxygen.png')
h,w,c = img.shape
print(img.shape)

arr = []

for i in range(w):
    if img[h//2][i][0]==img[h//2][i][1]==img[h//2][i][2]:
        arr.append(img[h//2][i][0])

arr = arr[::7]
for i in arr:
    print(chr(i),end="")
print()
#convert the new ascii values obtained.

next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in next_level:
    print(chr(i),end="")

#answer is 'integrity'
