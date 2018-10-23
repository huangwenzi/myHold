
# 这里保存了各种enum的类

# 对于按下的键的返回定义
class KeysRet():
    # 是功能 键
    isFun = 0
    # 不是功能键
    noFun = 1
    # 退出程序
    isExit = 2
# 实例化这个过程处理类
keysRet = KeysRet()

class Log_type():
    # 打印到控制台
    dos = 0
    # 打印到本地
    local = 1
    # 两者都有
    both = 2
    # 弹窗警告
    popup = 3
log_type = Log_type()