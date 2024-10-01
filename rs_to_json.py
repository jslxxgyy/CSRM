import configparser
import json
import os
import argparse

def load_rs_file(path,encoding='gbk'):
    """
    加载电台配置文件。
    """
    config = configparser.ConfigParser()
    with open(path,'r',encoding=encoding) as file:
        config.read_file(file)
    return config

def write_json(data, filename):
    """
    将电台配置数据写入 JSON 文件。
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def convert_rs_to_json(input_path, output_path):
    config = load_rs_file(input_path,encoding='gbk')
    
    # 确保输出目录存在，如果不存在则创建
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # 处理 [RadioNetwork] 节
    radio_network = {
        "name": config['RadioNetwork']['name'],
        "description": config['RadioNetwork']['description'],
        "descriptionId": config['RadioNetwork']['descriptionId'],
        "icon": config['RadioNetwork']['icon'],
        "allowAds": config['RadioNetwork'].getboolean('allowAds')
    }
    write_json(radio_network, os.path.join(output_path, 'RadioNetwork.json'))
    
    # 处理 [RadioChannel] 节
    radio_channel = {
        "name": config['RadioChannel']['name'],
        "description": config['RadioChannel']['description'],
        "icon": config['RadioChannel']['icon']
    }
    write_json(radio_channel, os.path.join(output_path, 'RadioChannel.json'))
    
    # 处理 [Program] 节
    program = {
        "name": config['Program']['name'],
        "description": config['Program']['description'],
        "icon":config['Program']['icon'],
        "startTime": config['Program']['startTime'],
        "endTime": config['Program']['endTime'],
        "loopProgram": config['Program'].getboolean('loopProgram'),
        "pairIntroOutro": config['Program'].getboolean('pairIntroOutro')
    }
    write_json(program, os.path.join(output_path, 'Program.json'))
    
    # 处理 [Segment] 节
    segment = {
        "type": "Playlist",
        "tags": [],
        "clipsCap": config['Segment'].getint('clipsCap')
    }
    write_json(segment, os.path.join(output_path, 'Segment.json'))

if __name__ == "__main__":
    # 获取当前脚本的运行目录
    current_directory = os.path.dirname(os.path.abspath(__file__))
    default_input_path = os.path.join(current_directory, 'temp','radio.rs')
    default_output_path = os.path.join(current_directory, 'temp')

    parser = argparse.ArgumentParser(description='Convert RS to JSON')
    # 添加命令行参数，可选，有默认值
    parser.add_argument('input_path', nargs='?', default=default_input_path,
                        help='Input RS file path')
    parser.add_argument('output_path', nargs='?', default=default_output_path,
                        help='Output JSON files directory')
    
    # 解析命令行参数
    args = parser.parse_args()
    # 调用转换函数
    convert_rs_to_json(args.input_path, args.output_path)