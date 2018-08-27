# date:2018/8/27 14:30
# -*- coding: utf-8 -*-
#author;cwd
"""
function:
    1:图像的数组表示
"""
from PIL import Image
from numpy import array
import numpy

fp = './images/simple.png'
im = array(Image.open(fp))
print(im.shape)
value = im[1:,:1]
print(value)