from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.logger import Logger
import time

logger = Logger().get_logger()


class DossierUpPage(BasePage):
    """卷宗上传页面类"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # 上传按钮和文件列表
        self.upload_button = (
        By.XPATH, "//div[@class='ant-table-fixed-right']/div[2]//tbody/tr[1]/td[3]/div/div[1]")  # 这个只能定位到第一个案件
        self.tree_button_group = (By.XPATH, "//div[@class='tree-button-group ant-btn-group']")

        # ZIP文件上传相关元素
        self.upload_zip_button = (By.XPATH, "//div[@class='tree-button-group ant-btn-group']//button[2]")
        self.file_input = (By.CSS_SELECTOR, "input[type='file']")
        self.zip_confirm_button = (By.XPATH, "//div[@class='ant-modal-root']//button[2]")

        # 单个文件上传相关元素
        self.upload_single_button = (By.XPATH,
                                     "//div[@class='custom-modal ant-modal-root custom-modal j-modal-box fullscreen custom-modal j-modal-box fullscreen']//button[3]")
        self.docx_file_input = (By.XPATH, "//input[@type='file' and contains(@accept, '.docx')]")
        self.single_file_confirm_button = (By.XPATH,
                                           "//div[.//div[@class='ant-modal-title' and text()='上传单个文件']]//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']")

        # 文件列表操作按钮
        self.refresh_button = (By.XPATH, "//div[@class='tree-button-group ant-btn-group']//button[1]")
        self.expand_button = (By.XPATH, "//button[@ant-click-animating-without-extra-node='true']")

        # 关闭按钮
        self.close_button = (By.XPATH, "//div[@class='ant-modal-footer']//button[2]")

    def click_upload_button(self):
        """点击上传卷宗按钮"""
        try:
            upload_btn = self.wait.until(EC.element_to_be_clickable(self.upload_button))
            upload_btn.click()
            logger.info("点击上传卷宗按钮成功")
            time.sleep(2)
            return True
        except Exception as e:
            logger.error(f"点击上传卷宗按钮失败: {str(e)}")
            return False

    def upload_zip_file(self, file_path):
        """上传ZIP文件"""
        try:
            # 点击上传zip按钮
            self.wait.until(EC.element_to_be_clickable(self.upload_zip_button)).click()
            logger.info("点击上传ZIP按钮成功")
            time.sleep(1)

            # 上传文件
            file_input = self.wait.until(EC.presence_of_element_located(self.file_input))
            file_input.send_keys(file_path)
            logger.info(f"选择ZIP文件: {file_path}")
            time.sleep(2)

            # 确认上传
            self.wait.until(EC.element_to_be_clickable(self.zip_confirm_button)).click()
            logger.info("确认ZIP文件上传")
            time.sleep(5)
            return True
        except Exception as e:
            logger.error(f"上传ZIP文件失败: {str(e)}")
            return False

    def upload_single_file(self, file_path):
        """上传单个文件"""
        try:
            # 点击上传单个文件按钮
            self.wait.until(EC.element_to_be_clickable(self.upload_single_button)).click()
            logger.info("点击上传单个文件按钮成功")
            time.sleep(1)

            # 上传文件
            file_input = self.wait.until(EC.presence_of_element_located(self.docx_file_input))
            file_input.send_keys(file_path)
            logger.info(f"选择单个文件: {file_path}")
            time.sleep(2)

            # 确认上传
            self.wait.until(EC.element_to_be_clickable(self.single_file_confirm_button)).click()
            logger.info("确认单个文件上传")
            time.sleep(2)
            return True
        except Exception as e:
            logger.error(f"上传单个文件失败: {str(e)}")
            return False

    def refresh_and_expand_file_list(self):
        """刷新并展开文件列表"""
        try:
            # 点击刷新按钮
            self.wait.until(EC.element_to_be_clickable(self.refresh_button)).click()
            logger.info("点击刷新按钮成功")
            time.sleep(1)

            # 尝试点击展开按钮
            try:
                self.wait.until(EC.element_to_be_clickable(self.expand_button)).click()
                logger.info("点击展开按钮成功")
                time.sleep(1)
            except:
                logger.warning("未找到展开按钮或按钮点击失败")

            return True
        except Exception as e:
            logger.error(f"刷新并展开文件列表失败: {str(e)}")
            return False

    def close_upload_window(self):
        """关闭上传窗口"""
        try:
            self.wait.until(EC.element_to_be_clickable(self.close_button)).click()
            logger.info("关闭上传窗口成功")
            time.sleep(2)
            return True
        except Exception as e:
            logger.error(f"关闭上传窗口失败: {str(e)}")
            return False 