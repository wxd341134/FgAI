from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.login_调试 import initialize_driver, login
import sys
print(sys.path)

old_username = "wxdfg"
old_password = "wxd341134@"
driver = initialize_driver()
driver, wait = login(driver, old_username, old_password)
current_time = "2025-03-21 05:52:58"
user_login = "wxd341134"

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'ant-select-dropdown-menu-item') and text()='第三人']"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".container_box .svg-icon"))).click()