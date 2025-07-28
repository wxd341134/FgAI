from selenium.webdriver.common.by import By


class CaseFilePage:
    """卷宗上传和目录操作页面元素定位"""

    # 卷宗上传相关元素
    UPLOAD_BUTTON = (By.XPATH, "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[2]/td[3]/div/div[1]")  # 上传卷宗按钮
    UPLOAD_ZIP_BUTTON = (By.XPATH, "//div[@class='tree-button-group ant-btn-group']//button[2]")  # 上传ZIP按钮
    ZIP_FILE_INPUT = (By.CSS_SELECTOR, "input[type='file']")  # ZIP文件选择输入框
    ZIP_CONFIRM_BUTTON = (By.XPATH, "//div[@class='ant-modal-root']//button[2]")  # ZIP上传确定按钮

    REFRESH_BUTTON = (By.XPATH, "//div[@class='tree-button-group ant-btn-group']//button[1]")  # 刷新按钮
    UPLOAD_SINGLE_BUTTON = (By.XPATH, "//div[@class='tree-button-group ant-btn-group']//button[3]")  # 上传单个文件按钮
    DOCX_FILE_INPUT = (By.XPATH, "//input[@type='file' and contains(@accept, '.docx')]")  # DOCX文件选择输入框
    SINGLE_FILE_CONFIRM_BUTTON = (By.XPATH,
                                  "//div[.//div[@class='ant-modal-title' and text()='上传单个文件']]//div[@class='ant-modal-footer']//button[2]")  # 单文件上传确定按钮

    COLLAPSE_ALL_BUTTON = (By.XPATH, "//div[@class='btnRow']//button[1]")  # 收起全部按钮
    EXPAND_ALL_BUTTON = (By.XPATH, "//div[@class='btnRow']//button[1]")  # 展开全部按钮

    # 卷宗目录操作相关元素
    NEW_DIR_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-warning']")  # 新建目录按钮
    DIR_NAME_INPUT = (By.XPATH, "//div[@class='ant-row ant-form-item']//input[@type='text']")  # 目录名称输入框
    DIR_CONFIRM_BUTTON = (By.XPATH, "//div[.//div[@class='ant-modal-title' and text()='新建目录']]//div[@class='ant-modal-footer']//button[2]")  # 目录操作确定按钮
    # DIR_CONFIRM_BUTTON = (By.XPATH, "//div[@class='ant-modal-root']//button[2]")  # 目录操作确定按钮

    PARENT_DIR_DROPDOWN = (By.XPATH,
                           "//div[.//div[@class='ant-modal-title' and text()='新建目录']]//i[@aria-label='图标: down']//*[name()='svg']")  # 上级目录下拉框
    DIR_OPTION_TEMPLATE = "//div[@class='ant-select-dropdown-content']//span[text()='{}']"  # 目录选项模板

    DELETE_ICON_TEMPLATE = "//span[text()='{}']/following-sibling::i//*[name()='svg']"  # 删除图标模板
    CHECKBOX_TEMPLATE = "//span[text()='{}']/ancestor::li[1]/span[2]/span"  # 复选框模板
    DELETE_CONFIRM_BUTTON = (
    By.XPATH, "//div[contains(@class, 'ant-modal-confirm ant-modal-confirm-confirm')]//button[2]")  # 删除确认按钮
    BATCH_DELETE_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-danger']")  # 批量删除按钮