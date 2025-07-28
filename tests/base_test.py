import pytest
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from utils.driver_manager import DriverManager
from utils.logger import Logger
import allure
import time

logger = Logger().get_logger()


class BaseTest:
    """测试基类，提供基础设置和清理功能"""

    @classmethod
    def setup_class(cls):
        """类级别的初始化"""
        logger.info(" 初始化测试类...")
        try:
            # 初始化driver
            cls.driver = DriverManager.get_driver()
            cls.wait = WebDriverWait(cls.driver, 10)
            cls.login_page = LoginPage(cls.driver)

            # 执行登录
            login_success = cls.login_page.login("wxdfg", "wxd341134@")
            if not login_success:
                raise Exception("登录失败")

            logger.info("2025-07-22 09:48:14 - wxd341134 - 登录成功")
            time.sleep(2)  # 等待页面加载

        except Exception as e:
            logger.error(f"2025-07-22 09:48:14 - wxd341134 - 初始化失败: {str(e)}")
            if hasattr(cls, 'driver'):
                allure.attach(
                    cls.driver.get_screenshot_as_png(),
                    "初始化失败截图",
                    allure.attachment_type.PNG
                )
                cls.driver.quit()
            raise

    @classmethod
    def teardown_class(cls):
        """类级别的清理"""
        logger.info("2025-07-22 09:48:14 - wxd341134 - 开始清理测试环境...")
        if hasattr(cls, 'driver'):
            try:
                cls.driver.quit()
                logger.info("2025-07-22 09:48:14 - wxd341134 - 浏览器已关闭")
            except Exception as e:
                logger.error(f"2025-07-22 09:48:14 - wxd341134 - 关闭浏览器失败: {str(e)}")

    @pytest.fixture(scope="function")
    def driver(self):
        """提供driver实例的fixture"""
        return self.driver