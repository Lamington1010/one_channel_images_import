#image import function
clear all
clc

#function to convert a range (m) of one channel images (n x n pixels),into 
#a n^2 x m array. Images must be of same dimensions. 
 
#e.g. for images labelled cell1.jpg, cell2.jpg,.... cell200,jpg 
#s1 = 'cell', s2 = '.jpg', s3 = jpg

function [Arr] = imgimport()
  
  s1 = input("image filename without numbers, e.g. cats")
  s2 = input("file type, e.g. .jpg, .tif, etc ")
  s3 = input("what is the range of images?") 
  x = 1; 
  Arr = 0;
  Arr(:,1) = [];
  
  while x <= s3;
    s4 = num2str(x);
    s5 = strcat(s1,s4,s2);
    img = imread(s5);
    imgprime = img';
    imgprimecol = imgprime(:);
    Arr = [Arr imgprimecol];
    x = x + 1;  
  endwhile
  
endfunction