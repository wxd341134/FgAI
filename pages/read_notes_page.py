from selenium.webdriver.common.by import By


class ReadNotesPage:
    # 阅卷笔记主要元素
    REVIEW_NOTES_BUTTON = (By.XPATH, "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[1]/div/i[2]")

    # 判决书相关元素
    JUDGMENT_DOC = (By.XPATH, "//span[@class='ant-tree-title']/span[text()='判决书']")
    ZOOM_OUT = (By.CSS_SELECTOR, "svg[viewBox='64 64 896 896'][data-icon='zoom-out']")
    ZOOM_IN = (By.CSS_SELECTOR, "svg[viewBox='64 64 896 896'][data-icon='zoom-in']")
    DOWNLOAD = (By.CSS_SELECTOR, "svg[viewBox='64 64 896 896'][data-icon='download']")
    PDF_DOWNLOAD = (By.XPATH, "//li[contains(text(),'PDF下载')]")
    CLOSE_PREVIEW = (By.XPATH, "//i[2]//img[1]")

    # 证据引用元素
    EVIDENCE_TAB = (By.XPATH, "//div[@class='ant-tabs-tab-active ant-tabs-tab']")
    COURT_RECORD_3 = (
    By.XPATH, "//div[@class='deptree ant-tabs-tabpane ant-tabs-tabpane-active']//span[text()='庭审笔录3']")
    ROTATE_CLOCKWISE = (By.CSS_SELECTOR, "svg[viewBox='64 64 896 896'][data-icon='redo']")
    ROTATE_COUNTER_CLOCKWISE = (By.CSS_SELECTOR, "svg[viewBox='64 64 896 896'][data-icon='undo']")
    VIEW_BUTTON = (By.CSS_SELECTOR, "svg[viewBox='64 64 896 896'][data-icon='profile']")
    DOUBLE_PAGE_VIEW = (By.XPATH, "//li[contains(text(),'双页视图')]")
    FULLSCREEN = (By.CSS_SELECTOR, "svg[viewBox='64 64 896 896'][data-icon='fullscreen']")
    EXIT_FULLSCREEN = (By.XPATH, "//i[@class='anticon anticon-fullscreen-exit']")

    # 笔记页面操作元素
    EXPORT_NOTES = (By.XPATH, "//a[@class='custom-note-btn primary']")
    SEARCH_REPLACE = (By.CSS_SELECTOR, "button[title='查找和替换'] span[class='tox-icon tox-tbtn__icon-wrap'] svg")
    FIND_INPUT = (By.XPATH, "//input[@placeholder='查找']")
    REPLACE_INPUT = (By.XPATH, "//input[@placeholder='替换为']")
    FIND_BUTTON = (By.XPATH, "//button[@title='查找']")
    REPLACE_BUTTON = (By.XPATH, "//button[@title='替换']")
    REPLACE_ALL_BUTTON = (By.XPATH, "//button[@title='全部替换']")
    CLOSE_DIALOG = (By.CSS_SELECTOR, "div[class='tox-icon'] svg")
    SAVE_BUTTON = (By.XPATH, "//a[contains(text(),'保存')]")

    # AI智能问答相关定位器
    AI_QA_BUTTON = (By.XPATH, "//button[@title='AI智能问答']")
    CLOSE_AI_QA_DIALOG = (By.XPATH, "//i[@aria-label='图标: close']//*[name()='svg']")
    AI_DIALOG = (By.XPATH, "//div[contains(@class, 'ant-modal-content')]")
    # 构成要件相关定位器
    CONSTITUENT_ELEMENTS_BUTTON = (By.XPATH, "//button[@title='构成要件']")



    # iframe 定位
    NOTES_IFRAME = (By.TAG_NAME, "iframe")  # 阅卷笔记的iframe

    # 文本内容区域定位
    NOTES_CONTENT = (By.XPATH, "//div[contains(@class, 'notes-content')]")

    # 字体相关定位
    FONT_FANGSONG = (By.XPATH, "//span[contains(text(),'仿宋_GB2312')]")  # 仿宋字体按钮
    FONT_KAITI = (By.XPATH, "//div[contains(text(),'楷体')]")  # 楷体选项

    # 字号相关定位
    FONT_SIZE_BUTTON = (By.CSS_SELECTOR, "button[title='字号'] span[class='tox-tbtn__select-label']")  # 字号按钮
    FONT_SIZE_ER_HAO = (By.XPATH, "//div[@title='二号']//div[1]")  # 二号字号选项

    # 段落格式相关定位
    PARAGRAPH_FORMAT_BUTTON = (By.CSS_SELECTOR, "button[title='格式'] span[class='tox-tbtn__select-label']")  # 格式按钮
    LINE_HEIGHT_BUTTON = (By.XPATH, "//div[@title='行高']//div[1]")  # 行高按钮
    LINE_HEIGHT_175 = (By.XPATH, "//p[normalize-space()='1.75']")  # 1.75行高选项

    # 文字样式定位
    BOLD_BUTTON = (By.XPATH, "//*[name()='path' and contains(@d,'M7.8 ')]")  # 加粗按钮
    ITALIC_BUTTON = (By.CSS_SELECTOR, "button[title='斜体'] span[class='tox-icon tox-tbtn__icon-wrap'] svg")  # 斜体按钮
    CLEAR_FORMAT_BUTTON = (By.XPATH, "//*[name()='path' and contains(@d,'M13.2 6a1 ')]")  # 清除格式按钮

    # 背景色相关定位
    BACKGROUND_COLOR_BUTTON = (By.CSS_SELECTOR, "div[title='背景色'] div:nth-child(2)")  # 背景色按钮
    RED_COLOR_OPTION = (By.XPATH, "//div[@title='Red']")  # 红色选项




