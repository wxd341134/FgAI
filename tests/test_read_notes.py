import time

import allure
import pytest
from common.read_notes_utils import ReadNotesUtils
from tests.base_test import BaseTest
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("阅卷笔记")
@allure.feature("阅卷笔记模块")
class TestReadNotes(BaseTest):

    @classmethod
    def setup_class(cls):
        """
        类级别的初始化：
        1. 调用父类的setup_class完成登录
        2. 初始化阅卷笔记工具类
        3. 打开阅卷笔记页面
        """
        super().setup_class()  # 调用父类的setup_class完成登录
        logger.info("初始化阅卷笔记模块...")
        try:
            cls.read_notes = ReadNotesUtils(cls.driver)
            # 登录后打开阅卷笔记页面
            cls.read_notes.open_reading_notes()
            logger.info("阅卷笔记页面已打开")
        except Exception as e:
            logger.error(f"阅卷笔记初始化失败: {str(e)}")
            allure.attach(
                cls.driver.get_screenshot_as_png(),
                "初始化失败截图",
                allure.attachment_type.PNG
            )
            raise

    def take_screenshot(self, name):
        """添加截图方法，用于在关键步骤或失败时截图"""
        try:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name,
                allure.attachment_type.PNG
            )
        except Exception as e:
            logger.error(f"截图失败: {str(e)}")

    @allure.story("判决书文档操作")
    @allure.title("测试判决书查看和下载功能")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_judgment_doc_operations(self):
        """
        测试判决书相关操作：
        1. 点击判决书
        2. 测试缩放功能
        3. 测试下载功能
        4. 关闭预览
        """
        logger.info("开始测试判决书操作...")
        try:
            with allure.step("执行判决书相关操作"):
                self.read_notes.operate_judgment_doc()
                self.take_screenshot("判决书操作完成")

            logger.info("判决书操作测试完成")
        except Exception as e:
            logger.error(f"判决书操作测试失败: {str(e)}")
            self.take_screenshot("判决书操作失败")
            raise

    @allure.story("证据引用功能")
    @allure.title("测试证据引用查看和操作功能")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_evidence_reference_operations(self):
        """
        测试证据引用相关操作：
        1. 点击证据引用
        2. 选择庭审笔录3
        3. 测试旋转功能
        4. 测试视图切换
        5. 测试全屏功能
        """
        logger.info("开始测试证据引用操作...")
        try:
            with allure.step("执行证据引用操作"):
                self.read_notes.operate_evidence_reference()
                self.take_screenshot("证据引用操作完成")

            logger.info("证据引用测试完成")
        except Exception as e:
            logger.error(f"证据引用测试失败: {str(e)}")
            self.take_screenshot("证据引用失败")
            raise

    @allure.story("查找替换功能")
    @allure.title("测试笔记内容的查找和替换")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_search_and_replace(self):
        """
        测试查找替换功能：
        1. 打开查找替换框
        2. 输入查找和替换内容
        3. 执行替换操作
        4. 保存更改
        """
        logger.info("开始测试查找替换功能...")
        try:
            with allure.step("执行查找替换操作"):
                self.read_notes.search_and_replace("号码", "号码")
                self.take_screenshot("查找替换操作")

            with allure.step("保存更改"):
                self.read_notes.save_notes()
                self.take_screenshot("保存完成")

            logger.info("查找替换测试完成")
        except Exception as e:
            logger.error(f"查找替换测试失败: {str(e)}")
            self.take_screenshot("查找替换失败")
            raise

    @allure.story("笔记导出功能")
    @allure.title("测试阅卷笔记导出功能")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_export_notes(self):
        """
        测试笔记导出功能：
        1. 点击导出按钮
        2. 验证导出成功
        """
        logger.info("开始测试笔记导出功能...")
        try:
            with allure.step("导出笔记"):
                self.read_notes.export_notes()
                self.take_screenshot("导出完成")

            logger.info("笔记导出测试完成")
        except Exception as e:
            logger.error(f"笔记导出测试失败: {str(e)}")
            self.take_screenshot("导出失败")
            raise

    @allure.story("文本格式化功能")
    @allure.title("测试文本选择和格式化")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_format_selected_text(self):
        """
        测试文本格式化功能：
        1. 使用JavaScript选中文本
        2. 设置背景色
        3. 更改字体为楷体
        4. 更改字号为二号
        5. 设置行高为1.75
        6. 设置加粗和斜体
        7. 保存更改
        8. 清除格式
        9，再次保存
        """
        logger.info("开始测试文本格式化功能...")
        try:
            with allure.step("选中文本并执行格式化"):
                self.read_notes.format_selected_text()
        except Exception as e:
            logger.error(f"测试失败: {str(e)}")
            raise

    @allure.story("AI智能问答和构成要件")
    @allure.title("测试选中文本并点击AI智能问答和构成要件")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_select_text_and_ai_qa(self):
        """
        测试文本选择和AI智能问答功能：
        1. 通过模拟鼠标滑动选中指定文本
        2. 点击AI智能问答按钮
        3. 等待5秒
        4. 关闭AI问答弹框
        """
        logger.info("开始测试AI智能问答和构成要件...")
        try:
            with allure.step("选中文本并点击AI智能问答和构成要件"):
                # 选中文本并使用AI智能问答
                self.read_notes.select_text_and_use_ai_qa("万家新城内")
                self.take_screenshot("AI智能问答和构成要件")

            with allure.step("验证弹框已关闭"):
                # 验证弹框已关闭，可以添加相应的验证逻辑
                time.sleep(1)
                self.take_screenshot("AI智能问答完成")

            logger.info("文本选择和AI智能问答测试完成")
        except Exception as e:
            logger.error(f"文本选择和AI智能问答测试失败: {str(e)}")
            self.take_screenshot("AI智能问答失败")
            raise

