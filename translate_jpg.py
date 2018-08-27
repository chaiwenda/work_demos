# date:2018/8/27 10:41
# -*- coding: utf-8 -*-
#author;cwd
"""
function: 将图像转换成其他格式
"""
from PIL import Image
import os

image_path = './images/simple.png'
out_image_path = './saveFile/simple.jpg'

# 判断文件名后缀
if image_path.endswith('.png'):
    print(True)

image = Image.open(image_path)
image.save(out_image_path)
