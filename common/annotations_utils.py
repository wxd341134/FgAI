import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.annotations_page import SearchAnnotationsPage
from utils.logger import Logger

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
        try:
            logger.info(f"尝试使用JS选中文本: {text}")

            js_script = """
            function selectText(searchText) {
                const textNodes = [];

                // 递归查找文本节点
                function findTextNodes(node) {
                    if (node.nodeType === 3) {
                        if (node.textContent.includes(searchText)) {
                            textNodes.push(node);
                        }
                    } else {
                        for (let child of node.childNodes) {
                            findTextNodes(child);
                        }
                    }
                }

                findTextNodes(document.body);

                if (textNodes.length === 0) {
                    return false;
                }

                // 使用第一个匹配的文本节点
                const textNode = textNodes[0];
                const range = document.createRange();
                const content = textNode.textContent;
                const startIndex = content.indexOf(searchText);

                // 设置选区
                range.setStart(textNode, startIndex);
                range.setEnd(textNode, startIndex + searchText.length);

                // 应用选区
                const selection = window.getSelection();
                selection.removeAllRanges();
                selection.addRange(range);

                // 滚动到选区
                const element = textNode.parentElement;
                element.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });

                return true;
            }

            return selectText(arguments[0]);
            """

            result = self.driver.execute_script(js_script, text)

            if not result:
                raise Exception(f"未找到文本: {text}")

            time.sleep(1)  # 等待选中效果
            logger.info(f"成功选中文本: {text}")

        except Exception as e:
            logger.error(f"选中文本失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "选中文本失败截图",
                allure.attachment_type.PNG
            )
            raise

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
                self.select_text_by_js(text_to_select)
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

    @allure.step("添加并编辑批注")
    def add_and_edit_annotation(self, text_to_select="如下文档", initial_text="123456", edited_text="123456修改"):
        """
        添加批注并编辑
        Args:
            text_to_select: 要选中的文本
            initial_text: 初始批注内容
            edited_text: 编辑后的批注内容
        """
        try:
            # 先添加批注
            self.add_annotation(text_to_select, initial_text)
            time.sleep(1)  # 等待添加完成

            # 然后编辑批注
            self.edit_annotation(edited_text)

            logger.info("添加并编辑批注流程执行完成")

        except Exception as e:
            logger.error(f"添加并编辑批注失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "添加并编辑批注失败截图",
                allure.attachment_type.PNG
            )
            raise