import cv2
import numpy as np
import matplotlib.pyplot as plt
import imageio
import imutils
import sys
cv2.ocl.setUseOpenCL(False)

feature_extractor = 'orb' # one of 'sift', 'surf', 'brisk', 'orb', 'kaze', 'akaze'
feature_matching = 'bf'

filename1 = sys.argv[1]
filename2 = sys.argv[2]

trainImg = imageio.imread(filename2)
trainImg_gray = cv2.cvtColor(trainImg, cv2.COLOR_BGR2GRAY)

queryImg = imageio.imread(filename1)

queryImg_gray = cv2.cvtColor(queryImg, cv2.COLOR_BGR2GRAY)



def detectAndDescribe(image, method=None):
    
    
    assert method is not None
    
    if method == 'sift':
        descriptor = cv2.xfeatures2d.SIFT_create()
    elif method == 'surf':
        descriptor = cv2.xfeatures2d.SURF_create()
    elif method == 'brisk':
        descriptor = cv2.BRISK_create()
    elif method == 'orb':
        descriptor = cv2.ORB_create()
    elif method == 'kaze':
        descriptor = cv2.KAZE_create()
    elif method == 'akaze':
        descriptor = cv2.AKAZE_create()
        
    
    (kps, features) = descriptor.detectAndCompute(image, None)
    
    return (kps, features)

kpsA, featuresA = detectAndDescribe(trainImg_gray, method=feature_extractor)
kpsB, featuresB = detectAndDescribe(queryImg_gray, method=feature_extractor)



def createMatcher(method,crossCheck):
    
    if method == 'sift' or method == 'surf' or method == 'kaze':
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=crossCheck)
    else:
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=crossCheck)
    return bf

def matchKeyPointsBF(featuresA, featuresB, method):
    bf = createMatcher(method, crossCheck=True)
        
    best_matches = bf.match(featuresA,featuresB)
    
    rawMatches = sorted(best_matches, key = lambda x:x.distance)

    return rawMatches



fig = plt.figure(figsize=(20,8))

matches = matchKeyPointsBF(featuresA, featuresB, method=feature_extractor)
img3 = cv2.drawMatches(trainImg,kpsA,queryImg,kpsB,matches[:100],
                           None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

#plt.imshow(img3)
#plt.show()

def getHomography(kpsA, kpsB, featuresA, featuresB, matches, reprojThresh):

    kpsA = np.float32([kp.pt for kp in kpsA])
    kpsB = np.float32([kp.pt for kp in kpsB])
    
    if len(matches) > 4:

    
        ptsA = np.float32([kpsA[m.queryIdx] for m in matches])
        ptsB = np.float32([kpsB[m.trainIdx] for m in matches])
        
    
        (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC,
            reprojThresh)

        return (matches, H, status)
    else:
        return None

M = getHomography(kpsA, kpsB, featuresA, featuresB, matches, reprojThresh=4)
if M is None:
    print("Error!")
(matches, H, status) = M

width = trainImg.shape[1] + queryImg.shape[1]
height = trainImg.shape[0] + queryImg.shape[0]


result = cv2.warpPerspective(trainImg, H, (width, height))

result[0:queryImg.shape[0], 0:queryImg.shape[1]] = queryImg


plt.imshow(result)

plt.show()



