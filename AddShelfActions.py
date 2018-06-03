import os
import json



def generateMSHFile():
    '''Generates a Mari Shelf File'''

    path = 'D:/AlphaPack Vol1/Output/'
    dirs =  os.listdir(path)

    for subfolder in dirs:
        srcdir = os.path.join(path + os.sep +  subfolder)
        texdirs = os.listdir(srcdir)
        key = 0

        for dir in texdirs:
            actionstring = ""
            absPath = srcdir + os.sep + dir
            mshFile = dir + '.msh'
            mshFilePath = absPath + os.sep + mshFile
            images = os.listdir(absPath)
            beginningOfFile = '<!DOCTYPE MariML><Mari Version="2.1" FnVersion="4.1"> <MriActionCollection Type="MriActionCollection"><objectName Type="QString"></objectName><selected Type="bool">false</selected><uuidString Type="QString">{1b960a07-0529-415a-bf60-4524bdceb3f2}</uuidString><supportedTypes Type="QStringList"></supportedTypes><name Type="QString">Unnamed</name><m_ActionSources Type="QPair&lt; QString, QString>" ContainerType="QVector" Size="1">'

            endofFile = '</m_ActionSources></MriActionCollection></Mari>'

            for img in images:
                if img.endswith('msh'):
                    pass
                else:
                    imgpath = os.path.join(absPath + os.sep + img)
                    actionstring = actionstring + '<Action m_ActionSources_key="' + str(key) + '" Data="'+ "/" +  img + '" ActionType="Mari/MriImagePath" Type="QPair&lt; QString, QString>" Label="' + img + '"></Action>'
                    key += 1
            fileOutput = beginningOfFile + actionstring + endofFile

            with open(mshFilePath, 'w') as file:
                file.write(fileOutput)
                file.close()


generateMSHFile()
