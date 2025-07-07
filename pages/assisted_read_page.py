from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.logger import Logger
import time

logger = Logger().get_logger()

class AssistedReadLocators:
    """辅助阅卷页面元素定位器"""

    # 主要操作区域
    AUXILIARY_READING = (
        By.XPATH,
        "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[2]/td[1]/div/i[1]"   #注意只能选择第2个案件
    )

    # 庭审笔录相关元素
    COURT_RECORD = (By.XPATH, "//span[@class='ant-tree-title']/span[text()='庭审笔录1']")
    SET_RECORD = (By.XPATH, "//span[@class='ant-tree-title']/span[text()='庭审笔录1']/following-sibling::i[2]")
    CANCEL_SET_RECORD = (By.CSS_SELECTOR, "svg[data-v-19fbe780][data-v-75e6b11e].plusType.svg-icon")
    CONFIRM_CANCEL_BUTTON = (By.CSS_SELECTOR, "button.ant-btn.ant-btn-primary.ant-btn-sm")

    # 处理意见相关元素
    OPINION1 = (By.XPATH, "//form/div[6]/div/div[1]/div[3]/div[2]/div/span/textarea[@placeholder='请输入处理意见']")
    OPINION2 = (By.XPATH, "//form/div[6]/div/div[2]/div[3]/div[2]/div/span/textarea[@placeholder='请输入处理意见']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")

    # 下载相关元素
    DOWNLOAD_BUTTON = (By.XPATH, "//span[@class='ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']")
    PDF_DOWNLOAD_OPTION = (By.XPATH, "//li[contains(text(),'PDF下载')]")

    # 庭审笔录2相关元素
    COURT_RECORD2 = (By.XPATH, "//span[@class='ant-tree-title']/span[text()='庭审笔录2']")
    ADD_EVIDENCE_BUTTON = (By.XPATH, "//span[@class='ant-tree-title']/span[text()='庭审笔录2']/following-sibling::i[3]")
    DIRECTORY_DROPDOWN = (By.XPATH, "//span[@class='ant-select-selection__placeholder']")
    COURT_MATERIALS_OPTION = (By.XPATH, "//span[@title='原告']")
    CONFIRM_ADD_EVIDENCE = (By.CSS_SELECTOR, "button[class='ant-btn ant-btn-primary']")

    # 庭审笔录3相关元素
    COURT_RECORD3_CHECKBOX = (
    By.XPATH, "//span[@class='ant-tree-title']/span[text()='庭审笔录3']/ancestor::li[1]/span[2]/span")
    EVIDENCE_ADD_BUTTON = (By.XPATH, "//span[contains(text(),'证据添加')]")
    DIRECTORY_DROPDOWN2 = (By.XPATH, "//span[@class='ant-select-selection__placeholder']")
    APPELLANT_OPTION = (By.XPATH, "//span[@title='第三方']")
    CONFIRM_EVIDENCE_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")

    # 证据引用相关元素
    EVIDENCE_REFERENCE_TAB = (By.XPATH, "//div[@aria-selected='false']")
    REFRESH_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-warning']")
    EVIDENCE_RECORD_DETAIL = (By.XPATH, "//a[contains(text(),'庭审笔录2')]")
    CLOSE_DETAIL_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-sm']")

    # 双屏阅卷相关元素
    RECORD2_CHECKBOX = (
    By.XPATH, "//a[contains(text(),'庭审笔录2')]/ancestor::tr[1]/td[1]//span[@class='ant-checkbox']")
    RECORD3_CHECKBOX = (
    By.XPATH, "//a[contains(text(),'庭审笔录3')]/ancestor::tr[1]/td[1]//span[@class='ant-checkbox']")
    RECORD4_CHECKBOX = (By.XPATH,
                        "//a[contains(text(),'庭审笔录3')]/ancestor::tr[1]/td[1]//span[@class='ant-checkbox ant-checkbox-checked']")
    DUAL_SCREEN_READING_BUTTON = (By.XPATH, "//div[@class='splitter-pane splitter-paneR vertical ']//button[1]")
    CLOSE_DUAL_SCREEN_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-sm']")

    # 上诉人/第三人选择相关元素
    APPELLANT_SELECTOR = (By.XPATH, "//div[@class='ant-select-selection__rendered']")
    THIRD_PARTY_OPTION = (By.XPATH, "//li[contains(@class, 'ant-select-dropdown-menu-item') and text()='第三人']")

    # 批量修改相关元素
    BATCH_EDIT_BUTTON = (By.XPATH, "//div[@class='splitter-pane splitter-paneR vertical ']//button[2]")
    EVIDENCE_NAME_CELL = (By.XPATH, "//td[text()='1']/following-sibling::td[1]/div")
    EVIDENCE_TYPE_CELL = (By.XPATH, "//td[text()='1']/following-sibling::td[2]/div")
    NO_OBJECTION_OPTION = (By.XPATH, "//li[contains(text(),'无异议')]")
    EVIDENCE_OPINION_CELL = (By.XPATH, "//td[text()='1']/following-sibling::td[3]/div")
    EVIDENCE_PURPOSE_CELL = (By.XPATH, "//td[text()='1']/following-sibling::td[4]/div")
    EVIDENCE_DOCUMENT_TYPE_CELL = (By.XPATH, "//td[text()='1']/following-sibling::td[5]/div")
    PHYSICAL_EVIDENCE_OPTION = (By.XPATH, "//li[contains(text(),'物证')]")
    EVIDENCE_FORM_CELL = (By.XPATH, "//td[text()='1']/following-sibling::td[6]/div")
    PHOTO_EVIDENCE_OPTION = (By.XPATH, "//li[contains(text(),'照片')]")
    CONFIRM_BATCH_EDIT_BUTTON = (
    By.XPATH, "//div[@class='ant-modal-root j-modal-box fullscreen j-modal-box fullscreen']//button[2]")

    # 案件查询相关定位器
    CASE_NUMBER_INPUT = (By.XPATH, "//span[@class='ant-input-affix-wrapper']//input[@placeholder='请输入案件编号']")
    CASE_NAME_INPUT = (By.XPATH, "//span[@class='ant-input-affix-wrapper']//input[@placeholder='请输入案件名称']")
    JUDGMENT_STATUS_DROPDOWN = (
    By.XPATH, "//label[@title='判决书状态']/ancestor::div[@class='form-item ant-row ant-form-item']/div[2]/div/span")
    JUDGMENT_STATUS_NOT_GENERATED = (By.XPATH, "//li[contains(text(),'未生成')]")
    HANDLER_DROPDOWN = (By.XPATH,
                        "//div[@class='ant-select ant-select-enabled ant-select-allow-clear']//div[@class='ant-select-selection__rendered']")
    HANDLER_ALL_OPTION = (By.XPATH, "//li[contains(text(),'全部')]")
    SEARCH_BUTTON = (By.XPATH, "//body//div//button[1]")
    RESET_BUTTON = (By.XPATH, "//body//div//button[3]")

    # 辅助阅卷按钮
    # ASSIST_READ_BUTTON = (
    #     By.XPATH,
    #     "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[1]/div/i[1]"
    # )

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


class AssistedReadPage:
    """辅助阅卷页面类"""

    def __init__(self, driver):
        """初始化页面对象"""
        self.driver = driver
        self.locators = AssistedReadLocators()

    def get_locator(self, locator_name):
        """获取元素定位器"""
        return getattr(self.locators, locator_name)