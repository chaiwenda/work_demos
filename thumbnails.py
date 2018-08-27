# date:2018/8/27 10:53
# -*- coding: utf-8 -*-
#author;cwd
"""
function:
1.创建缩略图
2.复制黏贴
"""
from  PIL import Image

fp = './images/simple.png'

# function 1
fi_im = Image.open(fp)
fi_im.thumbnail((64,64))
# fi_im.show()

# funtion2
# 创建需要修改的图片对象
img1 = Image.open('.\images\\simple.png')
# 创建一个新的图片对象
img2 = Image.new('RGB', (402, 402), (255, 255, 255))
# 圈出需要复制的图片框(这里其实是复制img整个图片)
img2.show()
box1 = (0, 0, 200, 100)
# box1中的四元组的四个值分别代表
#   ：左边线的x坐标
#   ：上边线的y坐标
#   ：右边线的x坐标
#   ：下边线的y坐标
# 按圈出的框复制图片
region = img1.crop(box1)
# 很多文档都有这一步, 这一步其实是为了显示图片被复制了，将复制的图片框旋转显示，具体旋转的情况，可以参见：http://hereson.iteye.com/blog/2224334
# region = region.transpose(Image.ROTATE_180)
# 粘贴图片（注意粘贴图片的位置，是从图片2的中间开始粘贴的）
img2.paste(region, (0, 0))
# 保存图片2
img2.save('./saveFile/simple2.jpg')
img2.show()
