import time
from datetime import datetime

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.usercenter_page import UserCenterPage
from utils.Common_utils import CommonUtils
from utils.logger import Logger


logger = Logger().get_logger()


class UserCenterUtils(CommonUtils):
    """个人中心相关操作工具类"""

    # def __init__(self, driver):
    #     """初始化工具类"""
    #     self.driver = driver
    #     self.wait = WebDriverWait(driver, 10)
    #     self.current_time = "2025-07-28 07:58:22"
    #     self.current_user = "wxd341134"

    def __init__(self, driver):
        super().__init__(driver)  # ✅ 调用父类初始化
        self.current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_user = "wxd341134"

    @allure.step("执行报表统计操作")
    def handle_report_statistics(self):
        """处理报表统计相关操作"""
        try:
            with allure.step("打开报表统计界面"):
                # 点击用户菜单
                self.click_element(
                    UserCenterPage.USER_MENU,
                    "用户菜单"
                )
                time.sleep(1)

                # 点击报表统计选项
                self.click_element(
                    UserCenterPage.REPORT_STATS_OPTION,
                    "报表统计选项"
                )
                time.sleep(1)

            with allure.step("设置统计方式"):
                # 点击下拉框
                self.click_element(
                    UserCenterPage.DEPARTMENT_OPTION,
                    "承办部门选项"
                )

                # 选择按承办人
                self.click_element(
                    UserCenterPage.HANDLER_OPTION,
                    "按承办人"
                )

            with allure.step("设置承办人"):
                # 点击下拉框
                self.click_element(
                    UserCenterPage.HANDLER_DROPDOWN,
                    "承办部门选项"
                )

                # 选择承办人
                self.click_element(
                    UserCenterPage.HANDLER_OPTION_WXDFG,
                    "wxdfg"
                )

            with allure.step("选择时间区间"):
                # 点击开始时间
                self.click_element(
                    UserCenterPage.START_DATE_INPUT,
                    "开始时间"
                )

                # 选择时间
                self.click_element(
                    UserCenterPage.SELECT_TIME_LINK,
                    "选择时间"
                )
                time.sleep(1)

                # 选择开始时间：2025-07-01 00:00:00
                self.click_element(
                    UserCenterPage.CALENDAR_START_INPUT,
                    "2025-07-01 00:00:00"
                )
                # 使用input_text方法输入时间
                self.input_text(
                    UserCenterPage.CALENDAR_START_INPUT,
                    "2025-07-01 00:00:00",
                    "开始时间输入框",
                )
                logger.info("已输入开始时间: 2025-07-01 00:00:00")
                time.sleep(1)

                # 选择结束时间：2025-07-01 00:00:00
                self.click_element(
                    UserCenterPage.CALENDAR_END_INPUT,
                    "2025-07-31 23:59:59"
                )
                # 使用input_text方法输入时间
                self.input_text(
                    UserCenterPage.CALENDAR_END_INPUT,
                    "2025-07-31 23:59:59",
                    "结束时间输入框"
                )
                logger.info("已输入开始时间: 2025-07-01 00:00:00")
                time.sleep(1)

                # 点击确定选择的时间
                self.click_element(
                    UserCenterPage.CONFIRM_TIME_BUTTON,
                    "确定"
                )



            with allure.step("执行报表操作"):
                # 点击查询
                self.click_element(
                    UserCenterPage.QUERY_BUTTON,
                    "查询按钮"
                )
                time.sleep(2)

                # 点击导出
                self.click_element(
                    UserCenterPage.EXPORT_BUTTON,
                    "导出按钮"
                )
                time.sleep(2)

                # 点击重置
                self.click_element(
                    UserCenterPage.RESET_BUTTON,
                    "重置按钮"
                )
                time.sleep(1)

            logger.info(f"{self.current_time} - {self.current_user} - 报表统计操作完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 报表统计操作失败: {str(e)}")
            return False

    @allure.step("执行字体下载操作")
    def handle_font_download(self):
        """处理字体下载相关操作"""
        try:
            with allure.step("打开字体下载界面"):
                # 点击返回
                self.click_element(
                    UserCenterPage.USER_BACK,
                    "返回按钮"
                )



                # 点击用户菜单
                # self.click_element(
                #     UserCenterPage.USER_MENU,
                #     "用户菜单"
                # )


                # 点击字体下载选项
                self.click_element(
                    UserCenterPage.FONT_DOWNLOAD_OPTION,
                    "字体下载选项"
                )

            with allure.step("下载字体"):
                # 下载方正字体
                self.click_element(
                    UserCenterPage.FANGZHENG_FONT_BUTTON,
                    "方正字体下载按钮"
                )
                time.sleep(1)

                # 关闭模态框
                self.click_element(
                    UserCenterPage.CLOSE_MODAL_BUTTON,
                    "关闭按钮"
                )

            logger.info(f"{self.current_time} - {self.current_user} - 字体下载操作完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 字体下载操作失败: {str(e)}")
            return False

    @allure.step("执行密码修改操作")
    def handle_password_change(self, old_pwd, new_pwd):
        """
        处理密码修改相关操作
        Args:
            old_pwd: 原密码
            new_pwd: 新密码
        """
        try:
            with allure.step("打开修改密码界面"):
                # 点击用户菜单
                self.click_element(
                    UserCenterPage.USER_MENU,
                    "用户菜单"
                )

                # 点击修改密码选项
                self.click_element(
                    UserCenterPage.CHANGE_PASSWORD_OPTION,
                    "修改密码选项"
                )

            with allure.step("输入密码信息"):
                # 输入原密码
                self.input_text(
                    UserCenterPage.OLD_PASSWORD_INPUT,
                    old_pwd,
                    "原密码输入框"
                )

                # 输入新密码
                self.input_text(
                    UserCenterPage.NEW_PASSWORD_INPUT,
                    new_pwd,
                    "新密码输入框"
                )

                # 确认新密码
                self.input_text(
                    UserCenterPage.CONFIRM_PASSWORD_INPUT,
                    new_pwd,
                    "确认密码输入框"
                )

            with allure.step("提交密码修改"):
                # 点击确认按钮
                self.click_element(
                    UserCenterPage.CONFIRM_BUTTON,
                    "确认按钮"
                )

            logger.info(f"{self.current_time} - {self.current_user} - 密码修改操作完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 密码修改操作失败: {str(e)}")
            return False