# -*- coding: utf-8 -*-
"""UDAY_SONI_PIET18CS147.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OD2-Xa823A-q5l3SdmstaPHt6i5QYsJ9

1 Question
"""

import numpy as np
import pandas as pd
import cv2 as cv
from google.colab.patches import cv2_imshow # for image display
from skimage import io
from PIL import Image 
import matplotlib.pylab as plt
#import matplotlib.image as mpimg 
#from matplotlib.pyplot import imshow
#%matplotlib inline

Direction = "Y" #@param ["X", "Y"]
Transformation = "Reflection" #@param ["Shearing", "Scaling", "Translation", "Reflection"]
Y_factor =  0#@param {type:"number"}
X_Factor =  0#@param {type:"number"}
img_T = cv.imread('/content/b.jpg')
image = cv.cvtColor(img_T, cv.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()

if Transformation == "Translation": 
  if Direction == "Y":
    M = np.float32([[1, 0, 20], 
                [0, 1, Y_factor], 
                [0, 0, 1]])
    img1 = cv.warpPerspective(image, M, (image.shape[1], image.shape[0]))
  else:
    M = np.float32([[1, 0, X_Factor], 
                [0, 1, 100], 
                [0, 0, 1]])
    img1 = cv.warpPerspective(image, M, (image.shape[1], image.shape[0]))
  plt.imshow(img1)
  plt.show()
if Transformation == "Shearing": 
  rows, cols, dim = image.shape
  if Direction == "Y":
     M1 = np.float32([[1, Y_factor, 0],
             	[0, 1  , 0],
            	[0, 0  , 1]])
     sheared_img = cv.warpPerspective(image,M1,(int(cols*1.5),int(rows*1.5)))
  else:
    M1 = np.float32([[1, 0, 0],
             	[X_Factor, 1  , 0],
            	[0, 0  , 1]])
    sheared_img = cv.warpPerspective(image,M1,(int(cols*1.5),int(rows*1.5)))
  plt.imshow(sheared_img)
  plt.show()

if Transformation == "Scaling": 
  rows, cols, dim = image.shape
  if Direction == "Y":
    M = np.float32([[1, 0  , 0],
            	[0,   Y_factor, 0],
            	[0,   0,   1]])
    scaled_img = cv.warpPerspective(image,M,(cols,rows))
  else:
    M = np.float32([[X_Factor, 0  , 0],
            	[0,   1, 0],
            	[0,   0,   1]])
    scaled_img = cv.warpPerspective(image,M,(cols,rows))
  plt.imshow(scaled_img)
  plt.show()

if Transformation == "Reflection": 
  rows, cols, dim = image.shape  
  if Direction == "Y":
    M = np.float32([[-1,  0, cols],
                [0, -1, rows],
                [0,  0, 1   ]])
    reflected_img = cv.warpPerspective(image,M,(int(cols),int(rows)))  
  else:
    M = np.float32([[-1,  0, cols],
                [0, -1, rows],
                [0,  0, 1   ]])
    reflected_img = cv.warpPerspective(image,M,(int(cols),int(rows)))   
  plt.imshow(reflected_img)
  plt.show()

"""2 Question

"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
def main():
    img = cv2.imread("/content/a.jpg", 1)
   
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    k1 = np.array(([0, -1, 0], [-1, 5, -1], [0, -1, 0]), np.float32)
    
    print(k1)
    print(type(k1))

    output = cv2.filter2D(img, -1, k1)
    
    plt.subplots(1,1,figsize=(10,10))
    plt.imshow(img)
    plt.title('Original Image')
    
    plt.subplots(1,1,figsize=(10,10))
    plt.imshow(output)
    plt.title('Sharpen Edges')
    
    plt.show()

if __name__== "__main__":
    main()