# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:23:01 2020

@author: lamington1010
"""
import cv2
import numpy as np
import os

def imgimport():
    s1 = input("image filename without numbers, e.g. cats")
    s2 = input("file type, e.g. .jpg, .tif, etc ")
    s3 = int(input("what is the range of images?")) 
    
    x = 1; 
    Arr = 0;
  
    while x < s3:
        s4 = str(x);
        s5 = s1+s4+s2
        img = cv2.imread(s5,cv2.IMREAD_GRAYSCALE);
        img = np.array(img)
        imgprime = np.transpose(img)
        imgprimecol = imgprime.flatten()
        imgprimenowcol = imgprimecol.reshape(len(img),1)
        Arr = Arr.append(imgprimenowcol);
        x = x + 1;