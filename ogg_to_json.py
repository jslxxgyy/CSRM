import json
import os
import argparse
from mutagen.oggvorbis import OggVorbis

def extract_metadata(file_path):
    """
    提取音频文件的元数据（曲名、专辑名、艺术家）。
    """
    metadata = {}
    try:
        # 使用 mutagen 库读取 Ogg Vorbis 文件的元数据
        audio = OggVorbis(file_path)
        metadata['Title'] = audio['title'][0]  # 曲名
        metadata['Album'] = audio['album'][0]  # 专辑名
        metadata['Artist'] = audio['artist'][0]  # 艺术家
    except Exception as e:
        print(f"提取 {file_path} 的元数据时出错: {str(e)}")
    return metadata

def process_music_files(dir):
    """
    处理指定目录中的所有音乐文件，提取元数据并存储为 JSON 文件。
    """
    for filename in os.listdir(dir):
        if filename.endswith(".ogg"):
            file_path = os.path.join(dir, filename)
            metadata = extract_metadata(file_path)  #提取音乐文件的元数据
            json_filename = os.path.splitext(file_path)[0] + ".json"  #拼接输出的 JSON 文件名
            with open(json_filename, 'w', encoding='utf-8') as f:
                #将元数据写入 JSON 文件
                json.dump(metadata, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='从指定目录中的音乐文件提取元数据并保存为 JSON 文件。')
    parser.add_argument('directory', help='包含 .ogg 音乐文件的目录路径')
    args = parser.parse_args()
    #处理音乐文件，提取元数据并保存为 JSON 文件
    process_music_files(args.directory)
