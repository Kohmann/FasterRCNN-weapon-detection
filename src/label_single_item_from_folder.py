#!/usr/bin/env python
# coding: utf-8

# In[134]:


import numpy as np
import cv2 as cv
import os

def training_data_from_baggage(path):
    
    folders = ["B0049", "B0050", "B0051", "B0076"] # "B0077"
    categories = {"B0049": 'handgun', "B0050": 'shuriken', "B0051": 'razorblade' ,"B0076": 'knife'} # extra "B0077": 'knife'
    
    dic = dict()
    
    for folder in folders:
        label = categories[folder]
        imageList = os.listdir(path +"/"+ folder)
        
        for image in imageList:
            if image[-3:] == 'png':
                img = cv.imread(path +"/"+ folder + "/" + image,0)
                ret,thresh = cv.threshold(1-img,60,255,0)
                cnt = sorted(cv.findContours(thresh, 2, 1)[-2], key=cv.contourArea)
                x,y,w,h = cv.boundingRect(cnt[-1])
                bbox = [x,y,x+w,y+h]
                dic.update( {image: [ [bbox],[label]] } )

    return dic

