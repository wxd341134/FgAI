import glob

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import ddddocr
from selenium.webdriver.support import expected_conditions as EC



def initialize_driver():
    try:
        chrome_driver_path = 'E:\\AutoTest\\FgAI\\chromedriver-win64\\chromedriver.exe'  # 使用双反斜杠
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


# 配置参数
CAPTCHA_SAVE_DIR = r"E:\AutoTest\FgAIHelp\tests\captchas"   #固定验证码保存路径
MAX_CAPTCHA_FILES = 4  # 最多保留的验证码文件数


def ensure_captcha_dir():
    """确保目录存在，并清理旧文件"""
    os.makedirs(CAPTCHA_SAVE_DIR, exist_ok=True)

    # 获取目录中所有验证码文件并按时间排序
    captcha_files = sorted(
        glob.glob(os.path.join(CAPTCHA_SAVE_DIR, "captcha_*.png")),
        key=os.path.getmtime,
        reverse=True
    )

    # 删除超出保留数量的旧文件
    for old_file in captcha_files[MAX_CAPTCHA_FILES:]:
        try:
            os.remove(old_file)
            print(f"已清理旧文件: {os.path.basename(old_file)}")
        except Exception as e:
            print(f"清理文件失败: {str(e)}")

    return CAPTCHA_SAVE_DIR


def recognize_captcha(captcha_element, captcha_dir):
    """识别验证码并保存"""
    # 确保目录存在
    captcha_dir = ensure_captcha_dir()

    # 生成带时间戳的文件名
    timestamp = int(time.time())
    captcha_path = os.path.join(captcha_dir, f"captcha_{timestamp}.png")

    # 保存验证码截图
    captcha_element.screenshot(captcha_path)
    print(f"验证码已保存至: {captcha_path}")

    # 识别验证码
    ocr = ddddocr.DdddOcr()
    with open(captcha_path, 'rb') as f:
        img_bytes = f.read()
    return ocr.classification(img_bytes)





def login(driver, username, password, max_retry=10):
    try:
        driver.get("http://192.168.2.76:86/#/case/index")
        print("当前页面标题:", driver.title)

        wait = WebDriverWait(driver, 10)

        # 输入账号密码（只输入一次）
        username_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='请输入账号']")))
        username_field.send_keys(username)

        password_field = driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']")
        password_field.send_keys(password)
        time.sleep(1)

        retry_count = 0
        while retry_count < max_retry:
            try:
                # 关键点：每次重试都重新获取验证码元素（等待刷新后的新元素）
                captcha_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//img[contains(@src, "/judge-ai/captcha")]'))
                )

                # 识别验证码
                captcha_text = recognize_captcha(captcha_element, CAPTCHA_SAVE_DIR)
                print(f"第 {retry_count + 1} 次尝试，验证码: {captcha_text}")

                # 输入验证码
                input_element = driver.find_element(By.XPATH, "//input[@placeholder='请输入验证码']")
                input_element.clear()
                input_element.send_keys(captcha_text)

                # 点击登录
                login_button = driver.find_element(By.XPATH, "//button[@type='button']")
                login_button.click()

                # 等待登录结果（根据实际需求调整）
                time.sleep(2)

                # 检查登录成功条件（更精确的判断）
                if "login" not in driver.current_url.lower():  # 浏览器URL中不包括login，就打印登录成功
                    print("登录成功！")
                    return driver, wait

            except Exception as e:
                print(f"尝试 {retry_count + 1} 出现异常: {str(e)}")

            # 登录失败时，系统会自动刷新验证码，只需增加重试计数
            retry_count += 1
            print(f"验证码错误，准备第 {retry_count + 1} 次尝试...")
            time.sleep(1)  # 等待系统自动刷新验证码

        print(f"登录失败，已重试 {max_retry} 次")
        driver.quit()
        return None, None

    except Exception as e:
        print(f"登录流程异常: {str(e)}")
        driver.quit()
        return None, None

# if __name__ == "__main__":
#     old_username = "wxdfg"
#     old_password = "wxd341134@"
#     print("Initializing driver...")  # 打印日志以确认函数调用
#     driver = initialize_driver()
#     driver, wait = login(driver, old_username, old_password, )
#     time.sleep(2)
