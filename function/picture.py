# 系统库
import os
from PIL import Image
from PySide2 import QtWidgets
from PySide2 import QtCore
# 项目库
from tools.log_tool import log_tool
from tools.config_tool import config_tool
from config.enums import enums

# 这个是用来处理图片的类
class Picture(QtWidgets.QWidget):

    # 初始化图片处理模块
    # parent : 父窗口
    def __init__(self, parent):
        super(Picture, self).__init__(parent)
        # 设置模态窗口
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setWindowModality(QtCore.Qt.WindowModal)

        # 界面设置
        cfg = config_tool.cfg_map["picture_windows"]
        self.setWindowTitle(cfg["windows_name"])
        self.resize(cfg["windows_width"], cfg["windows_height"])

        # 界面部件
        # 标签
        # 目标目录
        self.lable_putin = QtWidgets.QLabel(self)
        self.lable_putin.setText("目标目录")
        # 输出目录
        self.lable_putout = QtWidgets.QLabel(self)
        self.lable_putout.setText("输出目录")
        # 输出宽度
        self.lable_width = QtWidgets.QLabel(self)
        self.lable_width.setText("输出宽度")
        # 输出高度
        self.lable_height = QtWidgets.QLabel(self)
        self.lable_height.setText("输出高度")

        # 文本输入
        # 目标目录
        self.lineEdit_putin = QtWidgets.QLineEdit(self)
        self.lineEdit_putin.resize(150, 30)
        # 输出目录
        self.lineEdit_putout = QtWidgets.QLineEdit(self)
        self.lineEdit_putout.resize(150, 30)
        # 输出宽度
        self.lineEdit_width = QtWidgets.QLineEdit(self)
        self.lineEdit_width.resize(30, 30)
        # 输出高度
        self.lineEdit_height = QtWidgets.QLineEdit(self)
        self.lineEdit_height.resize(30, 30)

        # 按钮
        self.button_change = QtWidgets.QPushButton(self)
        self.button_change.setText("开始修改")

        # 布局管理器
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.lable_putin, 0, 0, 1, 1)
        self.layout.addWidget(self.lineEdit_putin, 0, 1, 1, 3)
        self.layout.addWidget(self.lable_putout, 1, 0, 1, 1)
        self.layout.addWidget(self.lineEdit_putout, 1, 1, 1, 3)
        self.layout.addWidget(self.lable_width, 2, 0, 1, 1)
        self.layout.addWidget(self.lineEdit_width, 2, 1, 1, 1)
        self.layout.addWidget(self.lable_height, 2, 2, 1, 1)
        self.layout.addWidget(self.lineEdit_height, 2, 3, 1, 1)
        self.layout.addWidget(self.button_change, 3, 0, 1, 1)
        self.setLayout(self.layout)

        # 设置连接信号
        self.button_change.clicked.connect(self.click_change)

    # 点击修改图片输出
    def click_change(self):
        putin = self.lineEdit_putin.text()
        putout = self.lineEdit_putout.text()
        width = self.lineEdit_width.text()
        heigth = self.lineEdit_height.text()

        # 检查目标目录的输入
        if os.path.exists(putin) == False:
            msg = "目标目录:" + putin + " 不存在"
            log_tool.log(msg, enums.log_type.popup, self)
            return
        # 检查输出目录的输入
        if os.path.exists(putout) == False:
            msg = "输出目录:" + putout + " 不存在"
            log_tool.log(msg, enums.log_type.popup, self)
            return
        # 检查输出宽度的输入
        if width.isdigit() == False:
            msg = "输出宽度:不正确"
            log_tool.log(msg, enums.log_type.popup, self)
            return
        # 检查输出高度的输入
        if heigth.isdigit() == False:
            msg = "输出高度:不正确"
            log_tool.log(msg, enums.log_type.popup, self)
            return

        # 获取目录下所有文件的文件名(只是单个目录，不递归每个子目录)
        file_name_list = os.listdir(putin)
        # log_tool.log(repr(file_name_list), enums.log_type.both)
        # log_tool.log(putout, enums.log_type.both)

        # 查找符合的文件
        name_list = []
        cfg = config_tool.cfg_map["picture_windows"]
        suffix_list = cfg["suffix_list"]
        # 遍历文件名
        for name in file_name_list:
            # 遍历后缀
            for suffix_name in suffix_list:
                if name.find(suffix_name) != -1 :
                    name_list.append(name)

        # 修改输出符合的文件
        for name in name_list:
            # 拼接文件地址
            im = Image.open(putin + "/" + name)
            out = im.resize((int(width), int(heigth)), Image.ANTIALIAS)
            out.save(putout + "/" + name)
