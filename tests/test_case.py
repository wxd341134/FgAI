import pytest
import json
import os
import allure
from datetime import datetime
from pages.login_page import LoginPage
from pages.case_page import CasePage
from common.case_utils import CaseUtils
from tests.base_test import BaseTest
from utils.common import load_json_data, get_project_root
from utils.logger import Logger
# from tests.base_test import BaseTest

# 创建logger实例
logger = Logger().get_logger()



class TestDataManager:
    """测试数据管理类"""

    @staticmethod
    def get_test_data():
        """获取测试数据"""
        try:
            data_file = os.path.join(get_project_root(), 'test_data', 'case_data.json')
            logger.info(f"尝试加载测试数据文件: {data_file}")

            if not os.path.exists(data_file):
                TestDataManager._create_default_test_data(data_file)

            test_data = load_json_data(data_file)
            logger.info("测试数据加载成功")
            return test_data

        except Exception as e:
            logger.error(f"加载测试数据失败: {e}")
            return TestDataManager._get_default_data()



@allure.epic("法官AI系统测试")
@allure.feature("案件管理功能")
class TestCaseManagement(BaseTest):
    """案件管理测试类"""

    def setup_method(self):
        """每个测试方法的初始化"""
        self.case_page = CasePage(self.driver)
        self.case_utils = CaseUtils(self.case_page)
        self.test_data = TestDataManager.get_test_data()
        logger.info("案件管理测试初始化完成")

    def teardown_method(self):
        """每个测试方法的清理"""
        logger.info("案件管理测试清理完成")

    @allure.story("案件增删改功能")
    @allure.title("测试案件的添加、修改和删除")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_crud(self):
        """测试案件的添加、修改和删除功能"""
        case_data = self.test_data["test_cases"][0]
        case_name = case_data["case_name"]
        case_number = case_data["case_number"]

        logger.info(f"开始测试案件增删改功能，案件名称: {case_name}")
        allure.dynamic.description(f"测试案件增删改功能，使用案件: {case_name}")

        try:
            # 添加案件
            with allure.step(f"添加案件: {case_name}"):
                self.case_utils.add_case(case_name, case_number)
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "案件添加成功截图",
                    allure.attachment_type.PNG
                )

            # 编辑案件
            with allure.step(f"编辑案件: {case_name}"):
                self.case_utils.edit_case(case_name)
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "案件编辑成功截图",
                    allure.attachment_type.PNG
                )

            # 删除案件
            with allure.step(f"删除案件: {case_number}"):
                self.case_utils.delete_case(case_number)
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "案件删除成功截图",
                    allure.attachment_type.PNG
                )

            logger.info(f"案件增删改功能测试完成，案件名称: {case_name}")

        except Exception as e:
            logger.error(f"案件操作失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "失败时的截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.story("案件数据验证")
    @allure.title("测试案件数据有效性")
    @allure.severity(allure.severity_level.NORMAL)
    def test_case_data_validation(self):
        """测试案件数据的有效性验证"""
        # 这里可以添加更多的测试用例
        pass


if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=./allure-results", "test_case_management.py"])