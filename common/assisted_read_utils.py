import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.logger import Logger
from datetime import datetime

logger = Logger().get_logger()


class AssistedReadUtils:
    """辅助阅卷工具类"""

    @staticmethod
    def execute_assisted_read_workflow(page):
        """
        执行完整的辅助阅卷工作流
        """
        try:
            workflow_steps = [
                AssistedReadUtils.click_auxiliary_reading,
                AssistedReadUtils.click_court_record1,
                AssistedReadUtils.set_as_court_record,
                AssistedReadUtils.cancel_set_record,
                AssistedReadUtils.download_pdf,
                AssistedReadUtils.add_court_record2_as_evidence,
                AssistedReadUtils.add_court_record3_as_evidence,
                AssistedReadUtils.check_evidence_reference,
                AssistedReadUtils.perform_dual_screen_reading,
                AssistedReadUtils.select_third_party,
                AssistedReadUtils.refresh_and_uncheck_record3,
                AssistedReadUtils.perform_batch_edit
            ]

            for step in workflow_steps:
                if not step(page):
                    return False
            return True
        except Exception as e:
            logger.error(f"执行辅助阅卷工作流失败: {str(e)}")
            return False

    @staticmethod
    def click_auxiliary_reading(page):
        """点击辅助阅卷按钮"""
        try:
            logger.info("点击辅助阅卷按钮")
            wait = WebDriverWait(page.driver, 10)
            auxiliary_reading = wait.until(
                EC.element_to_be_clickable(page.locators.AUXILIARY_READING)
            )
            auxiliary_reading.click()
            time.sleep(2)
            logger.info("成功点击辅助阅卷")
            return True
        except Exception as e:
            logger.error(f"点击辅助阅卷失败: {str(e)}")
            return False

    @staticmethod
    def click_court_record1(page):
        """点击庭审笔录1"""
        try:
            logger.info("点击庭审笔录1")
            wait = WebDriverWait(page.driver, 10)
            court_record = wait.until(
                EC.element_to_be_clickable(page.locators.COURT_RECORD)
            )
            court_record.click()
            time.sleep(2)
            logger.info("成功点击庭审笔录1")
            return True
        except Exception as e:
            logger.error(f"点击庭审笔录1失败: {str(e)}")
            return False

    @staticmethod
    def set_as_court_record(page):
        """设为庭审笔录"""
        try:
            logger.info("设置为庭审笔录")
            wait = WebDriverWait(page.driver, 10)
            set_record = wait.until(
                EC.element_to_be_clickable(page.locators.SET_RECORD)
            )
            set_record.click()
            time.sleep(1)
            logger.info("成功设置为庭审笔录")
            return True
        except Exception as e:
            logger.error(f"设置庭审笔录失败: {str(e)}")
            return False

    @staticmethod
    def enter_opinions(page, opinion1="无意见1", opinion2="无意见2"):
        """输入处理意见"""
        try:
            logger.info(f"输入处理意见: {opinion1}, {opinion2}")
            wait = WebDriverWait(page.driver, 10)

            # 输入第一个意见
            opinion1_elem = wait.until(
                EC.presence_of_element_located(page.locators.OPINION1)
            )
            opinion1_elem.clear()
            opinion1_elem.send_keys(opinion1)
            time.sleep(1)

            # 输入第二个意见
            opinion2_elem = wait.until(
                EC.presence_of_element_located(page.locators.OPINION2)
            )
            opinion2_elem.clear()
            opinion2_elem.send_keys(opinion2)
            time.sleep(1)

            logger.info("成功输入处理意见")
            return True
        except Exception as e:
            logger.error(f"输入处理意见失败: {str(e)}")
            return False

    @staticmethod
    def confirm_settings(page):
        """确认设置"""
        try:
            logger.info("确认设置")
            wait = WebDriverWait(page.driver, 10)
            confirm_button = wait.until(
                EC.element_to_be_clickable(page.locators.CONFIRM_BUTTON)
            )
            confirm_button.click()
            time.sleep(2)
            logger.info("成功确认设置")
            return True
        except Exception as e:
            logger.error(f"确认设置失败: {str(e)}")
            return False

    @staticmethod
    def cancel_set_record(page):
        """取消设置庭审笔录"""
        try:
            logger.info("开始取消设置庭审笔录...")

            # 添加更长的等待时间
            wait = WebDriverWait(page.driver, 20)

            # 先点击庭审笔录1
            logger.info("点击庭审笔录1")
            court_record = wait.until(
                EC.element_to_be_clickable(page.locators.COURT_RECORD)
            )
            court_record.click()
            time.sleep(2)

            try:
                # 尝试直接点击
                logger.info("尝试点击取消设置按钮")
                cancel_button = wait.until(
                    EC.element_to_be_clickable(page.locators.CANCEL_SET_RECORD)
                )
                cancel_button.click()
            except:
                logger.warning("直接点击取消按钮失败，尝试JavaScript点击")
                # 如果直接点击失败，尝试使用JavaScript点击
                cancel_button = page.driver.find_element(*page.locators.CANCEL_SET_RECORD)
                page.driver.execute_script("arguments[0].click();", cancel_button)

            time.sleep(2)

            # 确认取消设置
            logger.info("点击确认取消按钮")
            confirm_button = wait.until(
                EC.element_to_be_clickable(page.locators.CONFIRM_CANCEL_BUTTON)
            )
            # 尝试两种方式点击确认按钮
            try:
                confirm_button.click()
            except:
                page.driver.execute_script("arguments[0].click();", confirm_button)

            time.sleep(2)
            logger.info("成功取消设置庭审笔录")
            return True

        except Exception as e:
            logger.error(f"取消设置庭审笔录失败: {str(e)}")
            # 添加更多的错误信息
            try:
                error_msg = f"""
                错误详情:
                - 错误类型: {type(e).__name__}
                - 错误信息: {str(e)}
                - 当前页面标题: {page.driver.title}
                - 当前URL: {page.driver.current_url}
                """
                logger.error(error_msg)
            except:
                pass
            return False

    @staticmethod
    def download_pdf(page):
        """下载PDF文件"""
        try:
            logger.info("开始下载PDF")
            wait = WebDriverWait(page.driver, 10)

            # 点击下载按钮
            download_button = wait.until(
                EC.element_to_be_clickable(page.locators.DOWNLOAD_BUTTON)
            )
            download_button.click()
            time.sleep(1)

            # 选择PDF下载选项
            pdf_option = wait.until(
                EC.element_to_be_clickable(page.locators.PDF_DOWNLOAD_OPTION)
            )
            pdf_option.click()
            time.sleep(3)

            logger.info("PDF下载成功")
            return True
        except Exception as e:
            logger.error(f"PDF下载失败: {str(e)}")
            return False

    @staticmethod
    def add_court_record2_as_evidence(page):
        """添加庭审笔录2为证据"""
        try:
            logger.info("添加庭审笔录2为证据")
            wait = WebDriverWait(page.driver, 10)

            # 点击庭审笔录2
            court_record2 = wait.until(
                EC.element_to_be_clickable(page.locators.COURT_RECORD2)
            )
            court_record2.click()
            time.sleep(2)

            # 点击添加为证据按钮
            add_evidence = wait.until(
                EC.element_to_be_clickable(page.locators.ADD_EVIDENCE_BUTTON)
            )
            add_evidence.click()
            time.sleep(2)

            # 选择目录
            dropdown = wait.until(
                EC.element_to_be_clickable(page.locators.DIRECTORY_DROPDOWN)
            )
            dropdown.click()
            time.sleep(1)

            court_materials = wait.until(
                EC.element_to_be_clickable(page.locators.COURT_MATERIALS_OPTION)
            )
            court_materials.click()
            time.sleep(1)

            # 确认添加
            confirm = wait.until(
                EC.element_to_be_clickable(page.locators.CONFIRM_ADD_EVIDENCE)
            )
            confirm.click()
            time.sleep(2)

            logger.info("成功添加庭审笔录2为证据")
            return True
        except Exception as e:
            logger.error(f"添加庭审笔录2为证据失败: {str(e)}")
            return False

    @staticmethod
    def add_court_record3_as_evidence(page):
        """将庭审笔录3添加为证据"""
        try:
            logger.info("添加庭审笔录3为证据")
            wait = WebDriverWait(page.driver, 10)

            # 选择庭审笔录3
            checkbox = wait.until(
                EC.element_to_be_clickable(page.locators.COURT_RECORD3_CHECKBOX)
            )
            checkbox.click()
            time.sleep(1)

            # 点击证据添加按钮
            add_button = wait.until(
                EC.element_to_be_clickable(page.locators.EVIDENCE_ADD_BUTTON)
            )
            add_button.click()
            time.sleep(1)

            # 选择目录
            dropdown = wait.until(
                EC.element_to_be_clickable(page.locators.DIRECTORY_DROPDOWN2)
            )
            dropdown.click()
            time.sleep(1)

            appellant = wait.until(
                EC.element_to_be_clickable(page.locators.APPELLANT_OPTION)
            )
            appellant.click()
            time.sleep(1)

            # 确认添加
            confirm = wait.until(
                EC.element_to_be_clickable(page.locators.CONFIRM_EVIDENCE_BUTTON)
            )
            confirm.click()
            time.sleep(2)

            logger.info("成功添加庭审笔录3为证据")
            return True
        except Exception as e:
            logger.error(f"添加庭审笔录3为证据失败: {str(e)}")
            return False

    @staticmethod
    def check_evidence_reference(page):
        """检查证据引用功能"""
        try:
            logger.info("开始检查证据引用")
            wait = WebDriverWait(page.driver, 10)

            # 点击证据引用标签页
            tab = wait.until(
                EC.element_to_be_clickable(page.locators.EVIDENCE_REFERENCE_TAB)
            )
            tab.click()
            time.sleep(2)

            # 点击刷新按钮
            refresh = wait.until(
                EC.element_to_be_clickable(page.locators.REFRESH_BUTTON)
            )
            refresh.click()
            time.sleep(2)

            # 查看详情
            detail = wait.until(
                EC.element_to_be_clickable(page.locators.EVIDENCE_RECORD_DETAIL)
            )
            detail.click()
            time.sleep(2)

            # 关闭详情
            close = wait.until(
                EC.element_to_be_clickable(page.locators.CLOSE_DETAIL_BUTTON)
            )
            close.click()
            time.sleep(2)

            logger.info("证据引用检查完成")
            return True
        except Exception as e:
            logger.error(f"证据引用检查失败: {str(e)}")
            return False

    @staticmethod
    def perform_dual_screen_reading(page):
        """执行双屏阅卷功能"""
        try:
            logger.info("开始执行双屏阅卷")
            wait = WebDriverWait(page.driver, 10)

            # 选择庭审笔录2和3
            record2 = wait.until(
                EC.element_to_be_clickable(page.locators.RECORD2_CHECKBOX)
            )
            record2.click()
            time.sleep(1)

            record3 = wait.until(
                EC.element_to_be_clickable(page.locators.RECORD3_CHECKBOX)
            )
            record3.click()
            time.sleep(1)

            # 点击双屏阅卷按钮
            dual_screen = wait.until(
                EC.element_to_be_clickable(page.locators.DUAL_SCREEN_READING_BUTTON)
            )
            dual_screen.click()
            time.sleep(3)

            # 关闭双屏阅卷
            close = wait.until(
                EC.element_to_be_clickable(page.locators.CLOSE_DUAL_SCREEN_BUTTON)
            )
            close.click()
            time.sleep(2)

            logger.info("双屏阅卷执行完成")
            return True
        except Exception as e:
            logger.error(f"双屏阅卷执行失败: {str(e)}")
            return False

    @staticmethod
    def select_third_party(page):
        """选择第三人"""
        try:
            logger.info("开始选择第三人")
            time.sleep(2)

            wait = WebDriverWait(page.driver, 10)
            selector = wait.until(
                EC.element_to_be_clickable(page.locators.APPELLANT_SELECTOR)
            )

            # 滚动到元素位置
            page.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                selector
            )
            time.sleep(1)

            # 尝试点击选择器
            try:
                selector.click()
            except:
                page.driver.execute_script("arguments[0].click();", selector)

            time.sleep(1)

            # 选择第三人选项
            try:
                third_party = wait.until(
                    EC.element_to_be_clickable(page.locators.THIRD_PARTY_OPTION)
                )
                third_party.click()
            except:
                # 尝试备用方法
                options = page.driver.find_elements(
                    By.XPATH,
                    "//li[contains(@class, 'ant-select-dropdown-menu-item')]"
                )
                for option in options:
                    if "第三人" in option.text:
                        option.click()
                        break

            time.sleep(2)
            logger.info("成功选择第三人")
            return True
        except Exception as e:
            logger.error(f"选择第三人失败: {str(e)}")
            return False

    @staticmethod
    def refresh_and_uncheck_record3(page):
        """刷新并取消选中庭审笔录3"""
        try:
            logger.info("刷新并取消选中庭审笔录3")
            wait = WebDriverWait(page.driver, 10)

            # 点击刷新按钮
            refresh = wait.until(
                EC.element_to_be_clickable(page.locators.REFRESH_BUTTON)
            )
            refresh.click()
            time.sleep(2)

            # 取消选中庭审笔录3
            record3 = wait.until(
                EC.element_to_be_clickable(page.locators.RECORD4_CHECKBOX)
            )
            record3.click()
            time.sleep(1)

            logger.info("成功刷新并取消选中庭审笔录3")
            return True
        except Exception as e:
            logger.error(f"刷新并取消选中庭审笔录3失败: {str(e)}")
            return False

    @staticmethod
    def perform_batch_edit(page):
        """执行批量修改"""
        try:
            logger.info("开始执行批量修改")
            wait = WebDriverWait(page.driver, 10)

            # 点击批量修改按钮
            batch_edit = wait.until(
                EC.element_to_be_clickable(page.locators.BATCH_EDIT_BUTTON)
            )
            batch_edit.click()
            time.sleep(2)

            # 修改证据名称
            AssistedReadUtils._fill_cell_value(
                page,
                page.locators.EVIDENCE_NAME_CELL,
                "庭审笔录2修改",
                "证据名称"
            )

            # 选择质证类型
            AssistedReadUtils._select_dropdown_option(
                page,
                page.locators.EVIDENCE_TYPE_CELL,
                page.locators.NO_OBJECTION_OPTION
            )

            # 填写质证意见 - 使用特殊处理方法
            AssistedReadUtils._fill_cell_js(
                page,
                page.locators.EVIDENCE_OPINION_CELL,
                "无意见",
                "质证意见"
            )

            # 填写证明目的 - 使用特殊处理方法
            AssistedReadUtils._fill_cell_js(
                page,
                page.locators.EVIDENCE_PURPOSE_CELL,
                "无目的",
                "证明目的"
            )

            # 选择证件类型
            AssistedReadUtils._select_dropdown_option(
                page,
                page.locators.EVIDENCE_DOCUMENT_TYPE_CELL,
                page.locators.PHYSICAL_EVIDENCE_OPTION
            )

            # 选择证据形式
            AssistedReadUtils._select_dropdown_option(
                page,
                page.locators.EVIDENCE_FORM_CELL,
                page.locators.PHOTO_EVIDENCE_OPTION
            )

            # 确认修改
            confirm = wait.until(
                EC.element_to_be_clickable(page.locators.CONFIRM_BATCH_EDIT_BUTTON)
            )
            page.driver.execute_script("arguments[0].click();", confirm)
            time.sleep(2)

            logger.info("批量修改执行完成")
            return True
        except Exception as e:
            logger.error(f"批量修改执行失败: {str(e)}")
            return False

    @staticmethod
    def _fill_cell_js(page, cell_locator, value, field_name="单元格"):
        """使用JavaScript填写单元格内容"""
        try:
            logger.info(f"开始填写{field_name}: {value}")
            wait = WebDriverWait(page.driver, 10)
            cell = wait.until(
                EC.presence_of_element_located(cell_locator)
            )

            # 使用JavaScript直接设置值
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
            page.driver.execute_script(js_script, cell, value)
            time.sleep(1)

            logger.info(f"成功填写{field_name}")
            return True
        except Exception as e:
            logger.error(f"填写{field_name}失败: {str(e)}")
            return False

    @staticmethod
    def _fill_cell_value(page, cell_locator, value, field_name="单元格"):
        """通用的单元格填写方法"""
        try:
            logger.info(f"开始填写{field_name}: {value}")
            wait = WebDriverWait(page.driver, 10)
            cell = wait.until(
                EC.presence_of_element_located(cell_locator)
            )

            # 使用JavaScript触发双击
            page.driver.execute_script("""
                var event = new MouseEvent('dblclick', {
                    'view': window,
                    'bubbles': true,
                    'cancelable': true
                });
                arguments[0].dispatchEvent(event);
            """, cell)
            time.sleep(1)

            # 使用 ActionChains 输入
            actions = ActionChains(page.driver)
            actions.send_keys(value).send_keys(Keys.ENTER).perform()
            time.sleep(1)

            logger.info(f"成功填写{field_name}")
            return True
        except Exception as e:
            logger.error(f"填写{field_name}失败: {str(e)}")
            return False

    @staticmethod
    def _select_dropdown_option(page, dropdown_locator, option_locator):
        """选择下拉选项"""
        try:
            wait = WebDriverWait(page.driver, 10)
            dropdown = wait.until(EC.element_to_be_clickable(dropdown_locator))

            # 滚动到元素位置
            page.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                dropdown
            )
            time.sleep(1)

            # 点击下拉框
            try:
                dropdown.click()
            except:
                page.driver.execute_script("arguments[0].click();", dropdown)
            time.sleep(1)

            # 选择选项
            option = wait.until(EC.element_to_be_clickable(option_locator))
            try:
                option.click()
            except:
                page.driver.execute_script("arguments[0].click();", option)
            time.sleep(1)

            return True
        except Exception as e:
            logger.error(f"选择下拉选项失败: {str(e)}")
            return False

    @staticmethod
    def perform_case_search(page, case_number="2025", case_name="(2025)苏0105民初0001号"):
        """执行案件查询"""
        try:
            logger.info("开始执行案件查询")
            wait = WebDriverWait(page.driver, 10)

            # 1. 点击承办人/助理下拉框
            logger.info("点击承办人/助理下拉框")
            handler_dropdown = wait.until(
                EC.element_to_be_clickable(page.locators.HANDLER_DROPDOWN)
            )
            handler_dropdown.click()
            time.sleep(1)

            # 2. 选择全部
            logger.info("选择全部")
            all_option = wait.until(
                EC.element_to_be_clickable(page.locators.HANDLER_ALL_OPTION)
            )
            all_option.click()
            time.sleep(2)

            # 3. 输入案件编号
            logger.info(f"输入案件编号: {case_number}")
            case_number_input = wait.until(
                EC.element_to_be_clickable(page.locators.CASE_NUMBER_INPUT)
            )
            case_number_input.clear()
            case_number_input.send_keys(case_number)
            time.sleep(1)

            # 4. 输入案件名称
            logger.info(f"输入案件名称: {case_name}")
            case_name_input = wait.until(
                EC.element_to_be_clickable(page.locators.CASE_NAME_INPUT)
            )
            case_name_input.clear()
            case_name_input.send_keys(case_name)
            time.sleep(1)

            # 5. 点击判决书状态下拉框
            logger.info("点击判决书状态下拉框")
            judgment_status = wait.until(
                EC.element_to_be_clickable(page.locators.JUDGMENT_STATUS_DROPDOWN)
            )
            judgment_status.click()
            time.sleep(1)

            # 6. 选择未生成状态
            logger.info("选择未生成状态")
            not_generated = wait.until(
                EC.element_to_be_clickable(page.locators.JUDGMENT_STATUS_NOT_GENERATED)
            )
            not_generated.click()
            time.sleep(1)

            # 7. 点击查询按钮
            logger.info("点击查询按钮")
            search_button = wait.until(
                EC.element_to_be_clickable(page.locators.SEARCH_BUTTON)
            )
            search_button.click()
            time.sleep(2)

            logger.info("案件查询执行完成")
            return True

        except Exception as e:
            logger.error(f"案件查询执行失败: {str(e)}")
            return False

    @staticmethod
    def reset_search_form(page):
        """重置查询表单"""
        try:
            logger.info("开始重置查询表单")
            wait = WebDriverWait(page.driver, 10)

            # 点击重置按钮
            reset_button = wait.until(
                EC.element_to_be_clickable(page.locators.RESET_BUTTON)
            )
            reset_button.click()
            time.sleep(2)

            logger.info("查询表单重置完成")
            return True

        except Exception as e:
            logger.error(f"重置查询表单失败: {str(e)}")
            return False