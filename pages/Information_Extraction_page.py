from selenium.webdriver.common.by import By


class InformationExtractionPage:
    """要素提取页面元素定位"""

    # 要素提取按钮（第4个案件）
    INFO_EXTRACT_BTN = (By.XPATH, "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[4]/td[1]/div/i[3]")

    # 展开/收起图标
    EXPAND_ICON = (By.XPATH, "//img[@class='icon']")

    # 文档树节点
    BUSINESS_LICENSE = (By.XPATH, "//span[@class='ant-tree-title']/span[text()='14_营业执照']")

    # 视图操作按钮
    ZOOM_OUT = (By.XPATH,
                "//div[@class='ant-row-flex']/div/div/div/div[3]/div[3]//i[@class='anticon anticon-zoom-out']//*[name()='svg']")
    ZOOM_IN = (By.XPATH,
               "//div[@class='ant-row-flex']/div/div/div/div[3]/div[3]//i[@class='anticon anticon-zoom-in']//*[name()='svg']")
    ROTATE_CLOCKWISE = (By.XPATH,
                        "//div[@class='ant-row-flex']/div/div/div/div[3]/div[3]//i[@class='anticon anticon-redo']//*[name()='svg']")
    ROTATE_COUNTERCLOCKWISE = (By.XPATH,
                               "//div[@class='ant-row-flex']/div/div/div/div[3]/div[3]//i[@class='anticon anticon-undo']//*[name()='svg']")

    # OCR相关元素
    # OCR_BUTTON = (By.XPATH,
    #               "//div[@class='ant-row-flex']/div/div/div/div[3]/div[3]//i[@class='anticon anticon-undo']/following-sibling::i[1]//*[name()='svg']")
    OCR_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/i[8]/*[name()='svg'][1]/*[name()='use'][1]")
    OCR_TEXTAREA = (By.XPATH, "//textarea[@class='custom-textarea ant-input']")
    SAVE_BUTTON = (By.XPATH, "//img[@title='保存']")

    # 窗口控制按钮
    MAXIMIZE_BUTTON = (By.XPATH, "//i[2]//img[1]")
    MINIMIZE_BUTTON = (By.XPATH, "//i[2]//img[1]")
    CLOSE_BUTTON = (By.XPATH, "//i[3]//img[1]")

    # 要素表相关元素
    COMPLAINT_TABLE = (By.XPATH, "//span[contains(text(),'起诉要素表')]")
    DEFENSE_TABLE = (By.XPATH, "//span[contains(text(),'答辩要素表')]")
    JUDGMENT_TABLE = (By.XPATH, "//span[contains(text(),'审判要素表')]")

    # 操作按钮
    REFRESH_BUTTON = (By.CSS_SELECTOR, "div[class='main-content noPadding'] a:nth-child(1)")
    EXPORT_BUTTON = (By.CSS_SELECTOR, "a[class='custom-note-btn primary'] svg")

    # 活动面板中的按钮
    ACTIVE_PANEL_REFRESH = (By.XPATH,
                            "//div[@class='ant-tabs-tabpane ant-tabs-tabpane-active']//a[@class='custom-note-btn info'][contains(text(),'刷新')]")
    ACTIVE_PANEL_EXPORT = (By.XPATH,
                           "//div[@class='ant-tabs-tabpane ant-tabs-tabpane-active']//a[@class='custom-note-btn primary'][contains(text(),'导出')]//*[name()='svg']")