# 测试
import config
import correctLiveCD
configDir=input("输入构建路径:")
config.buildConfig()
config.readConfig()
config.configSend()
config.writeConfig()
correctLiveCD.liveBuild()
correctLiveCD.mountIso()
correctLiveCD.DIY_live()
correctLiveCD.isoBuild()
