import pytest
import allure
from common.Mediation_utils import MediationUtils
from tests.base_test import BaseTest
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("调节模块功能测试")
class TestMediation(BaseTest):
    """调节模块功能测试用例"""

    @pytest.fixture(autouse=True)
    def setup_mediation(self, driver):
        """
        测试前后处理
        前置：初始化MediationUtils对象
        后置：记录日志
        """
        logger.info("开始测试前置操作...")
        try:
            self.mediation_utils = MediationUtils(driver)
            yield
            logger.info("测试后置操作完成")
        except Exception as e:
            logger.error(f"测试前置/后置操作失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "设置或清理失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("调节功能")
    @allure.story("基本调节操作")
    @allure.title("测试调节基本功能")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_mediation_basic(self, driver):
        """
        测试调节基本功能，包括：
        1. 打开调节界面
        2. 卷宗预览
        3. 保存和导出
        4. 查找替换功能（包括单次替换和全部替换）
        """
        try:
            # 执行调节操作
            with allure.step("执行调节操作"):
                result = self.mediation_utils.perform_mediation_operations()
                assert result, "调节操作失败"

        except Exception as e:
            logger.error(f"调节测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "测试失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("调节功能")
    @allure.story("查找替换操作")
    @allure.title("测试查找替换功能")
    @allure.severity(allure.severity_level.NORMAL)
    def test_find_replace_operation(self, driver):
        """测试查找替换功能"""
        try:

            with allure.step("执行查找替换测试"):
                # 执行查找替换操作
                result = self.mediation_utils.perform_mediation_operations()
                assert result, "查找替换操作失败"

        except Exception as e:
            logger.error(f"查找替换测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "查找替换测试失败截图",
                allure.attachment_type.PNG
            )
            raise