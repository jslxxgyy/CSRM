import configparser
import json

def ini_to_new_json(ini_file, new_json_file):
    # 创建 ConfigParser 对象
    config = configparser.ConfigParser()
    # 读取 ini 文件，这里使用 GBK 编码，根据实际情况可以调整编码方式
    config.read(ini_file, encoding='GBK')

    # 创建一个空字典来存储所有的配置数据
    all_data = {}

    # 遍历 ini 文件中的所有段落（sections）
    for section in config.sections():
        # 将每个段落下的所有键值对存储到字典中
        all_data[section] = {key: config[section][key] for key in config[section]}

    # 新建一个 JSON 文件，并将配置数据写入
    with open(new_json_file, 'w', encoding='utf-8') as file:
        json.dump(all_data, file, ensure_ascii=False, indent=4)

    print(f"JSON 文件 {new_json_file} 已创建并存储了配置数据。")

# 指定 ini 文件和新 JSON 文件的路径
ini_file = 'radio.ini'
new_json_file = 'RadioNetwork.json'

# 执行函数，创建新的 JSON 文件
ini_to_new_json(ini_file, new_json_file)