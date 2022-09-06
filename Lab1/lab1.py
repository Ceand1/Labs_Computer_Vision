import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
#from skimage import io

#abre imagem
filename = sys.argv[1]
im = cv2.imread(filename)

#converte cores
im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

#split
#im_h,im_s,im_v = cv2.split(im)
im_h = im[:,:,0]
im_s = im[:,:,1]
im_v = im[:,:,2]

#lower=np.array([50, 100,100])
#upper=np.array([70, 255, 255])

#mask = cv2.inRange(im, lower, upper)
width = im.shape[1]
height = im.shape[0]

#troca as cores
for c in range(0, width-1):
	for l in range(0, height-1):
		if(im_h[l][c] >= 16 and im_h[l][c]<=75):
			im_h[l][c]+=65
		elif(im_h[l][c] >= 80 and im_h[l][c]<=112):
			im_h[l][c]-=40

	
#combina as imagens
im = cv2.merge([im_h,im_s,im_v])

#mostra imagens
imagens = [im_h,im_s,im_v]

im = cv2.cvtColor(im, cv2.COLOR_HSV2BGR)

#x_values = np.arange(256)

#plt.subplot(1,4,1),plt.imshow(imagens[0],cmap = 'gray')
#plt.subplot(1,4,2),plt.imshow(imagens[1],cmap = 'gray')
#plt.subplot(1,4,3),plt.imshow(imagens[2],cmap = 'gray')
#plt.subplot(1,1,1),plt.imshow(im,cmap = 'gray')


cv2.imshow("Trocada",im)
cv2.waitKey(0)

#plt.show()












