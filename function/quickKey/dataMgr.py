
# 数据管理类
class DataMgr():
    # 是否开启快捷键功能
    openFlag = True
    # 记录按下的键，只是按下，没有弹起
    keyDown = []
    # 保存记录快捷键对应坐标的字典{"number" : [x,y],...}
    position = {}
    
# 可以考虑将数据保存留在下一次载入
dataMgr = DataMgr()

# 这里返回值的枚举
class KeysRet():
    # 是功能 键
    isFun = 0
    # 不是功能键
    noFun = 1
    # 退出程序
    isExit = 2

# 实例化这个过程处理类
keysRet = KeysRet()