import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.archives_search_page import ArchivesSearchPage
from utils.Common_utils import CommonUtils
from utils.logger import Logger

logger = Logger().get_logger()

class ArchivesSearchUtils(CommonUtils):  # 继承父类CommonUtils，也会继承父类属性和方法
    """卷宗检索工具类"""

    def __init__(self, driver):
        super().__init__(driver)  # ✅ 调用父类初始化

    @allure.step("执行完整的卷宗检索流程")
    def perform_archives_search(self, keyword="判决"):
        """
        执行完整的卷宗检索流程
        Args:
            keyword: 搜索关键词
        """
        try:
            logger.info(f"开始执行卷宗检索流程，关键词: {keyword}")

            # 1. 点击辅助阅卷
            with allure.step("点击辅助阅卷按钮"):
                self.click_element(
                    ArchivesSearchPage.ASSIST_READ_BUTTON,
                    "辅助阅卷按钮"
                )
                time.sleep(1)

            # 1. 点击卷宗检索
            with allure.step("点击卷宗检索按钮"):
                self.click_element(
                    ArchivesSearchPage.ARCHIVES_SEARCH_BUTTON,
                    "卷宗检索按钮"
                )
                time.sleep(1)

            # 2. 输入搜索内容
            with allure.step(f"输入搜索关键词: {keyword}"):
                self.input_text(
                    ArchivesSearchPage.SEARCH_INPUT,
                    keyword,
                    "搜索输入框"
                )

            # 3. 点击搜索
            with allure.step("点击搜索按钮"):
                self.click_element(
                    ArchivesSearchPage.SEARCH_BUTTON,
                    "搜索按钮"
                )
                time.sleep(2)

            # 4. 点击预览卷宗
            with allure.step("点击预览卷宗"):
                self.click_element(
                    ArchivesSearchPage.PREVIEW_ARCHIVE,
                    "预览卷宗按钮"
                )
                time.sleep(2)

            # 5. 关闭预览
            with allure.step("关闭卷宗预览"):
                self.click_element(
                    ArchivesSearchPage.CLOSE_PREVIEW_BUTTON,
                    "关闭预览按钮"
                )
                time.sleep(2)

            # 6. 点击仅显示文件名
            with allure.step("勾选仅显示文件名"):
                self.click_element(
                    ArchivesSearchPage.FILENAME_ONLY_CHECKBOX,
                    "仅显示文件名复选框"
                )
                time.sleep(1)

            # 7. 关闭搜索
            with allure.step("关闭卷宗检索"):
                self.click_element(
                    ArchivesSearchPage.CLOSE_SEARCH_BUTTON,
                    "关闭搜索按钮"
                )
                time.sleep(1)


            logger.info("卷宗检索流程执行完成")

        except Exception as e:
            logger.error(f"卷宗检索流程执行失败: {str(e)}")
            raise