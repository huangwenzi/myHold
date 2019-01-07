# 系统库
import time
from PySide2 import QtWidgets
# 项目库
from config.enums import enums
from tools.time_tool import time_tool

# 打印日志的工具

class Log_tool():
    fd = None

    # 初始化log工具
    def __init__(self):
        # 把要写入数据的文本打开保存
        log_name = time_tool.get_log_name()
        self.fd = open(log_name, 'a+', encoding='utf-8')
    
    # enums.log_type : 打印的类型 enum.enums.log_type
    # msg : 要写入的字符串
    def log(self, msg, logType=enums.log_type.both, parent=None):
        # 添加log时间
        # 跳过弹窗的提示
        if logType != enums.log_type.popup:
            msg = time_tool.now_time() + msg + "\n"

        # 开始区分打印的方式
        if logType == enums.log_type.dos:
            print(msg)
        elif logType == enums.log_type.local:
            self.write_local(msg)
        elif logType == enums.log_type.both:
            print(msg)
            self.write_local(msg)
        elif logType == enums.log_type.popup and parent:
            self.popup(parent, msg)

    # 写到本地
    # ps : 这里有坑，如果不调用close，数据不会马上保存到磁盘，而是在内存中等待处理器有空的时候再写入
    # msg : 要写入的字符串
    def write_local(self, msg):
        self.fd.write(msg)
        # 下面这一段是为了马上看的到log数据,后面加一个定时器，定时写入log
        self.fd.close()
        log_name = time_tool.get_log_name()
        self.fd = open(log_name, 'a+', encoding='utf-8')


    # 弹窗提示
    # parent : 弹窗的父窗口
    # msg : 要写入的字符串
    def popup(self, parent, msg):
        QtWidgets.QMessageBox.critical(parent, "Critical", msg)

log_tool = Log_tool()