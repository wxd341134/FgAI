from selenium.webdriver.common.by import By

class StatuteSearchPage:
    """法条检索页面元素定位"""

    # 辅助阅卷按钮
    ASSIST_READ_BUTTON = (
        By.XPATH,
        "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[1]/div/i[1]"
    )

    # 法条检索按钮
    STATUTE_SEARCH_BUTTON = (
        By.XPATH,
        "//i[contains(@class, 'side-icon-ftjs')]"
    )

    # 搜索输入框
    SEARCH_INPUT = (
        By.XPATH,
        "//input[@placeholder='请输入']"
    )

    # 搜索按钮
    SEARCH_BUTTON = (
        By.XPATH,
        "//button[@type='button']"
    )

    # 第一条法条预览按钮
    FIRST_STATUTE_PREVIEW = (
        By.XPATH,
        "//div[@class='ant-spin-container']//div[1]//h3[1]//span[1]"
    )

    # 关闭预览按钮
    CLOSE_PREVIEW_BUTTON = (
        By.XPATH,
        "//i[@aria-label='图标: close']//*[name()='svg']"
    )

    # 关闭搜索按钮
    CLOSE_SEARCH_BUTTON = (
        By.XPATH,
        "//i[@title='关闭']//*[name()='svg']"
    )