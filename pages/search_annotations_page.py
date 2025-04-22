from selenium.webdriver.common.by import By


class SearchAnnotationsPage:
    """检索批注页面元素定位"""

    # 辅助阅卷按钮
    ASSIST_READ_BUTTON = (By.XPATH, "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[1]/div/i[1]")

    # AI助手安装文档链接
    AI_ASSISTANT_DOC = (By.XPATH, "//span[@class='ant-tree-title']//span[text()='法官AI助手安装文档']")

    # 批注按钮
    ANNOTATION_BUTTON = (By.XPATH, "//div[@class='tip__compact']/a[text()='批注']")

    # 批注输入框
    ANNOTATION_INPUT = (By.XPATH, "//textarea[@placeholder='请输入批注...']")

    # 标签下拉框
    LABEL_DROPDOWN = (By.XPATH, "//div[contains(@class, 'ant-select ant-select-enabled')]//div[text()='请选择标签']")

    # 证据标签选项
    EVIDENCE_LABEL = (By.XPATH, "//li[contains(text(),'证据')]")

    # 保存按钮
    SAVE_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")

    # 编辑批注相关的元素定位器
    EDIT_ANNOTATION_BUTTON = (
    By.XPATH, "//p[text()=' 如下文档 ']/ancestor::div[1]/div/span/i[@class='anticon anticon-edit']")
    EDIT_TEXTAREA = (By.XPATH, "//textarea[@placeholder='请输入内容']")
    EDIT_LABEL_DROPDOWN = (By.XPATH, "//div[@class='ant-select-selection__rendered']")
    LEGAL_REGULATIONS_LABEL = (By.XPATH, "//li[contains(text(),'法律法规')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-sm']")

    # 删除批注相关的元素定位器
    DELETE_ANNOTATION_BUTTON = (
    By.XPATH, "//p[text()=' 如下文档 ']/ancestor::div[1]/div/span/i[@class='anticon anticon-delete']")
    DELETE_CONFIRM_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")

    # 引用法条相关的元素定位器
    SEARCH_LINK = (By.XPATH, "//div[@class='tip__compact']/a[text()='检索']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='请输入']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[class='ant-btn ant-btn-primary ant-input-search-button']")
    LAW_REFERENCE = (
    By.XPATH, "//span[contains(text(), '第二十七章')]/following-sibling::i[@class='anticon anticon-link']")

    # 预览法条相关的元素定位器
    PREVIEW_LAW = (By.XPATH, "//a[contains(text(),'中华人民共和国民事诉讼法')]")
    CLOSE_PREVIEW = (By.XPATH,
                     "//div[@class='ant-modal-root j-modal-box is-not-fullscreen j-modal-box is-not-fullscreen']//i[@aria-label='图标: close']//*[name()='svg']")

    # 编辑法条相关的元素定位器
    EDIT_LAW_BUTTON = (By.XPATH, "//i[@aria-label='图标: edit']//*[name()='svg']")
    EDIT_LAW_INPUT = (By.XPATH, "//textarea[@placeholder='请输入内容']")
    TAG_DROPDOWN = (By.XPATH, "//div[@class='ant-select-selection__placeholder']")
    DISPUTE_FOCUS_OPTION = (By.XPATH, "//li[contains(text(),'争议焦点')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-sm']")

    # 删除法条相关的元素定位器
    DELETE_LAW_BUTTON = (By.XPATH, "//i[@aria-label='图标: delete']//*[name()='svg']")
    CONFIRM_DELETE = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")

    # 页面跳转相关的元素定位器
    SIDEBAR_TOGGLE = (By.XPATH, "//div[@class='page-control']//*[name()='svg']")
    PAGE_THREE = (By.XPATH, "//div[(@class='pdf-thumbnail')]/div/div[text()=' 3 ']")
    COPY_TEXT_BUTTON = (By.XPATH, "//div[@class='tip__compact']/a[text()='复制文本']")
    PAGE_INPUT = (By.XPATH, "//div[@class='page-control']//input")

