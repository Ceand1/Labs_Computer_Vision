import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


filename = sys.argv[1]
img = cv2.imread(filename)

kernel = np.array([[0.3, 0.59, 0.11],[0.3, 0.59, 0.11],[0.3, 0.59, 0.11]])
                   
result = cv2.transform(img, kernel)

#im_b,im_g,im_r = cv2.split(img)


#result = cv2.merge([im_r*0.3,im_g*0.59,im_b*0.11])

plt.subplot(111),plt.imshow(result,cmap = 'gray'),plt.title('Result')
plt.xticks([]), plt.yticks([])
plt.show()
#cv2.imshow('result', result)
#cv2.waitKey(0)
