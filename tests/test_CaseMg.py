import time
import pytest
import allure

from common.caseMg_utils import CaseMgUtils
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("案件管理")
@allure.feature("案件管理模块")
@pytest.mark.usefixtures("setup_class")  # ✅ 使用 conftest.py 中定义的类级 fixture,应用到整个类
class TestCaseManagement:
    """案件管理测试类，适配 fixture 驱动的初始化方式"""
    # driver: WebDriver  # 告诉 PyCharm，self.driver 是 WebDriver 类型

    @pytest.fixture(autouse=True)
    def setup_case(self):
        """
        测试用例级别的 setup/teardown
        自动使用 self.driver（由 setup_class 注入）
        """
        logger.info("2025-07-18 09:52:51 - wxd341134 - 开始测试前置操作")
        try:
            self.case_utils = CaseMgUtils(self.driver)  # ✅ 使用 self.driver 创建一个 CaseMgUtils 实例，并将当前的浏览器驱动传入，让它可以操作页面
            yield
            logger.info(" 测试后置操作完成")
        except Exception as e:
            logger.error(f" 测试前置/后置操作失败: {str(e)}")
            self.case_utils.take_screenshot("设置/清理失败截图")  # 调用 CommonUtils 的截图方法
            raise

    @allure.story("案件基本操作")
    @allure.title("案件增删改功能测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_crud(self):
        """测试案件的添加、编辑和删除功能"""
        try:
            case_name = "(2025)苏0105民初0001号"

            with allure.step(f"添加案件: {case_name}"):
                self.case_utils.add_case(case_name, case_name)
                self.case_utils.take_screenshot("案件添加成功")
                time.sleep(3)

            with allure.step(f"编辑案件: {case_name}"):
                self.case_utils.edit_case(case_name)
                self.case_utils.take_screenshot("案件编辑成功")
                time.sleep(3)

            with allure.step(f"删除案件: {case_name}"):
                self.case_utils.delete_case(case_name)
                self.case_utils.take_screenshot("案件删除成功")
                time.sleep(1)

            logger.info("案件操作测试完成")
            self.case_utils.take_screenshot("基本流程成功")
        except Exception as e:
            logger.error(f"测试执行失败: {str(e)}")
            self.case_utils.take_screenshot("基本流程失败")
            raise

