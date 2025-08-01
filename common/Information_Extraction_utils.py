import datetime
import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.common2 import CommonUtils
from utils.logger import Logger
from pages.Information_Extraction_page import InformationExtractionPage

logger = Logger().get_logger()

class InformationExtractionUtils(CommonUtils):
    """要素提取功能操作工具类"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_user = "wxd341134"

    @allure.step("执行要素提取基本操作")
    def handle_basic_operations(self):
        """执行要素提取基本操作"""
        try:
            # 点击要素提取按钮
            self.click_element(
                InformationExtractionPage.INFO_EXTRACT_BTN,
                "要素提取按钮"
            )

            # 展开文档树
            self.click_element(
                InformationExtractionPage.EXPAND_ICON,
                "展开图标"
            )

            # 选择营业执照
            self.click_element(
                InformationExtractionPage.BUSINESS_LICENSE,
                "营业执照"
            )

            # 收起文档树
            self.click_element(
                InformationExtractionPage.EXPAND_ICON,
                "收起图标"
            )

            logger.info(f"{self.current_time} - {self.current_user} - 要素提取基本操作完成")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 要素提取基本操作失败: {str(e)}")
            return False

    @allure.step("执行OCR操作")
    def handle_ocr_operations(self):
        """
        执行OCR完整操作流程
        包含：
        1. 打开OCR
        2. 文本输入
        3. 保存内容
        4. 窗口操作（最大化、缩小）
        5. 关闭OCR
        """
        try:
            # 1. 打开OCR功能
            with allure.step("打开OCR功能"):
                logger.info(f"{self.current_time} - {self.current_user} - 准备打开OCR功能")
                self.click_element(
                    InformationExtractionPage.OCR_BUTTON,
                    "OCR按钮"
                )
                time.sleep(1)

            # 2. 追加OCR文本（不清除原有内容）
            with allure.step("输入OCR文本"):
                logger.info(f"{self.current_time} - {self.current_user} - 准备输入OCR文本")
                self.input_text(
                    InformationExtractionPage.OCR_TEXTAREA,
                    "123456",
                    "OCR文本框",
                    clear_first=False  # 设置为False表示追加文本
                )
                time.sleep(1)

            # 3. 保存OCR内容
            with allure.step("保存OCR内容"):
                logger.info(f"{self.current_time} - {self.current_user} - 准备保存OCR内容")
                self.click_element(
                    InformationExtractionPage.SAVE_BUTTON,
                    "保存按钮"
                )
                time.sleep(1)

            # 4. 窗口操作
            with allure.step("执行窗口操作"):
                # 最大化窗口
                logger.info(f"{self.current_time} - {self.current_user} - 执行窗口最大化")
                self.click_element(
                    InformationExtractionPage.MAXIMIZE_BUTTON,
                    "最大化按钮"
                )
                time.sleep(1)

                # 缩小窗口
                logger.info(f"{self.current_time} - {self.current_user} - 执行窗口缩小")
                self.click_element(
                    InformationExtractionPage.MINIMIZE_BUTTON,
                    "缩小按钮"
                )
                time.sleep(1)

            # 5. 关闭OCR
            with allure.step("关闭OCR功能"):
                logger.info(f"{self.current_time} - {self.current_user} - 准备关闭OCR功能")
                self.click_element(
                    InformationExtractionPage.CLOSE_BUTTON,
                    "关闭按钮"
                )
                time.sleep(1)

            logger.info(f"{self.current_time} - {self.current_user} - OCR操作流程执行完成")
            return True

        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - OCR操作失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "OCR操作失败截图",
                allure.attachment_type.PNG
            )
            return False

    @allure.step("执行视图操作")
    def handle_view_operations(self):
        """执行视图相关操作"""
        try:
            # 缩放操作
            self.click_element(
                InformationExtractionPage.ZOOM_OUT,
                "缩小按钮"
            )
            self.click_element(
                InformationExtractionPage.ZOOM_IN,
                "放大按钮"
            )

            # 旋转操作
            self.click_element(
                InformationExtractionPage.ROTATE_CLOCKWISE,
                "顺时针旋转"
            )
            self.click_element(
                InformationExtractionPage.ROTATE_COUNTERCLOCKWISE,
                "逆时针旋转"
            )
            time.sleep(1)

            logger.info(f"{self.current_time} - {self.current_user} - 视图操作完成")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 视图操作失败: {str(e)}")
            return False



    # def verify_ocr_content(self, expected_text="123456"):
    #     """
    #     验证OCR文本内容
    #     Args:
    #         expected_text: 期望的文本内容
    #     """
    #     try:
    #         with allure.step(f"验证OCR文本内容是否为: {expected_text}"):
    #             text_element = self.wait.until(
    #                 EC.presence_of_element_located(InformationExtractionPage.OCR_TEXTAREA)
    #             )
    #             actual_text = text_element.get_attribute("value")
    #
    #             assert actual_text == expected_text, f"OCR文本验证失败: 期望'{expected_text}', 实际'{actual_text}'"
    #             logger.info(f"{self.current_time} - {self.current_user} - OCR文本验证通过")
    #             return True
    #     except Exception as e:
    #         logger.error(f"{self.current_time} - {self.current_user} - OCR文本验证失败: {str(e)}")
    #         allure.attach(
    #             self.driver.get_screenshot_as_png(),
    #             "OCR文本验证失败截图",
    #             allure.attachment_type.PNG
    #         )
    #         return False

    @allure.step("执行要素表操作")
    def handle_table_operations(self):
        """执行要素表相关操作"""
        try:
            # 起诉要素表操作
            self.click_element(
                InformationExtractionPage.COMPLAINT_TABLE,
                "起诉要素表"
            )
            self.click_element(
                InformationExtractionPage.REFRESH_BUTTON,
                "刷新按钮"
            )
            self.click_element(
                InformationExtractionPage.EXPORT_BUTTON,
                "导出按钮"
            )

            # 答辩要素表操作
            self.click_element(
                InformationExtractionPage.DEFENSE_TABLE,
                "答辩要素表"
            )

            # 审判要素表操作
            self.click_element(
                InformationExtractionPage.JUDGMENT_TABLE,
                "审判要素表"
            )
            self.click_element(
                InformationExtractionPage.ACTIVE_PANEL_REFRESH,
                "刷新按钮"
            )
            self.click_element(
                InformationExtractionPage.ACTIVE_PANEL_EXPORT,
                "导出按钮"
            )

            logger.info(f"{self.current_time} - {self.current_user} - 要素表操作完成")
            return True
        except Exception as e:
            logger.error(f"{self.current_time} - {self.current_user} - 要素表操作失败: {str(e)}")
            return False