# 系统库
import json
# 项目库
from config.enums import enums
from tools.log_tool import log_tool

# 这个是加载处理各配置文件的工具


class Config_tool():
    cfg_map = {}

    # 初始化加载各个配置文件
    def __init__(self):
        log_tool.log("load all config", enums.log_type.both)
        self.load_cfg("main_windows", "config/main_windows.json")                   # 主窗口配置
        # 功能模块的配置
        self.load_cfg("picture_windows", "config/picture_windows.json")             # 图片处理配置
        self.load_cfg("quickkey_windows", "config/quickkey_windows.json")           # 快捷键配置
        self.load_cfg("check_excel_windows", "config/check_excel_windows.json")     # excel处理配置
        self.load_cfg("translate_windows", "config/translate_windows.json")         # 翻译配置
        # 菜单栏的配置
        self.load_cfg("setting_windows", "config/setting_windows.json")         # 设置配置


    # 加载对应配置
    # cfg_obj : 配置名
    # cfg_file : 文件地址
    def load_cfg(self, cfg_name, cfg_file):
        with open(cfg_file, 'r', encoding='utf-8') as f:
            self.cfg_map[cfg_name] = json.load(f)

# 实例化
config_tool = Config_tool()