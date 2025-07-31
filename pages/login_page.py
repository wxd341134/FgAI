import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
from io import StringIO
from contextlib import redirect_stdout
import ddddocr
import time

import glob
from utils.logger import Logger



logger = Logger().get_logger()


class LoginPage:
    """登录页面类"""

    # 页面元素
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='请输入账号']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='请输入密码']")
    CAPTCHA_INPUT = (By.XPATH, "//input[@placeholder='请输入验证码']")
    CAPTCHA_IMG = (By.XPATH, '//img[contains(@src, "/judge-ai/captcha")]')
    LOGIN_BUTTON = (By.XPATH, "//button[@type='button']")

    # 添加退出登录相关元素定位器
    user_dropdown_menu = (By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']")
    logout_option = (By.XPATH, "//li[contains(text(),'退出')]")
    login_page_indicator = (By.XPATH, "//input[@placeholder='请输入账号']")  # 用于验证是否退出到登录页面

    # 配置参数
    CAPTCHA_SAVE_DIR = r"E:\AutoTest\FgAIHelp\tests\captchas"
    MAX_CAPTCHA_FILES = 4
    LOGIN_URL = "http://192.168.2.76:86/#/case/index"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.current_time = "2025-07-22 09:48:14"
        self.current_user = "wxd341134"

    def ensure_captcha_dir(self):
        """确保验证码保存目录存在并清理旧文件"""
        try:
            # 创建目录
            os.makedirs(self.CAPTCHA_SAVE_DIR, exist_ok=True)

            # 获取并排序验证码文件
            captcha_files = sorted(
                glob.glob(os.path.join(self.CAPTCHA_SAVE_DIR, "captcha_*.png")),
                key=os.path.getmtime,
                reverse=True
            )

            # 删除超出数量的旧文件
            for old_file in captcha_files[self.MAX_CAPTCHA_FILES:]:
                try:
                    os.remove(old_file)
                    logger.info(f"{self.current_time} - {self.current_user} - 清理旧验证码文件: {old_file}")
                except Exception as e:
                    logger.error(f"{self.current_time} - {self.current_user} - 清理验证码文件失败: {str(e)}")

            return self.CAPTCHA_SAVE_DIR
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 验证码目录操作失败: {str(e)}")
            raise

    def recognize_captcha(self, captcha_element):
        """识别验证码"""
        try:


            # 确保目录存在
            captcha_dir = self.ensure_captcha_dir()

            # 保存验证码图片
            timestamp = int(time.time())
            captcha_path = os.path.join(captcha_dir, f"captcha_{timestamp}.png")
            captcha_element.screenshot(captcha_path)
            logger.info(f"{self.current_time} - {self.current_user} - 验证码已保存: {captcha_path}")

            # 🔥 关键：使用 redirect_stdout 屏蔽 ddddocr 初始化时的 print
            with redirect_stdout(StringIO()):
                ocr = ddddocr.DdddOcr()

            # 识别验证码
            # ocr = ddddocr.DdddOcr()
            with open(captcha_path, 'rb') as f:
                img_bytes = f.read()
            result = ocr.classification(img_bytes)
            logger.info(f"{self.current_time} - {self.current_user} - 验证码识别结果: {result}")
            return result
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 验证码识别失败: {str(e)}")
            raise

    def login(self, username, password, max_retry=10):
        """登录方法"""
        try:
            logger.info(f"{self.current_time} - {self.current_user} - 开始登录流程")

            # 打开登录页面
            self.driver.get(self.LOGIN_URL)
            logger.info(f"{self.current_time} - {self.current_user} - 当前页面: {self.driver.title}")

            # 输入用户名和密码
            self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT)).send_keys(username)
            self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
            time.sleep(1)

            # 验证码识别和登录尝试
            retry_count = 0
            while retry_count < max_retry:
                try:
                    # 获取验证码图片
                    captcha_element = self.wait.until(
                        EC.presence_of_element_located(self.CAPTCHA_IMG)
                    )

                    # 识别验证码
                    captcha_text = self.recognize_captcha(captcha_element)
                    logger.info(
                        f"{self.current_time} - {self.current_user} - 第 {retry_count + 1} 次尝试验证码: {captcha_text}")

                    # 输入验证码
                    captcha_input = self.driver.find_element(*self.CAPTCHA_INPUT)
                    captcha_input.clear()
                    captcha_input.send_keys(captcha_text)

                    # 点击登录
                    self.driver.find_element(*self.LOGIN_BUTTON).click()
                    time.sleep(2)

                    # 验证登录结果
                    if "login" not in self.driver.current_url.lower():
                        logger.info(f"{self.current_time} - {self.current_user} - 登录成功")
                        return True

                    retry_count += 1
                    logger.warning(
                        f"{self.current_time} - {self.current_user} - 验证码错误，准备第 {retry_count + 1} 次尝试")
                    time.sleep(1)

                except Exception as e:
                    retry_count += 1
                    logger.error(f"{self.current_time} - {self.current_user} - 登录尝试 {retry_count} 失败: {str(e)}")
                    if retry_count >= max_retry:
                        raise

            logger.error(f"{self.current_time} - {self.current_user} - 登录失败，已达到最大重试次数: {max_retry}")
            return False

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 登录过程异常: {str(e)}")
            raise

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