# 系统库
import sys
from pynput import keyboard
import _thread
from PySide2 import QtWidgets
from PySide2 import QtCore
# 项目库
from function.basic.dataMgr import dataMgr
from config.enums import enums
from function.quickKey.keyEvent import keysEvent
from tools.log_tool import log_tool
from tools.config_tool import config_tool

# 数据管理类
class Data_mgr():
    # 是否开启快捷键功能
    openFlag = True
    # 记录按下的键，只是按下，没有弹起
    keyDown = []
    # 保存记录快捷键对应坐标的字典{"number" : [x,y],...}
    position = {}

# 快捷键的类
class QuickKey(QtWidgets.QWidget):
    # 保存使用到的数据
    data_mgr = Data_mgr()

    # 初始化
    def __init__(self, parent):
        super(QuickKey, self).__init__(parent)
        # 设置模态窗口
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setWindowModality(QtCore.Qt.WindowModal)

        # 界面设置
        cfg = config_tool.cfg_map["quickkey_windows"]
        self.setWindowTitle(cfg["windows_name"])
        self.resize(cfg["windows_width"], cfg["windows_height"])

        # 界面部件
        # 显示当前快捷键是否有开启
        self.label_open_flag = QtWidgets.QLabel(self)
        self.label_open_flag.setText("True")

        # 显示快捷键坐标的label
        self.label_key_list = []
        for index in range(0, 9):
            tmp = QtWidgets.QLabel(self)
            tmp.resize(150, 50)
            tmp.setText(str(index + 1))
            self.label_key_list.append(tmp)

        # 布局管理器
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.label_open_flag, 0, 0, 1, 1)
        for index in range(0, 9):
            self.layout.addWidget(self.label_key_list[index], index/cfg["row_num"] + 1, index%cfg["row_num"], 1, 1)
        self.setLayout(self.layout)

        # 按键的监听需要分一个线程去执行
        # 创建两个线程
        try:
            _thread.start_new_thread(self.keyEvent)
        except:
            log_tool.log("Error: 无法启动线程")
            log_tool.log("Error: 无法启动线程", enums.log_type.popup)

    # 更新界面数据
    def update(self):
        index = 1
        # 循环更新全部保存位
        for label_tmp in self.label_key_list:
            # 判断对应的字段是否有保存快捷键位置
            if str(index) not in dataMgr.position.keys():
                index += 1
                continue

            position = str(index) + ".x:" + str(dataMgr.position[str(
                index)][0]) + " y:" + str(dataMgr.position[str(index)][1])
            label_tmp.setText(position)
            index += 1

    # 监听按键事件
    def keyEvent(self):
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()


# 键盘按下事件
def on_press(key):
    ret = keysEvent.keyDown(dataMgr, key)
    if ret == enums.keysRet.isExit:
        sys.exit()

# 键盘放开事件
def on_release(key):
    keysEvent.keyUp(dataMgr, key)
