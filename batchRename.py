import os

"""改名脚本"""

rootPath = 'C:\\Users\\lishuli\\Desktop\\NewFolderForm'

if __name__ == '__main__':
    # start = time.time()
    for (rootPath, rootDirName, rootFileName) in os.walk(rootPath):

        for iterRootDir in rootDirName:

            eachRootDirPath = os.path.join(rootPath, iterRootDir)
            # print(eachRootDirPath)
            subFilesList = os.listdir(eachRootDirPath)

            totalSubFileNum = len(subFilesList)

            orgImageNamesList = []
            xmlNameList = []

            for eachFileIter in range(0, totalSubFileNum, 1):

                # if subFilesList[eachFileIter].find('.jpg'):
                if subFilesList[eachFileIter].split('.')[1] == 'jpg':
                    fileName = subFilesList[eachFileIter]
                    orgImageNamesList.append(fileName)
                if subFilesList[eachFileIter].split('.')[1] == 'xml':
                    xmlName = subFilesList[eachFileIter]
                    xmlNameList.append(xmlName)
                if subFilesList[eachFileIter].split(".")[1] != 'jpg' and subFilesList[eachFileIter].split(".")[1] != 'xml':
                    errorFile = subFilesList[eachFileIter].split('.')[0]
                    print(errorFile)
            for eachRenameIter in range(0, len(orgImageNamesList), 1):
                orgFilePath = os.path.join(eachRootDirPath, orgImageNamesList[eachRenameIter])
                orgXmlPath = os.path.join(eachRootDirPath, xmlNameList[eachRenameIter])
                newFileName = orgImageNamesList[eachRenameIter].split('.')[0] + '_new1'+'.jpg'
                newXmlName = xmlNameList[eachRenameIter].split('.')[0] + '_new1'+'.xml'

                desFilePath = os.path.join(eachRootDirPath, newFileName)
                desXmlPath = os.path.join(eachRootDirPath, newXmlName)

                os.rename(orgFilePath, desFilePath)
                os.rename(orgXmlPath, desXmlPath)

