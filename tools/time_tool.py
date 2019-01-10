# 系统库
import time
# 项目库


# 时间处理工具
class Time_tool():
    
    # 初始化工具
    def __init__(self):
        pass

    # 获取当前时间的字符串格式
    def now_time(self):
        return time.strftime("%Y-%m-%d %H-%M-%S :", time.localtime())

    # 获取今天的log名称
    def get_log_name(self):
        return time.strftime("./logs/out_log_%Y-%m-%d.log", time.localtime())
    
    # 获取图片名称
    def get_photo_name(self):
        return time.strftime("%Y-%m-%d_%H-%M-%S.png", time.localtime())

time_tool = Time_tool()