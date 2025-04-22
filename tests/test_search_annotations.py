import time

import allure
import pytest
from common.search_annotations_utils import SearchAnnotationsUtils
from tests.base_test import BaseTest
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("法官AI助手")
@allure.feature("检索批注功能")
class TestSearchAnnotations(BaseTest):
    """检索批注测试类"""

    @pytest.fixture(autouse=True)
    def setup_teardown(self, driver):
        """
        测试用例级别的设置和清理
        Args:
            driver: 从基类获取的 WebDriver 实例
        """
        logger.info("开始测试前置操作...")
        try:
            # 初始化检索批注工具类
            self.annotations = SearchAnnotationsUtils(driver)
            logger.info("检索批注工具类初始化完成")

            # 执行测试用例
            yield

            logger.info("开始测试后置操作...")

        except Exception as e:
            logger.error(f"测试前置/后置操作失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "设置或清理失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.story("基础批注功能")
    @allure.title("测试添加批注")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_annotation(self):
        """测试添加批注的基本功能"""
        try:
            with allure.step("执行基本批注流程"):
                self.annotations.add_annotation()

                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    "批注添加完成",
                    allure.attachment_type.PNG
                )

        except Exception as e:
            logger.error(f"添加批注测试失败: {str(e)}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.story("编辑批注功能")
    @allure.title("测试编辑现有批注")
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_annotation(self, driver):
        """测试编辑批注功能"""
        try:
            with allure.step("执行批注编辑流程"):
                # 先添加批注，然后编辑
                self.annotations.edit_annotation(
                    new_text="123456修改"
                )

        except Exception as e:
            logger.error(f"编辑批注测试失败: {str(e)}")
            raise

    @allure.story("批注删除功能")
    @allure.title("测试删除批注")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_annotation(self, driver):
        """测试删除批注的基本功能"""
        try:
            with allure.step("执行批注删除流程"):
                self.annotations.delete_annotation()

        except Exception as e:
            logger.error(f"批注删除测试失败: {str(e)}")
            raise

    @allure.story("法条管理完整流程")
    @allure.title("测试法条完整生命周期")
    def test_law_lifecycle(self, driver):
        """
        测试法条的完整生命周期：
        1. 引用法条
        2. 预览法条
        3. 编辑法条
        4. 删除法条
        """
        try:
            # 1. 引用法条
            with allure.step("步骤1：引用法条"):
                self.annotations.cite_law(
                    text_to_select="服务器",
                    search_keyword="诉讼法"
                )

                time.sleep(1)

            # 2. 预览法条
            with allure.step("步骤2：预览法条"):
                self.annotations.preview_law()

                time.sleep(1)

            # 3. 编辑法条
            with allure.step("步骤3：编辑法条"):
                self.annotations.edit_law(
                    new_text="中华人民共和国民事诉讼法修改"
                )

                time.sleep(1)

            # 4. 删除法条
            with allure.step("步骤4：删除法条"):
                self.annotations.delete_law()


            logger.info("法条完整生命周期测试完成")

        except Exception as e:
            logger.error(f"法条生命周期测试失败: {str(e)}")
            raise

    @allure.story("页面跳转功能")
    @allure.title("测试页面跳转")
    def test_page_navigation(self, driver):
        """测试页面跳转功能"""
        try:
            with allure.step("执行页面跳转操作"):
                self.annotations.page_navigation()


        except Exception as e:
            logger.error(f"页面跳转测试失败: {str(e)}")

            raise


if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=./allure-results"])