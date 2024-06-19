import configparser
import json
import os

# 读取INI配置文件
config = configparser.ConfigParser()
config.read('./temp/radio.ini')

# 路径设置
output_dir = './temp'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 处理[RadioNetwork]节
radio_network = {
    "name": "电台网络名",
    "nameId": "电台网络名",
    "description": "这是一个示例电台网络",
    "descriptionId": "这是一个示例电台网络",
    "icon": "coui://extendedradio/CustomRadios/电台网络/电台网络图标.svg",
    "allowAds": config['RadioNetwork'].getboolean('allowAds')
}
with open(os.path.join(output_dir, 'RadioNetwork.json'), 'w', encoding='utf-8') as f:
    json.dump(radio_network, f, ensure_ascii=False, indent=4)

# 处理[RadioChannel]节
radio_channel = {
    "name": "频道1",
    "nameId": "频道1",
    "description": "这是电台网络的频道1",
    "icon": "coui://extendedradio/CustomRadios/电台网络/频道1/频道图标.svg"
}
with open(os.path.join(output_dir, 'RadioChannel.json'), 'w', encoding='utf-8') as f:
    json.dump(radio_channel, f, ensure_ascii=False, indent=4)

# 处理[Program]节
program = {
    "name": "节目1",
    "description": "这是电台网络的频道1的其中一个节目",
    "startTime": "00:00",
    "endTime": "00:00",
    "loopProgram": config['Program'].getboolean('loopProgram'),
    "pairIntroOutro": config['Program'].getboolean('pairIntroOutro')
}
with open(os.path.join(output_dir, 'Program.json'), 'w', encoding='utf-8') as f:
    json.dump(program, f, ensure_ascii=False, indent=4)

# 处理[Segment]节
segment = {
    "type": "Playlist",
    "tags": [
        "type:Music",
        "radio channel:音乐"
    ],
    "clipsCap": config['Segment'].getint('clipsCap')
}
with open(os.path.join(output_dir, 'Segment.json'), 'w', encoding='utf-8') as f:
    json.dump(segment, f, ensure_ascii=False, indent=4)

print("所有JSON文件已生成并保存至'./temp'目录下。")