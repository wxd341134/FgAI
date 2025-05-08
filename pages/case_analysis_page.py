from selenium.webdriver.common.by import By


class CaseAnalysisPage:
    """案件分析页面元素定位"""

    # 进入案件分析
    ENTER_ANALYSIS = (By.XPATH, "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[2]/div/i[2]")

    # 导航相关
    # NAVIGATION_TOGGLE = (By.XPATH, "//div[@class='custom-anchor']/img[1]")
    # EVIDENCE_LIST = (By.XPATH, "//a[@title='证据列表']")
    COURT_OPINION_PREVIEW = (By.XPATH, "//a[@title='判决依据及主文预览']")
    FACT_DESCRIPTION = (By.XPATH, "//a[@title='事实描述']")

    # 证据认同相关
    # TRANSFER_RECEIPT = (By.XPATH, "//p[text()='转账凭证截图']/ancestor::div[1]/p/i[@class='custom-icon-a rentong']")
    # OPINION_INPUT = (By.XPATH, "//textarea[@class='ant-input']")
    # CONFIRM_BUTTON = (By.CSS_SELECTOR, "div[value='true'] button:nth-child(1)")

    # 展开收起相关
    EXPAND_MORE = (By.XPATH, "//div[@id='courtOpinion']//span[@class='s-btn'][contains(text(),'展开更多')]")
    COLLAPSE_MORE = (By.XPATH, "//div[@id='courtOpinion']//span[@class='s-btn'][contains(text(),'收起更多')]")

    # 完善事实描述相关
    EDIT_TRANSFER_RECEIPT = (By.XPATH, "//p[text()='2. 转账凭证截图 ']/i")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@class='custom-textarea ant-input']")
    SAVE_BUTTON = (By.XPATH, "//body//div//button[2]")

    # 导航和公共元素
    NAVIGATION_TOGGLE = (By.XPATH, "//div[@class='custom-anchor']/img[1]")
    EVIDENCE_LIST = (By.XPATH, "//a[@title='证据列表']")

    # 证据状态元素
    EVIDENCE_AGREE_STATUS = (
    By.XPATH, "//p[text()='转账凭证截图']/ancestor::div[1]/p/i[@class='custom-icon-a rentong']")
    EVIDENCE_DISAGREE_STATUS = (
    By.XPATH, "//p[text()='转账凭证截图']/ancestor::div[1]/p/i[@class='custom-icon-a quxiao']")

    # 认同/不认同选项
    AGREE_RADIO = (By.XPATH, "//label[.//span[text()='认同']]")
    DISAGREE_RADIO = (By.XPATH, "//label[.//span[text()='不认同']]")

    # 意见输入和确认
    OPINION_INPUT = (By.XPATH, "//textarea[@class='ant-input']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "div[value='true'] button:nth-child(1)")

    # 庭审笔录相关元素
    COURT_RECORD = (By.XPATH, "//div[@class='left-area ant-row']//div[text()='庭审笔录']")
    SIDEBAR_TOGGLE = (By.XPATH, "//div[@class='page-control']//*[name()='svg']")
    PAGE_THREE = (By.XPATH, "//div[@class='scrolling-document pdf-preview']//div[text()=' 3 ']")
    PAGE_INPUT = (By.XPATH, "//div[@class='page-control']//input")

    # 视图控制
    VIEW_BUTTON = (By.XPATH, "//i[@aria-label='图标: profile']//*[name()='svg']")
    DOUBLE_PAGE_VIEW = (By.XPATH, "//li[contains(text(),'双页视图')]")
    FIT_WIDTH = (By.XPATH, "//i[@aria-label='图标: column-width']//*[name()='svg']")
    FIT_HEIGHT = (By.XPATH, "//*[name()='path' and contains(@d,'M840 836H1')]")

    # 缩放和旋转
    ZOOM_OUT = (By.XPATH, "//i[@aria-label='图标: zoom-out']//*[name()='svg']")
    ZOOM_IN = (By.XPATH, "//i[@aria-label='图标: zoom-in']//*[name()='svg']")
    ROTATE_CLOCKWISE = (By.XPATH, "//i[@aria-label='图标: redo']//*[name()='svg']")
    ROTATE_COUNTERCLOCKWISE = (By.XPATH, "//i[@aria-label='图标: undo']//*[name()='svg']")

    # 其他控制
    DOWNLOAD_BUTTON = (By.XPATH, "//i[@aria-label='图标: download']//*[name()='svg']")
    PDF_DOWNLOAD = (By.XPATH, "//li[contains(text(),'PDF下载')]")
    FULLSCREEN_BUTTON = (By.XPATH, "//i[@aria-label='图标: fullscreen']//*[name()='svg']")  #全屏操作
    EXIT_FULLSCREEN = (By.XPATH, "//i[@class='anticon anticon-fullscreen-exit']")  #退出全屏




