import time
import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.case_analysis_page import CaseAnalysisPage
from utils.logger import Logger

logger = Logger().get_logger()


class CaseAnalysisUtils:
    """案件分析工具类"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator, element_name):
        """点击元素的通用方法"""
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

    def input_text(self, locator, text, element_name):
        """输入文本的通用方法"""
        try:
            logger.info(f"尝试在{element_name}中输入文本: {text}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
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

    @allure.step("进入案件分析")
    def enter_case_analysis(self):
        """进入案件分析页面"""
        try:
            self.click_element(CaseAnalysisPage.ENTER_ANALYSIS, "进入案件分析")
            time.sleep(2)
        except Exception as e:
            logger.error(f"进入案件分析失败: {str(e)}")
            raise

    def check_and_get_evidence_status(self):
        """
        检查转账凭证截图的认同状态并返回对应的元素定位器
        Returns:
            tuple: (是否认同状态, 状态元素定位器)
        """
        try:
            # 检查是否存在认同状态的图标
            agree_element = self.driver.find_elements(*CaseAnalysisPage.EVIDENCE_AGREE_STATUS)
            if agree_element:
                logger.info("当前是认同状态")
                return True, CaseAnalysisPage.EVIDENCE_AGREE_STATUS
            else:
                # 检查是否存在不认同状态的图标
                disagree_element = self.driver.find_elements(*CaseAnalysisPage.EVIDENCE_DISAGREE_STATUS)
                if disagree_element:
                    logger.info("当前是不认同状态")
                    return False, CaseAnalysisPage.EVIDENCE_DISAGREE_STATUS
                else:
                    raise Exception("未找到证据状态元素")
        except Exception as e:
            logger.error(f"检查证据状态失败: {str(e)}")
            raise

    @allure.step("切换证据认同状态")
    def toggle_evidence_status(self):
        """根据当前状态切换证据的认同/不认同状态"""
        try:
            logger.info("开始执行证据状态切换流程...")

            # 1. 打开导航
            with allure.step("打开导航"):
                self.click_element(CaseAnalysisPage.NAVIGATION_TOGGLE, "打开导航")
                time.sleep(1)

            # 2. 点击证据列表
            with allure.step("点击证据列表"):
                self.click_element(CaseAnalysisPage.EVIDENCE_LIST, "证据列表")
                time.sleep(1)

            # 3. 检查当前状态并点击对应的状态图标
            with allure.step("检查并点击状态图标"):
                is_agreed, status_locator = self.check_and_get_evidence_status()
                self.click_element(status_locator, "证据状态图标")
                time.sleep(1)

            # 4. 根据当前状态选择相反的选项
            if is_agreed:
                # 如果当前是认同状态，选择不认同
                with allure.step("切换为不认同状态"):
                    # self.select_radio_option(CaseAnalysisPage.DISAGREE_RADIO, "不认同选项")
                    self.click_element(CaseAnalysisPage.DISAGREE_RADIO, "不认同选项")
                    time.sleep(1)

                    # 输入不认同意见
                    self.input_text(
                        CaseAnalysisPage.OPINION_INPUT,
                        "有意见，不认同转账凭据截图",
                        "意见输入框"
                    )
                    time.sleep(1)
            else:
                # 如果当前是不认同状态，选择认同
                with allure.step("切换为认同状态"):
                    # self.select_radio_option(CaseAnalysisPage.AGREE_RADIO, "认同选项")
                    self.click_element(CaseAnalysisPage.AGREE_RADIO, "认同选项")
                    time.sleep(1)

                    # 输入认同意见
                    self.input_text(
                        CaseAnalysisPage.OPINION_INPUT,
                        "无意见，认同转账凭据截图",
                        "意见输入框"
                    )
                    time.sleep(1)

            # 5. 点击确定按钮
            with allure.step("保存更改"):
                self.click_element(CaseAnalysisPage.CONFIRM_BUTTON, "确定按钮")
                time.sleep(1)

            # 6. 关闭导航
            with allure.step("关闭导航"):
                self.click_element(CaseAnalysisPage.NAVIGATION_TOGGLE, "关闭导航")
                time.sleep(2)

            logger.info("证据状态切换完成")

        except Exception as e:
            logger.error(f"证据状态切换失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "状态切换失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.step("展开收起操作")
    def expand_collapse_operation(self):
        """展开收起功能测试"""
        try:
            # 1. 打开导航
            self.click_element(CaseAnalysisPage.NAVIGATION_TOGGLE, "打开导航")
            time.sleep(1)

            # 2. 点击判决理由预览
            self.click_element(CaseAnalysisPage.COURT_OPINION_PREVIEW, "判决理由预览")
            time.sleep(1)

            # 3. 点击展开更多
            self.click_element(CaseAnalysisPage.EXPAND_MORE, "展开更多")
            time.sleep(1)

            # 4. 点击收起更多
            self.click_element(CaseAnalysisPage.COLLAPSE_MORE, "收起更多")
            time.sleep(1)

            # 5. 关闭导航
            self.click_element(CaseAnalysisPage.NAVIGATION_TOGGLE, "关闭导航")
            time.sleep(2)

        except Exception as e:
            logger.error(f"展开收起操作失败: {str(e)}")
            raise

    @allure.step("完善事实描述")
    def complete_fact_description(self, description="这是完善的内容"):
        """完善事实描述"""
        try:
            # 1. 打开导航
            self.click_element(CaseAnalysisPage.NAVIGATION_TOGGLE, "打开导航")
            time.sleep(1)

            # 2. 点击事实描述
            self.click_element(CaseAnalysisPage.FACT_DESCRIPTION, "事实描述")
            time.sleep(1)

            # 3. 点击编辑
            self.click_element(CaseAnalysisPage.EDIT_TRANSFER_RECEIPT, "编辑按钮")
            time.sleep(1)

            # 4. 输入描述内容
            self.input_text(
                CaseAnalysisPage.DESCRIPTION_INPUT,
                description,
                "描述输入框"
            )
            time.sleep(2)

            # 5. 保存
            self.click_element(CaseAnalysisPage.SAVE_BUTTON, "保存按钮")
            time.sleep(2)

            # 6. 关闭导航
            self.click_element(CaseAnalysisPage.NAVIGATION_TOGGLE, "关闭导航")
            time.sleep(2)

        except Exception as e:
            logger.error(f"完善事实描述失败: {str(e)}")
            raise

    @allure.step("操作庭审笔录")
    def handle_court_record(self):
        """处理庭审笔录相关操作"""
        try:
            logger.info("开始庭审笔录操作...")

            # 1. 打开庭审笔录
            with allure.step("点击庭审笔录"):
                self.click_element(CaseAnalysisPage.COURT_RECORD, "庭审笔录")
                time.sleep(1)

            # 2. 显示侧边栏
            with allure.step("点击笔录侧边栏"):
                self.click_element(CaseAnalysisPage.SIDEBAR_TOGGLE, "侧边栏")
                time.sleep(1.5)

            # 3. 跳转到第三页
            with allure.step("点击第3页"):
                self.click_element(CaseAnalysisPage.PAGE_THREE, "第3页")
                time.sleep(1)

            # 4. 输入页码并跳转
            with allure.step("输入页码"):
                page_input = self.wait.until(
                    EC.presence_of_element_located(CaseAnalysisPage.PAGE_INPUT)
                )
                page_input.clear()
                page_input.send_keys("5")
                page_input.send_keys(Keys.ENTER)
                time.sleep(1)

            # 5. 切换视图
            with allure.step("切换到双页视图"):
                self.click_element(CaseAnalysisPage.VIEW_BUTTON, "视图按钮")
                time.sleep(1)
                self.click_element(CaseAnalysisPage.DOUBLE_PAGE_VIEW, "双页视图")
                time.sleep(1)

            # 6-7. 适配页面
            with allure.step("调整页面适配"):
                self.click_element(CaseAnalysisPage.FIT_WIDTH, "适合页宽")
                time.sleep(1)
                self.click_element(CaseAnalysisPage.FIT_HEIGHT, "适合页高")
                time.sleep(1)

            # 8-9. 缩放操作
            with allure.step("执行缩放操作"):
                self.click_element(CaseAnalysisPage.ZOOM_OUT, "缩小")
                time.sleep(1)
                self.click_element(CaseAnalysisPage.ZOOM_IN, "放大")
                time.sleep(1)

            # 10-11. 旋转操作
            with allure.step("执行旋转操作"):
                self.click_element(CaseAnalysisPage.ROTATE_CLOCKWISE, "顺时针旋转")
                time.sleep(1)
                self.click_element(CaseAnalysisPage.ROTATE_COUNTERCLOCKWISE, "逆时针旋转")
                time.sleep(1)


            # 13-14. 全屏操作
            with allure.step("执行全屏操作"):
                self.click_element(CaseAnalysisPage.FULLSCREEN_BUTTON, "全屏")
                time.sleep(1)
                self.click_element(CaseAnalysisPage.EXIT_FULLSCREEN, "退出全屏")
                time.sleep(1)

            # 12. 下载操作
            with allure.step("执行下载操作"):
                self.click_element(CaseAnalysisPage.DOWNLOAD_BUTTON, "下载按钮")
                time.sleep(1)
                self.click_element(CaseAnalysisPage.PDF_DOWNLOAD, "PDF下载")
                time.sleep(1)

            # 15. 关闭侧边栏
            with allure.step("关闭侧边栏"):
                self.click_element(CaseAnalysisPage.SIDEBAR_TOGGLE, "关闭侧边栏")
                time.sleep(1)

            logger.info("庭审笔录操作完成")

        except Exception as e:
            logger.error(f"庭审笔录操作失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "庭审笔录操作失败截图",
                allure.attachment_type.PNG
            )
            raise