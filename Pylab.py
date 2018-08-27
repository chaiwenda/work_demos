# date:2018/8/27 13:44
# -*- coding: utf-8 -*-
#author;cwd
"""
function:
1. 绘制
"""
from PIL import Image
from pylab import *

im = array(Image.open('./images/simple.png'))
imshow(im)

x = [100, 150, 150, 100, 100]
y = [100, 100, 150, 150, 100]

# 带有与圆圈标记的绿线
# plot(x[:2], y[:2], "go-")
plot(x, y)

show()