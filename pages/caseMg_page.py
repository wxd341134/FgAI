from selenium.webdriver.common.by import By


class CaseMgPage:
    """案件管理页面元素定位"""

    # 案件添加元素
    ADD_BUTTON = (By.XPATH, "//body//div//button[2]")
    CASE_NAME_INPUT = (By.XPATH, "//div[@class='ant-col ant-col-24']//input[@placeholder='请输入案件名称']")
    CASE_NUMBER_INPUT = (By.XPATH, "//div[@class='ant-col ant-col-12']//input[@placeholder='请输入案件编号']")
    CASE_TYPE_DROPDOWN = (
    By.XPATH, "//div[text()='请选择案件类型']/ancestor::div[1]/following-sibling::div[1]//*[name()='svg']")
    CASE_TYPE_CIVIL = (By.XPATH, "//label[contains(text(),'民事')]")
    CASE_TYPE_CIVIL_FIRST = (By.XPATH, "//label[contains(text(),'民事一审')]")
    CASE_REASON_DROPDOWN = (
    By.XPATH, "//div[text()='请选择案由类型']/ancestor::div[1]/following-sibling::div[1]//*[name()='svg']")
    CASE_REASON_ADMIN = (By.XPATH, "//label[contains(text(), '行政案由')]")
    FILING_DATE_INPUT = (By.XPATH, "//input[@placeholder='选择开始日期']/following-sibling::i//*[name()='svg']")
    TODAY_OPTION = (By.XPATH, "//a[text()= '今天']")
    CONFIRM_BUTTON = (By.XPATH, "//div[@class= 'ant-modal-root']//button[2]")

    # 案件编辑元素
    EDIT_BUTTON_TEMPLATE = "//td[@title='{}']/ancestor::div[contains(@class, 'ant-table-content')]/div[3]//tbody/tr[1]//td[3]/div/div[3]"   #只能编辑第一个案件
    ASSISTANT_DROPDOWN = (By.XPATH, "//label[text()='法官助理']/ancestor::div[1]//following-sibling::div/div")
    ASSISTANT_OPTION = (By.XPATH, "//li[normalize-space()='wxdfg']")

    # 案件删除元素
    DELETE_BUTTON_TEMPLATE = "//td[@title='{}']/ancestor::div[contains(@class, 'ant-table-content')]/div[3]//tbody/tr[1]//td[3]/div/div[4]"  #只能删除第一个案件
    DELETE_CONFIRM = (By.XPATH, "//div[@class='ant-modal-body']//button[2]")