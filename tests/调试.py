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

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-row-flex']/div/div/div/div[3]/div[3]//i[@class='anticon anticon-undo']/following-sibling::i[1]//*[name()='svg']"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td[class='ant-calendar-cell ant-calendar-selected-end-date ant-calendar-last-day-of-month ant-calendar-selected-day'] div[class='ant-calendar-date']"))).click()