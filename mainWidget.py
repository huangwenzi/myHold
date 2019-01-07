# 系统库
import sys
from PySide2 import QtWidgets
# 项目库
from function.quickKey.quickKey import QuickKey
from function.picture import Picture
from tools.log_tool import log_tool
from tools.config_tool import config_tool

# MainWidget继承于QtGui.QWidget类
class MainWidget(QtWidgets.QWidget): 

    # 需要调用两个构造方法
    def __init__(self):
        log_tool.log("开始初始软件")
        # 为被继承的父类即QtGui.QWidget类调用一次
        super(MainWidget, self).__init__()

        # 主界面设置
        windows_cfg = config_tool.cfg_map["main_windows"]
        self.setWindowTitle(windows_cfg["windows_name"])
        self.resize(windows_cfg["windows_height"], windows_cfg["windows_width"])

        # 初始化各个功能类
        # 快捷键
        self.quickKey = QuickKey(self)
        # 图片处理
        self.picture = Picture(self)

        # 初始化界面部件
        # 按钮类
        self.button_quickKey = QtWidgets.QPushButton(self)
        self.button_quickKey.setText(windows_cfg["button_quick_key_name"])
        self.button_picture = QtWidgets.QPushButton(self)
        self.button_picture.setText(windows_cfg["button_picture_name"])

        # 布局管理器
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.button_quickKey, 0, 0, 1, 1)
        self.layout.addWidget(self.button_picture, 1, 0, 1, 1)
        self.setLayout(self.layout)

        # 设置连接信号
        self.button_quickKey.clicked.connect(self.click_quickKey)
        self.button_picture.clicked.connect(self.click_picture)

        self.show()
        log_tool.log("初始化软件完毕")

    # 按钮的点击信号处理
    # 快捷键的点击
    def click_quickKey(self):
        self.quickKey.update()
        self.quickKey.show()

    # 图片处理的点击
    def click_picture(self):
        self.picture.show()


        
        