import time

import pytest
import allure
from common.caseMg_utils import CaseMgUtils
from tests.base_test import BaseTest
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("案件管理系统")
@allure.feature("案件管理模块")
class TestCaseManagement(BaseTest):
    """案件管理测试类"""

    @pytest.fixture(autouse=True)
    def setup_case(self, driver):
        """
        测试前后处理
        前置：初始化CaseMgUtils对象
        后置：记录日志
        """
        logger.info("2025-07-18 09:52:51 - wxd341134 - 开始测试前置操作")
        try:
            self.case_utils = CaseMgUtils(driver)
            yield
            logger.info(" 测试后置操作完成")
        except Exception as e:
            logger.error(f" 测试前置/后置操作失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "setup_failed",
                allure.attachment_type.PNG
            )
            raise

    @allure.story("案件基本操作")
    @allure.title("案件增删改功能测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_crud(self, driver):
        """测试案件的添加、编辑和删除功能"""
        try:
            case_name = "(2025)苏0105民初0001号"

            # 添加案件
            with allure.step(f"添加案件: {case_name}"):
                assert self.case_utils.add_case(case_name, case_name)
                time.sleep(3)

            # 编辑案件
            with allure.step(f"编辑案件: {case_name}"):
                assert self.case_utils.edit_case(case_name)
                time.sleep(3)

            # 删除案件
            with allure.step(f"删除案件: {case_name}"):
                assert self.case_utils.delete_case(case_name)
                time.sleep(1)

            logger.info("案件操作测试完成")

        except AssertionError as ae:
            logger.error(f" 断言失败: {str(ae)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "assertion_failed",
                allure.attachment_type.PNG
            )
            raise
        except Exception as e:
            logger.error(f"测试执行失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "test_failed",
                allure.attachment_type.PNG
            )
            allure.attach(
                str(e),
                "error_message",
                allure.attachment_type.TEXT
            )
            raise


if __name__ == "__main__":
    pytest.main([
        "-v",
        "--alluredir=./reports/allure-results",
        __file__
    ])