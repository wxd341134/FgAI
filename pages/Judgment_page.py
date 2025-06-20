from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class JudgmentPage:
    """判决书页面元素定位器类"""

    # 基础操作元素
    ENTER_JUDGMENT = (
    By.XPATH, "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[2]/div/i[1]")  # 点击进入判决书的按钮
    RECORD_TAB = (By.XPATH,
                  "//div[@class='left-area ant-row']//div[@class='ant-tabs-nav ant-tabs-nav-animated']//div//div[1]")  # 笔录标签页按钮
    RECORD_SIDEBAR = (By.XPATH, "//div[@class='page-control']//*[name()='svg']")  # 笔录侧边栏切换按钮
    RECORD_PREVIEW = (By.XPATH, "//div[@class='ant-tabs-tabpane ant-tabs-tabpane-active']//div//div[@class='content-flex annotation']//div[@class='annotation-pdf']//div//div[@class='page-control']//*[name()='svg']")  # 卷宗预览侧边栏切换按钮

    # 页面导航元素
    PAGE_3 = (By.XPATH, "//div[@class='scrolling-page']//div[text()=' 3 ']")  # 第3页按钮
    PAGE_2 = (By.XPATH, "//div[@class='scrolling-page']//div[text()=' 2 ']")  # 第2页按钮
    PAGE_INPUT = (By.XPATH, "//div[@class='page-control']/input")  # 页码输入框

    # 视图控制元素
    VIEW_BUTTON = (By.XPATH, "//i[@aria-label='图标: profile']//*[name()='svg']")  # 笔录视图切换按钮
    VIEW_BUTTON_PREVIEW = (By.XPATH, "//div[@class='ant-row-flex']/div[1]/div/div/div[3]/div[3]//i[@aria-label='图标: profile']//*[name()='svg']")  # 卷宗视图切换按钮
    DOUBLE_PAGE_VIEW = (By.XPATH, "//li[contains(text(),'双页视图')]")  # 双页视图选项
    BOOK_VIEW = (By.XPATH, "//li[contains(text(),'书籍视图')]")  # 书籍视图选项
    FIT_WIDTH = (By.XPATH, "//i[@aria-label='图标: column-width']//*[name()='svg']")  # 适合页宽按钮
    FIT_HEIGHT = (By.XPATH, "//i[@aria-label='图标: column-height']//*[name()='svg']")  # 适合页高按钮

    # 缩放控制元素
    ZOOM_OUT = (By.XPATH, "//i[@aria-label='图标: zoom-out']//*[name()='svg']")  # 缩小按钮
    ZOOM_IN = (By.XPATH, "//i[@aria-label='图标: zoom-in']//*[name()='svg']")  # 放大按钮

    # 旋转控制元素
    ROTATE_CLOCKWISE = (By.XPATH, "//i[@aria-label='图标: redo']//*[name()='svg']")  # 顺时针旋转按钮
    ROTATE_COUNTERCLOCKWISE = (By.XPATH, "//i[@aria-label='图标: undo']//*[name()='svg']")  # 逆时针旋转按钮

    # 文件操作元素
    DOWNLOAD = (By.XPATH, "//i[@aria-label='图标: download']//*[name()='svg']")  # 下载按钮
    PDF_DOWNLOAD = (By.XPATH, "//li[contains(text(),'PDF下载')]")  # PDF下载选项

    # 全屏控制元素
    FULLSCREEN = (By.XPATH, "//i[@aria-label='图标: fullscreen']//*[name()='svg']")  # 进入全屏按钮
    EXIT_FULLSCREEN = (By.XPATH, "//i[@class='anticon anticon-fullscreen-exit']")  # 退出全屏按钮

    # OCR相关元素
    OCR = (By.XPATH, "//i[@aria-label='图标: undo']/following-sibling::i[1]//*[name()='svg']")  # 笔录OCR功能按钮
    OCR_PREVIEW = (By.XPATH, "//div[@class='ant-row-flex']/div[1]/div/div/div[3]/div[3]//i[@aria-label='图标: undo']/following-sibling::i[1]//*[name()='svg']")  # 卷宗OCR功能按钮
    OCR_TEXTAREA = (By.XPATH, "//textarea[@class='custom-textarea ant-input']")  # OCR文本编辑框
    SAVE_BUTTON = (By.XPATH, "//img[@title='保存']")  # OCR内容保存按钮
    OCR_ZOOM_IN = (By.XPATH, "//i[2]//img[1]")  # OCR内容放大按钮
    OCR_ZOOM_OUT = (By.XPATH, "//i[2]//img[1]")  # OCR内容缩小按钮
    CLOSE_BUTTON = (By.XPATH, "//i[3]//img[1]")  # OCR关闭按钮


    # 卷宗预览相关元素
    EXPAND_BUTTON = (By.XPATH, "//img[@class='icon']")  # 展开按钮
    JUDGMENT_DOC = (By.XPATH, "//ul[@class='ant-tree-child-tree ant-tree-child-tree-open']/li[1]//span[text()='判决书']")  # 判决书选项
    COLLAPSE_BUTTON = (By.XPATH, "//img[@class='icon']")  # 收起按钮

    # 判决书操作相关元素
    JUDGMENT_SELECT = (By.XPATH, "//div[@class='note-title']/span[1]//div[@role='combobox']")  # 判决书选择下拉框
    JUDGMENT_0422 = (By.XPATH, "//li[normalize-space()='2025-04-22 16:52:42']")  # 0422判决书选项
    EXPORT_BUTTON = (By.XPATH, "//div[@class='note-title']/span[3]/a[3]")  # 导出判决书按钮
    MORE_BUTTON = (By.XPATH, "//div[@class='note-title']/span[3]/a[4][text()='更多 ']")  # 更多按钮
    IMPORT_OPTION = (By.XPATH, "//li[@role='menuitem'][contains(text(),'导入')]")  # 导入选项
    FILE_UPLOAD = (By.XPATH, "//input[@type='file']")  # 修改为查找 input[type='file'] 元素  # 选择文件按钮
    CONFIRM_BUTTON = (By.XPATH, "//div[@class='ant-modal-root']//button[2]")  # 确定按钮

    # 判决书对比相关元素
    COMPARE_OPTION = (By.XPATH, "//li[contains(text(),'比对')]")  # 比对选项
    OLD_VERSION_SELECT = (By.XPATH, "//span[text()='旧版本：']/following-sibling::div[1]/div[@role='combobox']")  # 旧版本选择框
    OLD_VERSION_0422 = (By.XPATH, "//li[normalize-space()='2025-04-22 16:52:42']")  # 0422日期判决书
    NEW_VERSION_SELECT = (By.XPATH, "//span[text()='新版本：']/following-sibling::div[1]/div[@role='combobox']")  # 新版本选择框
    NEW_VERSION_0423 = (By.XPATH, "//div[@id='81fc46ab-718c-483c-8be5-39e491da17de']//li[normalize-space()='2025-04-23 12:03:20']")  # 0423日期判决书
    SMALL_WINDOW = (By.XPATH, "//i[1]//img[1]")  # 小窗按钮
    LARGE_WINDOW = (By.XPATH, "//i[1]//img[1]")  # 大窗按钮
    CLOSE_COMPARE = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")  # 关闭比对按钮

    # 右侧辅助阅卷相关元素
    ASSIST_READING = (By.XPATH, "//i[@class='side-icon-fzyj']")  # 辅助阅卷按钮
    AI_DOC = (By.XPATH,"//li[@class='ant-tree-treenode-switcher-open']//span[text()='法官AI助手安装文档']")  # AI助手安装文档
    ZOOM_OUT2 = (By.XPATH, "//i[@aria-label='图标: zoom-out']//*[name()='svg']")  # 缩小按钮
    FIT_HEIGHT2 = (By.XPATH, "//i[@aria-label='图标: column-height']//*[name()='svg']")  # 适合页高按钮
    SEARCH_BUTTON = ( By.XPATH, "//i[@class='ant-dropdown-link anticon anticon-search ant-dropdown-trigger']//*[name()='svg']")  # 搜索按钮
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='查找']")  # 搜索输入框
    ARROW_LEFT = (By.XPATH, "//i[@aria-label='图标: arrow-left']//*[name()='svg']")  # 左箭头
    HIGHLIGHT_CHECKBOX = (By.XPATH, "//span[text()=' 高亮全部']")  # 高亮复选框
    CLOSE_SEARCH = (By.XPATH, "//i[@class='ant-dropdown-link anticon anticon-search ant-dropdown-trigger ant-dropdown-open']//*[name()='svg']")  # 关闭搜索按钮
    # BACK_BUTTON = (By.XPATH, "//div[@class='header fluid']//div[3]//*[name()='svg']")  # 返回上一层按钮

    # 法条检索相关元素
    LAW_SEARCH = (By.XPATH, "//i[@class='side-icon-ftjs']")  # 法条检索按钮
    LAW_SEARCH_INPUT = (By.XPATH, "//input[@placeholder='请输入']")  # 法条搜索输入框
    SEARCH_BUTTON2 = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-input-search-button']")  # 搜索按钮
    LAW_PREVIEW = (By.XPATH,
                   "//div[@class='kd-search-content ant-spin-nested-loading']/div/div[1]//span[text()='公安机关办理刑事案件程序规定（外交）']")  # 法条预览按钮
    PREVIEW_SEARCH = (By.XPATH,
                      "//div[@class='ant-modal-body']//div//div[@class='content-flex annotation']//div[@class='annotation-pdf']//div//i[@aria-label='图标: search']//*[name()='svg']")  # 预览中的搜索按钮
    PREVIEW_SEARCH_INPUT = (By.XPATH, "//input[@placeholder='查找']")  # 预览中的搜索输入框
    CLOSE_PREVIEW = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-sm']")  # 关闭预览按钮
    PAGE_4 = (By.XPATH, "//a[normalize-space()='4']")  # 第4页按钮
    CLOSE_LAW_SEARCH = (By.XPATH, "//i[@title='关闭']//*[name()='svg']")  # 关闭法条检索按钮


    # 卷宗检索相关元素
    DOSSIER_SEARCH = (By.XPATH, "//i[contains(@class, 'side-icon-jzjs')]")  # 卷宗检索按钮
    DOSSIER_SEARCH_INPUT = (By.XPATH, "//input[@placeholder='请输入']")  # 卷宗搜索输入框
    DOSSIER_SEARCH_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-input-search-button']")  # 卷宗搜索按钮
    FILENAME_ONLY = (By.XPATH, "//span[contains(text(),'仅显示文件名')]")  # 仅显示文件名选项
    TRIAL_RECORD_3 = (By.XPATH, "//div[@class='ant-spin-container']//span[text()='庭审笔录3']")  # 庭审笔录3链接
    CLOSE_PREVIEW2 = (By.XPATH, "//i[2]//img[1]")  # 关闭预览按钮
    CLOSE_DOSSIER_SEARCH = (By.XPATH, "//i[@title='关闭']//*[name()='svg']")  # 关闭卷宗检索按钮

    # 智能问答相关元素
    SMART_QA = (By.XPATH, "//i[contains(@class, 'side-icon-znwd')]")  # 智能问答按钮
    DISPUTE_FOCUS = (By.XPATH, "//span[contains(text(),'本案的争议焦点')]")  # 本案的争议焦点按钮
    QA_INPUT = (By.XPATH, "//textarea[@placeholder='在这里输入你的问题（Ctrl + Enter = 发送）']")  # 问答输入框
    SEND_BUTTON = (By.XPATH, "//img[@title='发送']")  # 发送按钮
    CLOSE_QA = (By.XPATH, "//i[@aria-label='图标: close']//*[name()='svg']")  # 关闭问答按钮

    # 智能问答结果验证相关元素
    QA_RESPONSE = (By.XPATH, "//div[contains(@class, 'qa-response')]")  # 问答响应内容区域








