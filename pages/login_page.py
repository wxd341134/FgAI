from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.core.manager import DriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from utils.logger import Logger
import allure
import time
import tkinter as tk
from tkinter import simpledialog

# from common.driver_manager import DriverManager  # 导入driver管理类

logger = Logger().get_logger()


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # 页面元素定位器
        self.username_input = (By.XPATH, "//input[@placeholder='请输入账号']")
        self.password_input = (By.XPATH, "//input[@placeholder='请输入密码']")
        self.verify_code_input = (By.XPATH, "//input[@placeholder='请输入验证码']")
        self.login_button = (By.XPATH, "//button[@type='button']")
        self.user_info = (By.XPATH, "//div[contains(@class, 'user-info')]")

        # 添加退出登录相关元素定位器
        self.user_dropdown_menu = (
        By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']")
        self.logout_option = (By.XPATH, "//li[contains(text(),'退出')]")
        self.login_page_indicator = (By.XPATH, "//input[@placeholder='请输入账号']")  # 用于验证是否退出到登录页面

    def handle_error(self, error_msg, take_screenshot=True):
        """统一的错误处理方法"""
        logger.error(error_msg)
        if take_screenshot:
            try:
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name="error_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except:
                logger.error("无法截图")
        # 关闭浏览器
        try:
            DriverManager.quit_driver()
        except Exception as e:
            logger.error(f"关闭浏览器失败: {str(e)}")
        raise Exception(error_msg)

    def get_verify_code_from_user(self):
        """弹出窗口获取验证码"""
        try:
            root = tk.Tk()
            root.withdraw()  # 隐藏主窗口
            root.attributes('-topmost', True)  # 窗口置顶

            # 创建验证码输入弹窗
            verify_code = simpledialog.askstring(
                "验证码输入",
                "请输入验证码：",
                parent=root
            )

            root.destroy()
            return verify_code

        except Exception as e:
            self.handle_error(f"验证码输入窗口创建失败: {str(e)}")

    def wait_for_verify_code(self, timeout=60):
        """等待并处理验证码输入"""
        try:
            # 找到验证码输入框
            verify_code_element = self.wait.until(
                EC.presence_of_element_located(self.verify_code_input)
            )

            # 高亮验证码输入框
            self.driver.execute_script("""
                arguments[0].style.border = '2px solid red';
                arguments[0].style.backgroundColor = '#fff3f3';
            """, verify_code_element)

            logger.info("=" * 50)
            logger.info("请在弹出窗口中输入验证码")
            logger.info("=" * 50)

            # 获取验证码
            verify_code = self.get_verify_code_from_user()

            if verify_code:
                # 清空输入框
                verify_code_element.clear()
                time.sleep(0.5)

                # 输入验证码
                verify_code_element.send_keys(verify_code)
                logger.info("验证码已自动填入")

                # 恢复输入框样式
                self.driver.execute_script("""
                    arguments[0].style.border = '';
                    arguments[0].style.backgroundColor = '';
                """, verify_code_element)

                time.sleep(1)
                return True
            else:
                self.handle_error("验证码输入为空")
                return False

        except Exception as e:
            self.handle_error(f"验证码处理失败: {str(e)}")
            return False

    def login(self, username="wxdfg", password="wxd341134@"):
        """执行登录操作"""
        try:
            # 打开登录页面
            self.open_login_page()

            # 输入用户名
            logger.info(f"开始输入用户名: {username}")
            try:
                username_element = self.wait.until(
                    EC.element_to_be_clickable(self.username_input)
                )
                username_element.clear()
                username_element.send_keys(username)
                logger.info("用户名输入完成")
            except Exception as e:
                self.handle_error(f"用户名输入失败: {str(e)}")

            # 输入密码
            logger.info("开始输入密码")
            try:
                password_element = self.wait.until(
                    EC.element_to_be_clickable(self.password_input)
                )
                password_element.clear()
                password_element.send_keys(password)
                logger.info("密码输入完成")
            except Exception as e:
                self.handle_error(f"密码输入失败: {str(e)}")

            # 处理验证码
            if not self.wait_for_verify_code():
                self.handle_error("验证码处理失败")

            # 点击登录按钮
            logger.info("尝试点击登录按钮")
            try:
                login_button = self.wait.until(
                    EC.element_to_be_clickable(self.login_button)
                )

                try:
                    login_button.click()
                except:
                    self.driver.execute_script("arguments[0].click();", login_button)

                logger.info("登录按钮点击成功")
            except Exception as e:
                self.handle_error(f"登录按钮点击失败: {str(e)}")

            # 登录成功后直接返回
            logger.info("登录成功")
            return True

        except Exception as e:
            self.handle_error(f"登录过程失败: {str(e)}")
            return False

    def open_login_page(self):
        """打开登录页面"""
        try:
            self.driver.get("http://192.168.2.176:86/#/case/index")
            time.sleep(2)
            logger.info("成功打开登录页面")
        except Exception as e:
            self.handle_error(f"打开登录页面失败: {str(e)}")

    def is_logged_in(self):
        """检查是否已登录"""
        try:
            return self.wait.until(
                EC.presence_of_element_located(self.user_info)
            ).is_displayed()
        except:
            return False

    def open(self):
        """打开登录页面"""
        try:
            # 假设登录页面的URL
            self.driver.get("http://your-application-url/login")
            logger.info("成功打开登录页面")
            return True
        except Exception as e:
            logger.error(f"打开登录页面失败: {str(e)}")
            return False

    def click_user_dropdown(self):
        """点击用户下拉菜单"""
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(self.user_dropdown_menu))
            dropdown.click()
            logger.info("成功点击用户下拉菜单")
            return True
        except Exception as e:
            logger.error(f"点击用户下拉菜单失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="user_dropdown_click_failed",
                attachment_type=allure.attachment_type.PNG
            )
            return False

    def click_logout_option(self):
        """点击退出选项"""
        try:
            logout = self.wait.until(EC.element_to_be_clickable(self.logout_option))
            logout.click()
            logger.info("成功点击退出选项")
            return True
        except Exception as e:
            logger.error(f"点击退出选项失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="logout_click_failed",
                attachment_type=allure.attachment_type.PNG
            )
            return False

    def is_on_login_page(self):
        """验证是否在登录页面"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.login_page_indicator))
            logger.info("验证成功：当前在登录页面")
            return True
        except Exception as e:
            logger.error(f"验证失败：当前不在登录页面, {str(e)}")
            return False