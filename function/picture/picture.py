
# 这个是用来处理图片的类

import os
from PIL import Image
from PySide2 import QtWidgets
from PySide2 import QtCore
from function.basic.logTool import logTool
from function.basic.enum import log_type

class Picture(QtWidgets.QWidget):

    def __init__(self, parent):
        super(Picture, self).__init__(parent)
        # 设置模态窗口
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setWindowModality(QtCore.Qt.WindowModal)

        # 界面设置
        self.setWindowTitle("图片处理")
        self.resize(300, 250)

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
            logTool.log(msg, log_type.popup, self)
            return
        # 检查输出目录的输入
        if os.path.exists(putout) == False:
            msg = "输出目录:" + putout + " 不存在"
            logTool.log(msg, log_type.popup, self)
            return
        # 检查输出宽度的输入
        if width.isdigit() == False:
            msg = "输出宽度:不正确"
            logTool.log(msg, log_type.popup, self)
            return
        # 检查输出高度的输入
        if heigth.isdigit() == False:
            msg = "输出高度:不正确"
            logTool.log(msg, log_type.popup, self)
            return

        # 获取目录下的图片格式(jpg, png)的文件名
        file_name_list = os.listdir(putin)
        logTool.log(repr(file_name_list), log_type.both)
        logTool.log(putout, log_type.both)

        # 查找符合的文件
        name_list = []
        for name in file_name_list:
            if(name.find(".jpg") or name.find(".png")):
                name_list.append(name)
        # 修改输出符合的文件
        for name in name_list:
            # 拼接文件地址
            im = Image.open(putin + "/" + name)
            #(x,y) = im.size()
            out = im.resize((int(width),int(heigth)),Image.ANTIALIAS)
            out.save(putout + "/" + name)

