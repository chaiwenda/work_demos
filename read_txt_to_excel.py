import os
import string
import openpyxl

"""
python3.5
function:将指定文件夹下的保存的txt文件内的数据copy到模板excel里
txt_log_path：txt保存的路径
j：插入excel表的原始行标
rootSrc_excel：打开模板excel表的路径
saveSrc_excel：保存excel表的路径
"""

txt_log_path = "F:\pythonProjectOpencv\\"
j = 3  # start index
rootSrc_excel = "./dataset/test2.xlsx"
saveSrc_excel = "./dataset/test4.xlsx"

write_lossrate_Lists1  = []
write_speedRate_Lists2  = []
for (rootPath, rootDirName, rootFileName) in os.walk(txt_log_path):
    print(rootFileName) # txt lists
    for item in rootFileName:
        eachRootDirPath = os.path.join(txt_log_path, item)
        line_number = open(eachRootDirPath)
        for line in line_number:
            if "丢失" in line:
                line = line.split("(")[1]
                line = line.split("丢")[0]
                lossrate = line.split("丢")[0].strip().split("%")[0]
                write_lossrate_Lists1.append(lossrate)
            elif "平均 = " in line:
                line = line.split("平均")[1]
                speedRate = line.split("=")[1].strip().split("ms")[0]
                write_speedRate_Lists2.append(speedRate)

print(write_lossrate_Lists1)
print(write_speedRate_Lists2)

# write into excel
wb = openpyxl.load_workbook(rootSrc_excel)
sheet = wb.get_sheet_by_name("Sheet1")

index = j
for write_lossrate_List1 in write_lossrate_Lists1:
        sheet["F" + str(index)] = write_lossrate_List1
        print("插入F" + str(index) + write_lossrate_List1)
        index += 1
index = j
for write_speedRate_List2 in write_speedRate_Lists2:
        sheet["C" + str(index)] = write_speedRate_List2
        print("插入C" + str(index) + write_speedRate_List2)
        index += 1
if os.path.exists(saveSrc_excel):
    os.remove(saveSrc_excel)
wb.save(saveSrc_excel)
print("收集 丢包率 + 平均速率 数据完毕")
