import os
import pytest
import allure
from tests.base_test import BaseTest
from pages.DossierUp_page import DossierUpPage
from common.DossierUp_utils import DossierUpUtils
from utils.common import get_project_root
from utils.logger import Logger

logger = Logger().get_logger()

@allure.epic("法官AI系统测试")
@allure.feature("卷宗管理")
class TestDossierUpload(BaseTest):
    """卷宗上传测试类"""

    def setup_method(self, method):
        """每个测试方法开始前执行"""
        logger.info(f"========== 开始执行测试方法: {method.__name__} ==========")
        # 创建卷宗上传页面对象
        self.dossier_page = DossierUpPage(self.driver)
        # 设置测试数据目录
        self.test_data_dir = os.path.join(get_project_root(), "test_data")

    def teardown_method(self, method):
        """每个测试方法结束后执行"""
        logger.info(f"========== 结束执行测试方法: {method.__name__} ==========")

    @allure.story("卷宗上传")
    @allure.title("卷宗上传流程测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dossier_upload(self):
        """测试卷宗上传流程"""
        try:
            logger.info("开始卷宗上传测试")
            
            # 执行完整的上传流程
            result = DossierUpUtils.execute_upload_workflow(self.dossier_page, self.test_data_dir)
            
            # 断言测试结果
            assert result, "卷宗上传流程失败"
            
            logger.info("卷宗上传测试完成")
            
        except Exception as e:
            logger.error(f"卷宗上传测试失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="test_failed",
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(
                str(e),
                name="error_message",
                attachment_type=allure.attachment_type.TEXT
            )
            raise


if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=./reports/allure-results", __file__])
