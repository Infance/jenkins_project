import yaml


# 解析yaml数据文件
def analyse_data(file_path, case_key):
    # 'rb'读取二进制文件
    with open(file_path, 'rb') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)[case_key]
        #  取到字典的所有值
        return data.values()





