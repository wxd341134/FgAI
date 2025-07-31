from selenium.webdriver.common.by import By


class UserCenterPage:
    """个人中心页面元素定位"""

    # 用户菜单相关元素
    USER_MENU = (By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']")
    USER_BACK = (By.CSS_SELECTOR, ".container_box .svg-icon")

    # 报表统计相关元素
    REPORT_STATS_OPTION = (By.XPATH, "//li[contains(text(),'报表统计')]")
    DEPARTMENT_OPTION = (By.XPATH, "//div[@title='按承办部门']")
    HANDLER_OPTION = (By.XPATH, "//li[contains(text(),'按承办人')]")
    # 1. 点击开始时间输入框
    START_DATE_INPUT = (By.XPATH, "//input[@placeholder='开始日期']")
    # 2. 选择开始日期：2025年7月1日
    START_DATE_DAY = (By.XPATH, "//td[@title='2025年7月1日']//div[@class='ant-calendar-date'][normalize-space()='1']")
    # 3. 选择结束日期：2025年7月31日
    END_DATE_DAY = (By.XPATH, "//td[@class='ant-calendar-cell ant-calendar-in-range-cell ant-calendar-last-day-of-month']")
    # 4. 点击确定按钮
    CONFIRM_BUTTON_DAY = (By.XPATH, "//a[contains(text(),'确 定')]")


    # 1. 点击承办人下拉框
    HANDLER_DROPDOWN = (
    By.XPATH, "//label[@title='承办人']/ancestor::div[2]/div[2]/div[@class='ant-form-item-control']")

    # 2. 选择下拉选项：wxdfg
    HANDLER_OPTION_WXDFG = (By.XPATH, "//li[normalize-space()='wxdfg']")


    RESET_BUTTON = (By.XPATH, "//button[@class='ant-btn']")  # 点击重置按钮
    QUERY_BUTTON = (By.XPATH, "//body//div//button[1]")  # 点击查询按钮
    EXPORT_BUTTON = (By.XPATH, "//body//div//button[3]")   # 点击导出按钮

    # 字体下载相关元素
    FONT_DOWNLOAD_OPTION = (By.XPATH, "//li[contains(text(),'字体下载')]")
    FANGZHENG_FONT_BUTTON = (By.XPATH, "//div[@class='ant-modal-body']//button[2]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//span[@class='ant-modal-close-x']")

    # 修改密码相关元素
    CHANGE_PASSWORD_OPTION = (By.XPATH, "//li[contains(text(),'修改密码')]")
    OLD_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='请输入原密码']")
    NEW_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='请输入新密码']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='请再次输入新密码']")
    CONFIRM_BUTTON = (By.XPATH, "//div[@class='ant-modal-footer']//button[2]")