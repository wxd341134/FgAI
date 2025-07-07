import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import Logger
from pages.Mediation_page import MediationPage

logger = Logger().get_logger()


class MediationUtils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator, element_name):
        """点击元素的通用方法"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"点击 {element_name} 成功")
        except Exception as e:
            logger.error(f"点击 {element_name} 失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                f"{element_name}点击失败截图",
                allure.attachment_type.PNG
            )
            raise

    def input_text(self, locator, text, element_name):
        """输入文本的通用方法"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            logger.info(f"在 {element_name} 中输入文本 '{text}' 成功")
        except Exception as e:
            logger.error(f"在 {element_name} 中输入文本失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                f"{element_name}输入失败截图",
                allure.attachment_type.PNG
            )
            raise

    def perform_mediation_operations(self):
        """执行调节相关操作"""
        with allure.step("执行调节操作"):
            try:
                # 1. 点击调节按钮
                with allure.step("打开调节界面"):
                    self.click_element(
                        MediationPage.MEDIATION_BUTTON,
                        "调节按钮"
                    )
                    time.sleep(1)

                # 2. 切换到卷宗预览
                with allure.step("切换到卷宗预览"):
                    self.click_element(
                        MediationPage.PREVIEW_TAB,
                        "卷宗预览标签"
                    )
                    time.sleep(1)

                # 3. 保存操作
                with allure.step("执行保存操作"):
                    self.click_element(
                        MediationPage.SAVE_BUTTON,
                        "保存按钮"
                    )
                    time.sleep(1)

                # 4. 导出操作
                with allure.step("执行导出操作"):
                    self.click_element(
                        MediationPage.EXPORT_BUTTON,
                        "导出按钮"
                    )
                    time.sleep(1)

                # 5. 查找替换操作
                with allure.step("执行查找替换操作"):
                    # 打开查找替换窗口
                    self.click_element(
                        MediationPage.FIND_REPLACE_BUTTON,
                        "查找和替换按钮"
                    )
                    time.sleep(1)

                    # 输入查找内容
                    self.input_text(
                        MediationPage.FIND_INPUT,
                        "校长",
                        "查找输入框"
                    )
                    time.sleep(1)

                    # 输入替换内容
                    self.input_text(
                        MediationPage.REPLACE_INPUT,
                        "校长",
                        "替换输入框"
                    )
                    time.sleep(1)

                    # 执行查找
                    self.click_element(
                        MediationPage.FIND_BUTTON,
                        "查找按钮"
                    )
                    time.sleep(1)

                    # 执行替换
                    self.click_element(
                        MediationPage.REPLACE_BUTTON,
                        "替换按钮"
                    )
                    time.sleep(1)

                    # 继续查找
                    self.click_element(
                        MediationPage.FIND_BUTTON,
                        "继续查找按钮"
                    )
                    time.sleep(1)

                    # 执行全部替换
                    self.click_element(
                        MediationPage.REPLACE_ALL_BUTTON,
                        "全部替换按钮"
                    )
                    time.sleep(1)

                    # 关闭查找替换窗口
                    self.click_element(
                        MediationPage.CLOSE_BUTTON,
                        "关闭按钮"
                    )
                    time.sleep(1)

                logger.info("调节操作完成")
                return True

            except Exception as e:
                logger.error(f"调节操作失败: {str(e)}")
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "调节操作失败截图",
                    allure.attachment_type.PNG
                )
                raise
