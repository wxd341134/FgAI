import os
import time
import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytesseract

from utils.driver_manager import DriverManager


class LoginPage:
    def __init__(self, config=None):
        # 默认配置
        self.config = {
            "url": "http://192.168.2.76:86/#/case/index",
            "username": "wxdfg",
            "password": "wxd341134@",
            "max_attempts": 5,
            "captcha_xpath": "//div[@class='ant-col ant-col-8']",
            "captcha_image_xpath": "//img[contains(@src, '/judge-ai/captcha?uu')]",
            "username_xpath": "//input[@placeholder='请输入账号']",
            "password_xpath": "//input[@placeholder='请输入密码']",
            "captcha_input_xpath": "//input[@placeholder='请输入验证码']",
            "login_button_xpath": "//button[@type='button']",
            "success_indicator_xpath": "//div[@id='success-indicator']",
            "error_indicator_xpath": "//div[contains(text(), '验证码错误')]"
        }

        # 如果传入了自定义配置，则合并更新
        if config:
            self.config.update(config)

        # 初始化 WebDriver
        driver_manager = DriverManager()
        self.driver = driver_manager.get_driver()
        self.driver.maximize_window()

        # 添加 wait 属性
        self.wait = WebDriverWait(self.driver, 15)


        # 调试用：是否保存验证码图片
        self.save_captcha = True
        self.captcha_dir = "captchas"
        if not os.path.exists(self.captcha_dir):
            os.makedirs(self.captcha_dir)

    def open_login_page(self):
        """打开登录页面"""
        self.driver.get(self.config['url'])

    def preprocess_captcha_image(self, image):
        """对验证码图片进行预处理以提高识别准确率"""
        try:
            # 转为灰度图
            image = image.convert('L')

            # 增强对比度
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(2)

            # 二值化处理
            image = image.point(lambda x: 0 if x < 128 else 255, '1')

            return image
        except Exception as e:
            print(f"图片预处理出错：{e}")
            return image

    def recognize_captcha(self, attempt=1):
        """
        刷新并识别网页上的验证码图片

        参数:
            attempt (int): 当前尝试次数（用于命名保存的图片）

        返回:
            str: 识别出的4位数字验证码；如果失败则返回空字符串
        """
        try:
            # 点击验证码图标刷新验证码
            captcha_icon = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, self.config['captcha_xpath']))
            )
            captcha_icon.click()
            time.sleep(2)  # 等待验证码加载

            # 定位验证码图片元素
            captcha_image_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, self.config['captcha_image_xpath']))
            )

            # 获取验证码图片的src属性值
            captcha_image_url = captcha_image_element.get_attribute('src')

            # 下载验证码图片
            response = requests.get(captcha_image_url)
            image_data = response.content
            image = Image.open(BytesIO(image_data))

            # 【只保存原始图片】
            if self.save_captcha:
                original_path = os.path.join(self.captcha_dir, f"original_captcha_{attempt}.png")
                image.save(original_path)
                print(f"已保存原始验证码图片：{original_path}")

            # 图像预处理（不保存处理后的图片）
            processed_image = self.preprocess_captcha_image(image)

            # 使用OCR识别验证码（只识别数字）
            captcha_text = pytesseract.image_to_string(processed_image, config='--psm 7 digits')
            captcha_text = captcha_text.strip()  # 去除前后空格

            # 验证是否为4位数字
            if len(captcha_text) != 4 or not captcha_text.isdigit():
                print("验证码识别失败或格式不正确")
                return ""

            print(f"识别到的验证码: {captcha_text}")
            return captcha_text

        except Exception as e:
            print(f"验证码处理过程中发生错误: {e}")
            return ""
    def login_with_captcha_and_retry(self, max_attempts=None):
        """
        输入用户名、密码，并自动识别验证码进行登录。
        如果验证码错误，会自动刷新并重试，直到成功或达到最大尝试次数。

        参数:
            max_attempts (int): 最大尝试次数，默认使用配置中的值

        返回:
            bool: 登录是否成功
        """
        max_attempts = max_attempts or self.config['max_attempts']
        attempt = 0
        input_filled = False  # 标记是否已填写用户名密码

        while attempt < max_attempts:
            attempt += 1
            print(f"第 {attempt} 次尝试登录...")

            try:
                if not input_filled:
                    # 第一次输入用户名和密码
                    user_input = WebDriverWait(self.driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, self.config['username_xpath']))
                    )
                    user_input.clear()
                    user_input.send_keys(self.config['username'])

                    pass_input = self.driver.find_element(By.XPATH, self.config['password_xpath'])
                    pass_input.clear()
                    pass_input.send_keys(self.config['password'])

                    input_filled = True

                # 识别验证码
                captcha_code = self.recognize_captcha(attempt=attempt)
                if not captcha_code:
                    print("未能成功识别验证码")
                    continue

                # 输入验证码
                captcha_input = self.driver.find_element(By.XPATH, self.config['captcha_input_xpath'])
                captcha_input.clear()
                captcha_input.send_keys(captcha_code)

                # 提交登录表单
                login_button = self.driver.find_element(By.XPATH, self.config['login_button_xpath'])
                login_button.click()

                time.sleep(3)  # 等待跳转

                # 检查是否登录成功
                success_indicator = self.driver.find_elements(By.XPATH, self.config['success_indicator_xpath'])
                if success_indicator:
                    print("✅ 登录成功！")
                    return True

                # 检查是否有“验证码错误”提示
                captcha_error = self.driver.find_elements(By.XPATH, self.config['error_indicator_xpath'])
                if captcha_error:
                    print("❌ 验证码错误，刷新后重试...")
                    continue

                # 其他错误情况
                print("⚠️ 登录失败，原因未知。可能不是验证码问题。")
                break

            except (TimeoutException, NoSuchElementException) as e:
                print(f"🚨 页面元素未找到或超时: {e}")
                break

        print(f"已尝试 {max_attempts} 次，登录未成功。")
        return False

    def quit(self):
        """关闭浏览器"""
        self.driver.quit()


# ========================
# 示例调用方式：
# ========================
if __name__ == "__main__":
    login_page = LoginPage()
    login_page.open_login_page()

    login_success = login_page.login_with_captcha_and_retry()

    if login_success:
        print("执行后续操作...")
    else:
        print("登录失败，请检查网络或账户信息。")

    login_page.quit()