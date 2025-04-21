import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from utils.driver_manager import DriverManager
from utils.logger import Logger
import allure

logger = Logger().get_logger()


class BaseTest:
    """测试基类，提供基础设置和清理功能"""

    @classmethod
    def setup_class(cls):
        """类级别的初始化"""
        logger.info("初始化测试类...")
        cls.driver = DriverManager.get_driver()  # 使用DriverManager获取driver实例
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.login_page = LoginPage(cls.driver)

        try:
            # 执行登录
            cls.login_page.login("wxdfg", "wxd341134@")
            logger.info("登录成功")
        except Exception as e:
            logger.error(f"登录失败: {str(e)}")
            if hasattr(cls, 'driver'):
                allure.attach(
                    cls.driver.get_screenshot_as_png(),
                    "登录失败截图",
                    allure.attachment_type.PNG
                )
            raise

    @classmethod
    def teardown_class(cls):
        """类级别的清理"""
        logger.info("清理测试类...")
        if hasattr(cls, 'driver'):
            try:
                cls.driver.quit()
                logger.info("浏览器已关闭")
            except Exception as e:
                logger.error(f"关闭浏览器失败: {str(e)}")

    @pytest.fixture(scope="function")
    def driver(self):
        """提供driver实例的fixture"""
        return self.driver
