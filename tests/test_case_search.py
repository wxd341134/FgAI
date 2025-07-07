import time
import pytest
import allure
from datetime import datetime
from tests.base_test import BaseTest
from pages.assisted_read_page import AssistedReadPage
from common.assisted_read_utils import AssistedReadUtils
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("案件列表")
@allure.feature("案件查询")
class TestCaseSearch(BaseTest):
    """案件查询测试类"""

    @classmethod
    def setup_class(cls):
        """类级别的初始化"""
        try:
            super().setup_class()

            # 记录测试开始信息
            current_time = "2025-04-15 06:24:01"
            current_user = "wxd341134"

            logger.info("=" * 50)
            logger.info(f"开始执行案件查询测试")
            logger.info(f"测试开始时间: {current_time}")
            logger.info(f"执行用户: {current_user}")
            logger.info("=" * 50)

            # 创建页面对象
            cls.assisted_page = AssistedReadPage(cls.driver)
            logger.info("页面对象初始化完成")

        except Exception as e:
            logger.error(f"案件查询测试初始化失败: {str(e)}")
            if hasattr(cls, 'driver'):
                allure.attach(
                    cls.driver.get_screenshot_as_png(),
                    name="setup_failed",
                    attachment_type=allure.attachment_type.PNG
                )
            raise

    def take_screenshot(self, name):
        """截图方法"""
        try:
            screenshot = self.driver.get_screenshot_as_png()
            timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
            allure.attach(
                screenshot,
                name=f"{name}_{timestamp}",
                attachment_type=allure.attachment_type.PNG
            )
            logger.info(f"截图成功: {name}")
        except Exception as e:
            logger.error(f"截图失败 {name}: {str(e)}")

    @allure.story("案件查询功能")
    @allure.title("根据案件不同条件查询")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_search(self):
        """测试案件查询功能"""
        try:
            # 1. 执行查询操作
            with allure.step("执行案件查询"):
                logger.info("开始案件查询流程")
                self.take_screenshot("before_search")

                result = AssistedReadUtils.perform_case_search(
                    self.assisted_page,
                    case_number="2024",
                    case_name="2024苏1003民初5832号"
                )

                if not result:
                    self.take_screenshot("search_failed")
                    raise AssertionError("案件查询执行失败")

                self.take_screenshot("after_search")

            # 2. 执行重置操作
            with allure.step("重置查询表单"):
                logger.info("开始重置查询表单")

                reset_result = AssistedReadUtils.reset_search_form(self.assisted_page)

                if not reset_result:
                    self.take_screenshot("reset_failed")
                    raise AssertionError("重置查询表单失败")

                self.take_screenshot("after_reset")

            logger.info("案件查询测试完成")

        except Exception as e:
            logger.error(f"案件查询测试失败: {str(e)}")
            self.take_screenshot("test_failed")
            allure.attach(
                str(e),
                name="error_message",
                attachment_type=allure.attachment_type.TEXT
            )
            raise


if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=./reports/allure-results", __file__])