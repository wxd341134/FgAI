from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CasePage(BasePage):
    """案件页面元素定位类"""

    # 页面元素定位
    add_button = (By.XPATH, "//body//div//button[2]")
    case_name_input = (By.XPATH, "//div[@class='ant-col ant-col-24']//input[@placeholder='请输入案件名称']")
    case_number_input = (By.XPATH, "//div[@class='ant-col ant-col-12']//input[@placeholder='请输入案件编号']")
    case_type_dropdown = (By.CSS_SELECTOR, "input.vue-treeselect__input")
    civil_case_option = (By.XPATH, "//label[contains(text(),'民事')]")
    civil_case_option2 = (By.XPATH, "//label[contains(text(),'民事一审')]")
    reason_select = (By.XPATH,
                     "//div[contains(@class, 'vue-treeselect__placeholder') and text()='请选择案由类型']/following-sibling::div//input[@class='vue-treeselect__input']")
    admin_case_option = (By.XPATH, '//label[contains(text(),"行政案由")]')
    original_case_input = (By.XPATH,
                           "//div[contains(@class, 'ant-select-selection__placeholder') and text()='请输入原审案号']/ancestor::div[contains(@class, 'ant-select-selection')]")
    original_case_field = (By.CSS_SELECTOR,
                           "div[class='ant-select ant-select-open ant-select-focused ant-select-enabled ant-select-allow-clear ant-select-no-arrow'] input[class='ant-select-search__field']")
    date_input = (By.XPATH, "//form/div/div[7]//input[@placeholder='选择开始日期']")
    today_option = (By.XPATH, '//a[text()="今天"]')
    confirm_button = (By.XPATH, '//div[@class="ant-modal-root"]//button[2]')