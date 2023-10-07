__author__ = 'Sundar Santhanam'

import cv2
import numpy as np

jc = cv2.imread("jc_orig.jpg")

scale_percent = 0.60

width = int(jc.shape[1]*scale_percent)
height = int(jc.shape[0]*scale_percent)

dim = (width,height)
resized = cv2.resize(jc,dim,interpolation = cv2.INTER_AREA)

kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1, 9,-1],
                              [-1,-1,-1]])
sharpened = cv2.filter2D(resized,-1,kernel_sharpening)



gray = cv2.cvtColor(sharpened , cv2.COLOR_BGR2GRAY)
inv = 255-gray
gauss = cv2.GaussianBlur(inv,ksize=(15,15),sigmaX=0,sigmaY=0)

def dodgeV2(image,mask):
    return cv2.divide(image,255-mask,scale=256)

pencil_jc = dodgeV2(gray,gauss)



cv2.imshow('resized',resized)
cv2.imshow('sharp',sharpened)
cv2.imshow('gray',gray)
cv2.imshow('inv',inv)
cv2.imshow('gauss',gauss)
cv2.imshow('pencil sketch',pencil_jc)
#cv2.imwrite("D:\Python36\siva_written.jpg",pencil_jc)
cv2.waitKey(0)
cv2.destroyAllWindows()

