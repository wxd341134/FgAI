import time
import allure
from utils.logger import Logger

logger = Logger().get_logger()


class UserCenterUtils:
    """个人中心相关操作工具类"""

    @staticmethod
    def handle_report_statistics(page):
        """处理报表统计功能"""
        with allure.step("执行报表统计操作"):
            try:
                page.open_report_statistics()
                time.sleep(1)

                page.select_department_view()
                time.sleep(1)

                page.select_handler_view()
                time.sleep(1)

                page.click_query()
                time.sleep(2)

                page.click_export()
                time.sleep(3)

                logger.info("报表统计操作完成")
                return True
            except Exception as e:
                logger.error(f"报表统计操作失败: {str(e)}")
                return False

    @staticmethod
    def handle_font_download(page):
        """处理字体下载功能"""
        with allure.step("执行字体下载操作"):
            try:
                page.open_font_download()
                time.sleep(1)

                page.download_fangzheng_font()
                time.sleep(2)

                page.close_modal()
                time.sleep(1)

                logger.info("字体下载操作完成")
                return True
            except Exception as e:
                logger.error(f"字体下载操作失败: {str(e)}")
                return False

    @staticmethod
    def handle_password_change(page, old_pwd, new_pwd):
        """处理密码修改功能"""
        with allure.step("执行密码修改操作"):
            try:
                page.open_change_password()
                time.sleep(1)

                page.change_password(old_pwd, new_pwd, new_pwd)
                time.sleep(2)

                logger.info("密码修改操作完成")
                return True
            except Exception as e:
                logger.error(f"密码修改操作失败: {str(e)}")
                return False