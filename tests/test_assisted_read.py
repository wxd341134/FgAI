import time
import pytest
import allure
from datetime import datetime
from tests.base_test import BaseTest
from pages.assisted_read_page import AssistedReadPage
from common.assisted_read_utils import AssistedReadUtils
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("FGAI自动化测试")
@allure.feature("辅助阅卷")
class TestAssistedReading(BaseTest):
    """辅助阅卷测试类"""

    @classmethod
    def setup_class(cls):
        """类级别的初始化"""
        try:
            # 调用父类的setup_class进行登录
            super().setup_class()

            # 记录测试开始信息
            current_time = "2025-04-14 10:28:11"  # UTC time
            current_user = "wxd341134"

            logger.info("=" * 50)
            logger.info(f"开始执行辅助阅卷测试类")
            logger.info(f"测试开始时间: {current_time}")
            logger.info(f"执行用户: {current_user}")
            logger.info("=" * 50)

            # 创建辅助阅卷页面对象
            cls.assisted_page = AssistedReadPage(cls.driver)
            logger.info("辅助阅卷页面对象初始化完成")

        except Exception as e:
            logger.error(f"辅助阅卷测试类初始化失败: {str(e)}")
            if hasattr(cls, 'driver'):
                allure.attach(
                    cls.driver.get_screenshot_as_png(),
                    name="setup_failed",
                    attachment_type=allure.attachment_type.PNG
                )
            raise

    @classmethod
    def teardown_class(cls):
        """类级别的清理"""
        try:
            time.sleep(3)
            logger.info("=" * 50)
            logger.info("辅助阅卷测试类执行完成")
            logger.info(f"测试结束时间: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")
            logger.info("=" * 50)
            super().teardown_class()
        except Exception as e:
            logger.error(f"测试类清理失败: {str(e)}")

    @allure.story("辅助阅卷流程")
    @allure.title("辅助阅卷完整流程测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    测试步骤：
    1. 点击辅助阅卷
    2. 点击并处理庭审笔录1
    3. 设置和取消设置庭审笔录
    4. 下载PDF文件
    5. 添加庭审笔录2和3为证据
    6. 测试证据引用功能
    7. 测试双屏阅卷功能
    8. 选择上诉人为第三人
    9. 执行批量修改功能
    """)
    def test_assisted_reading(self):
        """测试辅助阅卷流程"""
        try:
            # 1. 点击辅助阅卷
            with allure.step("点击辅助阅卷"):
                logger.info("步骤1: 点击辅助阅卷按钮")
                assert AssistedReadUtils.click_auxiliary_reading(self.assisted_page)
                self.take_screenshot("step1_auxiliary_reading_clicked")

            # 2. 点击庭审笔录1
            with allure.step("点击并处理庭审笔录1"):
                logger.info("步骤2: 点击庭审笔录1")
                assert AssistedReadUtils.click_court_record1(self.assisted_page)
                self.take_screenshot("step2_court_record1_clicked")

            # 3. 设为庭审笔录和输入处理意见
            with allure.step("设置庭审笔录并输入处理意见"):
                logger.info("步骤3: 设置庭审笔录并输入处理意见")
                assert AssistedReadUtils.set_as_court_record(self.assisted_page)
                assert AssistedReadUtils.enter_opinions(self.assisted_page, "无意见1", "无意见2")
                assert AssistedReadUtils.confirm_settings(self.assisted_page)
                self.take_screenshot("step3_set_court_record_complete")

            # 4. 取消设置庭审笔录
            with allure.step("取消设置庭审笔录"):
                logger.info("步骤4: 取消设置庭审笔录")
                assert AssistedReadUtils.cancel_set_record(self.assisted_page)
                self.take_screenshot("step4_cancel_set_record_complete")

            # 5. 下载PDF
            with allure.step("下载笔录PDF"):
                logger.info("步骤5: 下载笔录PDF")
                assert AssistedReadUtils.download_pdf(self.assisted_page)
                self.take_screenshot("step5_pdf_download_complete")

            # 6. 添加庭审笔录2为证据
            with allure.step("添加庭审笔录2为证据"):
                logger.info("步骤6: 添加庭审笔录2为证据")
                assert AssistedReadUtils.add_court_record2_as_evidence(self.assisted_page)
                self.take_screenshot("step6_add_evidence2_complete")

            # 7. 将庭审笔录3添加为证据
            with allure.step("将庭审笔录3添加为证据"):
                logger.info("步骤7: 添加庭审笔录3为证据")
                assert AssistedReadUtils.add_court_record3_as_evidence(self.assisted_page)
                self.take_screenshot("step7_add_evidence3_complete")

            # 8. 证据引用功能
            with allure.step("测试证据引用功能"):
                logger.info("步骤8: 测试证据引用功能")
                assert AssistedReadUtils.check_evidence_reference(self.assisted_page)
                self.take_screenshot("step8_evidence_reference_complete")

            # 9. 双屏阅卷功能
            with allure.step("测试双屏阅卷功能"):
                logger.info("步骤9: 测试双屏阅卷功能")
                assert AssistedReadUtils.perform_dual_screen_reading(self.assisted_page)
                self.take_screenshot("step9_dual_screen_reading_complete")

            # 10. 选择上诉人为第三人
            with allure.step("选择上诉人为第三人"):
                logger.info("步骤10: 选择上诉人为第三人")
                assert AssistedReadUtils.select_third_party(self.assisted_page)
                self.take_screenshot("step10_select_third_party_complete")

            # 11. 刷新并取消选中庭审笔录3
            with allure.step("刷新并取消选中庭审笔录3"):
                logger.info("步骤11: 刷新并取消选中庭审笔录3")
                assert AssistedReadUtils.refresh_and_uncheck_record3(self.assisted_page)
                self.take_screenshot("step11_refresh_uncheck_record3_complete")

            # 12. 批量修改功能
            with allure.step("执行批量修改功能"):
                logger.info("步骤12: 执行批量修改功能")
                assert AssistedReadUtils.perform_batch_edit(self.assisted_page)
                self.take_screenshot("step12_batch_edit_complete")

            logger.info("辅助阅卷测试用例执行完成")

        except Exception as e:
            logger.error(f"辅助阅卷测试失败: {str(e)}")
            self.take_screenshot("test_failed")
            allure.attach(
                str(e),
                name="error_message",
                attachment_type=allure.attachment_type.TEXT
            )
            raise

    def take_screenshot(self, name):
        """截图方法"""
        try:
            screenshot = self.driver.get_screenshot_as_png()
            timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
            allure.attach(
                screenshot,
                name=f"{name}_{timestamp}",
                attachment_type=allure.attachment_type.PNG
            )
            logger.info(f"截图成功: {name}")
        except Exception as e:
            logger.error(f"截图失败 {name}: {str(e)}")


if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=./reports/allure-results", __file__])