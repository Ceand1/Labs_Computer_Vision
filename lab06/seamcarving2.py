#pip install seam-carving
#https://pypi.org/project/seam-carving/

import numpy as np
from PIL import Image
import cv2
import sys
import argparse
import seam_carving
import glob


def waitKey(window_name, key):
    while cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) >= 1:
        keyCode = cv2.waitKey(1000) & 0xFF
        if (keyCode == key):
            cv2.destroyAllWindows()
            break




# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="Arquivo de imagem a ser redimensionada")
ap.add_argument("-fe","--forward", action='store_true', help="Calcular a energia adicionada")
ap.add_argument("-hf","--height_first", action='store_true', help="Remover primeiro as linhas")
ap.add_argument("-x", "--x_scale", type=int,default="100", help="Percentual de redimensionamento em x (0 a 100)")
ap.add_argument("-y", "--y_scale", type=int,default="100", help="Percentual de redimensionamento em y (0 a 100)")
args = vars(ap.parse_args())



#Imagem
img = cv2.VideoCapture(args["image"])

if(args["forward"]):
    e_mode = 'forward'
else:
    e_mode = 'backward'
    
#Ordem de remoção dos seams
if(args["height_first"]):
    carving_order = 'height-first'
else:
    carving_order = 'width-first'
    
    
i=0
while True:
	isTrue, frame = img.read()
	
	if isTrue == False:
		break
	
	frame_h, frame_w, _ = frame.shape
	
	x_scale = args["x_scale"]/100
	y_scale = args["y_scale"]/100

	new_size = (frame_w*x_scale, frame_h*y_scale)
	
	
	frame_seam = seam_carving.resize(
    		frame, new_size,
    		energy_mode=e_mode,   
    		order=carving_order)
    		
	width  = frame_seam.shape[1]
	height = frame_seam.shape[0]
	
	M_rotation = cv2.getRotationMatrix2D((width, height), -180, 1)
	frame_seam = cv2.warpAffine(frame_seam, M_rotation, (width*3,height*3))
	
	
	#cv2.imshow('Video', frame_seam)
	cv2.imwrite('images/kang'+str(i)+'.jpg',frame_seam)
	i+=1
	
	
	#vet.append(frame_seam)
	
	if cv2.waitKey(20) & 0xFF==ord('d'):
		break



#Escala

#Cálculo da energia

#Seam Carving


# Show
img.release()
#video.release()
cv2.destroyAllWindows()

