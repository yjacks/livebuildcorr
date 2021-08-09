# 测试
import config
import correctLiveCD

config.buildConfig()
config.readConfig()
config.configSend()
config.writeConfig()
correctLiveCD.liveBuild()
correctLiveCD.mountIso()
correctLiveCD.DIY_live()
