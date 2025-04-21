from selenium.webdriver.common.by import By

class ArchivesSearchPage:
    """卷宗检索页面元素定位"""

    # 辅助阅卷按钮
    ASSIST_READ_BUTTON = (
        By.XPATH,
        "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[1]/div/i[1]"
    )

    # 卷宗检索按钮
    ARCHIVES_SEARCH_BUTTON = (
        By.XPATH,
        "//i[contains(@class, 'side-icon-jzjs')]"
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

    # 预览卷宗按钮（庭审笔录3）
    PREVIEW_ARCHIVE = (
        By.XPATH,
        "//div[@class='recognitionBox']//span[text()='庭审笔录3']"
    )

    # 关闭预览按钮
    CLOSE_PREVIEW_BUTTON = (
        By.XPATH,
        "//i[2]//img[1]"
    )

    # 仅显示文件名复选框
    FILENAME_ONLY_CHECKBOX = (
        By.XPATH,
        "//span[contains(text(),'仅显示文件名')]"
    )

    # 关闭搜索按钮
    CLOSE_SEARCH_BUTTON = (
        By.XPATH,
        "//i[@title='关闭']//*[name()='svg']"
    )

    # 搜索结果容器
    SEARCH_RESULTS = (
        By.XPATH,
        "//div[contains(@class, 'recognitionBox')]"
    )