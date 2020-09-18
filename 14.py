#initialise a 3d array.
#spirally navigate the new array and assign values values from wire.png
#and create a new image out of it.
import cv2
import numpy as np

img = cv2.imread('wire.png')
print(img.shape)

reshaped = cv2.imread('correct.jpg')

def spiralPrint(m, n, imarr):
    rgb = [0,0,0]
    picture = [[rgb for i in range(100)]for j in range(100)]

    k = 0; l = 0
    imstart = 0
    while (k < m and l < n) :
        for i in range(l, n) :
            picture[k][i]=imarr[imstart]
            imstart += 1

        k += 1
        for i in range(k, m) :
            picture[i][n-1]=imarr[imstart]
            imstart += 1

        n -= 1
        if ( k < m) :
            for i in range(n - 1, (l - 1), -1) :
                picture[m-1][i]=imarr[imstart]
                imstart += 1

            m -= 1

        if (l < n) :
            for i in range(m - 1, k - 1, -1) :
                picture[i][l]=imarr[imstart]
                imstart += 1
            l += 1
    return picture

imarr = [img[0][i] for i in range(10000)]
picture = spiralPrint(100,100,imarr)
picture = np.array(picture)

print(picture.shape)
cv2.imwrite('ans.jpg',picture)

#answer is uzi

