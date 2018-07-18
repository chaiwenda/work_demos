import os
"""
delete files from the file path
"""

matchList = ["0056","0060","0062","0078",
            "0078","0078",
             "0216","0254",
             "0489",
             "0670","0670","0686","0686",
             "0932","0934","0942","0974","0996",
             1000,1006,1031,1033,1046,1048,1050,1062,1064,1066,
             1165,1177,1181,1185,1196,
             1217,1219,1227,1231,1235,1239,1241,1245,1246,1247,1249,1253,1261,1270,1271,
             1388,
             1404,1412,1414,1420,1430,1434,1464,
             1514,1516,1518,1520,1532,1540,1542,1544,1548,1552,1554,1556,1558,1560,1562,1570,
             1610,1612,1690,
             1786,
             1809,1815,1872,1885,1886,1887,
             1901,1913,1917,1931,1933,1939,1953,1954,1970,1972,
             2097,2099,
             2137,2144,2205,2241,2243,2269,2322,2367,2399,
             2404,2419,2457,2458,
             2669
             ]
delList = []
delDir = "C:/Users/chaiwenda/Desktop/MaiDong"
delList = os.listdir(delDir)

print(os.path.exists("C:/Users/chaiwenda/Desktop/MaiDong/MaiDong_0026.jpg"))

i = 0
for f in matchList:
    # print("MaiDong_" + str(f))
    name_file_remove = "MaiDong_" + str(f)
    for matchfile in delList:
        if str(f) in matchfile :
            i = i + 1
            print(f)
            print("删除文件" + str(delDir) + str(name_file_remove) + ".jpg")
            print("删除文件" + str(delDir) + str(name_file_remove) + ".xml")
            # print()
            if os.path.exists("C:/Users/chaiwenda/Desktop/MaiDong/MaiDong_" + str(f) + '.jpg'):
                os.remove("C:/Users/chaiwenda/Desktop/MaiDong/" + name_file_remove + ".jpg")
                os.remove("C:/Users/chaiwenda/Desktop/MaiDong/" + name_file_remove + ".xml")

print(i)