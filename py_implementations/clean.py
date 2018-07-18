# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 16:57:09 2018

@author: adityac8
"""
import matplotlib.image as mpimg
from glob import glob
import os

def rem(directory):
    for f in glob(directory+'/*'):
        img=mpimg.imread(f)
        b = os.path.getsize(f)
        if len(img)>100 or b<500:
            os.remove(f)

for i in range(12):
    rem(str(i))
