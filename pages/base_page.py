from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys
import allure

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import Logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = Logger().get_logger()

    def find_element(self, locator):
        """查找元素"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element
        except Exception as e:
            self.logger.error(f"查找元素失败: {locator}, 错误: {e}")
            self.take_screenshot(f"find_element_failed_{locator[1]}")
            raise

    def click_element(self, locator):
        """点击元素"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"点击元素: {locator}")
        except Exception as e:
            self.logger.error(f"点击元素失败: {locator}, 错误: {e}")
            self.take_screenshot(f"click_element_failed_{locator[1]}")
            raise

    def input_text(self, locator, text):
        """输入文本"""
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            self.logger.info(f"输入文本: {text}, 元素: {locator}")
        except Exception as e:
            self.logger.error(f"输入文本失败: {locator}, 文本: {text}, 错误: {e}")
            self.take_screenshot(f"input_text_failed_{locator[1]}")
            raise

    def take_screenshot(self, name):
        """截图并添加到Allure报告"""
        try:
            screenshot = self.driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.info(f"截图已添加到Allure报告: {name}")
        except Exception as e:
            self.logger.error(f"截图失败: {name}, 错误: {e}")