


import os


def getTxt():
    fPath = os.listdir(path='C:\\drillFolder\\')



    fPath2 = 'C:\\drillFolder\\'

    file = 'Flex.txt'
    file2 = 'Text.txt'
    jPath = os.path.join(fPath2,file)
    print(jPath)


    tPath = os.path.getmtime(file)
    print(tPath)
    wPath = os.path.join(fPath2,file2)

    sPath = os.path.getmtime(file2)

    print(wPath)
    print (sPath)


getTxt()
