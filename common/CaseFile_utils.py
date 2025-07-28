import os
import time
from datetime import datetime

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.common import get_project_root
from utils.logger import Logger
from pages.CaseFile_page import CaseFilePage

logger = Logger().get_logger()


class CaseFileUtils:
    """卷宗上传和目录操作工具类"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_user = "wxd341134"


    def _click_element(self, locator, element_name):
        """通用点击元素方法"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"{self.current_time} - {self.current_user} - 点击 {element_name} 成功")
            time.sleep(1)
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 点击 {element_name} 失败: {str(e)}")
            self._take_screenshot(f"{element_name}点击失败")
            return False

    def _input_text(self, locator, text, element_name):
        """通用文本输入方法"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            logger.info(f"{self.current_time} - {self.current_user} - 在 {element_name} 中输入文本 '{text}' 成功")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 文本输入失败: {str(e)}")
            self._take_screenshot(f"{element_name}输入失败")
            return False

    def _input_file(self, locator, file_path, element_name):
        """通用文件输入方法"""
        try:
            file_input = self.wait.until(EC.presence_of_element_located(locator))
            file_input.send_keys(file_path)
            logger.info(f"{self.current_time} - {self.current_user} - 选择文件 {file_path} 成功")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 文件选择失败: {str(e)}")
            self._take_screenshot(f"{element_name}文件选择失败")
            return False

    def _take_screenshot(self, name):
        """统一的截图方法"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("上传ZIP文件")
    def upload_zip_file(self):
        """上传ZIP文件流程"""
        try:
            # 构造ZIP文件路径
            zip_file = "(2024)鲁0502民初374号.zip"
            file_path = os.path.join(get_project_root(), "test_data", zip_file)

            # 点击上传ZIP按钮
            if not self._click_element(CaseFilePage.UPLOAD_ZIP_BUTTON, "上传ZIP按钮"):
                return False

            # 选择文件
            if not self._input_file(CaseFilePage.ZIP_FILE_INPUT, file_path, "ZIP文件选择"):
                return False

            # 点击确定
            if not self._click_element(CaseFilePage.ZIP_CONFIRM_BUTTON, "确定按钮"):
                return False

            time.sleep(5)  # 等待上传完成
            logger.info(f"{self.current_time} - {self.current_user} - ZIP文件上传成功")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - ZIP文件上传失败: {str(e)}")
            self._take_screenshot("zip_upload_failed")
            return False

    @allure.step("上传单个文件")
    def upload_single_file(self):
        """上传单个文件流程"""
        try:
            # 构造文件路径
            docx_file = "法官AI助手安装文档.docx"
            file_path = os.path.join(get_project_root(), "test_data", docx_file)

            # 点击上传单个文件按钮
            if not self._click_element(CaseFilePage.UPLOAD_SINGLE_BUTTON, "上传单个文件按钮"):
                return False

            # 选择文件
            if not self._input_file(CaseFilePage.DOCX_FILE_INPUT, file_path, "DOCX文件选择"):
                return False

            # 点击确定
            if not self._click_element(CaseFilePage.SINGLE_FILE_CONFIRM_BUTTON, "确定按钮"):
                return False

            logger.info(f"{self.current_time} - {self.current_user} - 单个文件上传成功")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 单个文件上传失败: {str(e)}")
            self._take_screenshot("single_file_upload_failed")
            return False

    @allure.step("创建目录: {dir_name}")
    def create_directory(self, dir_name, parent_dir=None):
        """
        创建目录
        :param dir_name: 目录名称
        :param parent_dir: 父目录名称，如果不为None则在指定目录下创建
        """
        try:
            # 点击新建目录按钮
            if not self._click_element(CaseFilePage.NEW_DIR_BUTTON, "新建目录按钮"):
                return False

            # 如果指定了父目录，选择父目录
            if parent_dir:
                if not self._click_element(CaseFilePage.PARENT_DIR_DROPDOWN, "父目录下拉框"):
                    return False
                parent_option = (By.XPATH, CaseFilePage.DIR_OPTION_TEMPLATE.format(parent_dir))
                if not self._click_element(parent_option, f"选择父目录 {parent_dir}"):
                    return False

            # 输入目录名称
            if not self._input_text(CaseFilePage.DIR_NAME_INPUT, dir_name, "目录名称输入框"):
                return False

            # 点击确定
            if not self._click_element(CaseFilePage.DIR_CONFIRM_BUTTON, "确定按钮"):
                return False

            logger.info(f"{self.current_time} - {self.current_user} - 创建目录 {dir_name} 成功")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 创建目录失败: {str(e)}")
            self._take_screenshot("create_directory_failed")
            return False

    @allure.step("删除目录: {dir_name}")
    def delete_directory(self, dir_name):
        """删除单个目录"""
        try:
            # 点击删除图标
            delete_icon = (By.XPATH, CaseFilePage.DELETE_ICON_TEMPLATE.format(dir_name))
            if not self._click_element(delete_icon, f"删除 {dir_name} 图标"):
                return False

            # 确认删除
            if not self._click_element(CaseFilePage.DELETE_CONFIRM_BUTTON, "删除确认按钮"):
                return False

            logger.info(f"{self.current_time} - {self.current_user} - 删除目录 {dir_name} 成功")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 删除目录失败: {str(e)}")
            self._take_screenshot("delete_directory_failed")
            return False

    @allure.step("批量删除目录")
    def batch_delete_directories(self, dir_names):
        """
        批量删除目录
        :param dir_names: 目录名称列表
        """
        try:
            # 选中要删除的目录
            for dir_name in dir_names:
                checkbox = (By.XPATH, CaseFilePage.CHECKBOX_TEMPLATE.format(dir_name))
                if not self._click_element(checkbox, f"选中 {dir_name}"):
                    return False

            # 点击批量删除按钮
            if not self._click_element(CaseFilePage.BATCH_DELETE_BUTTON, "批量删除按钮"):
                return False

            # 确认删除
            if not self._click_element(CaseFilePage.DELETE_CONFIRM_BUTTON, "删除确认按钮"):
                return False

            logger.info(f"{self.current_time} - {self.current_user} - 批量删除目录成功")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 批量删除目录失败: {str(e)}")
            self._take_screenshot("batch_delete_failed")
            return False

    @allure.step("执行完整的卷宗上传流程")
    def execute_upload_workflow(self):
        """执行完整的卷宗上传流程"""
        try:
            # 点击上传卷宗按钮
            with allure.step("点击上传卷宗按钮"):
                if not self._click_element(CaseFilePage.UPLOAD_BUTTON, "上传卷宗按钮"):
                    return False

            # 上传ZIP文件
            with allure.step("上传ZIP文件"):
                if not self.upload_zip_file():
                    return False

            # 刷新文件列表
            with allure.step("刷新文件列表"):
                if not self._click_element(CaseFilePage.REFRESH_BUTTON, "刷新按钮"):
                    return False

            # 上传单个文件
            with allure.step("上传单个文件"):
                if not self.upload_single_file():
                    return False

            # 收起和展开操作
            with allure.step("收起和展开文件列表"):
                if not self._click_element(CaseFilePage.COLLAPSE_ALL_BUTTON, "收起全部按钮"):
                    return False
                time.sleep(1)
                if not self._click_element(CaseFilePage.EXPAND_ALL_BUTTON, "展开全部按钮"):
                    return False

            logger.info(f"{self.current_time} - {self.current_user} - 卷宗上传流程执行完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 卷宗上传流程执行失败: {str(e)}")
            self._take_screenshot("upload_workflow_failed")
            return False

    @allure.step("执行完整的目录操作流程")
    def execute_directory_workflow(self):
        """执行完整的目录操作流程"""
        try:
            # 创建一级目录
            with allure.step("创建一级目录"):
                if not self.create_directory("测试目录1"):
                    return False

            # 创建二级目录
            with allure.step("创建二级目录"):
                if not self.create_directory("测试目录2", "测试目录1"):
                    return False

            # 删除单个目录
            with allure.step("删除单个目录"):
                if not self.delete_directory("庭审笔录1"):
                    return False

            # 批量删除目录
            with allure.step("批量删除目录"):
                if not self.batch_delete_directories(["庭审笔录2", "庭审笔录3"]):
                    return False

            logger.info(f"{self.current_time} - {self.current_user} - 目录操作流程执行完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 目录操作流程执行失败: {str(e)}")
            self._take_screenshot("directory_workflow_failed")
            return False