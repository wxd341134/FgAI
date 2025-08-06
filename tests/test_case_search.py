import pytest
import allure
from common.case_search_utils import CaseSearchUtils
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("案件列表")
@allure.feature("案件查询模块")
@pytest.mark.usefixtures("setup_class")  # ✅ 使用 conftest.py 中定义的类级 fixture,应用到整个类
class TestCaseSearch:
    """案件查询测试类"""

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """
        测试用例级别的设置和清理
        使用基类的driver fixture
        """
        logger.info("开始测试前置操作...")
        try:
            # 初始化案件查询工具类
            self.case_search = CaseSearchUtils(self.driver)
            logger.info("案件查询工具类初始化完成")

            # 执行测试
            yield

            logger.info("测试后置操作完成")

        except Exception as e:
            logger.error(f"测试前置/后置操作失败: {str(e)}")
            self.case_search.take_screenshot("设置/清理失败截图")
            raise

    @allure.story("案件查询功能")
    @allure.title("测试案件查询条件组合")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_search(self):
        """测试案件查询功能"""
        try:
            logger.info("开始执行案件查询测试...")

            # 1. 按案件编号查询
            with allure.step("按案件编号查询"):
                assert self.case_search.search_by_case_number("(2024)鲁0502民初374号")
                logger.info("案件编号查询完成")

            # 2. 重置查询条件
            with allure.step("重置查询条件"):
                assert self.case_search.reset_search()
                logger.info("查询条件已重置")

            # 3. 按判决书状态查询
            with allure.step("按判决书状态查询"):
                assert self.case_search.search_by_judgment_status()
                logger.info("判决书状态查询完成")

            # 4. 重置查询条件
            with allure.step("重置查询条件"):
                assert self.case_search.reset_search()
                logger.info("查询条件已重置")

            # 5. 按承办人查询
            with allure.step("按承办人查询"):
                assert self.case_search.search_by_handler()
                logger.info("承办人查询完成")

            # 6. 最后重置
            with allure.step("最终重置查询条件"):
                assert self.case_search.reset_search()
                logger.info("最终重置完成")

            logger.info("案件查询测试执行完成")
            self.case_search.take_screenshot("基本流程成功")

        except AssertionError as ae:
            logger.error(f"wxd341134 - 断言失败: {str(ae)}")
            self.case_search.take_screenshot("断言失败截图")
            raise
        except Exception as e:
            logger.error(f"wxd341134 - 测试执行失败: {str(e)}")
            self.case_search.take_screenshot("基本流程失败")
            raise
