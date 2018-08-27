# date:2018/8/27 14:12
# -*- coding: utf-8 -*-
#author;cwd
"""
function:
    绘制图像轮廓和直方图
"""
from PIL import Image
from pylab import *

fp = './images/simple.png'
im = array(Image.open(fp).convert('L'))
im2 = Image.open(fp).convert('L')
im2.show()

# new figure
figure()
gray()

contour(im, origin='image')
axis('equal')
figure()
hist(im.flatten(), 128)
show()