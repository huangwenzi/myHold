


# 按下的键的返回定义
class KeysRet():
    # 是功能 键
    isFun = 0
    # 不是功能键
    noFun = 1
    # 退出程序
    isExit = 2


# log输出的类型
class Log_type():
    # 打印到控制台
    dos = 0
    # 打印到本地
    local = 1
    # 两者都有
    both = 2
    # 弹窗警告
    popup = 3

# 这里保存了各种enum的类
class Enums():
    keysRet = None
    log_type = None
    # 初始化全部枚举
    def __init__(self):
        self.keysRet = KeysRet()    # 按下的键的返回定义
        self.log_type = Log_type()    # log输出的类型
enums = Enums()
