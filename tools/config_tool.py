# 系统库
import json
import os
# 项目库
from configs.enums import enums
from tools.log_tool import log_tool

# 这个是加载处理各配置文件的工具


class Config_tool():
    cfg_map = {}

    # 初始化加载各个配置文件
    def __init__(self):
        self.file_arr = ["configs/main_windows.json",         # 主窗口配置
                         "configs/picture_windows.json",      # 图片处理配置
                         "configs/quickkey_windows.json",     # 快捷键配置
                         "configs/check_excel_windows.json",  # excel处理配置
                         "configs/translate_windows.json",    # 翻译配置
                         "configs/setting_windows.json"]      # 设置配置

        log_tool.log("load all config")
        for file_name in self.file_arr:
            # 解析配置名
            begin = file_name.rfind("/")
            end = file_name.rfind(".json")
            cfg_name = file_name[begin + 1: end]
            log_tool.log("load " + cfg_name)
            if self.load_cfg(cfg_name, file_name) == False:
                log_tool.log("load " + cfg_name + "error")

    # 加载对应配置
    # cfg_obj : 配置名
    # cfg_file : 文件地址

    def load_cfg(self, cfg_name, cfg_file):
        if os.path.exists(cfg_file) == False:
            print("config_tool, load_cfg, cfg_name:%s, cfg_file:%s not exists"%(cfg_name, cfg_file))
            return False

        with open(cfg_file, 'r', encoding='utf-8') as f:
            self.cfg_map[cfg_name] = json.load(f)

        return True


# 实例化
config_tool = Config_tool()
