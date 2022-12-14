import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


# Abre a imagem
filename = sys.argv[1]
#img = cv2.imread(filename)

img = cv2.VideoCapture(filename)



while True:
	isTrue, frame = img.read()
	
	if isTrue == False:
		break
	
	img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	model_path = "./models/haarcascade_frontalface_default.xml"
	detector = cv2.CascadeClassifier(model_path)
	
	results = detector.detectMultiScale(img_gray, scaleFactor=1.15,minNeighbors=5,minSize=(50, 50))

	for (x,y,w,h) in results:
    		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    		
  	model_path = "./models/haarcascade_smile.xml"
    	
    	detector = cv2.CascadeClassifier(model_path)
	
	results = detector.detectMultiScale(img_gray, scaleFactor=1.15,minNeighbors=5,minSize=(50, 50))

	for (x,y,w,h) in results:
    		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
	
	cv2.imshow('Video', frame)
	
	
	#vet.append(frame_seam)
	
	if cv2.waitKey(20) & 0xFF==ord('d'):
		break


#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#outros modelos em:
# https://github.com/opencv/opencv/tree/master/data/haarcascades


## Carrega o modelo
#model_path = "./models/haarcascade_frontalface_default.xml"
#detector = cv2.CascadeClassifier(model_path)

#Detecção
#results = detector.detectMultiScale(img_gray, scaleFactor=1.2,minNeighbors=1,minSize=(10, 10))

# Exibe os resultados
#for (x,y,w,h) in results:
#    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
  
#cv2.imshow('result',img)
cv2.waitKey(0)
img.release()
cv2.destroyAllWindows()





