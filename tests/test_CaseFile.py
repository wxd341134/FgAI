import os
import pytest
import allure
from common.CaseFile_utils import CaseFileUtils
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("案件管理")
@allure.feature("卷宗管理")
@pytest.mark.usefixtures("setup_class")  # ✅ 使用 conftest.py 中定义的类级 fixture,应用到整个类
class TestCaseFile:
    """卷宗管理测试类"""

    @pytest.fixture(autouse=True)
    def setup_case_file(self):
        """
        测试前后处理
        前置：初始化CaseFileUtils对象
        后置：记录日志
        """
        logger.info("开始测试前置操作...")
        try:
            # 初始化工具类
            self.case_file_utils = CaseFileUtils(self.driver)
            yield
            logger.info("测试后置操作完成")
        except Exception as e:
            logger.error(f"测试前置/后置操作失败: {str(e)}")
            self.case_file_utils.take_screenshot("设置/清理失败截图")
            raise

    @allure.story("卷宗上传")
    @allure.title("卷宗上传基本流程")
    def test_case_file_upload(self):
        """
        测试卷宗上传基本流程
        步骤：
        1. 点击上传卷宗按钮
        2. 上传ZIP文件
        3. 刷新文件列表
        4. 上传单个文件
        5. 收起和展开文件列表
        """
        try:
            # 执行上传流程
            with allure.step("执行卷宗上传流程"):
                self.case_file_utils.execute_upload_workflow()
            logger.info("卷宗上传测试完成")

        except Exception as e:
            logger.error(f"卷宗上传测试失败: {str(e)}")
            self.case_file_utils.take_screenshot("卷宗上传失败截图")
            raise

    @allure.story("目录操作")
    @allure.title("目录操作基本流程")
    def test_directory_operations(self):
        """
        测试目录操作基本流程
        步骤：
        1. 创建一级目录
        2. 创建二级目录
        3. 删除单个目录
        4. 批量删除目录
        """
        try:
            # 执行目录操作流程
            with allure.step("执行目录操作流程"):
                self.case_file_utils.execute_directory_workflow()

            logger.info("目录操作测试完成")
        except Exception as e:
            logger.error(f"目录操作测试失败: {str(e)}")
            self.case_file_utils.take_screenshot("目录操作失败截图")
            raise

