# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:23:01 2020

@author: lamington1010
"""
import cv2
import numpy as np

def imgimport():
    s1 = input("image filename without numbers, e.g. cats")
    s2 = input("file type, e.g. .jpg, .tif, etc ")
    s3 = int(input("what is the range of images?")) 
    s3a = 'file directory'
    
    x = 1; 
    Matrix = [];
  
    while x < s3:
        s4 = str(x);
        s5 = s3a+s1+s4+s2
        img = cv2.imread(s5,cv2.IMREAD_GRAYSCALE);
        img = np.array(img)
        imgprime = np.transpose(img)
        imgprimecol = imgprime.flatten()
       
        Arr = np.reshape(imgprimecol,(len(imgprimecol),1))
        Matrix.append(Arr);
        x = x + 1;
        print(np.size(Matrix))
    
    A = np.shape(Matrix)
        
    return np.reshape(Matrix,(A[0],A[1]))