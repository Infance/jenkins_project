import yaml
import traceback
import os


def analyze_data():
    s = traceback.extract_stack()
    # 装饰器所在的文件的绝对路径
    file_path = s[-2][0]
    # 装饰器所在行号
    line_number = s[-2][1]

    with open(file_path, "r") as f:
        # 从行号往后读取文件的每一行，找到第一个 "def test_"
        for line in f.readlines()[line_number:]:
            if "def test_" in line:
                break

    # 获取该装饰器所在文件的文件名，去掉test_，并增加_data后缀（数据文件名）
    file_path = os.path.split(file_path)[1]
    file_path = os.path.splitext(file_path)[0]
    file_name = file_path[5:] + "_data"

    # 获取该装饰器修饰的函数名（应该调用的数据文件字典名）
    start = line.index("def ")
    end = line.index("(")
    func_name = line[start + 4:end]

    # 解析数据
    with open("./data/" + file_name + ".yaml", "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)[func_name]
        data_list = list()
        data_list.extend(data.values())
        return data_list
