import time
import json
import os

def load_json_data(file_path):
    """加载JSON格式的测试数据"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def wait_for_seconds(seconds=1):
    """等待指定的秒数"""
    time.sleep(seconds)

def get_project_root():
    """获取项目根目录路径"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))