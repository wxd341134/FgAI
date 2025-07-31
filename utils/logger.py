import logging
import os
import time
from datetime import datetime, timedelta


class Logger:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, logger_name='automation'):
        # 确保只初始化一次
        if Logger._initialized:
            return

        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        # 清除所有已存在的处理器
        if self.logger.handlers:
            for handler in self.logger.handlers[:]:
                self.logger.removeHandler(handler)

        # 创建logs目录
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 日志文件名
        log_file = os.path.join(log_dir, f'test_{time.strftime("%Y%m%d")}.log')

        # 文件处理器
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        # 控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # 日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 添加处理器
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        # 自动清理过期日志
        self.clean_old_logs(log_dir, 7)  # 保留最近7天的日志

        # 标记为已初始化
        Logger._initialized = True

    def get_logger(self):
        return self.logger

    @staticmethod
    def clean_old_logs(log_dir, retention_days=7):
        """
        清理旧的日志文件，只保留最近retention_days天的日志。
        :param log_dir: 日志文件所在的目录。
        :param retention_days: 需要保留的最近日志天数，默认7天。
        """
        now = datetime.now()
        retention_date = now - timedelta(days=retention_days)

        for filename in os.listdir(log_dir):
            file_path = os.path.join(log_dir, filename)
            if os.path.isfile(file_path):
                try:
                    # 尝试解析日志文件名中的日期部分
                    date_part = filename.split('_')[-1].split('.')[0]
                    log_date = datetime.strptime(date_part, "%Y%m%d")
                    if log_date < retention_date:
                        os.remove(file_path)
                        print(f"Deleted old log file: {filename}")
                except ValueError:
                    continue  # 如果文件名不符合预期格式，则跳过该文件