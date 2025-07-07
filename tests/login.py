from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


def initialize_driver():
    try:
        chrome_driver_path = '/chromedriver-win64/chromedriver.exe'  # 使用双反斜杠
        print(f"ChromeDriver path: {chrome_driver_path}")  # 打印路径以确认
        service = Service(chrome_driver_path)
        print("Service created.")  # 打印日志以确认 Service 对象创建
        driver = webdriver.Chrome(service=service)
        print("WebDriver initialized.")  # 打印日志以确认 WebDriver 对象创建
        driver.maximize_window()
        print("Window maximized.")  # 打印日志以确认窗口最大化
        return driver
    except Exception as e:
        print(f"An error occurred: {e}")  # 打印详细错误信息
        raise


def login(driver, username, password):
    try:
        driver.get("http://192.168.2.76:86/#/case/index")
        print(driver.title)

        wait = WebDriverWait(driver, 10)

        # Login process
        username_field = driver.find_element(By.XPATH, "//input[@placeholder='请输入账号']")
        username_field.send_keys(username)
        time.sleep(1)

        password_field = driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']")
        password_field.send_keys(password)
        time.sleep(1)

        captcha_element = driver.find_element(By.XPATH, '//img[contains(@src, "/judge-ai/captcha")]')
        print("请查看页面上的验证码，并在接下来的输入框中输入验证码：")
        captcha_text = input("请输入验证码: ")

        input_element = driver.find_element(By.XPATH, "//input[@placeholder='请输入验证码']")
        input_element.clear()
        input_element.send_keys(captcha_text)

        login_button = driver.find_element(By.XPATH, "//button[@type='button']")
        login_button.click()
        time.sleep(2)

        return driver, wait
    except Exception as e:
        print(f"Login failed: {e}")
        driver.quit()
        return None, None

if __name__ == "__main__":
    old_username = "wxdfg"
    old_password = "wxd341134@"
    print("Initializing driver...")  # 打印日志以确认函数调用
    driver = initialize_driver()
    driver, wait = login(driver, old_username, old_password, )
    time.sleep(2)
