import time
from datetime import datetime
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.logger import Logger
from pages.caseMg_page import CaseMgPage

logger = Logger().get_logger()


class CaseMgUtils:
    """案件管理工具类"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_user = "wxd341134"

    def _click_element(self, locator, element_name):
        """通用点击元素方法"""
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
        """通用文本输入方法"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            logger.info(f"{self.current_time} - {self.current_user} - 输入文本 '{text}' 到 {element_name} 成功")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 输入文本失败: {str(e)}")
            self._take_screenshot(f"{element_name}_input_failed")
            return False

    def _take_screenshot(self, name):
        """统一的截图方法"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("添加案件")
    def add_case(self, case_name, case_number):
        """添加案件流程"""
        try:
            # 点击添加按钮
            with allure.step("点击添加按钮"):
                if not self._click_element(CaseMgPage.ADD_BUTTON, "添加按钮"):
                    return False

            # 填写基本信息
            with allure.step("填写案件信息"):
                if not self._input_text(CaseMgPage.CASE_NAME_INPUT, case_name, "案件名称"):
                    return False
                if not self._input_text(CaseMgPage.CASE_NUMBER_INPUT, case_number, "案件编号"):
                    return False

            # 选择案件类型
            with allure.step("选择案件类型"):
                if not self._click_element(CaseMgPage.CASE_TYPE_DROPDOWN, "案件类型下拉框"):
                    return False
                if not self._click_element(CaseMgPage.CASE_TYPE_CIVIL, "民事类型"):
                    return False
                if not self._click_element(CaseMgPage.CASE_TYPE_CIVIL_FIRST, "民事一审"):
                    return False

            # 选择案由类型
            with allure.step("选择案由类型"):
                if not self._click_element(CaseMgPage.CASE_REASON_DROPDOWN, "案由类型下拉框"):
                    return False
                if not self._click_element(CaseMgPage.CASE_REASON_ADMIN, "行政案由"):
                    return False

            # 选择立案日期
            with allure.step("选择立案日期"):
                if not self._click_element(CaseMgPage.FILING_DATE_INPUT, "立案日期"):
                    return False
                if not self._click_element(CaseMgPage.TODAY_OPTION, "今天"):
                    return False

            # 提交
            with allure.step("提交案件信息"):
                if not self._click_element(CaseMgPage.CONFIRM_BUTTON, "确定按钮"):
                    return False

            logger.info(f"{self.current_time} - {self.current_user} - 添加案件成功")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 添加案件失败: {str(e)}")
            self._take_screenshot("add_case_failed")
            return False

    @allure.step("编辑案件: {case_name}")
    def edit_case(self, case_name):
        """编辑案件流程"""
        try:
            # 点击编辑按钮
            with allure.step("点击编辑按钮"):
                edit_locator = (By.XPATH, CaseMgPage.EDIT_BUTTON_TEMPLATE.format(case_name))
                if not self._click_element(edit_locator, "编辑按钮"):
                    return False

            # 修改案件名称
            with allure.step("修改案件名称"):
                try:
                    # 等待输入框可见
                    name_input = self.wait.until(EC.presence_of_element_located(CaseMgPage.CASE_NAME_INPUT))

                    # 获取当前值
                    current_value = name_input.get_attribute('value')
                    print(current_value)
                    logger.info(f"2025-07-22 05:14:42 - wxd341134 - 当前案件名称: {current_value}")

                    # 在现有名称后添加"修改"
                    new_name = current_value + "修改"
                    print(new_name)

                    # 清空并输入新名称
                    name_input.send_keys(Keys.CONTROL + "a")
                    name_input.send_keys(Keys.BACKSPACE)
                    time.sleep(1)
                    name_input.send_keys(new_name)
                    time.sleep(0.5)

                    logger.info(f"2025-07-22 05:14:42 - wxd341134 - 修改后的案件名称: {new_name}")

                except Exception as e:
                    logger.error(f"2025-07-22 05:14:42 - wxd341134 - 修改案件名称失败: {str(e)}")
                    return False

            # 选择法官助理
            with allure.step("选择法官助理"):
                if not self._click_element(CaseMgPage.ASSISTANT_DROPDOWN, "法官助理下拉框"):
                    return False
                if not self._click_element(CaseMgPage.ASSISTANT_OPTION, "选择助理"):
                    return False

            # 提交修改
            with allure.step("提交修改"):
                if not self._click_element(CaseMgPage.CONFIRM_BUTTON, "确定按钮"):
                    return False

            logger.info(f"{self.current_time} - {self.current_user} - 编辑案件成功")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 编辑案件失败: {str(e)}")
            self._take_screenshot("edit_case_failed")
            return False

    @allure.step("删除案件: {case_name}")
    def delete_case(self, case_name):
        """删除案件流程"""
        try:
            # 点击删除按钮
            with allure.step("点击删除按钮"):
                delete_locator = (By.XPATH, CaseMgPage.DELETE_BUTTON_TEMPLATE.format(case_name))
                if not self._click_element(delete_locator, "删除按钮"):
                    return False

            # 确认删除
            with allure.step("确认删除"):
                if not self._click_element(CaseMgPage.DELETE_CONFIRM, "确认删除"):
                    return False

            logger.info(f"{self.current_time} - {self.current_user} - 删除案件成功")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 删除案件失败: {str(e)}")
            self._take_screenshot("delete_case_failed")
            return False