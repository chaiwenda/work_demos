import os

"""
    删除文件
"""
def file_extension(path):
  return os.path.splitext(path)[1]

delList = []
jpgList = []
xmlList = []
delDir = "C:/Users/chaiwenda/Desktop/MaiDong"
delList = os.listdir(delDir)
print(delList)
print(delList.index('MaiDong_0026.xml'))

for name in delList:
    file_name = name # 去当前要匹配的文件名（）

    # acquire filename without 后缀 ：name
    index = name.rfind('.')
    name = name[:index]
    for match_file_name  in delList:
        i = 0
        if name in match_file_name:
            i = i+1
            if i > 1 :
                continue
    if i == 1:
        print("删除" + str(name))
        if os.path.exists("C:/Users/chaiwenda/Desktop/MaiDong/" + str(name) + '.xml'):
            os.remove("C:/Users/chaiwenda/Desktop/MaiDong/" + str(name) + '.xml')
        if os.path.exists("C:/Users/chaiwenda/Desktop/MaiDong/" + str(name) + '.jpg'):
            os.remove("C:/Users/chaiwenda/Desktop/MaiDong/" + str(name) + '.jpg')