# O filtro passa-baixa deixa passar apenas as frequências abaixo de uma determinada frequência
# Na primeira imagem há muitos ruídos, então o fator de corte teve que ser 40 para eliminá-los
# em grande parte, por conta disso a imagem ficou borrada.
# Na segunda imagem o fator foi aumentado um pouco. A maioria dos ruídos foram eliminados 
# porém a imagem ficou um pouco distorcida.
# Não houve mudanças significativas na terceira imagem.




import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from cv_utils import waitKey

filename = sys.argv[1]
img = cv2.imread(filename,0)

img_fft = np.fft.fft2(img)
img_fft_shift = np.fft.fftshift(img_fft)

#ret,im_thresh = cv2.threshold(img_fft_shift,127,0,cv2.THRESH_BINARY)

rows = img.shape[0]
cols = img.shape[1]
crow,ccol = rows//2 , cols//2

mask = np.zeros([rows,cols])
mask = mask.astype(np.uint8) 
mask[crow-40:crow+40, ccol-40:ccol+40] = 1
fshift = img_fft_shift*mask

idft_shift = np.fft.ifftshift(fshift) 
ifimg = np.fft.ifft2(idft_shift)
ifimg = np.abs(ifimg)


img_fft = np.log(np.abs(img_fft))
img_fft_shift = np.log(np.abs(img_fft_shift))




#image plot
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img_fft_shift, cmap = 'gray')
plt.title('shifted'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_fft, cmap = 'gray')
plt.title('fft'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(ifimg, cmap = 'gray')
plt.title('LP'), plt.xticks([]), plt.yticks([])

plt.show() 

#cv2.imshow('image',img_fft_shift)
#cv2.waitKey(0) #27 = ESC	       


   
