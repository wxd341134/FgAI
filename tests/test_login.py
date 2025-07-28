import pytest
import allure
from pages.login_page import LoginPage
from utils.driver_manager import DriverManager
from utils.logger import Logger
# from common.driver_manager import DriverManager
from common.login_utils import LoginUtils

logger = Logger().get_logger()


@allure.epic("系统登录测试")
@allure.feature("登录与退出功能")
class TestLogin:
    """登录和退出登录测试类"""

    @allure.story("初始化测试环境")
    def setup_class(self):
        """测试类初始化"""
        logger.info("========== 开始执行登录和退出登录测试 ==========")
        allure.attach("初始化WebDriver和页面对象", "测试准备", allure.attachment_type.TEXT)

        # 获取driver实例
        driver_manager = DriverManager()
        self.driver = driver_manager.get_driver()
        self.driver.maximize_window()

        # 创建页面对象
        self.login_page = LoginPage(self.driver)

    @allure.story("清理测试环境")
    def teardown_class(self):
        """测试类清理"""
        logger.info("========== 登录和退出登录测试执行完成 ==========")
        allure.attach("清理资源并关闭浏览器", "测试清理", allure.attachment_type.TEXT)

        # 关闭浏览器
        try:
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()
                logger.info("已关闭浏览器")
        except Exception as e:
            logger.warning(f"关闭浏览器时出错: {str(e)}")

    @allure.story("登录系统并退出登录")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("测试用户登录系统后是否能成功退出登录")
    @pytest.mark.smoke
    def test_login_and_logout(self):
        """测试登录系统并退出登录"""
        try:
            allure.attach("开始测试登录并退出功能", "测试开始", allure.attachment_type.TEXT)

            # 使用LoginUtils执行完整的登录-退出流程
            LoginUtils.execute_login_logout_workflow(self.login_page)

            allure.attach("登录并退出测试成功完成", "测试结束", allure.attachment_type.TEXT)

        except Exception as e:
            logger.error(f"测试过程中出现错误: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="测试失败截图",
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(str(e), "错误详情", allure.attachment_type.TEXT)
            raise


if __name__ == "__main__":
    # 单独运行此测试时使用，生成allure报告
    pytest.main(["-v", "--alluredir=./allure-results", __file__])
