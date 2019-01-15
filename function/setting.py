# 系统库
from PySide2 import QtWidgets
from PySide2 import QtCore
# 项目库
from tools.log_tool import log_tool
from tools.config_tool import config_tool
from config.enums import enums

# 设置的类
class Setting(QtWidgets.QWidget):
    pass

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
        lw_cfg.resize(500, 400)
        # 新加的模块需要在这里添加
        item_list =["快捷键", "图片", "excel", "翻译"]
        for tmp_item in item_list:
            lw_cfg.addItem(tmp_item)
        lw_cfg.setWindowTitle('模块配置')
        # 模块的设置窗口
        self.stackedWidget_setting = QtWidgets.QStackedWidget(self)
        



