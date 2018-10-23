
# 主界面入口

#coding:utf-8
import sys
from PySide2 import QtWidgets
from mainWidget import MainWidget


app = QtWidgets.QApplication(sys.argv)
ex = MainWidget()

# 正常退出的0也是回报异常，只能先把它放到这里处理
try:
    ret = app.exec_()
    sys.exit(ret)
except :
    pass
    #print("error:" + str(ret))
