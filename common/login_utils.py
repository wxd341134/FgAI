import time
import allure
from utils.logger import Logger

logger = Logger().get_logger()


class LoginUtils:
    """登录相关工具类"""

    @staticmethod
    @allure.step("执行登录操作")
    def perform_login(login_page, username="wxdfg", password="wxd341134@"):
        """执行登录操作并记录到报告中"""
        try:
            logger.info("开始执行登录")
            login_page.login(username=username, password=password)
            time.sleep(3)

            # 截图记录登录成功状态
            allure.attach(
                login_page.driver.get_screenshot_as_png(),
                name="登录完成",
                attachment_type=allure.attachment_type.PNG
            )
            logger.info("登录操作完成")
            return True
        except Exception as e:
            logger.error(f"登录操作失败: {str(e)}")
            allure.attach(
                login_page.driver.get_screenshot_as_png(),
                name="登录失败",
                attachment_type=allure.attachment_type.PNG
            )
            raise

    @staticmethod
    @allure.step("执行退出登录操作")
    def perform_logout(login_page):
        """执行退出登录操作并记录到报告中"""
        try:
            # 点击用户下拉菜单
            logger.info("点击用户下拉菜单")
            login_page.click_user_dropdown()
            time.sleep(1)

            # 截图记录下拉菜单状态
            allure.attach(
                login_page.driver.get_screenshot_as_png(),
                name="用户菜单展开",
                attachment_type=allure.attachment_type.PNG
            )

            # 点击退出选项
            logger.info("点击退出选项")
            login_page.click_logout_option()
            time.sleep(2)

            # 截图记录退出后状态
            allure.attach(
                login_page.driver.get_screenshot_as_png(),
                name="退出完成",
                attachment_type=allure.attachment_type.PNG
            )

            logger.info("退出登录操作完成")
            return True
        except Exception as e:
            logger.error(f"退出登录操作失败: {str(e)}")
            allure.attach(
                login_page.driver.get_screenshot_as_png(),
                name="退出失败",
                attachment_type=allure.attachment_type.PNG
            )
            raise

    @staticmethod
    @allure.step("验证退出登录状态")
    def verify_logout_success(login_page):
        """验证是否成功退出到登录页面"""
        try:
            logger.info("验证是否退出到登录页面")
            result = login_page.is_on_login_page()

            if result:
                logger.info("验证成功：已退出到登录页面")
                allure.attach("已成功退出到登录页面", "验证结果", allure.attachment_type.TEXT)
            else:
                logger.error("验证失败：未退出到登录页面")
                allure.attach("未能退出到登录页面", "验证结果", allure.attachment_type.TEXT)
                allure.attach(
                    login_page.driver.get_screenshot_as_png(),
                    name="退出验证失败",
                    attachment_type=allure.attachment_type.PNG
                )

            assert result, "验证失败：未退出到登录页面"
            return result
        except Exception as e:
            logger.error(f"验证退出状态失败: {str(e)}")
            allure.attach(
                login_page.driver.get_screenshot_as_png(),
                name="验证失败",
                attachment_type=allure.attachment_type.PNG
            )
            raise

    @staticmethod
    @allure.step("完整登录退出流程")
    def execute_login_logout_workflow(login_page, username="wxdfg", password="wxd341134@"):
        """执行完整的登录-退出流程"""
        try:
            # 1. 执行登录
            LoginUtils.perform_login(login_page, username, password)

            # 2. 执行退出登录
            LoginUtils.perform_logout(login_page)

            # 3. 验证退出状态
            LoginUtils.verify_logout_success(login_page)

            logger.info("登录-退出流程执行完成")
            return True
        except Exception as e:
            logger.error(f"登录-退出流程执行失败: {str(e)}")
            raise