import json
import configparser
import argparse
import os

def update_game_data_path(config_filename="CSUL.config", ini_filename="load.ini"):
    """
    尝试从CSUL的配置文件中读取游戏文件目录或者游戏数据目录。
    参数:
    config_filename (str): CSUL的.config文件路径。
    ini_filename (str): CSRM的.ini配置文件路径。
    """

    #读CSUL的配置文件
    with open(config_filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    #读CSRM的配置文件
    config = configparser.ConfigParser()
    config.read(ini_filename)

    #0.2.2版本移除了BeplnEx支持
    path_to_write = data['GameData']['Value'].encode('utf-8').decode('unicode_escape').strip('"')
    
    # 更新配置文件
    config.set('path', 'GameDataPath', path_to_write)
    with open(ini_filename, 'w', encoding='GBK') as configfile:
        config.write(configfile)

if __name__=='__main__':
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="Update GameDataPath in an INI file based on ModForm.")
    parser.add_argument('config_filename', help="The filename of the JSON configuration file.")
    parser.add_argument('ini_filename', help="The filename of the INI file to update.")

    args = parser.parse_args()
    
    update_game_data_path(args.config_filename, args.ini_filename)

