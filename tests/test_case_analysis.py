import pytest
import allure
from common.case_analysis_utils import CaseAnalysisUtils
from tests.base_test import BaseTest
from utils.logger import Logger

logger = Logger().get_logger()

@allure.epic("案件管理系统")
@allure.feature("案件分析功能")
class TestCaseAnalysis(BaseTest):
    """案件分析测试类"""

    @pytest.fixture(autouse=True)
    def setup_case_analysis(self, driver):
        """测试前后处理"""
        logger.info("开始测试前置操作...")
        try:
            self.case_analysis = CaseAnalysisUtils(driver)
            # # 进入案件分析页面
            # self.case_analysis.enter_case_analysis()
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

    @allure.story("证据状态切换")
    @allure.title("测试证据认同状态切换")
    def test_toggle_evidence_status(self, driver):
        # 进入案件分析页面
        self.case_analysis.enter_case_analysis()
        """测试证据认同状态的切换功能"""
        try:
            with allure.step("执行证据状态切换"):
                self.case_analysis.toggle_evidence_status()
                # self.take_screenshot("状态切换完成")

        except Exception as e:
            logger.error(f"证据状态切换测试失败: {str(e)}")
            # self.take_screenshot("状态切换失败")
            raise

    @allure.story("展开收起功能")
    @allure.title("测试展开收起操作")
    def test_expand_collapse(self, driver):
        """测试展开收起功能"""
        try:
            with allure.step("执行展开收起操作"):
                self.case_analysis.expand_collapse_operation()
        except Exception as e:
            logger.error(f"展开收起测试失败: {str(e)}")
            raise

    @allure.story("事实描述功能")
    @allure.title("测试完善事实描述")
    def test_complete_fact_description(self, driver):
        """测试完善事实描述功能"""
        try:
            with allure.step("执行完善事实描述"):
                self.case_analysis.complete_fact_description()
        except Exception as e:
            logger.error(f"完善事实描述测试失败: {str(e)}")
            raise

    @allure.story("庭审笔录功能")
    @allure.title("测试庭审笔录操作")
    def test_court_record(self):
        """测试庭审笔录功能"""
        # 进入案件分析页面
        self.case_analysis.enter_case_analysis()
        try:
            with allure.step("执行庭审笔录操作"):
                self.case_analysis.handle_court_record()
        except Exception as e:
            logger.error(f"庭审笔录测试失败: {str(e)}")
            raise

if __name__ == "__main__":
    pytest.main([
        "-v",
        "--alluredir=./allure-results",
        "--clean-alluredir"
    ])