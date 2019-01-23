# 系统库
from PySide2 import QtWidgets
from PySide2 import QtCore
import json
# 项目库
from tools.log_tool import log_tool
from tools.config_tool import config_tool
from tools.file_tool import file_tool
from config.enums import enums

# 设置的类
class Setting(QtWidgets.QWidget):
    # 保存设置窗口，在堆栈里的索引id
    listWidget_arr = {}
    # 是否有修改过配置
    change_flag = False

    def __init__(self, parent):
        super(Setting, self).__init__(parent)
        # 设置模态窗口
        self.setWindowFlags(QtCore.Qt.Dialog)
        # self.setWindowModality(QtCore.Qt.WindowModal)

        # 界面设置
        self.cfg = config_tool.cfg_map["setting_windows"]
        cfg = self.cfg
        self.setWindowTitle(cfg["windows_name"])
        self.resize(cfg["windows_width"], cfg["windows_height"])

        # 界面部件
        # 包含全部模块配置的listwidget展示
        # 设置初始大小，增加条目，设置标题
        self.listWidget_config = QtWidgets.QListWidget(self)
        lw_cfg = self.listWidget_config
        lw_cfg.resize(cfg["listWidget_width"], cfg["listWidget_height"])
        # 新加的模块需要在这里添加
        for cfg_name in config_tool.cfg_map:
            tmp_cfg = config_tool.cfg_map[cfg_name]
            lw_cfg.addItem(tmp_cfg["windows_name"])
            # 添加对应窗口名的map
            self.listWidget_arr[tmp_cfg["windows_name"]] = {}
        lw_cfg.setWindowTitle('模块配置')

        # 模块的设置窗口
        self.stackedWidget_setting = QtWidgets.QStackedWidget(self)
        self.stackedWidget_setting.resize(cfg["stackedWidget_width"], cfg["stackedWidget_height"])
        for cfg_name in config_tool.cfg_map:
            tmp_cfg = config_tool.cfg_map[cfg_name]
            listWidget = self.listWidget_arr[tmp_cfg["windows_name"]]
            listWidget["index"] = self.stackedWidget_setting.addWidget(Set_window(tmp_cfg, self))
        self.stackedWidget_setting.setCurrentIndex(0)

        # 按钮
        self.button_sava = QtWidgets.QPushButton(self)
        self.button_sava.setText("保存配置")
        self.button_reset = QtWidgets.QPushButton(self)
        self.button_reset.setText("恢复初始")

        # 布局管理器
        self.layout = QtWidgets.QGridLayout(self)
        # 纵向
        # self.layout.addWidget(self.listWidget_config, 0, 0, 2, 2)   # 这里修改比例有可能造成stackedWidget_setting的不显示
        # self.layout.addWidget(self.stackedWidget_setting, 2, 0, 4, 4)
        # 横向
        self.layout.addWidget(self.listWidget_config, 0, 0, 4, 2)   # 这里修改比例有可能造成stackedWidget_setting的不显示
        self.layout.addWidget(self.stackedWidget_setting, 0, 2, 4, 6)
        self.layout.addWidget(self.button_sava, 4, 0, 1, 1)
        self.layout.addWidget(self.button_reset, 4, 1, 1, 1)

        self.setLayout(self.layout)

        # 单击触发绑定的槽函数
        lw_cfg.itemClicked.connect(self.listWidget_clicked)
        self.button_sava.clicked.connect(self.click_sava)
        self.button_reset.clicked.connect(self.click_reset)

    # 槽函数
    # 根据按下的对应选项，设置当前设置窗口
    def listWidget_clicked(self, item):
        item_name = item.text()
        print(item_name)
        for tmp_lw in self.listWidget_arr:
            if item_name == tmp_lw:
                self.stackedWidget_setting.setCurrentIndex(self.listWidget_arr[tmp_lw]["index"])
                break

    # 点击保存
    def click_sava(self):
        # 根据configTool获取用到的配置名
        file_name_arr = []
        for cfg_name in config_tool.cfg_map:
            cfg_name = "config/" + cfg_name + ".json"
            file_name_arr.append(cfg_name)
        
        # 检查文件是否都存在
        for file_name in file_name_arr:
            if file_tool.check_path(file_name) == False:
                log_tool.log("setting, click_sava, check_path %s not exists"%(file_name))
                return

        # 直接写入覆盖旧文件
        for file_name in file_name_arr:
            with open(file_name, 'w', encoding='utf-8') as f:
                # 解析配置名
                begin = file_name.rfind("/")
                end = file_name.rfind(".json")
                cfg_name = file_name[begin + 1: end]
                # 转化为json, 加 ensure_ascii=False, 否者会把中文转义
                tmp = json.dumps(config_tool.cfg_map[cfg_name], ensure_ascii = False)
                f.write(tmp)
        


    # 点击恢复初始
    def click_reset(self):
        pass


# 设置窗口
class Set_window(QtWidgets.QLabel):
    label_arr = []      # 对应字段的标签数组
    lineEdit_arr = []   # 对应数值的输入数组

    # 初始化
    # width : 宽度
    # height : 高度
    def __init__(self, cfg, parent):
        super(Set_window, self).__init__(parent)

        # 窗口设置
        self.cfg = cfg

        # 布局管理器
        # 遍历创建对应的设置
        self.layout = QtWidgets.QGridLayout(self)
        index = 0
        for tmp_set in cfg:
            Label_tmp = QtWidgets.QLabel(tmp_set)
            lineEdit_tmp = QtWidgets.QLineEdit(str(cfg[tmp_set]))
            self.layout.addWidget(Label_tmp, index, 0, 1, 1)
            self.layout.addWidget(lineEdit_tmp, index, 1, 1, 1)
            self.label_arr.append(Label_tmp)
            self.lineEdit_arr.append(lineEdit_tmp)
            index += 1

        self.setLayout(self.layout)
