import pytest
import allure
from tests.base_test import BaseTest
from pages.usercenter_page import UserCenterPage
from common.usercenter_utils import UserCenterUtils
from utils.logger import Logger

logger = Logger().get_logger()


@allure.feature("个人中心")
class TestPersonalCenter(BaseTest):
    """个人中心功能测试类"""

    @allure.story("报表统计、字体下载、修改密码")
    def test_personal_center_workflow(self):
        """测试个人中心完整流程"""
        try:
            user_center_page = UserCenterPage(self.driver)

            # 1. 报表统计
            with allure.step("测试报表统计功能"):
                assert UserCenterUtils.handle_report_statistics(user_center_page)

            # 2. 字体下载
            with allure.step("测试字体下载功能"):
                assert UserCenterUtils.handle_font_download(user_center_page)

            # 3. 修改密码
            with allure.step("测试修改密码功能"):
                assert UserCenterUtils.handle_password_change(
                    user_center_page,
                    "wxd341134@",
                    "wxd341134@"
                )

        except Exception as e:
            logger.error(f"个人中心测试流程失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise



if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=./allure-results", "test_usercenter.py"])