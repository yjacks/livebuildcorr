import sys

from globol import *

correctList={}


def buildConfig():
    w = open("a.sh", "w")
    w.write("cd " + configDir)
    w.write("\nmkdir " + configDir + "/live")
    w.write("\ncd " + configDir + "/live")
    w.write("\nlb config")
    w.close()
    os.system("sh a.sh")


def readConfig():
    readFileIOList = []
    readFileTextList = []
    readFileTextListEnd = []
    n = -1
    for i in range(5):
        n += 1
        readFileIOList.append(open(configDir + "/live/config/" + readFilesList[n], "r"))

    for o in readFileIOList:
        readFileTextList.append(o.readlines())
        o.close()
    for r in readFileTextList:
        m = []
        for mid_r in r:
            if mid_r.find("=") != -1:
                m.append(mid_r)
        readFileTextListEnd.append(m)
    fileMap = readFileTextListEnd
    n = -1
    for i in fileMap:
        n += 1
        w = open(configDir + "/live/config/" + readFilesList[n], "w")
        w.writelines(i)
        w.close()
    return fileMap


def correctConfigMod(v, cor):
    n = v.find("=")
    return ''.join([v[0:n], v[n:cor]])


def configSend():
    print("""
    菜单依次为
    "binary"
    "bootstrap"
    "chroot"
    "common"
    "source"
    """)
    while True:
        cc = False
        # 头菜单
        while True:
            clearWindow()
            treeF = input("")
            if treeF == "exit":
                sys.exit()
            try:
                configFileSelect = selectTypeKeys[treeF]
            except:
                print("重选")
            else:
                break
        # 可选项分项菜单
        while True:
            clearWindow()
            for i in list(configFileSelect.keys()):
                print("可选项子菜单:\n")
                print(i + "\n")
            configFileSelectTemp = configFileSelect
            while True:
                treeF = input()
                if treeF == "exit":
                    cc = True
                    break
                configFileSelect = configFileSelectTemp
                try:
                    configFileSelect = configFileSelect[treeF]
                except:
                    print("重选")
                else:
                    break
            break
        if cc:
            continue
        # 选项菜单(选号)
        while True:
            n = -1
            print("选项:(填写序号)")
            for i in configFileSelect:
                print(str(n) + "\t" + i)
            while True:
                try:
                    treeF = input()
                except:
                    print("填写序号")
                else:
                    clearWindow()
                    break
            break
        if cc:
            continue
        while True:
            # 这里要保存变量到global
            # 实现思路 保存已被定义的变量为一个字典的key,值为values
            print("输入您需要修改的值:")
            corr_values=input()
            correctList[treeF]=corr_values
