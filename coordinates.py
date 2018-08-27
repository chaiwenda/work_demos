# date:2018/8/27 11:35
# -*- coding: utf-8 -*-
#author;cwd
"""
function:获取鼠标在图像上的当前坐标
"""
from PIL import Image
from pylab import *

im = array(Image.open('./images/set.png'))
imshow(im)
# print('Please click 3 points')
# x = ginput(3)
# print('you clicked:', x)

