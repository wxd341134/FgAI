import time
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.search_annotations_page import SearchAnnotationsPage
from utils.logger import Logger
from utils.JStextSelection import JSTextSelector

logger = Logger().get_logger()

class SearchAnnotationsUtils:
    """检索批注工具类"""

    def __init__(self, driver):
        """
        初始化
        Args:
            driver: WebDriver实例
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    @allure.step("点击元素: {element_name}")
    def click_element(self, locator, element_name):
        """
        点击元素的通用方法
        Args:
            locator: 元素定位器
            element_name: 元素名称（用于日志）
        """
        try:
            logger.info(f"尝试点击元素: {element_name}")
            element = self.wait.until(EC.element_to_be_clickable(locator))

            # 滚动到元素位置
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                element
            )
            time.sleep(0.5)  # 等待滚动完成

            # 确保元素可见和可点击
            self.wait.until(EC.visibility_of(element))
            self.wait.until(EC.element_to_be_clickable(element))

            # 尝试直接点击
            try:
                element.click()
            except:
                # 如果直接点击失败，尝试使用JavaScript点击
                self.driver.execute_script("arguments[0].click();", element)

            logger.info(f"成功点击元素: {element_name}")

        except Exception as e:
            logger.error(f"点击元素失败 {element_name}: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                f"点击{element_name}失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("输入文本: {text}")
    def input_text(self, locator, text, element_name):
        """
        输入文本的通用方法
        Args:
            locator: 元素定位器
            text: 要输入的文本
            element_name: 元素名称（用于日志）
        """
        try:
            logger.info(f"尝试在{element_name}中输入文本: {text}")
            element = self.wait.until(EC.presence_of_element_located(locator))

            # 确保元素可见和可交互
            self.wait.until(EC.visibility_of(element))

            # 清除现有文本
            element.clear()
            time.sleep(0.5)

            # 输入新文本
            element.send_keys(text)
            logger.info(f"成功输入文本: {text}")

        except Exception as e:
            logger.error(f"输入文本失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "输入文本失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("使用JS选中文本: {text}")
    def select_text_by_js(self, text):
        """
        使用JavaScript选中指定文本
        Args:
            text: 要选中的文本
        """
        return JSTextSelector.select_text(self.driver, text)

    @allure.step("执行检索批注")
    def add_annotation(self, text_to_select="如下文档", annotation_text="123456"):
        """
        执行完整的检索批注流程
        Args:
            text_to_select: 要选中的文本
            annotation_text: 批注内容
        """
        try:
            # 1. 点击辅助阅卷
            with allure.step("点击辅助阅卷"):
                self.click_element(
                    SearchAnnotationsPage.ASSIST_READ_BUTTON,
                    "辅助阅卷按钮"
                )
                time.sleep(1)

            # 2. 点击AI助手安装文档
            with allure.step("点击AI助手安装文档"):
                self.click_element(
                    SearchAnnotationsPage.AI_ASSISTANT_DOC,
                    "AI助手安装文档"
                )
                time.sleep(2)

            # 3. 使用JS选中文本
            with allure.step(f"选中文本: {text_to_select}"):
                JSTextSelector.select_text(self.driver, text_to_select)
                time.sleep(1)

            # 4. 点击批注按钮
            with allure.step("点击批注按钮"):
                self.click_element(
                    SearchAnnotationsPage.ANNOTATION_BUTTON,
                    "批注按钮"
                )

            # 5. 输入批注内容
            with allure.step("输入批注内容"):
                self.input_text(
                    SearchAnnotationsPage.ANNOTATION_INPUT,
                    annotation_text,
                    "批注输入框"
                )

            # 6. 点击标签下拉框
            with allure.step("点击标签下拉框"):
                self.click_element(
                    SearchAnnotationsPage.LABEL_DROPDOWN,
                    "标签下拉框"
                )
                time.sleep(0.5)

            # 7. 选择证据标签
            with allure.step("选择证据标签"):
                self.click_element(
                    SearchAnnotationsPage.EVIDENCE_LABEL,
                    "证据标签"
                )

            # 8. 保存批注
            with allure.step("保存批注"):
                self.click_element(
                    SearchAnnotationsPage.SAVE_BUTTON,
                    "保存按钮"
                )
                time.sleep(1)

            logger.info("检索批注流程执行完成")

        except Exception as e:
            logger.error(f"检索批注流程失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "检索批注失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("编辑批注")
    def edit_annotation(self, new_text="123456修改"):
        """
        编辑现有批注
        Args:
            new_text: 新的批注内容
        """
        try:
            logger.info("开始执行编辑批注流程...")

            # 1. 点击编辑按钮
            with allure.step("点击编辑按钮"):
                self.click_element(
                    SearchAnnotationsPage.EDIT_ANNOTATION_BUTTON,
                    "编辑批注按钮"
                )
                time.sleep(1)

            # 2. 修改批注内容
            with allure.step(f"修改批注内容为: {new_text}"):
                self.input_text(
                    SearchAnnotationsPage.EDIT_TEXTAREA,
                    new_text,
                    "批注编辑框"
                )
                time.sleep(1)

            # 3. 点击标签下拉框
            with allure.step("点击标签下拉框"):
                self.click_element(
                    SearchAnnotationsPage.EDIT_LABEL_DROPDOWN,
                    "标签下拉框"
                )
                time.sleep(1)

            # 4. 选择法律法规标签
            with allure.step("选择法律法规标签"):
                self.click_element(
                    SearchAnnotationsPage.LEGAL_REGULATIONS_LABEL,
                    "法律法规标签"
                )

            # 5. 点击确定按钮
            with allure.step("点击确定按钮"):
                self.click_element(
                    SearchAnnotationsPage.CONFIRM_BUTTON,
                    "确定按钮"
                )
                time.sleep(1)

            logger.info("编辑批注流程执行完成")

        except Exception as e:
            logger.error(f"编辑批注失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "编辑批注失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("删除批注")
    def delete_annotation(self):
        """删除指定的批注"""
        try:
            logger.info("开始执行删除批注流程...")

            # 1. 点击删除按钮
            with allure.step("点击删除按钮"):
                self.click_element(
                    SearchAnnotationsPage.DELETE_ANNOTATION_BUTTON,
                    "删除批注按钮"
                )
                time.sleep(0.5)  # 等待确认对话框显示

            # 2. 点击确定按钮
            with allure.step("确认删除"):
                self.click_element(
                    SearchAnnotationsPage.DELETE_CONFIRM_BUTTON,
                    "确认删除按钮"
                )
                time.sleep(1)  # 等待删除操作完成

            logger.info("删除批注流程执行完成")

        except Exception as e:
            logger.error(f"删除批注失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "删除批注失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("引用法条")
    def cite_law(self, text_to_select="服务器", search_keyword="诉讼法"):
        """
        引用法条
        Args:
            text_to_select: 要选中的文本
            search_keyword: 搜索关键词
        """
        try:
            logger.info("开始执行引用法条流程...")

            # 1. 选中文本
            with allure.step(f"选中文本: {text_to_select}"):
                JSTextSelector.select_text(self.driver, text_to_select)
                time.sleep(1)

            # 2. 点击检索
            with allure.step("点击检索"):
                self.click_element(
                    SearchAnnotationsPage.SEARCH_LINK,
                    "检索链接"
                )
                time.sleep(1)

            # 3. 输入搜索内容
            with allure.step(f"输入搜索内容: {search_keyword}"):
                self.input_text(
                    SearchAnnotationsPage.SEARCH_INPUT,
                    search_keyword,
                    "搜索输入框"
                )

            # 4. 点击搜索按钮
            with allure.step("点击搜索"):
                self.click_element(
                    SearchAnnotationsPage.SEARCH_BUTTON,
                    "搜索按钮"
                )

            # 5. 引用法条
            with allure.step("引用指定法条"):
                self.click_element(
                    SearchAnnotationsPage.LAW_REFERENCE,
                    "法条引用按钮"
                )

            logger.info("引用法条流程执行完成")

        except Exception as e:
            logger.error(f"引用法条失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "引用法条失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("预览法条")
    def preview_law(self):
        """预览法条"""
        try:
            logger.info("开始执行预览法条流程...")

            # 1. 点击预览
            with allure.step("点击预览"):
                self.click_element(
                    SearchAnnotationsPage.PREVIEW_LAW,
                    "法条预览链接"
                )
                time.sleep(1)

            # 2. 关闭预览
            with allure.step("关闭预览"):
                self.click_element(
                    SearchAnnotationsPage.CLOSE_PREVIEW,
                    "关闭预览按钮"
                )

            logger.info("预览法条流程执行完成")

        except Exception as e:
            logger.error(f"预览法条失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "预览法条失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("编辑法条")
    def edit_law(self, new_text="中华人民共和国民事诉讼法修改"):
        """
        编辑法条
        Args:
            new_text: 新的法条内容
        """
        try:
            logger.info("开始执行编辑法条流程...")

            # 1. 点击编辑按钮
            with allure.step("点击编辑按钮"):
                self.click_element(
                    SearchAnnotationsPage.EDIT_LAW_BUTTON,
                    "编辑法条按钮"
                )
                time.sleep(1)

            # 2. 输入新内容
            with allure.step(f"输入新内容: {new_text}"):
                self.input_text(
                    SearchAnnotationsPage.EDIT_LAW_INPUT,
                    new_text,
                    "法条编辑框"
                )

            # 3. 点击标签下拉框
            with allure.step("点击标签下拉框"):
                self.click_element(
                    SearchAnnotationsPage.TAG_DROPDOWN,
                    "标签下拉框"
                )
                time.sleep(0.5)

            # 4. 选择争议焦点标签
            with allure.step("选择争议焦点标签"):
                self.click_element(
                    SearchAnnotationsPage.DISPUTE_FOCUS_OPTION,
                    "争议焦点选项"
                )

            # 5. 点击确定
            with allure.step("确认编辑"):
                self.click_element(
                    SearchAnnotationsPage.CONFIRM_BUTTON,
                    "确认按钮"
                )

            logger.info("编辑法条流程执行完成")

        except Exception as e:
            logger.error(f"编辑法条失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "编辑法条失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("删除法条")
    def delete_law(self):
        """删除法条"""
        try:
            logger.info("开始执行删除法条流程...")

            # 1. 点击删除按钮
            with allure.step("点击删除按钮"):
                self.click_element(
                    SearchAnnotationsPage.DELETE_LAW_BUTTON,
                    "删除法条按钮"
                )
                time.sleep(0.5)

            # 2. 确认删除
            with allure.step("确认删除"):
                self.click_element(
                    SearchAnnotationsPage.CONFIRM_DELETE,
                    "确认删除按钮"
                )

            logger.info("删除法条流程执行完成")

        except Exception as e:
            logger.error(f"删除法条失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "删除法条失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("页面跳转操作")
    def page_navigation(self):
        """执行页面跳转和文本操作"""
        try:
            logger.info("开始执行页面跳转流程...")

            # 1. 点击打开侧边栏
            with allure.step("打开侧边栏"):
                self.click_element(
                    SearchAnnotationsPage.SIDEBAR_TOGGLE,
                    "侧边栏切换按钮"
                )
                time.sleep(1)

            # 2. 点击选中第3页
            with allure.step("选择第3页"):
                self.click_element(
                    SearchAnnotationsPage.PAGE_THREE,
                    "第3页缩略图"
                )
                time.sleep(2)  # 等待页面加载

            # 3. 选择文本"导入镜像"
            with allure.step("选中文本'导入镜像'"):
                JSTextSelector.select_text(self.driver, "导入镜像")
                time.sleep(1)

            # 4. 点击复制文本
            with allure.step("点击复制文本"):
                self.click_element(
                    SearchAnnotationsPage.COPY_TEXT_BUTTON,
                    "复制文本按钮"
                )
                time.sleep(1)

            # 5. 跳转到第10页
            with allure.step("跳转到第10页"):
                # 点击页数输入框
                page_input = self.wait.until(
                    EC.presence_of_element_located(SearchAnnotationsPage.PAGE_INPUT)
                )
                page_input.click()
                time.sleep(1)

                # 清除现有内容并输入10
                page_input.clear()
                page_input.send_keys("10")
                page_input.send_keys(Keys.RETURN)
                time.sleep(3)  # 等待页面加载

            # 6. 关闭侧边栏
            with allure.step("关闭侧边栏"):
                self.click_element(
                    SearchAnnotationsPage.SIDEBAR_TOGGLE,
                    "侧边栏切换按钮"
                )

            logger.info("页面跳转流程执行完成")

        except Exception as e:
            logger.error(f"页面跳转操作失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "页面跳转失败截图",
                allure.attachment_type.PNG
            )
            raise

