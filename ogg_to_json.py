import json
import os
import argparse
from mutagen.oggvorbis import OggVorbis

def extract_metadata(file_path):
    """
    提取音频文件的元数据（曲名、专辑名、艺术家）。
    参数：
    file_path (str):要处理的音频文件
    """
    metadata = {}
    try:
        audio = OggVorbis(file_path)
        metadata['Title'] = audio['title'][0]  #曲名
        metadata['Album'] = audio['album'][0]  #专辑名
        metadata['Artist'] = audio['artist'][0]  #艺术家
    except Exception as e:
        print(f"提取 {file_path} 的元数据时出错: {str(e)}")
    metadata['Type'] = None  #添加Type键，值为None，不加这个读不了元数据
    return metadata

def process_music_files(dir):
    """
    处理指定目录中的所有音乐文件，提取元数据并存储为json文件。
    参数:
    dir (str):要处理的目录和输出目录
    """
    for filename in os.listdir(dir):
        if filename.endswith(".ogg"):
            ogg_file_path = os.path.join(dir, filename) #拼接音乐文件的完整路径
            metadata = extract_metadata(ogg_file_path)  #提取音乐文件的元数据
            json_filename = os.path.splitext(ogg_file_path)[0] + ".json"  #拼接输出的json文件名
            with open(json_filename, 'w', encoding='utf-8') as f:
                #写入json文件
                json.dump(metadata, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    args = parser.parse_args()
    
    process_music_files(args.directory)
