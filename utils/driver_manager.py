from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.logger import Logger
import os
import time

logger = Logger().get_logger()


class DriverManager:
    """浏览器驱动管理类"""

    driver = None
    _last_used = None

    @classmethod
    def get_driver(cls):
        """获取或创建WebDriver实例"""
        try:
            if cls.driver:
                try:
                    # 检查现有driver是否可用
                    cls.driver.current_url
                    logger.info("使用现有的WebDriver实例")
                    return cls.driver
                except:
                    logger.info("现有WebDriver实例不可用，将创建新实例")
                    cls.driver = None

            logger.info("开始创建Chrome WebDriver实例...")

            # 创建 Chrome 选项
            chrome_options = Options()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

            # 添加保持浏览器打开的选项
            chrome_options.add_experimental_option("detach", True)

            # 使用项目中的 chromedriver-win64 文件夹中的 chromedriver.exe
            driver_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'chromedriver-win64',
                'chromedriver.exe'
            )

            if os.path.exists(driver_path):
                logger.info(f"使用本地 ChromeDriver: {driver_path}")
                service = Service(executable_path=driver_path)
                cls.driver = webdriver.Chrome(service=service, options=chrome_options)
            else:
                logger.error(f"ChromeDriver不存在: {driver_path}")
                raise FileNotFoundError(f"ChromeDriver不存在: {driver_path}")

            cls.driver.implicitly_wait(10)
            cls._last_used = time.time()
            logger.info("Chrome WebDriver 创建成功")

            return cls.driver

        except Exception as e:
            logger.error(f"创建WebDriver实例失败: {str(e)}")
            raise

    @classmethod
    def quit_driver(cls):
        """关闭WebDriver实例"""
        if cls.driver:
            cls.driver.quit()
            cls.driver = None