import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.statute_search_page import StatuteSearchPage
from utils.logger import Logger

logger = Logger().get_logger()

class StatuteSearchUtils:
    """法条检索工具类"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def safe_click(self, locator, element_name):
        """安全点击元素的方法"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"成功点击{element_name}")
        except Exception as e:
            logger.error(f"点击{element_name}失败: {str(e)}")
            raise

    def safe_input(self, locator, text, element_name):
        """安全输入文本的方法"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            logger.info(f"成功在{element_name}中输入文本: {text}")
        except Exception as e:
            logger.error(f"在{element_name}中输入文本失败: {str(e)}")
            raise

    @allure.step("执行完整的法条检索流程")
    def perform_statute_search(self, keyword="身份证"):
        """
        执行完整的法条检索流程
        Args:
            keyword: 搜索关键词
        """
        try:
            logger.info(f"开始执行法条检索流程，关键词: {keyword}")

            # 1. 点击辅助阅卷
            with allure.step("点击辅助阅卷按钮"):
                self.safe_click(
                    StatuteSearchPage.ASSIST_READ_BUTTON,
                    "辅助阅卷按钮"
                )
                time.sleep(1)

            # 2. 点击法条检索
            with allure.step("点击法条检索按钮"):
                self.safe_click(
                    StatuteSearchPage.STATUTE_SEARCH_BUTTON,
                    "法条检索按钮"
                )
                time.sleep(1)

            # 3. 输入搜索内容
            with allure.step(f"输入搜索关键词: {keyword}"):
                self.safe_input(
                    StatuteSearchPage.SEARCH_INPUT,
                    keyword,
                    "搜索输入框"
                )

            # 4. 点击搜索
            with allure.step("点击搜索按钮"):
                self.safe_click(
                    StatuteSearchPage.SEARCH_BUTTON,
                    "搜索按钮"
                )
                time.sleep(2)

            # 5. 点击第一条法条预览
            with allure.step("点击预览第一条法条"):
                self.safe_click(
                    StatuteSearchPage.FIRST_STATUTE_PREVIEW,
                    "第一条法条预览"
                )
                time.sleep(2)

            # 6. 关闭预览
            with allure.step("关闭法条预览"):
                self.safe_click(
                    StatuteSearchPage.CLOSE_PREVIEW_BUTTON,
                    "关闭预览按钮"
                )
                time.sleep(1)

            # 7. 关闭搜索
            with allure.step("关闭法条检索"):
                self.safe_click(
                    StatuteSearchPage.CLOSE_SEARCH_BUTTON,
                    "关闭搜索按钮"
                )

            logger.info("法条检索流程执行完成")

        except Exception as e:
            logger.error(f"法条检索流程执行失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise