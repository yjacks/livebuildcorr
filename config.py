from globalProject import *

correctList = {}
configDir = "/home/jack/Data/Sources/Temp/Test"

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


def configSend():
    global correctList
    print("""
    菜单依次为
    "binary"
    "bootstrap"
    "chroot"
    "common"
    "source"
    如果输入"exit",
    则在全部页面都会跳转至本页面
    """)
    while True:
        cc = False
        # 头菜单
        while True:
            treeF = input("")
            if treeF == "exit":
                cc = True
                break
            try:
                configFileSelect = selectTypeKeys[treeF]
            except:
                print("重选")
            else:
                break
        # 可选项分项菜单
        if cc:
            break
        while True:
            clearWindow()
            print("可选项子菜单:\n")
            # noinspection PyUnboundLocalVariable
            for i in list(configFileSelect.keys()):
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
                n += 1
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
            corr_values = input()
            if corr_values=="exit":
                print("跳转到1级页面")
                continue
            correctList[treeF] = corr_values
            break


def writeConfig():
    # 通过corrCon函数写回
    for i in readFilesList:
        with open(configDir+"/live/config/"+i,"r") as r:
            sourcesSelectList=r.readlines()
        for v in sourcesSelectList:
            for n in correctList:
                if n==v[0:v.find("=")]:
                    num = sourcesSelectList.index(v)
                    sourcesSelectList.remove(v)
                    v=v[0:v.find("=")+1]+n
                    sourcesSelectList.insert(num,v)
        with open(configDir+i,"w") as w:
            w.writelines(sourcesSelectList)
