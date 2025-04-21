from selenium.webdriver.common.by import By


class SearchAnnotationsPage:
    """检索批注页面元素定位"""

    # 辅助阅卷按钮
    ASSIST_READ_BUTTON = (
        By.XPATH,
        "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[1]/div/i[1]"
    )

    # AI助手安装文档链接
    AI_ASSISTANT_DOC = (
        By.XPATH,
        "//span[@class='ant-tree-title']//span[text()='法官AI助手安装文档']"
    )

    # 批注按钮
    ANNOTATION_BUTTON = (
        By.XPATH,
        "//div[@class='tip__compact']/a[text()='批注']"
    )

    # 批注输入框
    ANNOTATION_INPUT = (
        By.XPATH,
        "//textarea[@placeholder='请输入批注...']"
    )

    # 标签下拉框
    LABEL_DROPDOWN = (
        By.XPATH,
        "//div[contains(@class, 'ant-select ant-select-enabled')]//div[text()='请选择标签']"
    )

    # 证据标签选项
    EVIDENCE_LABEL = (
        By.XPATH,
        "//li[contains(text(),'证据')]"
    )

    # 保存按钮
    SAVE_BUTTON = (
        By.XPATH,
        "//button[@class='ant-btn ant-btn-primary']"
    )

    # 编辑批注相关的元素定位器
    EDIT_ANNOTATION_BUTTON = (
        By.XPATH,
        "//p[text()=' 如下文档 ']/ancestor::div[1]/div/span/i[@class='anticon anticon-edit']"
    )

    EDIT_TEXTAREA = (
        By.XPATH,
        "//textarea[@placeholder='请输入内容']"
    )

    EDIT_LABEL_DROPDOWN = (
        By.XPATH,
        "//div[@class='ant-select-selection__rendered']"
    )

    LEGAL_REGULATIONS_LABEL = (
        By.XPATH,
        "//li[contains(text(),'法律法规')]"
    )

    CONFIRM_BUTTON = (
        By.XPATH,
        "//button[@class='ant-btn ant-btn-primary ant-btn-sm']"
    )

    # 删除批注相关的元素定位器
    DELETE_ANNOTATION_BUTTON = (
        By.XPATH,
        "//p[text()=' 如下文档 ']/ancestor::div[1]/div/span/i[@class='anticon anticon-delete']"
    )

    DELETE_CONFIRM_BUTTON = (
        By.XPATH,
        "//button[@class='ant-btn ant-btn-primary']"
    )

