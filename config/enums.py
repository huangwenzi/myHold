
# 按下的键的返回定义
class Keys_ret():
    # 是功能键
    is_fun = 0
    # 是普通键
    is_ordinary = 1
    # 退出程序
    is_exit = 2


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
        self.keys_ret = Keys_ret()    # 按下的键的返回定义
        self.log_type = Log_type()    # log输出的类型
enums = Enums()
