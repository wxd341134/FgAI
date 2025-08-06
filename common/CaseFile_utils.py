import os
import time
from datetime import datetime

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from utils.common import get_project_root
from utils.Common_utils import CommonUtils
from utils.logger import Logger
from pages.CaseFile_page import CaseFilePage

logger = Logger().get_logger()


class CaseFileUtils(CommonUtils):
    """卷宗上传和目录操作工具类"""

    def __init__(self, driver):
        super().__init__(driver)  # ✅ 调用父类初始化
        self.current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_user = "wxd341134"

    @allure.step("上传ZIP文件")
    def upload_zip_file(self):
        """上传ZIP文件流程"""
        try:
            # 构造ZIP文件路径
            zip_file = "(2024)鲁0502民初374号.zip"
            file_path = os.path.join(self.get_project_root(), "test_data", zip_file)

            # 点击上传ZIP按钮
            self.click_element(CaseFilePage.UPLOAD_ZIP_BUTTON, "上传ZIP按钮")
            time.sleep(1)


            # 选择文件
            self.input_file(CaseFilePage.ZIP_FILE_INPUT, file_path, "ZIP文件选择")
            time.sleep(1)


            # 点击确定
            self.click_element(CaseFilePage.ZIP_CONFIRM_BUTTON, "确定按钮")
            time.sleep(5)  # 等待上传完成
            logger.info(f"{self.current_time} - {self.current_user} - ZIP文件上传成功")


        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - ZIP文件上传失败: {str(e)}")
            raise

    @allure.step("上传单个文件")
    def upload_single_file(self):
        """上传单个文件流程"""
        try:
            # 构造文件路径
            docx_file = "法官AI助手安装文档.docx"
            file_path = os.path.join(self.get_project_root(), "test_data", docx_file)

            # 点击上传单个文件按钮
            self.click_element(CaseFilePage.UPLOAD_SINGLE_BUTTON, "上传单个文件按钮")
            time.sleep(1)

            # 选择文件
            self.input_file(CaseFilePage.DOCX_FILE_INPUT, file_path, "DOCX文件选择")
            time.sleep(1)

            # 点击确定
            self.click_element(CaseFilePage.SINGLE_FILE_CONFIRM_BUTTON, "确定按钮")
            time.sleep(1)
            logger.info(f"{self.current_time} - {self.current_user} - 单个文件上传成功")

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 单个文件上传失败: {str(e)}")
            raise

    @allure.step("创建目录: {dir_name}")
    def create_directory(self, dir_name, parent_dir=None):
        """
        创建目录
        :param dir_name: 目录名称
        :param parent_dir: 父目录名称，如果不为None则在指定目录下创建
        """
        try:
            # 点击新建目录按钮
            self.click_element(CaseFilePage.NEW_DIR_BUTTON, "新建目录按钮")
            time.sleep(0.5)

            # 如果指定了父目录，选择父目录
            if parent_dir:
                self.click_element(CaseFilePage.PARENT_DIR_DROPDOWN, "父目录下拉框")
                parent_option = (By.XPATH, CaseFilePage.DIR_OPTION_TEMPLATE.format(parent_dir))
                self.click_element(parent_option, f"选择父目录 {parent_dir}")

            # 输入目录名称
            self.input_text(CaseFilePage.DIR_NAME_INPUT, dir_name, "目录名称输入框")
            time.sleep(0.5)

            # 点击确定
            self.click_element(CaseFilePage.DIR_CONFIRM_BUTTON, "确定按钮")
            time.sleep(0.5)
            logger.info(f"{self.current_time} - {self.current_user} - 创建目录 {dir_name} 成功")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 创建目录失败: {str(e)}")
            return False

    @allure.step("删除目录: {dir_name}")
    def delete_directory(self, dir_name):
        """删除单个目录"""
        try:
            # 点击删除图标
            delete_icon = (By.XPATH, CaseFilePage.DELETE_ICON_TEMPLATE.format(dir_name))
            self.click_element(delete_icon, f"删除 {dir_name} 图标")
            time.sleep(0.5)

            # 确认删除
            self.click_element(CaseFilePage.DELETE_CONFIRM_BUTTON, "删除确认按钮")
            time.sleep(0.5)

            logger.info(f"{self.current_time} - {self.current_user} - 删除目录 {dir_name} 成功")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 删除目录失败: {str(e)}")
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
                self.click_element(checkbox, f"选中 {dir_name}")

            # 点击批量删除按钮
            self.click_element(CaseFilePage.BATCH_DELETE_BUTTON, "批量删除按钮")
            time.sleep(0.5)

            # 确认删除
            self.click_element(CaseFilePage.DELETE_CONFIRM_BUTTON, "删除确认按钮")
            time.sleep(0.5)

            logger.info(f"{self.current_time} - {self.current_user} - 批量删除目录成功")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 批量删除目录失败: {str(e)}")
            return False

    @allure.step("执行完整的卷宗上传流程")
    def execute_upload_workflow(self):
        """执行完整的卷宗上传流程"""
        try:
            # 点击上传卷宗按钮
            with allure.step("点击上传卷宗按钮"):
                self.click_element(CaseFilePage.UPLOAD_BUTTON, "上传卷宗按钮")

            # 上传ZIP文件
            with allure.step("上传ZIP文件"):
                self.upload_zip_file()

            # 刷新文件列表
            with allure.step("刷新文件列表"):
                self.click_element(CaseFilePage.REFRESH_BUTTON, "刷新按钮")

            # 上传单个文件
            with allure.step("上传单个文件"):
                self.upload_single_file()

            # 收起和展开操作
            with allure.step("收起和展开文件列表"):
                self.click_element(CaseFilePage.COLLAPSE_ALL_BUTTON, "收起全部按钮")
                time.sleep(1)
                self.click_element(CaseFilePage.EXPAND_ALL_BUTTON, "展开全部按钮")

            logger.info(f"{self.current_time} - {self.current_user} - 卷宗上传流程执行完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 卷宗上传流程执行失败: {str(e)}")
            return False

    @allure.step("执行完整的目录操作流程")
    def execute_directory_workflow(self):
        """执行完整的目录操作流程"""
        try:
            # 创建一级目录
            with allure.step("创建一级目录"):
                self.create_directory("测试目录1")

            # 创建二级目录
            with allure.step("创建二级目录"):
                self.create_directory("测试目录2", "测试目录1")

            # 删除单个目录
            with allure.step("删除单个目录"):
                self.delete_directory("庭审笔录1")

            # 批量删除目录
            with allure.step("批量删除目录"):
                self.batch_delete_directories(["庭审笔录2", "庭审笔录3"])

            logger.info(f"{self.current_time} - {self.current_user} - 目录操作流程执行完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 目录操作流程执行失败: {str(e)}")
            return False
