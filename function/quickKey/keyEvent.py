
# 这里处理键盘按下的事件

import os
from pynput.mouse import Button, Controller
mouse = Controller()
import pyautogui
import time
from function.basic.enum import keysRet
from function.basic.logTool import logTool
from function.basic.enum import log_type

# 一些全局定义
# 辅助键，标识需要特殊处理的事件
AUXILIARY_KEY = "0"

class KeysEvent():

    def __init__(self):
        pass


    # 按下键
    # data : 用户数据
    # key : 传入的key对象
    def keyDown(self, data, key):
        # 如果是功能键，进入功能键函数，退出普通按键效果
        ret = self.isFun(data, key)
        if ret == keysRet.isFun:
            return ret
        elif ret == keysRet.isExit:
            return ret

        # 提取按下的键
        # 鉴于pynput只能在key.char中保存一般按键，不能保存特殊键
        if hasattr(key, "char"):
            # 把按下的键值存入数据中
            if key.char not in data.keyDown:
                data.keyDown.append(key.char)
                # print(data.keyDown)
        # 特殊键先不处理
        else :
            return ret

        # 如果快捷键功能没有开启，则退出
        if not data.openFlag:
            return ret

        # 执行快捷键操作
        char = key.char
        # 鼠标移动到保存的位置
        if char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
            # 这个位置是否有保存过位置
            if char in data.position.keys():
                position = data.position[char]
                mouse.position = position
                mouse.click(Button.left)
                # print("move,X:" + str(position[0]) + "Y:" + str(position[1]) )
        return ret


    # 放开键
    # data : 用户数据
    # key : 传入的key对象
    def keyUp(self, data, key):
        if hasattr(key, "char"):
            # 把放开的键从按下的键表中删除
            if key.char in data.keyDown:
                data.keyDown.remove(key.char)
                # print(data.keyDown)


    # 检查是不是功能键
    # data : 用户数据
    # key : 传入的key对象
    # return : 返回 0:不是功能处理  1:是功能处理  2:退出
    def isFun(self, data, key):
        # 如果辅助键没有同时按下，则不是功能处理
        if AUXILIARY_KEY not in data.keyDown:
            return keysRet.noFun

        # 下面是各功能键的处理，不包含特殊键
        if hasattr(key, "char"):
            char = key.char
            # 开启快捷键
            if char == ".":
                # 取反开启的标志位
                data.openFlag = not data.openFlag
                if data.openFlag:
                    logTool.log("quickKey open", log_type.dos)
                else:
                    logTool.log("quickKey close", log_type.dos)
            # 保存快捷点
            elif char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
                data.position[char] = mouse.position
                logTool.log(data.position, log_type.dos)
            # 截图
            elif char == "+":
                # 检查目标文件夹是否存在
                flag = os.path.exists("screenshot")
                if flag == False:
                    os.makedirs("screenshot")

                # 用当前时间做名字保存
                name = time.strftime("screenshot\\%Y-%m-%d_%H-%M-%S.png", time.localtime())
                pyautogui.screenshot(name)
                logTool.log("sava screenshot in " + name)
            # 退出 因为按键的事件是另开线程处理的，这里的退出只是退出处理按键事件的线程，不能退出整个界面
            elif char == "-":
                logTool.log("exit", log_type.dos)
                return keysRet.isExit
            # 不存在的功能键就返回false
            else :
                return keysRet.noFun

        return keysRet.isFun


# 实例化这个过程处理类
keysEvent = KeysEvent()