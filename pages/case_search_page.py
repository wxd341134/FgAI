from selenium.webdriver.common.by import By


class CaseSearchPage:
    """案件查询页面元素定位"""

    # 查询条件元素
    CASE_NUMBER_INPUT = (By.XPATH, "//span[@class='ant-input-affix-wrapper']//input[@placeholder='请输入案件编号']")
    SEARCH_BUTTON = (By.XPATH, "//body//div//button[1]")
    RESET_BUTTON = (By.XPATH, "//body//div//button[3]")

    # 判决书状态
    JUDGMENT_STATUS_DROPDOWN = (
    By.XPATH, "//label[@title='判决书状态']/ancestor::div[@class='form-item ant-row ant-form-item']/div[2]/div/span")
    JUDGMENT_NOT_GENERATED = (By.XPATH, "//li[contains(text(),'未生成')]")

    # 承办人/助理
    HANDLER_DROPDOWN = (By.CSS_SELECTOR,
                        "div[class='ant-select ant-select-enabled ant-select-allow-clear'] div[class='ant-select-selection__rendered']")
    HANDLER_ALL = (By.XPATH, "//li[normalize-space()='lvxh']")


