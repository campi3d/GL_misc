import os



path = 'D:/AlphaPack Vol1/Output'
dirs =  os.listdir(path)
srcdir = os.path.join(path + os.sep +  dirs[0])
texdirs = os.listdir(srcdir)

for dir in texdirs:
    absPath = srcdir + os.sep + dir
    images = os.listdir(absPath)
    for img in images:
        imgpath = os.path.join(absPath + os.sep + img)
        actionstring = '<Action m_ActionSources_key="0" Type="QPair&lt; QString, QString>" Data="'+imgpath + '" ActionType="Mari/MriImagePath" Label="' + img + '"></Action>'
        print actionstring




