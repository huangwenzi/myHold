
# 快捷键的类

import sys
from pynput import keyboard
import _thread
from PySide2 import QtWidgets
from PySide2 import QtCore
from function.basic.dataMgr import dataMgr
from function.basic.enum import keysRet
from function.quickKey.keyEvent import keysEvent
from function.basic.logTool import logTool
from function.basic.enum import log_type

class QuickKey(QtWidgets.QWidget):

    def __init__(self, parent):
        super(QuickKey, self).__init__(parent)
        # 设置模态窗口
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setWindowModality(QtCore.Qt.WindowModal)

        # 界面设置
        self.setWindowTitle("快捷键")
        self.resize(300, 250)

        # 界面部件
        # 显示快捷键坐标的label
        self.label_key_list = []
        for index in range(1, 10):
            tmp = QtWidgets.QLabel(self)
            tmp.resize(150, 50)
            tmp.move((index-1) % 2 * 150, (index-1) // 2 * 50)
            tmp.setText(str(index))
            tmp.show()
            self.label_key_list.append(tmp)

        # 按键的监听需要分一个线程去执行
        # 创建两个线程
        try:
            _thread.start_new_thread(self.keyEvent)
        except:
            logTool.log("Error: 无法启动线程")
            logTool.log("Error: 无法启动线程", log_type.popup)

    # 更新数据
    def update(self):
        index = 1
        # 循环更新全部保存位
        for label_tmp in self.label_key_list:
            # 判断对应的字段是否有保存快捷键位置
            if str(index) not in dataMgr.position.keys():
                index += 1
                continue

            position = str(index) + ".x:" + str(dataMgr.position[str(index)][0]) + " y:" + str(dataMgr.position[str(index)][1])
            label_tmp.setText(position)
            index += 1

    # 监听按键事件
    def keyEvent(self):
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
            

# 键盘按下事件
def on_press(key):
    ret = keysEvent.keyDown(dataMgr, key)
    if ret == keysRet.isExit:
        sys.exit()

# 键盘放开事件
def on_release(key):
    keysEvent.keyUp(dataMgr, key)
