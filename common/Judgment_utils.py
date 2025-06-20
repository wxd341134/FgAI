import os
import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.Judgment_page import JudgmentPage
from utils.common import get_project_root
from utils.logger import Logger

logger = Logger().get_logger()


class JudgmentUtils:
    """判决书功能操作工具类"""

    def __init__(self, driver):
        """
        初始化判决书工具类
        :param driver: WebDriver实例
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator, element_name):
        """
        点击元素的通用方法
        :param locator: 元素定位器
        :param element_name: 元素名称
        """
        try:
            logger.info(f"尝试点击元素: {element_name}")
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"成功点击元素: {element_name}")
        except Exception as e:
            logger.error(f"点击元素失败 {element_name}: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                f"点击{element_name}失败截图",
                allure.attachment_type.PNG
            )
            raise

    def enter_judgment(self):
        """进入判决书"""
        with allure.step("进入判决书"):
            self.click_element(JudgmentPage.ENTER_JUDGMENT, "进入判决书按钮")
            time.sleep(2)

    def open_record_tab(self):
        """打开笔录标签"""
        with allure.step("打开笔录标签"):
            self.click_element(JudgmentPage.RECORD_TAB, "笔录标签")
            time.sleep(1)

    def toggle_record_sidebar(self):
        """切换笔录侧边栏"""
        with allure.step("切换笔录侧边栏"):
            self.click_element(JudgmentPage.RECORD_SIDEBAR, "笔录侧边栏按钮")
            time.sleep(2)

    def toggle_preview_sidebar(self):
        """切换笔录侧边栏"""
        with allure.step("切换卷宗侧边栏"):
            self.click_element(JudgmentPage.RECORD_PREVIEW, "卷宗侧边栏按钮")
            time.sleep(2)

    def goto_page(self, page_number):
        """
        跳转到指定页码
        :param page_number: 目标页码
        """
        with allure.step(f"跳转到第{page_number}页"):
            try:
                logger.info(f"准备跳转到第{page_number}页")
                input_element = self.wait.until(
                    EC.presence_of_element_located(JudgmentPage.PAGE_INPUT)
                )
                input_element.clear()
                input_element.send_keys(str(page_number))
                input_element.send_keys(Keys.ENTER)
                logger.info(f"成功跳转到第{page_number}页")
                time.sleep(1)
            except Exception as e:
                logger.error(f"页面跳转失败: {str(e)}")
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "页面跳转失败截图",
                    allure.attachment_type.PNG
                )
                raise

    def switch_to_double_page_view(self):
        """切换到双页视图"""
        with allure.step("切换到双页视图"):
            self.click_element(JudgmentPage.VIEW_BUTTON, "视图按钮")
            self.click_element(JudgmentPage.DOUBLE_PAGE_VIEW, "双页视图选项")
            time.sleep(1)

    def zoom_operations(self):
        """执行缩放操作"""
        with allure.step("执行缩放操作"):
            self.click_element(JudgmentPage.ZOOM_OUT, "缩小按钮")
            time.sleep(0.5)
            self.click_element(JudgmentPage.ZOOM_IN, "放大按钮")
            time.sleep(0.5)

    def rotate_operations(self):
        """执行旋转操作"""
        with allure.step("执行旋转操作"):
            self.click_element(JudgmentPage.ROTATE_CLOCKWISE, "顺时针旋转按钮")
            time.sleep(0.5)
            self.click_element(JudgmentPage.ROTATE_COUNTERCLOCKWISE, "逆时针旋转按钮")
            time.sleep(0.5)

    def fullscreen_operations(self):
        """执行全屏操作"""
        with allure.step("执行全屏操作"):
            self.click_element(JudgmentPage.FULLSCREEN, "全屏按钮")
            time.sleep(1)
            self.click_element(JudgmentPage.EXIT_FULLSCREEN, "退出全屏按钮")
            time.sleep(1)

    def open_ocr(self):
        """打开OCR功能"""
        with allure.step("打开OCR功能"):
            self.click_element(JudgmentPage.OCR, "OCR按钮")
            time.sleep(1)

    def edit_ocr_text(self, text):
        """
        编辑OCR文本
        :param text: 要输入的文本
        """
        with allure.step("编辑OCR文本"):
            try:
                logger.info("准备编辑OCR文本")
                textarea = self.wait.until(
                    EC.presence_of_element_located(JudgmentPage.OCR_TEXTAREA)
                )
                textarea.send_keys(text)
                logger.info("OCR文本编辑完成")
                time.sleep(1)
            except Exception as e:
                logger.error(f"OCR文本编辑失败: {str(e)}")
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "OCR文本编辑失败截图",
                    allure.attachment_type.PNG
                )
                raise

    def save_ocr(self):
        """保存OCR内容"""
        with allure.step("保存OCR内容"):
            self.click_element(JudgmentPage.SAVE_BUTTON, "保存按钮")
            time.sleep(1)

    def ocr_zoom_operations(self):
        """OCR内容缩放操作"""
        with allure.step("OCR内容缩放"):
            self.click_element(JudgmentPage.OCR_ZOOM_IN, "OCR放大按钮")
            time.sleep(0.5)
            self.click_element(JudgmentPage.OCR_ZOOM_OUT, "OCR缩小按钮")
            time.sleep(0.5)

    def close_ocr(self):
        """关闭OCR功能"""
        with allure.step("关闭OCR功能"):
            self.click_element(JudgmentPage.CLOSE_BUTTON, "关闭按钮")
            time.sleep(1)

    def download_pdf(self):
        """下载PDF文件"""
        with allure.step("下载PDF文件"):
            self.click_element(JudgmentPage.DOWNLOAD, "下载按钮")
            self.click_element(JudgmentPage.PDF_DOWNLOAD, "PDF下载选项")
            time.sleep(2)

    def preview_judgment_document(self):
        """预览判决书文档"""
        with allure.step("预览判决书文档"):
            # 展开文档树
            self.click_element(JudgmentPage.EXPAND_BUTTON, "展开按钮")
            time.sleep(1)
            # 选择判决书
            self.click_element(JudgmentPage.JUDGMENT_DOC, "判决书选项")
            time.sleep(1)
            # 收起文档树
            self.click_element(JudgmentPage.COLLAPSE_BUTTON, "收起按钮")
            time.sleep(1)

    def switch_to_book_view(self):
        """切换到书籍视图"""
        with allure.step("切换到书籍视图"):
            self.click_element(JudgmentPage.VIEW_BUTTON_PREVIEW, "视图按钮")
            self.click_element(JudgmentPage.BOOK_VIEW, "书籍视图选项")
            time.sleep(1)

    def handle_ocr_operations(self):
        """处理OCR相关操作"""
        with allure.step("OCR操作"):
            self.click_element(JudgmentPage.OCR_PREVIEW, "OCR按钮")
            time.sleep(1)
            self.click_element(JudgmentPage.CLOSE_BUTTON, "关闭OCR按钮")
            time.sleep(1)

    def select_judgment_by_date(self):
        """选择指定日期的判决书"""
        with allure.step("选择2025-04-22的判决书"):
            self.click_element(JudgmentPage.JUDGMENT_SELECT, "判决书选择下拉框")
            time.sleep(1)
            self.click_element(JudgmentPage.JUDGMENT_0422, "2025-04-22的判决书")
            time.sleep(1)

    def export_judgment(self):
        """导出判决书"""
        with allure.step("导出判决书"):
            self.click_element(JudgmentPage.EXPORT_BUTTON, "导出判决书按钮")
            time.sleep(2)

    def import_judgment(self):
        """导入判决书"""
        with allure.step("导入判决书"):
            try:
                # 点击更多按钮
                self.click_element(JudgmentPage.MORE_BUTTON, "更多按钮")
                time.sleep(1)

                # 选择导入选项
                self.click_element(JudgmentPage.IMPORT_OPTION, "导入选项")
                time.sleep(1)

                # 构建文件路径
                file_path = os.path.join(
                    get_project_root(),
                    "test_data",
                    "(2025)苏0105民初0001号民事判决书.docx"
                )
                logger.info(f"上传文件路径: {file_path}")

                # 上传文件
                # 查找隐藏的文件上传input元素
                upload_input = self.driver.execute_script("""
                                   return document.querySelector('input[type="file"]');
                               """)
                # 发送文件路径到input元素
                upload_input.send_keys(file_path)
                logger.info("文件已选择")
                time.sleep(1)

                # 点击确定按钮
                self.click_element(JudgmentPage.CONFIRM_BUTTON, "确定按钮")
                time.sleep(2)

            except Exception as e:
                logger.error(f"导入判决书失败: {str(e)}")
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "导入判决书失败截图",
                    allure.attachment_type.PNG
                )
                raise

    def compare_judgments(self):
        """执行判决书对比操作"""
        with allure.step("执行判决书对比"):
            try:
                # 1. 点击更多按钮
                logger.info("点击更多按钮")
                self.click_element(JudgmentPage.MORE_BUTTON, "更多按钮")
                time.sleep(1)

                # 2. 选择比对选项
                logger.info("选择比对选项")
                self.click_element(JudgmentPage.COMPARE_OPTION, "比对选项")
                time.sleep(1)

                # 3. 选择旧版本
                with allure.step("选择旧版本判决书"):
                    logger.info("选择旧版本判决书")
                    self.click_element(JudgmentPage.OLD_VERSION_SELECT, "旧版本选择框")
                    time.sleep(1)
                    self.click_element(JudgmentPage.OLD_VERSION_0422, "2025-04-22版本")
                    time.sleep(1)

                # 4. 选择新版本
                with allure.step("选择新版本判决书"):
                    logger.info("选择新版本判决书")
                    self.click_element(JudgmentPage.NEW_VERSION_SELECT, "新版本选择框")
                    time.sleep(1)
                    # self.click_element(JudgmentPage.NEW_VERSION_0423, "2025-04-23版本")
                    # time.sleep(1)

                # 5. 执行窗口操作
                with allure.step("执行窗口操作"):
                    logger.info("切换小窗显示")
                    self.click_element(JudgmentPage.SMALL_WINDOW, "小窗按钮")
                    time.sleep(1.5)

                    logger.info("切换大窗显示")
                    self.click_element(JudgmentPage.LARGE_WINDOW, "大窗按钮")
                    time.sleep(1)

                # 6. 关闭对比
                with allure.step("关闭判决书对比"):
                    logger.info("关闭对比窗口")
                    self.click_element(JudgmentPage.CLOSE_COMPARE, "关闭按钮")
                    time.sleep(1)

                logger.info("判决书对比操作完成")
                return True

            except Exception as e:
                logger.error(f"判决书对比操作失败: {str(e)}")
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "判决书对比失败截图",
                    allure.attachment_type.PNG
                )
                raise

    def assist_reading_operations(self):
        """执行辅助阅卷相关操作"""
        with allure.step("执行辅助阅卷操作"):
            try:
                # 1. 打开辅助阅卷
                with allure.step("打开辅助阅卷"):
                    logger.info("点击辅助阅卷按钮")
                    self.click_element(JudgmentPage.ASSIST_READING, "辅助阅卷按钮")
                    time.sleep(1)

                # 2. 选择AI助手安装文档
                with allure.step("选择AI助手安装文档"):
                    logger.info("点击法官AI助手安装文档")
                    self.click_element(JudgmentPage.AI_DOC, "AI助手安装文档")
                    time.sleep(1)

                # 3. 执行视图操作
                with allure.step("执行视图操作"):
                    logger.info("点击缩小按钮")
                    self.click_element(JudgmentPage.ZOOM_OUT2, "缩小按钮")
                    time.sleep(1)

                    logger.info("点击适合页高按钮")
                    self.click_element(JudgmentPage.FIT_HEIGHT2, "适合页高按钮")
                    time.sleep(1)

                # 4. 执行搜索操作
                with allure.step("执行搜索操作"):
                    # 打开搜索框
                    logger.info("打开搜索框")
                    self.click_element(JudgmentPage.SEARCH_BUTTON, "搜索按钮")
                    time.sleep(1)

                    # 输入搜索内容
                    try:
                        logger.info("输入搜索内容")
                        search_input = self.wait.until(
                            EC.presence_of_element_located(JudgmentPage.SEARCH_INPUT)
                        )
                        search_input.clear()
                        search_input.send_keys("安装包")
                        search_input.send_keys(Keys.ENTER)
                        time.sleep(1)
                    except Exception as e:
                        logger.error(f"搜索输入失败: {str(e)}")
                        raise

                    # 点击左箭头
                    logger.info("点击左箭头")
                    self.click_element(JudgmentPage.ARROW_LEFT, "左箭头按钮")
                    time.sleep(1)

                    # 取消高亮
                    logger.info("取消高亮全部")
                    self.click_element(JudgmentPage.HIGHLIGHT_CHECKBOX, "高亮复选框")
                    time.sleep(1)

                    # 关闭搜索框
                    logger.info("关闭搜索框")
                    self.click_element(JudgmentPage.CLOSE_SEARCH, "关闭搜索按钮")
                    time.sleep(1)

                # 5. 返回上一层
                # with allure.step("返回上一层"):
                #     logger.info("点击返回上一层")
                #     self.click_element(JudgmentPage.BACK_BUTTON, "返回上一层按钮")
                #     time.sleep(1)

                logger.info("辅助阅卷操作完成")
                return True

            except Exception as e:
                logger.error(f"辅助阅卷操作失败: {str(e)}")
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "辅助阅卷操作失败截图",
                    allure.attachment_type.PNG
                )
                raise

    def law_search_operations(self):
        """执行法条检索相关操作"""
        with allure.step("执行法条检索操作"):
            try:

                # 1. 打开法条检索
                with allure.step("打开法条检索"):
                    logger.info("点击法条检索按钮")
                    self.click_element(JudgmentPage.LAW_SEARCH, "法条检索按钮")
                    time.sleep(1)

                # 2. 执行法条搜索
                with allure.step("执行法条搜索"):
                    # 输入搜索内容
                    logger.info("输入搜索内容: 证据")
                    search_input = self.wait.until(
                        EC.presence_of_element_located(JudgmentPage.LAW_SEARCH_INPUT)
                    )
                    search_input.clear()
                    search_input.send_keys("刑事案件")
                    time.sleep(1)

                    # 点击搜索按钮
                    logger.info("点击搜索按钮")
                    self.click_element(JudgmentPage.SEARCH_BUTTON2, "搜索按钮")
                    time.sleep(2)

                # 3. 预览法条
                with allure.step("预览法条"):
                    # 点击预览
                    logger.info("点击预览法条")
                    self.click_element(JudgmentPage.LAW_PREVIEW, "法条预览")
                    time.sleep(2)

                    # 在预览中执行搜索
                    logger.info("在预览中执行搜索")
                    self.click_element(JudgmentPage.PREVIEW_SEARCH, "预览搜索按钮")
                    time.sleep(1)

                    # 输入预览搜索内容
                    preview_search = self.wait.until(
                        EC.presence_of_element_located(JudgmentPage.PREVIEW_SEARCH_INPUT)
                    )
                    preview_search.clear()
                    preview_search.send_keys("任务")
                    preview_search.send_keys(Keys.ENTER)
                    time.sleep(1)

                    # 关闭预览
                    logger.info("关闭预览弹框")
                    self.click_element(JudgmentPage.CLOSE_PREVIEW, "关闭预览按钮")
                    time.sleep(1)

                # 4. 翻页操作
                with allure.step("翻页操作"):
                    logger.info("点击第4页")
                    self.click_element(JudgmentPage.PAGE_4, "第4页")
                    time.sleep(1.5)

                # 5. 关闭法条检索
                with allure.step("关闭法条检索"):
                    logger.info("关闭法条检索")
                    self.click_element(JudgmentPage.CLOSE_LAW_SEARCH, "关闭法条检索按钮")
                    time.sleep(2)

                logger.info("法条检索操作完成")
                return True

            except Exception as e:
                logger.error(f"法条检索操作失败: {str(e)}")
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "法条检索操作失败截图",
                    allure.attachment_type.PNG
                )
                raise

    def dossier_search_operations(self):
        """执行卷宗检索相关操作"""
        with allure.step("执行卷宗检索操作"):
            try:
                # 1. 打开卷宗检索
                with allure.step("打开卷宗检索"):
                    logger.info("点击卷宗检索按钮")
                    self.click_element(JudgmentPage.DOSSIER_SEARCH, "卷宗检索按钮")
                    time.sleep(1)

                # 2. 执行搜索操作
                with allure.step("执行搜索操作"):
                    # 输入搜索内容
                    logger.info("输入搜索内容: 被告")
                    search_input = self.wait.until(
                        EC.presence_of_element_located(JudgmentPage.DOSSIER_SEARCH_INPUT)
                    )
                    search_input.clear()
                    search_input.send_keys("被告")
                    time.sleep(1)

                    # 点击搜索按钮
                    logger.info("点击搜索按钮")
                    self.click_element(JudgmentPage.DOSSIER_SEARCH_BUTTON, "搜索按钮")
                    time.sleep(2)

                # 3. 文件名显示切换
                with allure.step("文件名显示切换"):
                    # 勾选仅显示文件名
                    logger.info("勾选仅显示文件名")
                    self.click_element(JudgmentPage.FILENAME_ONLY, "仅显示文件名选项")
                    time.sleep(1)

                    # 取消勾选仅显示文件名
                    logger.info("取消勾选仅显示文件名")
                    self.click_element(JudgmentPage.FILENAME_ONLY, "仅显示文件名选项")
                    time.sleep(1)

                # 4. 查看庭审笔录
                with allure.step("查看庭审笔录"):
                    # 点击庭审笔录3
                    logger.info("点击庭审笔录3")
                    self.click_element(JudgmentPage.TRIAL_RECORD_3, "庭审笔录3")
                    time.sleep(2)

                    # 关闭预览
                    logger.info("关闭预览")
                    self.click_element(JudgmentPage.CLOSE_PREVIEW2, "关闭预览按钮")
                    time.sleep(1)

                # 5. 关闭卷宗检索
                with allure.step("关闭卷宗检索"):
                    logger.info("关闭卷宗检索")
                    self.click_element(JudgmentPage.CLOSE_DOSSIER_SEARCH, "关闭卷宗检索按钮")
                    time.sleep(1)

                logger.info("卷宗检索操作完成")
                return True

            except Exception as e:
                logger.error(f"卷宗检索操作失败: {str(e)}")
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "卷宗检索操作失败截图",
                    allure.attachment_type.PNG
                )
                raise

    def smart_qa_operations(self):
        """执行智能问答相关操作"""
        with allure.step("执行智能问答操作"):
            try:
                # 1. 打开智能问答
                with allure.step("打开智能问答"):
                    logger.info("点击智能问答按钮")
                    self.click_element(JudgmentPage.SMART_QA, "智能问答按钮")
                    time.sleep(1)

                # 2. 点击争议焦点
                with allure.step("查看本案争议焦点"):
                    logger.info("点击本案的争议焦点")
                    self.click_element(JudgmentPage.DISPUTE_FOCUS, "本案的争议焦点")
                    time.sleep(5)  # 等待3秒加载内容

                # 3. 提问操作
                with allure.step("执行提问操作"):
                    # 输入问题
                    logger.info("输入问题: 案件如何定性")
                    question_input = self.wait.until(
                        EC.presence_of_element_located(JudgmentPage.QA_INPUT)
                    )
                    question_input.clear()
                    question_input.send_keys("案件如何定性")
                    time.sleep(1)

                    # 发送问题
                    logger.info("点击发送按钮")
                    self.click_element(JudgmentPage.SEND_BUTTON, "发送按钮")
                    time.sleep(5)  # 等待5秒获取回答

                    # 添加问答内容到报告
                    try:
                        response_element = self.wait.until(
                            EC.presence_of_element_located(JudgmentPage.QA_RESPONSE)
                        )
                        response_text = response_element.text
                        allure.attach(
                            response_text,
                            "智能问答回复内容",
                            allure.attachment_type.TEXT
                        )
                        logger.info(f"获取到回答: {response_text}")
                    except Exception as e:
                        logger.warning(f"未能获取回答内容: {str(e)}")

                # 4. 关闭智能问答
                with allure.step("关闭智能问答"):
                    logger.info("关闭智能问答")
                    self.click_element(JudgmentPage.CLOSE_QA, "关闭按钮")
                    time.sleep(1)

                logger.info("智能问答操作完成")
                return True

            except Exception as e:
                logger.error(f"智能问答操作失败: {str(e)}")
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "智能问答操作失败截图",
                    allure.attachment_type.PNG
                )
                raise






