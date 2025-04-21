import allure
import pytest
from common.statute_search_utils import StatuteSearchUtils
from tests.base_test import BaseTest
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("案件管理系统")
@allure.feature("法条检索模块")
class TestStatuteSearch(BaseTest):
    """法条检索测试类"""

    @pytest.fixture(autouse=True)
    def setup_teardown(self, driver):
        """
        测试用例级别的设置和清理
        使用基类的driver fixture
        """
        logger.info("开始测试前置操作...")
        try:
            # 初始化法条检索工具类
            self.statute_search = StatuteSearchUtils(driver)
            logger.info("法条检索工具类初始化完成")

            # 执行测试
            yield

            logger.info("测试后置操作完成")

        except Exception as e:
            logger.error(f"测试前置/后置操作失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "设置/清理失败截图",
                allure.attachment_type.PNG
            )
            raise

    def take_screenshot(self, name):
        """截图方法"""
        try:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name,
                allure.attachment_type.PNG
            )
        except Exception as e:
            logger.error(f"截图失败: {str(e)}")

    @allure.story("法条检索功能")
    @allure.title("测试法条检索基本流程")
    @allure.severity(allure.severity_level.NORMAL)
    def test_basic_statute_search(self, driver):
        """
        测试法条检索基本流程：
        1. 点击辅助阅卷
        2. 点击法条检索
        3. 输入搜索内容
        4. 点击搜索
        5. 预览法条
        6. 关闭预览
        7. 关闭搜索
        """
        try:
            with allure.step("执行法条检索基本流程"):
                self.statute_search.perform_statute_search("身份证")
                self.take_screenshot("基本流程完成")

        except Exception as e:
            logger.error(f"法条检索测试失败: {str(e)}")
            self.take_screenshot("基本流程失败")
            raise