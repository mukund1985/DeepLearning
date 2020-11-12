import cv2
import numpy as np

print("Package Imported")

##################################
# Read - Images - Videos - WebCam
##################################

####################
# To Read the Image
####################

img = cv2.imread("Resources/lena.png")

#######################
# To Display the Image
#######################

cv2.imshow("Output", img)
cv2.waitKey(1000)

##########################
# How to Import the Video
##########################


