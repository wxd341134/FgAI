from selenium.webdriver.common.by import By


class MediationPage:
    """调节页面的元素定位"""

    # 调节相关元素
    MEDIATION_BUTTON = (By.XPATH, "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[1]/div/i[4]")  # 调节按钮
    PREVIEW_TAB = (By.XPATH,
                   "//div[@class='left-area ant-row']//div[@class='ant-tabs-nav ant-tabs-nav-animated']//div//div[2]")  # 卷宗预览标签
    SAVE_BUTTON = (By.XPATH, "//a[contains(text(),'保存')]")  # 保存按钮
    EXPORT_BUTTON = (By.XPATH, "//a[@class='custom-note-btn primary']")  # 导出按钮

    # 查找替换相关元素
    FIND_REPLACE_BUTTON = (By.XPATH, "//button[@title='查找和替换']")  # 查找和替换按钮
    FIND_INPUT = (By.XPATH, "//input[@placeholder='查找']")  # 查找输入框
    REPLACE_INPUT = (By.XPATH, "//input[@placeholder='替换为']")  # 替换输入框
    FIND_BUTTON = (By.XPATH, "//button[@title='查找']")  # 查找按钮
    REPLACE_BUTTON = (By.XPATH, "//button[@title='替换']")  # 替换按钮
    REPLACE_ALL_BUTTON = (By.XPATH, "//button[@title='全部替换']")  # 全部替换按钮
    CLOSE_BUTTON = (By.XPATH, "//div[@class='tox-icon']//*[name()='svg']")  # 关闭按钮

