# 系统库
import os
from PIL import Image
from PySide2 import QtWidgets
from PySide2 import QtCore
# 项目库
from tools.log_tool import log_tool
from tools.config_tool import config_tool
from config.enums import enums

# 处理excel的类
class Check_excel(QtWidgets.QWidget):

    # parent : 父窗口
    def __init__(self, parent):
        super(Check_excel, self).__init__(parent)
        # 设置模态窗口
        self.setWindowFlags(QtCore.Qt.Dialog)
        # self.setWindowModality(QtCore.Qt.WindowModal)

        # 界面设置
        self.cfg = config_tool.cfg_map["check_excel_windows"]
        cfg = self.cfg
        self.setWindowTitle(cfg["windows_name"])
        self.resize(cfg["windows_width"], cfg["windows_height"])

        # 界面部件
        # 标签
        # 目标目录
        self.lable_putin = QtWidgets.QLabel(self)
        self.lable_putin.setText("目标目录")

        # 文本输入
        # 目标目录
        self.lineEdit_putin = QtWidgets.QLineEdit(self)
        self.lineEdit_putin.resize(150, 30)
        # 输出文本
        self.lineEdit_out_text = QtWidgets.QTextEdit(self)
        self.lineEdit_out_text.resize(150, 150)

        # 按钮
        # 检查文件的空行
        self.button_check_null = QtWidgets.QPushButton(self)
        self.button_check_null.setText("检查空行")

        # 布局管理器
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.lable_putin, 0, 0, 1, 1)
        self.layout.addWidget(self.lineEdit_putin, 0, 1, 1, 3)
        self.layout.addWidget(self.button_check_null, 1, 0, 1, 1)
        self.layout.addWidget(self.lineEdit_out_text, 2, 0, 4, 4)
        self.setLayout(self.layout)

        # 设置连接信号
        self.button_check_null.clicked.connect(self.click_check_null)

    # xiu'g
    def click_check_null(self):
        pass