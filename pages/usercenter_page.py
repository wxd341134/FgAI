from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserCenterPage(BasePage):
    """个人中心页面元素定位和基本操作"""

    # 页面元素定位器
    LOCATORS = {
        "user_menu": (By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']"),
        "report_stats_option": (By.XPATH, "//li[contains(text(),'报表统计')]"),
        "department_option": (By.XPATH, "//div[@title='按承办部门']"),
        "handler_option": (By.XPATH, "//li[contains(text(),'按承办人')]"),
        "query_button": (By.XPATH, "//body//div//button[1]"),
        "export_button": (By.XPATH, "//body//div//button[3]"),
        "font_download_option": (By.XPATH, "//li[contains(text(),'字体下载')]"),
        "fangzheng_font_button": (By.XPATH, "//div[@class='ant-modal-body']//button[2]"),
        "close_modal_button": (By.XPATH, "//span[@class='ant-modal-close-x']"),
        "change_password_option": (By.XPATH, "//li[contains(text(),'修改密码')]"),
        "old_password_input": (By.XPATH, "//input[@placeholder='请输入原密码']"),
        "new_password_input": (By.XPATH, "//input[@placeholder='请输入新密码']"),
        "confirm_password_input": (By.XPATH, "//input[@placeholder='请再次输入新密码']"),
        "confirm_button": (By.XPATH, "//div[@class='ant-modal-footer']//button[2]")

    }

    def __init__(self, driver):
        super().__init__(driver)

    def click_user_menu(self):
        """点击用户菜单"""
        self.click_element(self.LOCATORS["user_menu"])

    def open_report_statistics(self):
        """打开报表统计"""
        self.click_user_menu()
        self.click_element(self.LOCATORS["report_stats_option"])

    def select_department_view(self):
        """选择承办部门视图"""
        self.click_element(self.LOCATORS["department_option"])

    def select_handler_view(self):
        """选择承办人视图"""
        self.click_element(self.LOCATORS["handler_option"])

    def click_query(self):
        """点击查询按钮"""
        self.click_element(self.LOCATORS["query_button"])

    def click_export(self):
        """点击导出按钮"""
        self.click_element(self.LOCATORS["export_button"])

    def open_font_download(self):
        """打开字体下载"""
        self.click_user_menu()
        self.click_element(self.LOCATORS["font_download_option"])

    def download_fangzheng_font(self):
        """下载方正字体"""
        self.click_element(self.LOCATORS["fangzheng_font_button"])

    def close_modal(self):
        """关闭模态框"""
        self.click_element(self.LOCATORS["close_modal_button"])

    def open_change_password(self):
        """打开修改密码"""
        self.click_user_menu()
        self.click_element(self.LOCATORS["change_password_option"])

    def change_password(self, old_password, new_password, confirm_password):
        """修改密码"""
        self.input_text(self.LOCATORS["old_password_input"], old_password)
        self.input_text(self.LOCATORS["new_password_input"], new_password)
        self.input_text(self.LOCATORS["confirm_password_input"], confirm_password)
        self.click_element(self.LOCATORS["confirm_button"])