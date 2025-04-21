import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

from pages.read_notes_page import ReadNotesPage
from utils.TextSelection import TextSelectionUtils
from utils.logger import Logger

logger = Logger().get_logger()


class ReadNotesUtils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 默认等待时间10秒
        self.short_wait = WebDriverWait(driver, 5)  # 短等待时间5秒
        self.long_wait = WebDriverWait(driver, 20)  # 长等待时间20秒

    def wait_for_element_clickable(self, locator, timeout=10, description=""):
        """
        等待元素可点击
        :param locator: 元素定位器
        :param timeout: 超时时间
        :param description: 元素描述，用于日志
        :return: 可点击的元素
        """
        try:
            logger.info(f"等待元素可点击: {description if description else locator}")
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            logger.error(f"等待元素可点击超时: {description if description else locator}")
            raise

    def safe_click(self, locator, description="", timeout=10):
        """
        安全点击元素，包含重试机制
        :param locator: 元素定位器
        :param description: 元素描述
        :param timeout: 超时时间
        """
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                element = self.wait_for_element_clickable(locator, timeout, description)
                element.click()
                logger.info(f"成功点击元素: {description if description else locator}")
                time.sleep(0.5)  # 点击后短暂等待
                return
            except ElementClickInterceptedException:
                if attempt == max_attempts - 1:
                    logger.error(f"元素点击失败，已重试{max_attempts}次")
                    raise
                time.sleep(1)
                continue

    @allure.step("打开阅卷笔记")
    def open_reading_notes(self):
        """打开阅卷笔记"""
        from pages.read_notes_page import ReadNotesPage
        logger.info("开始打开阅卷笔记")
        try:
            self.safe_click(ReadNotesPage.REVIEW_NOTES_BUTTON, "阅卷笔记按钮")
            time.sleep(2)  # 等待页面加载
            logger.info("阅卷笔记打开成功")
        except Exception as e:
            logger.error(f"打开阅卷笔记失败: {str(e)}")
            raise

    @allure.step("操作判决书")
    def operate_judgment_doc(self):
        """操作判决书相关功能"""
        from pages.read_notes_page import ReadNotesPage
        logger.info("开始操作判决书")
        try:
            # 点击判决书
            self.safe_click(ReadNotesPage.JUDGMENT_DOC, "判决书选项")
            time.sleep(2)  # 等待文档加载

            # 缩小操作
            self.safe_click(ReadNotesPage.ZOOM_OUT, "缩小按钮")
            time.sleep(1)

            # 放大操作
            self.safe_click(ReadNotesPage.ZOOM_IN, "放大按钮")
            time.sleep(1)

            # 下载操作
            self.safe_click(ReadNotesPage.DOWNLOAD, "下载按钮")
            time.sleep(1)
            self.safe_click(ReadNotesPage.PDF_DOWNLOAD, "PDF下载选项", timeout=15)
            time.sleep(2)  # 等待下载对话框

            # 关闭预览
            self.safe_click(ReadNotesPage.CLOSE_PREVIEW, "关闭预览按钮")
            time.sleep(1)

            logger.info("判决书操作完成")
        except Exception as e:
            logger.error(f"判决书操作失败: {str(e)}")
            raise

    @allure.step("操作证据引用")
    def operate_evidence_reference(self):
        """操作证据引用相关功能"""
        from pages.read_notes_page import ReadNotesPage
        logger.info("开始操作证据引用")
        try:
            # 点击证据引用标签
            self.safe_click(ReadNotesPage.EVIDENCE_TAB, "证据引用标签")
            time.sleep(2)

            # 选择庭审笔录
            self.safe_click(ReadNotesPage.COURT_RECORD_3, "庭审笔录3")
            time.sleep(2)  # 等待文档加载

            # 旋转操作
            self.safe_click(ReadNotesPage.ROTATE_CLOCKWISE, "顺时针旋转")
            time.sleep(1)
            self.safe_click(ReadNotesPage.ROTATE_COUNTER_CLOCKWISE, "逆时针旋转")
            time.sleep(1)

            # 视图操作
            self.safe_click(ReadNotesPage.VIEW_BUTTON, "视图按钮")
            time.sleep(1)
            self.safe_click(ReadNotesPage.DOUBLE_PAGE_VIEW, "双页视图")
            time.sleep(2)

            # 全屏操作
            self.safe_click(ReadNotesPage.FULLSCREEN, "全屏按钮")
            time.sleep(2)
            self.safe_click(ReadNotesPage.EXIT_FULLSCREEN, "退出全屏")
            time.sleep(1)

            # 关闭预览
            self.safe_click(ReadNotesPage.CLOSE_PREVIEW, "关闭预览")
            time.sleep(1)

            logger.info("证据引用操作完成")
        except Exception as e:
            logger.error(f"证据引用操作失败: {str(e)}")
            raise

    @allure.step("执行查找和替换")
    def search_and_replace(self, search_text, replace_text):
        """
        执行查找和替换操作
        :param search_text: 要查找的文本
        :param replace_text: 要替换的文本
        """
        from pages.read_notes_page import ReadNotesPage
        logger.info(f"开始执行查找替换: 查找'{search_text}', 替换为'{replace_text}'")
        try:
            # 点击查找替换按钮
            self.safe_click(ReadNotesPage.SEARCH_REPLACE, "查找替换按钮")
            time.sleep(1)

            # 输入查找内容
            find_input = self.wait_for_element_clickable(ReadNotesPage.FIND_INPUT, 10, "查找输入框")
            find_input.clear()
            find_input.send_keys(search_text)
            time.sleep(1)

            # 输入替换内容
            replace_input = self.wait_for_element_clickable(ReadNotesPage.REPLACE_INPUT, 10, "替换输入框")
            replace_input.clear()
            replace_input.send_keys(replace_text)
            time.sleep(1)

            # 执行查找
            self.safe_click(ReadNotesPage.FIND_BUTTON, "查找按钮")
            time.sleep(1)

            # 执行替换
            self.safe_click(ReadNotesPage.REPLACE_BUTTON, "替换按钮")
            time.sleep(1)

            # 执行全部替换
            self.safe_click(ReadNotesPage.REPLACE_ALL_BUTTON, "全部替换按钮")
            time.sleep(2)

            # 关闭对话框
            self.safe_click(ReadNotesPage.CLOSE_DIALOG, "关闭对话框")
            time.sleep(1)

            logger.info("查找替换操作完成")
        except Exception as e:
            logger.error(f"查找替换操作失败: {str(e)}")
            raise

    @allure.step("保存阅卷笔记")
    def save_notes(self):
        """保存阅卷笔记"""
        from pages.read_notes_page import ReadNotesPage
        logger.info("开始保存阅卷笔记")
        try:
            self.safe_click(ReadNotesPage.SAVE_BUTTON, "保存按钮")
            time.sleep(2)  # 等待保存完成
            logger.info("阅卷笔记保存成功")
        except Exception as e:
            logger.error(f"保存阅卷笔记失败: {str(e)}")
            raise

    @allure.step("导出阅卷笔记")
    def export_notes(self):
        """导出阅卷笔记"""
        from pages.read_notes_page import ReadNotesPage
        logger.info("开始导出阅卷笔记")
        try:
            self.safe_click(ReadNotesPage.EXPORT_NOTES, "导出按钮", timeout=15)
            time.sleep(3)  # 等待导出完成
            logger.info("阅卷笔记导出成功")
        except Exception as e:
            logger.error(f"导出阅卷笔记失败: {str(e)}")
            raise

    def switch_to_notes_frame(self):
        """切换到阅卷笔记的iframe"""
        try:
            logger.info("尝试切换到阅卷笔记iframe")
            self.driver.switch_to.default_content()
            time.sleep(0.5)
            iframe = self.wait.until(
                EC.presence_of_element_located(ReadNotesPage.NOTES_IFRAME)
            )
            self.driver.switch_to.frame(iframe)
            logger.info("成功切换到iframe")
            time.sleep(0.5)
        except Exception as e:
            logger.error(f"切换到iframe失败: {str(e)}")
            raise

    def switch_to_main_content(self):
        """切换回主文档"""
        try:
            self.driver.switch_to.default_content()
            logger.info("已切换回主文档")
            time.sleep(1)
        except Exception as e:
            logger.error(f"切换回主文档失败: {str(e)}")
            raise

    @allure.step("执行文本格式化操作")
    def format_selected_text(self, text_to_select="原告欠款560000元"):
        """对选中文本执行一系列格式化操作"""
        try:
            logger.info(f"开始执行文本格式化操作: {text_to_select}")

            # 1. 切换到iframe并选中文本
            selection_info = TextSelectionUtils.switch_to_frame_and_select_text(
                self.driver,
                ReadNotesPage.NOTES_IFRAME,
                text_to_select
            )

            # 2. 触发右键菜单
            TextSelectionUtils.trigger_context_menu_and_keep_selection(self.driver)

            # 3. 切换到主文档
            self.switch_to_main_content()

            # 4. 设置背景色
            logger.info("设置背景色...")
            self.safe_click(ReadNotesPage.BACKGROUND_COLOR_BUTTON, "背景色按钮")
            time.sleep(0.5)
            self.safe_click(ReadNotesPage.RED_COLOR_OPTION, "红色背景色")
            time.sleep(0.5)

            # 5. 切回iframe重新选择文本
            self.switch_to_notes_frame()
            TextSelectionUtils.reselect_text_in_frame(self.driver, text_to_select)

            # 切回主文档继续其他操作
            self.switch_to_main_content()

            # 6. 更改字体为楷体
            logger.info("开始更改字体...")
            self.safe_click(ReadNotesPage.FONT_FANGSONG, "仿宋字体按钮")
            time.sleep(0.5)
            self.safe_click(ReadNotesPage.FONT_KAITI, "楷体选项")
            time.sleep(0.5)

            # 7. 更改字号为二号
            logger.info("开始更改字号...")
            self.safe_click(ReadNotesPage.FONT_SIZE_BUTTON, "字号按钮")
            time.sleep(0.5)
            self.safe_click(ReadNotesPage.FONT_SIZE_ER_HAO, "二号字号选项")
            time.sleep(0.5)

            # 8. 设置行高为1.75
            logger.info("开始设置行高...")
            self.safe_click(ReadNotesPage.PARAGRAPH_FORMAT_BUTTON, "格式按钮")
            time.sleep(0.5)
            self.safe_click(ReadNotesPage.LINE_HEIGHT_BUTTON, "行高按钮")
            time.sleep(0.5)
            self.safe_click(ReadNotesPage.LINE_HEIGHT_175, "1.75行高选项")
            time.sleep(0.5)

            # 9. 设置加粗和斜体
            logger.info("开始设置文字样式...")
            self.safe_click(ReadNotesPage.BOLD_BUTTON, "加粗按钮")
            time.sleep(0.5)
            self.safe_click(ReadNotesPage.ITALIC_BUTTON, "斜体按钮")
            time.sleep(0.5)

            # 10. 保存
            logger.info("开始保存...")
            self.safe_click(ReadNotesPage.SAVE_BUTTON, "保存按钮")
            time.sleep(2)

            # 11. 清除格式
            logger.info("开始清除格式...")
            self.safe_click(ReadNotesPage.CLEAR_FORMAT_BUTTON, "清除格式按钮")
            time.sleep(1)

            # 12. 再次保存
            logger.info("再次保存...")
            self.safe_click(ReadNotesPage.SAVE_BUTTON, "保存按钮")
            time.sleep(2)

            logger.info("所有文本格式化操作完成")

        except Exception as e:
            logger.error(f"文本格式化操作失败: {str(e)}")
            if hasattr(self, 'driver'):
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "操作失败截图",
                    allure.attachment_type.PNG
                )
            raise

    @allure.step("选中文本并选择AI智能问答和构成要件")
    def select_text_and_use_ai_qa(self, text_to_select="全国银行间同业拆借"):
        """
        模拟鼠标滑动选中文本并使用AI智能问答功能
        Args:
            text_to_select: 要选择的文本，默认为"全国银行间同业拆借"
        """
        try:
            logger.info(f"开始选中文本并使用AI智能问答: {text_to_select}")

            # 1. 切换到iframe并选中文本
            selection_info = TextSelectionUtils.switch_to_frame_and_select_text(
                self.driver,
                ReadNotesPage.NOTES_IFRAME,
                text_to_select
            )

            # 2. 切换到主文档
            self.switch_to_main_content()

            # 点击清除格式，触发弹框
            logger.info("开始清除格式...")
            self.safe_click(ReadNotesPage.CLEAR_FORMAT_BUTTON, "清除格式按钮")
            time.sleep(1)

            # 3. 等待并点击AI智能问答按钮
            logger.info("等待AI智能问答按钮...")
            self.safe_click(ReadNotesPage.AI_QA_BUTTON, "点击AI回答按钮")
            logger.info("已点击AI智能问答按钮")

            # 4. 等待5秒
            logger.info("等待5秒...")
            time.sleep(5)

            # 5. 点击关闭弹框按钮
            logger.info("准备关闭弹框...")
            self.safe_click(ReadNotesPage.CLOSE_AI_QA_DIALOG, "关闭弹框")
            logger.info("已关闭弹框")

            # 点击清除格式，触发弹框
            logger.info("开始清除格式...")
            self.safe_click(ReadNotesPage.CLEAR_FORMAT_BUTTON, "清除格式按钮")
            time.sleep(1)

            # 6. 等待并点击构成要件按钮
            logger.info("等待构成要件按钮...")
            self.safe_click(
                ReadNotesPage.CONSTITUENT_ELEMENTS_BUTTON,
                "点击构成要件按钮"
            )
            logger.info("已点击构成要件按钮")

            # 7. 等待5秒
            logger.info("等待5秒...")
            time.sleep(5)

            # 8. 点击关闭弹框按钮
            logger.info("准备关闭弹框...")
            self.safe_click(ReadNotesPage.CLOSE_AI_QA_DIALOG, "关闭弹框")
            logger.info("已关闭弹框")

            # 9. 切回iframe重新选择文本以保持状态
            self.switch_to_notes_frame()
            TextSelectionUtils.reselect_text_in_frame(self.driver, text_to_select)

            logger.info("选中文本并使用AI智能问答操作完成")

        except Exception as e:
            logger.error(f"选中文本并使用AI智能问答失败: {str(e)}")
            if hasattr(self, 'driver'):
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "操作失败截图",
                    allure.attachment_type.PNG
                )
            raise

