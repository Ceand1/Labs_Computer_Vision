import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


filename = sys.argv[1]
img = cv2.imread(filename)

kernel = np.array([[0.393, 0.769, 0.189],
                   [0.349, 0.686, 0.168],
                   [0.272, 0.534, 0.131]])
                   
result = cv2.transform(img, kernel)

plt.subplot(111),plt.imshow(result,cmap = 'gray'),plt.title('Result')
plt.xticks([]), plt.yticks([])
plt.show()
#cv2.imshow('result', result)
#cv2.waitKey(0)
