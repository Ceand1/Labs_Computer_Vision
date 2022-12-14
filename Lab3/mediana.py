# O filtro mediana subtitui o valor de um pixel pelo valor da mediano dos valores de
# seus vizinhos.
# Na imagem do circuto é mostrado ruído sal e pimenta, em comparação com o filtro média,
# que desfoca a imagem e deixa alguns ruídos, o filtro mediana é melhor.
# Na segunda imagem o mediana foi o filtro que mais tirou ruídos e "realçou".
# A terceira imagem quase não possui ruídos e o mediana é um dos filtros que menos 
#altera a imagem.  


import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

from cv_utils import waitKey

filename = sys.argv[1]
im = cv2.imread(filename, 0)

median_blur = cv2.medianBlur(im,5)


plt.subplot(111),plt.imshow(median_blur,cmap = 'gray'),plt.title('Mediana')
plt.xticks([]), plt.yticks([])
plt.show()
