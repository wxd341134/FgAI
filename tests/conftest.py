import pytest
from utils.driver_manager import DriverManager
from pages.login_page import LoginPage
from datetime import datetime
from utils.logger import Logger
import allure

logger = Logger().get_logger()

@pytest.fixture(scope="class")
def setup_class(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = "wxd341134"

    logger.info(f"{current_time} - {user} - 开始类级初始化")

    driver = None
    try:
        driver = DriverManager.get_driver()
        login_page = LoginPage(driver)

        # 登录
        login_success = login_page.login("wxdfg", "wxd341134@")
        if not login_success:
            raise Exception("登录失败")

        logger.info(f"{current_time} - {user} - 登录成功")

        # 将 driver 注入到测试类中
        request.cls.driver = driver
        request.cls.login_page = login_page

        # 执行测试类中的所有测试方法
        yield

    except Exception as e:
        error_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.error(f"{error_time} - {user} - 初始化失败: {str(e)}")
        if driver is not None:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="初始化失败截图",
                attachment_type=allure.attachment_type.PNG
            )
        raise

    finally:
        # 清理操作
        cleanup_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"{cleanup_time} - {user} - 开始清理测试环境...")
        if driver is not None:
            try:
                driver.quit()
                logger.info(f"{cleanup_time} - {user} - 浏览器已关闭")
            except Exception as e:
                logger.error(f"{cleanup_time} - {user} - 关闭浏览器失败: {str(e)}")