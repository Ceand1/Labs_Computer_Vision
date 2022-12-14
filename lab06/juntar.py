import cv2
import os
import glob

video_name = 'video.avi'

images = glob.glob('images/*.jpg')
images.sort()

frame = cv2.imread(images[0])
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 25, (width,height))

for image in images:
    video.write(cv2.imread(image))
    
vet = []

vet.append=1.5

cv2.destroyAllWindows()
video.release() 
