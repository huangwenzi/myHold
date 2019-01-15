# 系统库
import sys
import os
from pynput import keyboard
import _thread
from PySide2 import QtWidgets
from PySide2 import QtCore
from pynput.mouse import Button, Controller
mouse = Controller()
import pyautogui
# 项目库
from config.enums import enums
from tools.log_tool import log_tool
from tools.config_tool import config_tool
from tools.time_tool import time_tool


# 普通快捷键用到的几个键位
quick_keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# 数据管理类
class Data_mgr():
    # 是否开启快捷键功能
    openFlag = False
    # 记录按下的键，只是按下，没有弹起
    keyDown = []
    # 保存记录快捷键对应坐标的字典{"number" : [x,y],...}
    position = {}
# 实例化一个对象给下面的使用
data_mgr = Data_mgr()

# 快捷键的类
class Quick_key(QtWidgets.QWidget):
    # 保存使用到的数据
    data_mgr = data_mgr

    # 初始化
    def __init__(self, parent):
        super(Quick_key, self).__init__(parent)
        # 设置模态窗口
        self.setWindowFlags(QtCore.Qt.Dialog)
        # self.setWindowModality(QtCore.Qt.WindowModal)

        # 界面设置
        self.cfg = config_tool.cfg_map["quickkey_windows"]
        cfg = self.cfg
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
            self.layout.addWidget(
                self.label_key_list[index], index/cfg["row_num"] + 1, index % cfg["row_num"], 1, 1)
        self.setLayout(self.layout)

        # 按键的监听需要分一个线程去执行
        try:
            _thread.start_new_thread(self.key_event)
        except:
            log_tool.log("quickKey, __init__, Error: 无法启动线程, key_event")


    # 更新界面数据
    def update(self):
        # 更新开启标识
        self.label_open_flag.setText(str(self.data_mgr.openFlag))

        # 更新快捷键的信息
        position = self.data_mgr.position
        for index in range(0, 9):
            index_str = str(index)
            # 已经设置有快捷键的
            if index_str in position:
                label_tmp = self.label_key_list[index-1]
                tmp_str = index_str + ".x:" + \
                    str(position[index_str][0]) + " y:" + \
                    str(position[index_str][1])
                label_tmp.setText(tmp_str)


    # 监听按键事件
    def key_event(self):
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()


# 键盘按下事件
# key : 传递的key值
def on_press(key):
    key_down(key)


# 键盘放开事件
# key : 传递的key值
def on_release(key):
    key_up(key)


# 键盘按下事件
# data_mgr : 数据管理器对象
# key : 按下的key值
def key_down(key):
    # 保存按下的键
    # 鉴于pynput只能在key.char中保存一般按键，不能保存特殊键
    if hasattr(key, "char"):
        # 把按下的键值存入数据中
        if key.char not in data_mgr.keyDown:
            data_mgr.keyDown.append(key.char)
            # print(data_mgr.keyDown)

    # 如果是功能键，进入功能键函数，退出普通按键效果
    ret = get_key_type(key)
    if ret == enums.keys_ret.is_ordinary:
        is_ordinary(key)
    elif ret == enums.keys_ret.is_fun:
        is_fun(key)
    # 暂时不提供，只能退出单个类，不能退出全部程序
    # elif ret == enums.keys_ret.is_exit:
    #     is_exit(key)

    return ret

# 放开键
# data : 用户数据
# key : 传入的key对象
def key_up(key):
    if hasattr(key, "char"):
        # 把放开的键从按下的键表中删除
        if key.char in data_mgr.keyDown:
            data_mgr.keyDown.remove(key.char)
            # print(data.keyDown)

# 判断按下的是什么键
# data_mgr : 数据管理器对象
# key : 按下的key值
def get_key_type(key):
    #　这里的配置必须重新拿一下
    cfg = config_tool.cfg_map["quickkey_windows"]

    # 如果辅助键没有同时按下，则不是功能处理, 只是一般按键
    if cfg["auxiliary_key"] not in data_mgr.keyDown:
        return enums.keys_ret.is_ordinary

    # 功能键的集合
    all_fun_keys = quick_keys + [cfg["auxiliary_key"], cfg["open_flag_key"], cfg["screenshot_key"]]
    # 判断是不是功能键
    if hasattr(key, "char"):
        char = key.char
        # 退出键
        if char == cfg["exit_key"]:
            return enums.keys_ret.is_exit
        elif char in all_fun_keys:
            return enums.keys_ret.is_fun
            
    return enums.keys_ret.is_ordinary


# 普通快捷键的处理
# data_mgr : 数据管理器对象
# key : 按下的key值
def is_ordinary(key):
    # 如果快捷键功能没有开启，则退出
    if not data_mgr.openFlag:
        return

    # 执行快捷键操作
    if ~hasattr(key, "char"):
        return
    char = key.char
    # 鼠标移动到保存的位置
    if char in quick_keys:
        # 这个位置是否有保存过位置
        if char in data_mgr.position.keys():
            position = data_mgr.position[char]
            mouse.position = position
            mouse.click(Button.left)
            # print("move,X:" + str(position[0]) + "Y:" + str(position[1]) )
    return


# 判断是否是扩展功能键, 需要两个键同时按下的
# data_mgr : 数据管理器对象
# key : 按下的key值
def is_fun(key):
    #　这里的配置必须重新拿一下
    cfg = config_tool.cfg_map["quickkey_windows"]
    char = key.char
    # 开启快捷键
    if char == cfg["open_flag_key"]:
        # 取反开启的标志位
        data_mgr.openFlag = not data_mgr.openFlag
        if data_mgr.openFlag:
            log_tool.log("quickKey open", enums.log_type.both)
        else:
            log_tool.log("quickKey close", enums.log_type.both)
    # 保存快捷键对应的鼠标位置
    elif char in quick_keys :
        data_mgr.position[char] = mouse.position
        log_tool.log(str(data_mgr.position), enums.log_type.dos)
    # 截图
    elif char == cfg["screenshot_key"]:
        # 检查目标文件夹是否存在
        flag = os.path.exists(cfg["screenshot_path"])
        if flag == False:
            os.makedirs(cfg["screenshot_path"])

        # 用当前时间做名字保存
        name = cfg["screenshot_path"] + \
            "/" + time_tool.get_photo_name()
        pyautogui.screenshot(name)
        log_tool.log("sava screenshot in " + name)
    # 退出 因为按键的事件是另开线程处理的，这里的退出只是退出处理按键事件的线程，不能退出整个界面
    elif char == cfg["exit_key"]:
        # log_tool.log("exit", enums.log_type.both)
        # sys.exit()  
        return enums.keys_ret.is_exit

    return enums.keys_ret.is_fun


# 判断是否是扩展功能键, 需要两个键同时按下的
# data_mgr : 数据管理器对象
# key : 按下的key值
def is_exit(key):
    log_tool.log("exit", enums.log_type.both)
    sys.exit()  