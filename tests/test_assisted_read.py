import pytest
import allure
import time
from datetime import datetime
from common.assisted_read_utils import AssistedReadUtils
from utils.logger import Logger

logger = Logger().get_logger()

@allure.epic("辅助阅卷")
@allure.feature("辅助阅卷模块")
@pytest.mark.usefixtures("setup_class")  # ✅ 使用 conftest.py 中定义的类级 fixture
class TestAssistedReading:
    """辅助阅卷测试类"""

    CURRENT_TIME = "2025-07-25 08:00:26"
    CURRENT_USER = "wxd341134"

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """
        测试用例级别的设置和清理
        使用基类的driver fixture
        """
        logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 开始测试前置操作...")
        try:
            # 初始化辅助阅卷工具类
            self.assisted_page = AssistedReadUtils(self.driver)
            logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 辅助阅卷工具类初始化完成")

            # 执行测试
            yield

            logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 测试后置操作完成")

        except Exception as e:
            logger.error(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 测试前置/后置操作失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "设置/清理失败截图",
                allure.attachment_type.PNG
            )
            raise

    def take_screenshot(self, name):
        """截图方法"""
        try:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                allure.attachment_type.PNG
            )
        except Exception as e:
            logger.error(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 截图失败: {str(e)}")

    @allure.story("辅助阅卷流程")
    @allure.title("辅助阅卷完整流程测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    测试步骤：
    1. 点击辅助阅卷
    2. 点击并处理庭审笔录1
    3. 设置和取消设置庭审笔录1
    4. 下载PDF文件
    5. 添加庭审笔录2和3为证据
    6. 测试证据引用功能
    7. 测试双屏阅卷功能
    8. 选择上诉人为第三人
    9. 刷新并取消选中庭审笔录3
    10. 执行批量修改功能
    """)
    def test_assisted_reading(self):
        """测试辅助阅卷流程"""
        try:
            # 1. 点击辅助阅卷
            with allure.step("点击辅助阅卷"):
                logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 步骤1: 点击辅助阅卷按钮")
                self.assisted_page.click_auxiliary_reading()
                self.take_screenshot("step1_auxiliary_reading_clicked")

            # 2. 点击庭审笔录1
            with allure.step("点击庭审笔录1"):
                logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 步骤2: 点击庭审笔录1")
                self.assisted_page.click_court_record1()
                self.take_screenshot("step2_court_record1_clicked")

            # 3. 设置庭审笔录并输入处理意见
            with allure.step("设置庭审笔录并输入处理意见"):
                logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 步骤3: 设置庭审笔录并输入处理意见")
                self.assisted_page.set_as_court_record()
                self.assisted_page.enter_opinions("无审查意见", "无裁判思路")
                self.assisted_page.confirm_settings()
                self.take_screenshot("step3_set_court_record_complete")

            # 4. 取消设置庭审笔录
            with allure.step("取消设置庭审笔录"):
                logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 步骤4: 取消设置庭审笔录")
                self.assisted_page.cancel_set_record()
                self.take_screenshot("step4_cancel_set_record_complete")

            # 5. 下载PDF
            with allure.step("下载笔录PDF"):
                logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 步骤5: 下载笔录PDF")
                self.assisted_page.download_pdf()
                self.take_screenshot("step5_pdf_download_complete")

            # 6. 添加庭审笔录2为证据
            with allure.step("添加庭审笔录2为证据"):
                logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 步骤6: 添加庭审笔录2为证据")
                self.assisted_page.add_court_record2_as_evidence()
                self.take_screenshot("step6_add_evidence2_complete")

            # 7. 将庭审笔录3添加为证据
            with allure.step("将庭审笔录3添加为证据"):
                logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 步骤7: 添加庭审笔录3为证据")
                self.assisted_page.add_court_record3_as_evidence()
                self.take_screenshot("step7_add_evidence3_complete")

            # 8. 证据引用功能
            with allure.step("测试证据引用功能"):
                logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 步骤8: 测试证据引用功能")
                self.assisted_page.check_evidence_reference()
                self.take_screenshot("step8_evidence_reference_complete")

            # 9. 双屏阅卷功能
            with allure.step("测试双屏阅卷功能"):
                logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 步骤9: 测试双屏阅卷功能")
                self.assisted_page.perform_dual_screen_reading()
                self.take_screenshot("step9_dual_screen_reading_complete")

            # 10. 选择上诉人为第三人
            with allure.step("选择上诉人为第三人"):
                logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 步骤10: 选择上诉人为第三人")
                self.assisted_page.select_third_party()
                self.take_screenshot("step10_select_third_party_complete")

            # 11. 刷新并取消选中庭审笔录3
            with allure.step("刷新并取消选中庭审笔录3"):
                logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 步骤11: 刷新并取消选中庭审笔录3")
                self.assisted_page.refresh_and_uncheck_record3()
                self.take_screenshot("step11_refresh_uncheck_record3_complete")

            # 12. 批量修改功能
            with allure.step("执行批量修改功能"):
                logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 步骤12: 执行批量修改功能")
                self.assisted_page.perform_batch_edit()
                self.take_screenshot("step12_batch_edit_complete")

            logger.info(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 辅助阅卷测试执行完成")

        except Exception as e:
            logger.error(f"{self.CURRENT_TIME} - {self.CURRENT_USER} - 测试执行失败: {str(e)}")
            self.take_screenshot("test_failed")
            raise

if __name__ == "__main__":
    pytest.main([
        "-v",
        "--alluredir=./reports/allure-results",
        __file__
    ])