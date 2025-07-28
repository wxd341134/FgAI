import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pages.assisted_read_page import AssistedReadPage
from utils.logger import Logger
import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.archives_search_page import ArchivesSearchPage
from utils.logger import Logger
from datetime import datetime

logger = Logger().get_logger()


class AssistedReadUtils:
    """辅助阅卷工具类"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.current_time = "2025-07-25 07:51:46"
        self.current_user = "wxd341134"

    def _click_element(self, locator, element_name):
        """通用点击方法"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(1)
            element.click()
            logger.info(f"{self.current_time} - {self.current_user} - 点击 {element_name} 成功")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 点击 {element_name} 失败: {str(e)}")
            self._take_screenshot(f"{element_name}_click_failed")
            return False

    # def _click_element_js(self, locator, element_name):
    #     """使用JavaScript点击方法"""
    #     try:
    #         element = self.wait.until(EC.presence_of_element_located(locator))
    #         self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    #         time.sleep(1)
    #         self.driver.execute_script("arguments[0].click();", element)
    #         logger.info(f"{self.current_time} - {self.current_user} - JavaScript点击 {element_name} 成功")
    #         return True
    #     except Exception as e:
    #         logger.error(f"{self.current_time} - {self.current_user} - JavaScript点击 {element_name} 失败: {str(e)}")
    #         self._take_screenshot(f"{element_name}_js_click_failed")
    #         return False

    def _input_text(self, locator, text, element_name):
        """通用输入方法"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            time.sleep(1)
            element.send_keys(text)
            logger.info(f"{self.current_time} - {self.current_user} - 在 {element_name} 输入: {text}")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 在 {element_name} 输入失败: {str(e)}")
            self._take_screenshot(f"{element_name}_input_failed")
            return False

    def _take_screenshot(self, name):
        """截图方法"""
        try:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                f"{name}_{time.strftime('%Y%m%d_%H%M%S')}",
                allure.attachment_type.PNG
            )
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 截图失败: {str(e)}")

    @allure.step("点击辅助阅卷")
    def click_auxiliary_reading(self):
        """点击辅助阅卷按钮"""
        return self._click_element(AssistedReadPage.AUXILIARY_READING, "辅助阅卷按钮")

    @allure.step("点击庭审笔录1")
    def click_court_record1(self):
        """点击庭审笔录1"""
        return self._click_element(AssistedReadPage.COURT_RECORD, "庭审笔录1")

    @allure.step("设为庭审笔录")
    def set_as_court_record(self):
        """设为庭审笔录"""
        return self._click_element(AssistedReadPage.SET_RECORD, "设为庭审笔录按钮")

    @allure.step("输入处理意见")
    def enter_opinions(self, opinion1="无意见1", opinion2="无意见2"):
        """输入处理意见"""
        try:
            if not self._input_text(AssistedReadPage.OPINION1, opinion1, "审查意见"):
                return False
            if not self._input_text(AssistedReadPage.OPINION2, opinion2, "裁判思路"):
                return False
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 输入处理意见失败: {str(e)}")
            self._take_screenshot("enter_opinions_failed")
            return False

    @allure.step("确认设置")
    def confirm_settings(self):
        """确认设置"""
        return self._click_element(AssistedReadPage.CONFIRM_BUTTON, "确认按钮")

    @allure.step("取消设置庭审笔录")
    def cancel_set_record(self):
        """取消设置庭审笔录"""
        try:
            logger.info(f"{self.current_time} - {self.current_user} - 开始取消设置庭审笔录")

            # 使用更长的等待时间
            long_wait = WebDriverWait(self.driver, 20)

            # 1. 点击庭审笔录1
            with allure.step("点击庭审笔录1"):
                logger.info(f"{self.current_time} - {self.current_user} - 点击庭审笔录1")
                try:
                    court_record = long_wait.until(
                        EC.element_to_be_clickable(AssistedReadPage.COURT_RECORD)
                    )
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", court_record)
                    time.sleep(1)
                    court_record.click()
                    time.sleep(2)
                except Exception as e:
                    logger.error(f"{self.current_time} - {self.current_user} - 点击庭审笔录1失败: {str(e)}")
                    self._take_screenshot("click_court_record_failed")
                    return False

            # 2. 点击取消设置按钮
            with allure.step("点击取消设置按钮"):
                logger.info(f"{self.current_time} - {self.current_user} - 尝试点击取消设置按钮")
                try:
                    # 首先尝试直接点击
                    cancel_button = long_wait.until(
                        EC.element_to_be_clickable(AssistedReadPage.CANCEL_SET_RECORD)
                    )
                    cancel_button.click()
                except Exception as e:
                    logger.warning(
                        f"{self.current_time} - {self.current_user} - 直接点击取消按钮失败，尝试JavaScript点击")
                    try:
                        # JavaScript点击
                        cancel_button = self.driver.find_element(*AssistedReadPage.CANCEL_SET_RECORD)
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cancel_button)
                        time.sleep(1)
                        self.driver.execute_script("arguments[0].click();", cancel_button)
                    except Exception as je:
                        logger.error(
                            f"{self.current_time} - {self.current_user} - JavaScript点击取消按钮也失败: {str(je)}")
                        self._take_screenshot("click_cancel_button_failed")
                        return False
                time.sleep(2)

            # 3. 确认取消设置
            with allure.step("确认取消设置"):
                logger.info(f"{self.current_time} - {self.current_user} - 点击确认取消按钮")
                try:
                    # 首先尝试直接点击
                    confirm_button = long_wait.until(
                        EC.element_to_be_clickable(AssistedReadPage.CONFIRM_CANCEL_BUTTON)
                    )
                    confirm_button.click()
                except Exception as e:
                    logger.warning(
                        f"{self.current_time} - {self.current_user} - 直接点击确认按钮失败，尝试JavaScript点击")
                    try:
                        # JavaScript点击
                        confirm_button = self.driver.find_element(*AssistedReadPage.CONFIRM_CANCEL_BUTTON)
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_button)
                        time.sleep(1)
                        self.driver.execute_script("arguments[0].click();", confirm_button)
                    except Exception as je:
                        logger.error(
                            f"{self.current_time} - {self.current_user} - JavaScript点击确认按钮也失败: {str(je)}")
                        self._take_screenshot("click_confirm_button_failed")
                        return False

            time.sleep(2)
            logger.info(f"{self.current_time} - {self.current_user} - 成功取消设置庭审笔录")
            return True

        except Exception as e:
            error_msg = f"""
            {self.current_time} - {self.current_user} - 取消设置庭审笔录失败
            错误详情:
            - 错误类型: {type(e).__name__}
            - 错误信息: {str(e)}
            - 当前页面标题: {self.driver.title}
            - 当前URL: {self.driver.current_url}
            """
            logger.error(error_msg)
            self._take_screenshot("cancel_set_record_failed")
            return False

    # def _handle_click_error(self, element_name, error):
    #     """处理点击错误的通用方法"""
    #     error_msg = f"""
    #     {self.current_time} - {self.current_user} - 点击{element_name}失败
    #     错误详情:
    #     - 错误类型: {type(error).__name__}
    #     - 错误信息: {str(error)}
    #     - 当前页面标题: {self.driver.title}
    #     - 当前URL: {self.driver.current_url}
    #     """
    #     logger.error(error_msg)
    #     self._take_screenshot(f"click_{element_name}_failed")

    @allure.step("下载PDF")
    def download_pdf(self):
        """下载PDF文件"""
        try:
            if not self._click_element(AssistedReadPage.DOWNLOAD_BUTTON, "下载按钮"):
                return False
            if not self._click_element(AssistedReadPage.PDF_DOWNLOAD_OPTION, "PDF下载选项"):
                return False
            time.sleep(3)  # 等待下载完成
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 下载PDF失败: {str(e)}")
            self._take_screenshot("download_pdf_failed")
            return False

    @allure.step("添加庭审笔录2为证据")
    def add_court_record2_as_evidence(self):
        """添加庭审笔录2为证据"""
        try:
            # 点击庭审笔录2
            if not self._click_element(AssistedReadPage.COURT_RECORD2, "庭审笔录2"):
                return False

            # 点击添加为证据按钮
            if not self._click_element(AssistedReadPage.ADD_EVIDENCE_BUTTON, "添加为证据按钮"):
                return False

            # 选择目录
            if not self._click_element(AssistedReadPage.DIRECTORY_DROPDOWN, "目录下拉框"):
                return False
            if not self._click_element(AssistedReadPage.COURT_MATERIALS_OPTION, "法庭材料选项"):
                return False

            # 确认添加
            if not self._click_element(AssistedReadPage.CONFIRM_ADD_EVIDENCE, "确认添加按钮"):
                return False

            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 添加庭审笔录2为证据失败: {str(e)}")
            self._take_screenshot("add_court_record2_failed")
            return False

    @allure.step("添加庭审笔录3为证据")
    def add_court_record3_as_evidence(self):
        """添加庭审笔录3为证据"""
        try:
            # 选择庭审笔录3
            if not self._click_element(AssistedReadPage.COURT_RECORD3_CHECKBOX, "庭审笔录3复选框"):
                return False

            # 点击添加为证据按钮
            if not self._click_element(AssistedReadPage.EVIDENCE_ADD_BUTTON, "添加为证据按钮"):
                return False

            # 点击目录下拉框
            if not self._click_element(AssistedReadPage.DIRECTORY_DROPDOWN2, "目录下拉框"):
                return False

            # 选择上诉人选项
            if not self._click_element(AssistedReadPage.APPELLANT_OPTION, "上诉人选项"):
                return False

            # 点击确认添加按钮
            if not self._click_element(AssistedReadPage.CONFIRM_EVIDENCE_BUTTON, "确认添加按钮"):
                return False

            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 添加庭审笔录3为证据失败: {str(e)}")
            self._take_screenshot("add_court_record3_failed")
            return False

    @allure.step("检查证据引用功能")
    def check_evidence_reference(self):
        """检查证据引用功能"""
        try:
            # 点击证据引用标签页
            if not self._click_element(AssistedReadPage.EVIDENCE_REFERENCE_TAB, "证据引用标签页"):
                return False

            # 点击刷新按钮
            if not self._click_element(AssistedReadPage.REFRESH_BUTTON, "刷新按钮"):
                return False

            # 点击查看详情按钮
            if not self._click_element(AssistedReadPage.EVIDENCE_RECORD_DETAIL, "证据记录详情"):
                return False

            # 点击关闭详情按钮
            if not self._click_element(AssistedReadPage.CLOSE_DETAIL_BUTTON, "关闭详情按钮"):
                return False

            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 检查证据引用功能失败: {str(e)}")
            self._take_screenshot("check_evidence_reference_failed")
            return False

    @allure.step("执行双屏阅卷")
    def perform_dual_screen_reading(self):
        """执行双屏阅卷功能"""
        try:
            # 选择庭审笔录2
            if not self._click_element(AssistedReadPage.RECORD2_CHECKBOX, "庭审笔录2复选框"):
                return False

            # 选择庭审笔录3
            if not self._click_element(AssistedReadPage.RECORD3_CHECKBOX, "庭审笔录3复选框"):
                return False

            # 点击双屏阅卷按钮
            if not self._click_element(AssistedReadPage.DUAL_SCREEN_READING_BUTTON, "双屏阅卷按钮"):
                return False

            time.sleep(3)  # 可视化等待

            # 关闭双屏阅卷窗口
            if not self._click_element(AssistedReadPage.CLOSE_DUAL_SCREEN_BUTTON, "关闭双屏阅卷按钮"):
                return False

            time.sleep(2)

            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 执行双屏阅卷失败: {str(e)}")
            self._take_screenshot("perform_dual_screen_reading_failed")
            return False

    @allure.step("选择第三方")
    def select_third_party(self):
        """选择第三方"""
        try:
            time.sleep(2)

            # 点击上诉人下拉框
            if not self._click_element(AssistedReadPage.APPELLANT_SELECTOR, "上诉人下拉框"):
                return False

            time.sleep(1)

            # 选择第三方选项
            if not self._click_element(AssistedReadPage.THIRD_PARTY_OPTION, "第三方选项"):
                return False

            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 选择第三方失败: {str(e)}")
            self._take_screenshot("select_third_party_failed")
            return False

    @allure.step("刷新并取消选中庭审笔录3")
    def refresh_and_uncheck_record3(self):
        """刷新并取消选中庭审笔录3"""
        try:
            # 点击刷新按钮
            if not self._click_element(AssistedReadPage.REFRESH_BUTTON, "刷新按钮"):
                return False

            time.sleep(2)

            # 定位庭审笔录3复选框并点击取消选中
            if not self._click_element(AssistedReadPage.RECORD4_CHECKBOX, "庭审笔录3复选框"):
                return False

            time.sleep(1)

            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 刷新并取消选中庭审笔录3失败: {str(e)}")
            self._take_screenshot("refresh_and_uncheck_record3_failed")
            return False

    @allure.step("执行批量修改")
    def perform_batch_edit(self):
        """执行批量修改"""
        try:
            # 点击批量修改按钮
            if not self._click_element(AssistedReadPage.BATCH_EDIT_BUTTON, "批量修改按钮"):
                return False

            time.sleep(2)

            # 修改证据名称
            if not self._fill_cell_value(AssistedReadPage.EVIDENCE_NAME_CELL, "庭审笔录2修改", "证据名称"):
                return False

            # 选择质证类型
            if not self._select_dropdown_option(AssistedReadPage.EVIDENCE_TYPE_CELL,
                                                AssistedReadPage.NO_OBJECTION_OPTION):
                return False

            # 填写质证意见
            if not self._fill_cell_js(AssistedReadPage.EVIDENCE_OPINION_CELL, "无意见", "质证意见"):
                return False

            # 填写证明目的
            if not self._fill_cell_js(AssistedReadPage.EVIDENCE_PURPOSE_CELL, "无目的", "证明目的"):
                return False

            # 选择证件类型
            if not self._select_dropdown_option(AssistedReadPage.EVIDENCE_DOCUMENT_TYPE_CELL,
                                                AssistedReadPage.PHYSICAL_EVIDENCE_OPTION):
                return False

            # 选择证据形式
            if not self._select_dropdown_option(AssistedReadPage.EVIDENCE_FORM_CELL,
                                                AssistedReadPage.PHOTO_EVIDENCE_OPTION):
                return False

            # 点击确认修改按钮
            if not self._click_element(AssistedReadPage.CONFIRM_BATCH_EDIT_BUTTON, "确认批量修改按钮"):
                return False

            time.sleep(2)

            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 执行批量修改失败: {str(e)}")
            self._take_screenshot("perform_batch_edit_failed")
            return False

    def _fill_cell_value(self, locator, value, field_name="单元格"):
        """通用的单元格填写方法"""
        try:
            logger.info(f"{self.current_time} - {self.current_user} - 开始填写{field_name}: {value}")

            # 等待单元格出现
            cell = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )

            # 使用 JavaScript 触发双击事件
            self.driver.execute_script("""
                var event = new MouseEvent('dblclick', {
                    'view': window,
                    'bubbles': true,
                    'cancelable': true
                });
                arguments[0].dispatchEvent(event);
            """, cell)
            time.sleep(1)

            # 使用 ActionChains 输入内容并回车
            actions = ActionChains(self.driver)
            actions.send_keys(value).send_keys(Keys.ENTER).perform()
            time.sleep(1)

            logger.info(f"{self.current_time} - {self.current_user} - 成功填写{field_name}")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 填写{field_name}失败: {str(e)}")
            self._take_screenshot(f"fill_cell_value_{field_name}_failed")
            return False

    def _select_dropdown_option(self, dropdown_locator, option_locator):
        """选择下拉选项"""
        try:
            logger.info(f"{self.current_time} - {self.current_user} - 开始选择下拉选项")

            # 等待下拉框可点击并点击
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(dropdown_locator)
            )

            # 滚动到元素位置
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
            time.sleep(1)

            # 尝试点击下拉框（常规点击 + JS 点击备用）
            try:
                dropdown.click()
            except:
                self.driver.execute_script("arguments[0].click();", dropdown)
            time.sleep(1)

            # 等待选项可点击并点击
            option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(option_locator)
            )

            try:
                option.click()
            except:
                self.driver.execute_script("arguments[0].click();", option)
            time.sleep(1)

            logger.info(f"{self.current_time} - {self.current_user} - 成功选择下拉选项")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 选择下拉选项失败: {str(e)}")
            self._take_screenshot("select_dropdown_option_failed")
            return False

    def _fill_cell_js(self, locator, value, field_name="单元格"):
        """使用JavaScript填写单元格内容"""
        try:
            logger.info(f"{self.current_time} - {self.current_user} - 开始填写{field_name}: {value}")

            # 等待元素出现
            cell = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )

            # 使用 JavaScript 设置值
            js_script = """
                var cell = arguments[0];
                cell.click();
                var input = cell.querySelector('input, textarea');
                if (!input) {
                    input = document.createElement('input');
                    cell.innerHTML = '';
                    cell.appendChild(input);
                }
                input.value = arguments[1];
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new Event('change', { bubbles: true }));
                input.dispatchEvent(new KeyboardEvent('keydown', {
                    key: 'Enter',
                    code: 'Enter',
                    keyCode: 13,
                    which: 13,
                    bubbles: true
                }));
            """
            self.driver.execute_script(js_script, cell, value)
            time.sleep(1)

            logger.info(f"{self.current_time} - {self.current_user} - 成功填写{field_name}")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 填写{field_name}失败: {str(e)}")
            self._take_screenshot(f"fill_cell_js_{field_name}_failed")
            return False

    # @staticmethod
    # def _fill_cell_js(page, cell_locator, value, field_name="单元格"):
    #     """使用JavaScript填写单元格内容"""
    #     try:
    #         logger.info(f"开始填写{field_name}: {value}")
    #         wait = WebDriverWait(page.driver, 10)
    #         cell = wait.until(
    #             EC.presence_of_element_located(cell_locator)
    #         )
    #
    #         # 使用JavaScript直接设置值
    #         js_script = """
    #             var cell = arguments[0];
    #             cell.click();
    #             var input = cell.querySelector('input, textarea');
    #             if (!input) {
    #                 input = document.createElement('input');
    #                 cell.innerHTML = '';
    #                 cell.appendChild(input);
    #             }
    #             input.value = arguments[1];
    #             input.dispatchEvent(new Event('input', { bubbles: true }));
    #             input.dispatchEvent(new Event('change', { bubbles: true }));
    #             input.dispatchEvent(new KeyboardEvent('keydown', {
    #                 key: 'Enter',
    #                 code: 'Enter',
    #                 keyCode: 13,
    #                 which: 13,
    #                 bubbles: true
    #             }));
    #         """
    #         page.driver.execute_script(js_script, cell, value)
    #         time.sleep(1)
    #
    #         logger.info(f"成功填写{field_name}")
    #         return True
    #     except Exception as e:
    #         logger.error(f"填写{field_name}失败: {str(e)}")
    #         return False
    #
    # @staticmethod
    # def _fill_cell_value(page, cell_locator, value, field_name="单元格"):
    #     """通用的单元格填写方法"""
    #     try:
    #         logger.info(f"开始填写{field_name}: {value}")
    #         wait = WebDriverWait(page.driver, 10)
    #         cell = wait.until(
    #             EC.presence_of_element_located(cell_locator)
    #         )
    #
    #         # 使用JavaScript触发双击
    #         page.driver.execute_script("""
    #             var event = new MouseEvent('dblclick', {
    #                 'view': window,
    #                 'bubbles': true,
    #                 'cancelable': true
    #             });
    #             arguments[0].dispatchEvent(event);
    #         """, cell)
    #         time.sleep(1)
    #
    #         # 使用 ActionChains 输入
    #         actions = ActionChains(page.driver)
    #         actions.send_keys(value).send_keys(Keys.ENTER).perform()
    #         time.sleep(1)
    #
    #         logger.info(f"成功填写{field_name}")
    #         return True
    #     except Exception as e:
    #         logger.error(f"填写{field_name}失败: {str(e)}")
    #         return False
    #
    # @staticmethod
    # def _select_dropdown_option(page, dropdown_locator, option_locator):
    #     """选择下拉选项"""
    #     try:
    #         wait = WebDriverWait(page.driver, 10)
    #         dropdown = wait.until(EC.element_to_be_clickable(dropdown_locator))
    #
    #         # 滚动到元素位置
    #         page.driver.execute_script(
    #             "arguments[0].scrollIntoView({block: 'center'});",
    #             dropdown
    #         )
    #         time.sleep(1)
    #
    #         # 点击下拉框
    #         try:
    #             dropdown.click()
    #         except:
    #             page.driver.execute_script("arguments[0].click();", dropdown)
    #         time.sleep(1)
    #
    #         # 选择选项
    #         option = wait.until(EC.element_to_be_clickable(option_locator))
    #         try:
    #             option.click()
    #         except:
    #             page.driver.execute_script("arguments[0].click();", option)
    #         time.sleep(1)
    #
    #         return True
    #     except Exception as e:
    #         logger.error(f"选择下拉选项失败: {str(e)}")
    #         return False
    #



    # @allure.step("执行完整的卷宗检索流程")
    # def perform_archives_search(self, keyword="判决"):
    #     """
    #     执行完整的卷宗检索流程
    #     Args:
    #         keyword: 搜索关键词
    #     """
    #     try:
    #         logger.info(f"开始执行卷宗检索流程，关键词: {keyword}")

            # 1. 点击辅助阅卷
            # with allure.step("点击辅助阅卷按钮"):
            #     self.safe_click(
            #         ArchivesSearchPage.ASSIST_READ_BUTTON,
            #         "辅助阅卷按钮"
            #     )
            #     time.sleep(1)

        #     # 1. 点击卷宗检索
        #     with allure.step("点击卷宗检索按钮"):
        #         self.safe_click(
        #             ArchivesSearchPage.ARCHIVES_SEARCH_BUTTON,
        #             "卷宗检索按钮"
        #         )
        #         time.sleep(1)
        #
        #     # 2. 输入搜索内容
        #     with allure.step(f"输入搜索关键词: {keyword}"):
        #         self.safe_input(
        #             ArchivesSearchPage.SEARCH_INPUT,
        #             keyword,
        #             "搜索输入框"
        #         )
        #
        #     # 3. 点击搜索
        #     with allure.step("点击搜索按钮"):
        #         self.safe_click(
        #             ArchivesSearchPage.SEARCH_BUTTON,
        #             "搜索按钮"
        #         )
        #         time.sleep(2)
        #
        #     # 4. 点击预览卷宗
        #     with allure.step("点击预览卷宗"):
        #         self.safe_click(
        #             ArchivesSearchPage.PREVIEW_ARCHIVE,
        #             "预览卷宗按钮"
        #         )
        #         time.sleep(2)
        #
        #     # 5. 关闭预览
        #     with allure.step("关闭卷宗预览"):
        #         self.safe_click(
        #             ArchivesSearchPage.CLOSE_PREVIEW_BUTTON,
        #             "关闭预览按钮"
        #         )
        #         time.sleep(2)
        #
        #     # 6. 点击仅显示文件名
        #     with allure.step("勾选仅显示文件名"):
        #         self.safe_click(
        #             ArchivesSearchPage.FILENAME_ONLY_CHECKBOX,
        #             "仅显示文件名复选框"
        #         )
        #         time.sleep(1)
        #
        #     # 7. 关闭搜索
        #     with allure.step("关闭卷宗检索"):
        #         self.safe_click(
        #             ArchivesSearchPage.CLOSE_SEARCH_BUTTON,
        #             "关闭搜索按钮"
        #         )
        #
        #     logger.info("卷宗检索流程执行完成")
        #
        # except Exception as e:
        #     logger.error(f"卷宗检索流程执行失败: {str(e)}")
        #     allure.attach(
        #         self.driver.get_screenshot_as_png(),
        #         "失败截图",
        #         allure.attachment_type.PNG
        #     )
        #     raise