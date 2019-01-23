# 系统库文件
import os
# 自己的库文件
# 项目文件

# 文件处理的库
class File_tool():
    
    # 检查路径是否存在
    # m_path : 路径
    def check_path(self, m_path):
        if os.path.exists(m_path) == False:
            print("file_tool, check_path, %s not exists"%(m_path))
            return False

    # 获取目录下的文件名
    # m_path : 目录路径
    # suffix_arr : 查找的后缀名数组, 为空者全选
    def get_file_name_by_dir(self, m_path, suffix_arr):
        # # 这个只能遍历当前目录
        # # 获取目录下的文件名
        # file_list = os.listdir(m_path)
        # # print("目录下有文件:")
        # # print(file_name_list)

        # 这个可以遍历子目录
        file_list = []
        for root, dirs, files in os.walk(m_path, topdown=False):
            for name in files:
                # print(os.path.join(root, name))
                file_list.append(os.path.join(root, name))

        # 遍历文件名查找符合的文件
        ret_file_list = []
        for tmp_name in file_list:
            # 如果不传入筛选，则全选
            if len(suffix_arr) == 0:
                ret_file_list.append(tmp_name)
                continue
            # 遍历后缀数组
            for tmp_suffix in suffix_arr:
                if tmp_name.find(tmp_suffix) != -1:
                    ret_file_list.append(tmp_name)
                    break
            
        # print("符合条件的文件有:")
        # print(ret_file_list)
        return ret_file_list

    # 根据关键字查找对应的行
    # file_arr : 要查找的文件列表
    # suffix_arr : 查找的关键字数组
    def get_line_by_str(self, file_arr, suffix_arr):
        # 保存要输出的字符串数组
        str_arr = []
        # 遍历读取文件列表
        for tmp_file in file_arr:
            # 读取文件
            with open(tmp_file, 'r', encoding='utf-8', errors='ignore') as fin:
                while True:
                    msg = fin.readline()
                    # 读取完退出
                    if msg: 
                        # 遍历后缀名数组
                        for tmp_suffix in suffix_arr:
                            if msg.find(tmp_suffix) != -1:
                                str_arr.append(msg)
                                break
                    else :
                        break
        return str_arr

    # 删除文件
    # file_arr : 要删除的文件
    def remove_file(self, file_arr):
        # 先检查文件是否存在
        for tmp_file in file_arr:
            if self.check_path(tmp_file) == False:
                return False

        for tmp_file in file_arr:
            os.remove(tmp_file)
            
        return True

# 实例化出工具对象
file_tool = File_tool()