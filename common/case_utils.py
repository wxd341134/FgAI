import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.logger import Logger

logger = Logger().get_logger()

class CaseUtils:
    """案件操作工具类"""

    def __init__(self, page):
        """
        初始化
        :param page: CasePage实例
        """
        self.page = page
        self.logger = logger

    @allure.step("添加案件")
    def add_case(self, case_name, case_number):
        """
        添加案件的业务流程
        :param case_name: 案件名称
        :param case_number: 案件编号
        """
        try:
            self.logger.info(f"开始添加案件: {case_name}")

            # 打开添加表单
            with allure.step("点击添加按钮"):
                self.page.click_element(self.page.add_button)
                time.sleep(1)
                self.page.take_screenshot("add_case_form")

            # 填写基本信息
            with allure.step(f"输入案件基本信息"):
                self._fill_case_basic_info(case_name, case_number)

            # 选择案件类型
            with allure.step("选择案件类型"):
                self._select_case_type()

            # 选择案由类型
            with allure.step("选择案由类型"):
                self._select_case_reason()

            # 填写原审案号
            with allure.step(f"输入原审案号: {case_number}"):
                self._fill_original_case_number(case_number)

            # 选择立案日期
            with allure.step("选择立案日期"):
                self._select_filing_date()

            # 提交表单
            with allure.step("提交案件信息"):
                self._submit_form()

            self.logger.info(f"案件添加成功: {case_name}")
            return True

        except Exception as e:
            self.logger.error(f"添加案件失败: {str(e)}")
            allure.attach(
                self.page.driver.get_screenshot_as_png(),
                "添加案件失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("编辑案件")
    def edit_case(self, case_name):
        """
        编辑案件的业务流程
        :param case_name: 要编辑的案件名称
        """
        try:
            self.logger.info(f"开始编辑案件: {case_name}")

            # 打开编辑表单
            with allure.step(f"定位并打开编辑表单"):
                self._open_edit_form(case_name)

            # 修改案件名称
            with allure.step(f"修改案件名称为: {case_name}修改"):
                self._modify_case_name(case_name)

            # 提交修改
            with allure.step("提交修改"):
                self._submit_form()

            self.logger.info(f"案件修改成功: {case_name}修改")
            return True

        except Exception as e:
            self.logger.error(f"编辑案件失败: {str(e)}")
            allure.attach(
                self.page.driver.get_screenshot_as_png(),
                "编辑案件失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("删除案件")
    def delete_case(self, case_number):
        """
        删除案件的业务流程
        :param case_number: 要删除的案件编号
        """
        try:
            self.logger.info(f"开始删除案件: {case_number}")

            # 点击删除按钮
            with allure.step("定位到删除按钮"):
                self._click_delete_button(case_number)

            # 确认删除
            with allure.step("确认删除"):
                self._confirm_delete()

            self.logger.info(f"案件删除成功: {case_number}")
            return True

        except Exception as e:
            self.logger.error(f"删除案件失败: {str(e)}")
            allure.attach(
                self.page.driver.get_screenshot_as_png(),
                "删除案件失败截图",
                allure.attachment_type.PNG
            )
            raise

    # 私有辅助方法
    def _fill_case_basic_info(self, case_name, case_number):
        """填写案件基本信息"""
        self.page.input_text(self.page.case_name_input, case_name)
        self.page.input_text(self.page.case_number_input, case_number)
        time.sleep(1)
        self.page.take_screenshot("basic_info_filled")

    def _select_case_type(self):
        """选择案件类型"""
        self.page.click_element(self.page.case_type_dropdown)
        self.page.click_element(self.page.civil_case_option)
        self.page.click_element(self.page.civil_case_option2)
        time.sleep(1)
        self.page.take_screenshot("case_type_selected")

    def _select_case_reason(self):
        """选择案由类型"""
        self.page.click_element(self.page.reason_select)
        self.page.click_element(self.page.admin_case_option)
        time.sleep(1)
        self.page.take_screenshot("reason_type_selected")

    def _fill_original_case_number(self, case_number):
        """填写原审案号"""
        self.page.click_element(self.page.original_case_input)
        time.sleep(1)
        element = self.page.find_element(self.page.original_case_field)
        element.send_keys(case_number)
        time.sleep(1)

    def _select_filing_date(self):
        """选择立案日期"""
        self.page.click_element(self.page.date_input)
        self.page.click_element(self.page.today_option)
        time.sleep(1)
        self.page.take_screenshot("date_selected")

    def _submit_form(self):
        """提交表单"""
        self.page.click_element(self.page.confirm_button)
        time.sleep(2)
        self.page.take_screenshot("form_submitted")

    def _open_edit_form(self, case_name):
        """打开编辑表单"""
        edit_xpath = f"//td[@title='{case_name}'][1]/ancestor::div[contains(@class, 'ant-table-content')]/div[3]/div[2]/div/table/tbody/tr/td[3]/div/div[3]"
        self.page.click_element((By.XPATH, edit_xpath))
        time.sleep(1)
        self.page.take_screenshot("edit_form_opened")

    def _modify_case_name(self, case_name):
        """修改案件名称"""
        case_name_field = self.page.find_element(self.page.case_name_input)
        case_name_field.send_keys(Keys.CONTROL + "a")
        case_name_field.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        case_name_field.send_keys(f'{case_name}修改')
        time.sleep(1)
        self.page.take_screenshot("case_name_modified")

    def _click_delete_button(self, case_number):
        """点击删除按钮"""
        delete_xpath = f"//td[@title='{case_number}'][1]/ancestor::div[contains(@class, 'ant-table-content')]/div[3]/div[2]/div/table/tbody/tr/td[3]/div/div[4]"
        self.page.click_element((By.XPATH, delete_xpath))
        time.sleep(1)
        self.page.take_screenshot("delete_button_clicked")

    def _confirm_delete(self):
        """确认删除"""
        confirm_delete_button = (By.XPATH, "//div[@class='ant-modal-body']//button[2]")
        self.page.click_element(confirm_delete_button)
        time.sleep(2)
        self.page.take_screenshot("delete_confirmed")

