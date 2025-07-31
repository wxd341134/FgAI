from datetime import datetime
import pytest
import allure
from utils.logger import Logger
from common.usercenter_utils import UserCenterUtils
from pages.usercenter_page import UserCenterPage

logger = Logger().get_logger()

CURRENT_TIME = "2025-07-28 07:50:34"
CURRENT_USER = "wxd341134"

@allure.epic("个人中心")
@allure.feature("个人中心功能")
@pytest.mark.usefixtures("setup_class")  # ✅ 使用 conftest.py 中定义的类级 fixture
class TestPersonalCenter:
    """个人中心功能测试类"""

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """
        测试用例级别的设置和清理
        """
        logger.info(f"{CURRENT_TIME} - {CURRENT_USER} - 开始测试前置操作...")
        try:
            # 初始化个人中心工具类
            self.user_center = UserCenterUtils(self.driver)
            logger.info(f"{CURRENT_TIME} - {CURRENT_USER} - 个人中心工具类初始化完成")

            # 执行测试用例
            yield

            logger.info(f"{CURRENT_TIME} - {CURRENT_USER} - 开始测试后置操作...")

        except Exception as e:
            logger.error(f"{CURRENT_TIME} - {CURRENT_USER} - 测试前置/后置操作失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "设置或清理失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.story("个人中心完整流程测试")
    @allure.title("测试报表统计、字体下载和密码修改功能")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_personal_center_workflow(self):
        """测试个人中心完整流程"""
        try:
            # 1. 报表统计
            with allure.step("执行报表统计功能测试"):
                assert self.user_center.handle_report_statistics(), "报表统计失败"
                logger.info(f"{CURRENT_TIME} - {CURRENT_USER} - 报表统计测试通过")

            # 2. 字体下载
            with allure.step("执行字体下载功能测试"):
                assert self.user_center.handle_font_download(), "字体下载失败"
                logger.info(f"{CURRENT_TIME} - {CURRENT_USER} - 字体下载测试通过")

            # 3. 修改密码
            with allure.step("执行密码修改功能测试"):
                assert self.user_center.handle_password_change(
                    "wxd341134@",
                    "wxd341134@"
                ), "密码修改失败"
                logger.info(f"{CURRENT_TIME} - {CURRENT_USER} - 密码修改测试通过")

        except AssertionError as ae:
            logger.error(f"{CURRENT_TIME} - {CURRENT_USER} - 断言失败: {str(ae)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "断言失败截图",
                allure.attachment_type.PNG
            )
            raise

        except Exception as e:
            logger.error(f"{CURRENT_TIME} - {CURRENT_USER} - 测试执行异常: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "异常失败截图",
                allure.attachment_type.PNG
            )
            raise


if __name__ == "__main__":
    pytest.main([
        "-v",
        "--alluredir=./allure-results",
        "test_usercenter.py"
    ])