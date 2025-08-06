
import time
from datetime import datetime

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.case_search_page import CaseSearchPage
from utils.Common_utils import CommonUtils
from utils.logger import Logger

logger = Logger().get_logger()


class CaseSearchUtils(CommonUtils):
    """案件查询工具类"""


    def __init__(self, driver):
        super().__init__(driver)  # ✅ 调用父类初始化
        self.current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_user = "wxd341134"


    @allure.step("按案件编号查询")
    def search_by_case_number(self, case_number):
        """按案件编号查询"""
        try:
            # 输入案件编号
            self.input_text(CaseSearchPage.CASE_NUMBER_INPUT, case_number, "案件编号", clear_first=False)

            # 点击查询
            self.click_element(CaseSearchPage.SEARCH_BUTTON, "查询按钮")
            time.sleep(2)
            logger.info(f"{self.current_time} - {self.current_user} - 案件编号查询完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 案件编号查询失败: {str(e)}")
            return False

    @allure.step("按判决书状态查询")
    def search_by_judgment_status(self):
        """按判决书状态查询"""
        try:
            # 点击判决书状态下拉框
            self.click_element(CaseSearchPage.JUDGMENT_STATUS_DROPDOWN, "判决书状态下拉框")

            # 选择未生成
            self.click_element(CaseSearchPage.JUDGMENT_NOT_GENERATED, "未生成选项")

            # 点击查询
            self.click_element(CaseSearchPage.SEARCH_BUTTON, "查询按钮")
            time.sleep(1)
            logger.info(f"{self.current_time} - {self.current_user} - 判决书状态查询完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 判决书状态查询失败: {str(e)}")
            return False

    @allure.step("按承办人查询")
    def search_by_handler(self):
        """按承办人查询"""
        try:
            # 点击承办人下拉框
            self.click_element(CaseSearchPage.HANDLER_DROPDOWN, "承办人下拉框")

            # 选择全部
            self.click_element(CaseSearchPage.HANDLER_ALL, "全部选项")

            # 点击查询
            self.click_element(CaseSearchPage.SEARCH_BUTTON, "查询按钮")
            time.sleep(1)
            logger.info(f"{self.current_time} - {self.current_user} - 承办人查询完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 承办人查询失败: {str(e)}")
            return False

    @allure.step("重置查询条件")
    def reset_search(self):
        """重置查询条件"""
        try:
            self.click_element(CaseSearchPage.RESET_BUTTON, "重置按钮")

            time.sleep(1)
            logger.info(f"{self.current_time} - {self.current_user} - 重置查询条件完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 重置查询条件失败: {str(e)}")
            return False