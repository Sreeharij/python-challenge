#get pixels of odd row and odd column or even row and even column.

import cv2
import numpy as np

img = cv2.imread('cave.jpg')
h,w,c = img.shape

arr1 = []
arr2 = []
for i in range(h):
    for j in range(w):
        if i%2!=0 and j%2!=0:
            arr1.append(img[i][j])

arr1 = np.array(arr1)
arr1 = np.reshape(arr1,(240,320,3))

for i in range(h):
    for j in range(w):
        if i%2==0 and j%2==0:
            arr2.append(img[i][j])

arr2 = np.array(arr2)
arr2 = np.reshape(arr2,(240,320,3))

cv2.imwrite('ans1.jpg',arr1)
cv2.imwrite('ans2.jpg',arr2)

#both the pictures are same,we need only one of them.
#answer is evil
