# date:2018/8/27 11:49
# -*- coding: utf-8 -*-
#author;cwd
"""
function:
    1.调整图像尺寸大小
    2.图像旋转
"""
from PIL import Image

fp ='./images/simple.png'
img = Image.open(fp)
img.show()
box = (128, 128)
img2 = img.resize(box)
img3 = img2.rotate(59)
img4 = img3.resize((256,256))
img4.show()