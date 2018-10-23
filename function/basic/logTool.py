
# 打印日志的工具
import time
from function.basic.enum import log_type
from PySide2 import QtWidgets

class LogTool():

    def __init__(self):
        pass
    
    # log_type : 打印的类型 enum.log_type
    # msg : 要打印的数据
    def log(self, msg, logType=log_type.both, parent=None):
        # 开始区分打印的方式
        if logType == log_type.dos:
            print(msg)
        elif logType == log_type.local:
            self.write_local(msg)
        elif logType == log_type.both:
            print(msg)
            self.write_local(msg)
        elif logType == log_type.popup and parent:
            self.popup(parent, msg)

    #　写到本地
    def write_local(self, msg):
        # 拼接保存的文本名
        file_date = time.strftime("%Y-%m-%d", time.localtime())
        name = "./log/" + file_date + ".txt"
        # 在需要保存的信息前面加上时间
        date = time.strftime("%Y-%m-%d %H:%M:%S : ", time.localtime())
        msg = date + msg
    
        # 写入文本
        with open(name, 'a+', encoding='utf-8') as f:
            f.write(msg)

    # 弹窗提示
    def popup(self, parent, msg):
        QtWidgets.QMessageBox.critical(parent, "Critical", msg)

logTool = LogTool()