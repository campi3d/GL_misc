
import os
import json


def saveMSH(data,jsonFilePath):
    "stores a specifc project path for a given variable"


    if os.path.exists(jsonFilePath):
        with open(jsonFilePath, "r") as jsonFile:
            try:
                data = json.load(jsonFile)
            except Exception:
                pass

    with open(jsonFilePath, "w+") as jsonFile:
        jsonFile.write(json.dumps(data))




def generateMSHFile():
    '''Generates a Mari Shelf File'''

    path = 'D:/AlphaPack Vol1/Output'
    dirs =  os.listdir(path)
    srcdir = os.path.join(path + os.sep +  dirs[0])
    texdirs = os.listdir(srcdir)
    key = 0

    for dir in texdirs:
        absPath = srcdir + os.sep + dir
        jsonFile = dir + '.msh'
        jsonFilePath = absPath + os.sep + jsonFile
        images = os.listdir(absPath)
        beginningOfFile = '<!DOCTYPE MariML><Mari Version="2.1" FnVersion="4.1"> <MriActionCollection Type="MriActionCollection"><objectName Type="QString"></objectName><selectedType="bool">false</selected><uuidString Type="QString">{1b960a07-0529-415a-bf60-4524bdceb3f2}</uuidString><supportedTypes Type="QStringList"></supportedTypes><name Type="QString">Unnamed</name><m_ActionSources Type="QPair&lt; QString, QString>" ContainerType="QVector" Size="1">'
        endofFile = '</m_ActionSources></MriActionCollection></Mari>'

        for img in images:
            imgpath = os.path.join(absPath + os.sep + img)
            actionstring = '<Action m_ActionSources_key="'+ str(key) + '" Type="QPair&lt; QString, QString>" Data="'+imgpath + '" ActionType="Mari/MriImagePath" Label="' + img + '"></Action>'

        fileOutput = beginningOfFile + actionstring + endofFile

        saveMSH(fileOutput,jsonFilePath)


generateMSHFile()
