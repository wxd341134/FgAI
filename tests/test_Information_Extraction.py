import pytest
import allure
from utils.logger import Logger
from common.Information_Extraction_utils import InformationExtractionUtils

logger = Logger().get_logger()

@allure.epic("要素提取")
@allure.feature("要素提取功能测试")
@pytest.mark.usefixtures("setup_class")
class TestInformationExtraction:
    """要素提取功能测试类"""

    @pytest.fixture(autouse=True)
    def setup_test(self):
        """
        测试用例级别的设置和清理
        """
        logger.info("开始测试前置操作...")
        try:
            # 初始化要素提取工具类
            self.info_extraction = InformationExtractionUtils(self.driver)
            logger.info("要素提取工具类初始化完成")

            yield

            logger.info("测试后置操作完成")

        except Exception as e:
            logger.error(f"测试前置/后置操作失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "设置或清理失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.story("要素提取基本功能")
    @allure.title("测试要素提取基本操作")
    def test_basic_operations(self):
        """测试要素提取基本操作"""
        try:
            assert self.info_extraction.handle_basic_operations(), "要素提取基本操作失败"
        except Exception as e:
            logger.error(f"要素提取基本功能测试失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise



    @allure.story("视图操作功能")
    @allure.title("测试视图操作")
    def test_view_operations(self):
        """测试视图操作功能"""
        try:
            assert self.info_extraction.handle_view_operations(), "视图操作失败"
        except Exception as e:
            logger.error(f"视图操作测试失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.story("OCR功能")
    @allure.title("测试OCR操作")
    def test_ocr_operations(self):
        """测试OCR相关功能"""
        try:
            assert self.info_extraction.handle_ocr_operations(), "OCR操作失败"
        except Exception as e:
            logger.error(f"OCR功能测试失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.story("要素表功能")
    @allure.title("测试要素表操作")
    def test_table_operations(self):
        """测试要素表相关功能"""
        try:
            assert self.info_extraction.handle_table_operations(), "要素表操作失败"
        except Exception as e:
            logger.error(f"要素表功能测试失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise

if __name__ == "__main__":
    pytest.main([
        "-v",
        "--alluredir=./allure-results",
        "test_Information_Extraction.py"
    ])