import time
import json
import os
import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger

logger = Logger().get_logger()

def load_json_data(file_path):
    """加载JSON格式的测试数据"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_project_root():
    """获取项目根目录路径"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def click_element(driver, locator, element_name):
    """点击元素的通用方法"""
    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()
        logger.info(f"点击 {element_name} 成功")
        time.sleep(0.5)
    except Exception as e:
        logger.error(f"点击 {element_name} 失败: {str(e)}")
        allure.attach(
            driver.get_screenshot_as_png(),
            f"{element_name}点击失败截图",
            allure.attachment_type.PNG
        )
        raise

def input_text(driver, locator, text, element_name, clear_first=True):
    """输入文本的通用方法"""
    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        if clear_first:
            element.clear()
        element.send_keys(text)
        action = "覆盖输入" if clear_first else "追加输入"
        logger.info(f"在 {element_name} 中{action}文本 '{text}' 成功")
    except Exception as e:
        logger.error(f"在 {element_name} 中输入文本失败: {str(e)}")
        allure.attach(
            driver.get_screenshot_as_png(),
            f"{element_name}输入失败截图",
            allure.attachment_type.PNG
        )
        raise
