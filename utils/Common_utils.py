import time
import json
import os
import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger

logger = Logger().get_logger()


class CommonUtils:
    """通用工具类，提供基础UI操作方法"""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_element(self, locator, element_name):
        """
        安全点击元素的方法

        Args:
            locator: 元素定位器
            element_name: 元素名称（用于日志记录）
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"成功点击{element_name}")
        except Exception as e:
            logger.error(f"点击{element_name}失败: {str(e)}")
            raise

    # def input_text(self, locator, text, element_name, clear_first=True):
    #     """
    #     安全输入文本的方法
    #
    #     Args:
    #         locator: 元素定位器
    #         text: 要输入的文本
    #         element_name: 元素名称（用于日志记录）
    #         clear_first: 是否先清除原有内容，默认为True ,Information_Extraction_utils中设置了clear_first=False
    #     """
    #     try:
    #         element = self.wait.until(EC.presence_of_element_located(locator))
    #         if clear_first:
    #             element.clear()
    #         element.send_keys(text)
    #         action = "覆盖输入" if clear_first else "追加输入"
    #         logger.info(f"在{element_name}中{action}文本: {text}")
    #     except Exception as e:
    #         logger.error(f"在{element_name}中输入文本失败: {str(e)}")
    #         raise



    def input_text(self, locator, text, element_name, clear_first=True):
        """
        安全输入文本，支持 Ant Design 等复杂组件
        """
        try:
            # 等待元素可见且可交互
            element = self.wait.until(EC.visibility_of_element_located(locator))

            # 获得焦点
            element.click()

            if clear_first:
                # 使用全选 + 删除，比 clear() 更可靠
                element.send_keys(Keys.CONTROL + "a")  # Windows
                # element.send_keys(Keys.COMMAND + "a")  # Mac
                element.send_keys(Keys.DELETE)
                # element.send_keys(Keys.BACK_SPACE)  # 双重保险
                time.sleep(0.3)  # 给前端反应时间

            # 输入新值
            element.send_keys(text)

            logger.info(f"在 {element_name} 中输入文本: {text}")

        except Exception as e:
            logger.error(f"在 {element_name} 中输入文本失败: {str(e)}")
            raise

    def input_file(self, locator, file_path, element_name):
        """
        通用文件输入方法

        Args:
            locator: 文件输入元素定位器
            file_path: 文件路径
            element_name: 元素名称（用于日志记录）
        """
        try:
            file_input = self.wait.until(EC.presence_of_element_located(locator))
            file_input.send_keys(file_path)
            logger.info(f"选择文件 {file_path} 成功")
        except Exception as e:
            logger.error(f"文件选择失败: {str(e)}")
            raise

    def take_screenshot(self, name):
        """截图方法"""
        try:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            logger.error(f"截图失败: {str(e)}")

    @staticmethod
    def load_json_data(file_path):
        """
        加载JSON格式的测试数据

        Args:
            file_path: JSON文件路径

        Returns:
            解析后的JSON数据
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)


    def get_project_root(self):
        """
        获取项目根目录路径

        Returns:
            项目根目录的绝对路径
        """
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


