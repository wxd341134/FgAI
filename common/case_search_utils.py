import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.case_search_page import CaseSearchPage
from utils.logger import Logger

logger = Logger().get_logger()


class CaseSearchUtils:
    """案件查询工具类"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.current_time = "2025-07-24 05:54:10"
        self.current_user = "wxd341134"

    def _click_element(self, locator, element_name):
        """通用点击方法"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(1)
            element.click()
            logger.info(f"{self.current_time} - {self.current_user} - 点击 {element_name} 成功")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 点击 {element_name} 失败: {str(e)}")
            self._take_screenshot(f"{element_name}_click_failed")
            return False

    def _input_text(self, locator, text, element_name):
        """通用输入方法"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            logger.info(f"{self.current_time} - {self.current_user} - 在 {element_name} 输入: {text}")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 输入文本失败: {str(e)}")
            self._take_screenshot(f"{element_name}_input_failed")
            return False

    def _take_screenshot(self, name):
        """截图方法"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name,
            allure.attachment_type.PNG
        )

    @allure.step("按案件编号查询")
    def search_by_case_number(self, case_number):
        """按案件编号查询"""
        try:
            # 输入案件编号
            if not self._input_text(CaseSearchPage.CASE_NUMBER_INPUT, case_number, "案件编号"):
                return False

            # 点击查询
            if not self._click_element(CaseSearchPage.SEARCH_BUTTON, "查询按钮"):
                return False

            time.sleep(2)
            logger.info(f"{self.current_time} - {self.current_user} - 案件编号查询完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 案件编号查询失败: {str(e)}")
            self._take_screenshot("search_by_case_number_failed")
            return False

    @allure.step("按判决书状态查询")
    def search_by_judgment_status(self):
        """按判决书状态查询"""
        try:
            # 点击判决书状态下拉框
            if not self._click_element(CaseSearchPage.JUDGMENT_STATUS_DROPDOWN, "判决书状态下拉框"):
                return False

            # 选择未生成
            if not self._click_element(CaseSearchPage.JUDGMENT_NOT_GENERATED, "未生成选项"):
                return False

            # 点击查询
            if not self._click_element(CaseSearchPage.SEARCH_BUTTON, "查询按钮"):
                return False

            time.sleep(1)
            logger.info(f"{self.current_time} - {self.current_user} - 判决书状态查询完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 判决书状态查询失败: {str(e)}")
            self._take_screenshot("search_by_judgment_status_failed")
            return False

    @allure.step("按承办人查询")
    def search_by_handler(self):
        """按承办人查询"""
        try:
            # 点击承办人下拉框
            if not self._click_element(CaseSearchPage.HANDLER_DROPDOWN, "承办人下拉框"):
                return False

            # 选择全部
            if not self._click_element(CaseSearchPage.HANDLER_ALL, "全部选项"):
                return False

            # 点击查询
            if not self._click_element(CaseSearchPage.SEARCH_BUTTON, "查询按钮"):
                return False

            time.sleep(1)
            logger.info(f"{self.current_time} - {self.current_user} - 承办人查询完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 承办人查询失败: {str(e)}")
            self._take_screenshot("search_by_handler_failed")
            return False

    @allure.step("重置查询条件")
    def reset_search(self):
        """重置查询条件"""
        try:
            if not self._click_element(CaseSearchPage.RESET_BUTTON, "重置按钮"):
                return False

            time.sleep(1)
            logger.info(f"{self.current_time} - {self.current_user} - 重置查询条件完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 重置查询条件失败: {str(e)}")
            self._take_screenshot("reset_search_failed")
            return False