import time
import pytest
import allure
from common.Judgment_utils import JudgmentUtils
from utils.logger import Logger
from tests.base_test import BaseTest

logger = Logger().get_logger()


@allure.epic("判决书功能测试")
class TestJudgment(BaseTest):
    """判决书功能测试用例"""

    @pytest.fixture(autouse=True)
    def setup_judgment(self, driver):
        """
        测试前后处理
        前置：初始化JudgmentUtils对象
        后置：记录日志
        """
        logger.info("开始测试前置操作...")
        try:
            self.judgment_utils = JudgmentUtils(driver)
            # self.judgment_utils.enter_judgment()  # 点击判决书
            yield
            logger.info("测试后置操作完成")
        except Exception as e:
            logger.error(f"测试前置/后置操作失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "设置或清理失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("笔录模块")
    @allure.story("笔录基本功能测试")
    @allure.title("测试笔录查看和基本操作")
    def test_record_basic_operations(self, driver):
        """
        测试笔录模块的基本功能，包括：
        1. 进入判决书
        2. 查看笔录
        3. 页面导航
        4. 视图操作
        """
        try:
            with allure.step("1. 点击进入判决书"):
                logger.info("点击进入判决书")
                self.judgment_utils.enter_judgment()
                time.sleep(2)

            with allure.step("2. 点击笔录标签"):
                logger.info("点击笔录标签")
                self.judgment_utils.open_record_tab()
                time.sleep(1)

            with allure.step("3. 打开笔录侧边栏"):
                logger.info("打开笔录侧边栏")
                self.judgment_utils.toggle_record_sidebar()
                time.sleep(1)

            with allure.step("4. 跳转到第3页"):
                logger.info("跳转到第3页")
                self.judgment_utils.goto_page(3)
                time.sleep(1)

            with allure.step("5. 关闭笔录侧边栏"):
                logger.info("关闭笔录侧边栏")
                self.judgment_utils.toggle_record_sidebar()
                time.sleep(1)

            with allure.step("6. 输入页码并跳转"):
                logger.info("输入页码5并回车")
                self.judgment_utils.goto_page(5)
                time.sleep(1)

        except Exception as e:
            logger.error(f"笔录基本功能测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("笔录模块")
    @allure.story("视图操作测试")
    @allure.title("测试文档视图操作功能")
    # @allure.severity(allure.severity_level.NORMAL)
    def test_view_operations(self, driver):
        """
        测试文档视图相关操作，包括：
        1. 切换视图模式
        2. 缩放操作
        3. 旋转操作
        4. 全屏操作
        """
        try:
            with allure.step("1. 切换视图模式"):
                logger.info("切换到双页视图")
                self.judgment_utils.switch_to_double_page_view()
                time.sleep(1)

            with allure.step("2. 执行缩放操作"):
                logger.info("测试页面缩放功能")
                self.judgment_utils.zoom_operations()
                time.sleep(1)

            with allure.step("3. 执行旋转操作"):
                logger.info("测试页面旋转功能")
                self.judgment_utils.rotate_operations()
                time.sleep(1)

            with allure.step("4. 测试全屏功能"):
                logger.info("进入全屏模式")
                self.judgment_utils.fullscreen_operations()
                time.sleep(1)

        except Exception as e:
            logger.error(f"视图操作测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("笔录模块")
    @allure.story("OCR功能测试")
    @allure.title("测试OCR文本识别及编辑功能")
    # @allure.severity(allure.severity_level.HIGH)
    def test_ocr_operations(self, driver):
        """
        测试OCR相关功能，包括：
        1. OCR文本识别
        2. 文本编辑
        3. 保存操作
        """
        try:
            with allure.step("1. 打开OCR功能"):
                logger.info("打开OCR功能")
                self.judgment_utils.open_ocr()
                time.sleep(1)

            with allure.step("2. 编辑OCR文本"):
                logger.info("在OCR文本框中添加内容")
                self.judgment_utils.edit_ocr_text("123456")
                time.sleep(1)

            with allure.step("3. 保存OCR内容"):
                logger.info("保存OCR内容")
                self.judgment_utils.save_ocr()
                time.sleep(1)

            with allure.step("4. OCR内容缩放测试"):
                logger.info("测试OCR内容缩放功能")
                self.judgment_utils.ocr_zoom_operations()
                time.sleep(1)

            with allure.step("5. 关闭OCR功能"):
                logger.info("关闭OCR功能")
                self.judgment_utils.close_ocr()
                time.sleep(1)

        except Exception as e:
            logger.error(f"OCR功能测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("笔录模块")
    @allure.story("文件操作测试")
    @allure.title("测试文件下载功能")
    # @allure.severity(allure.severity_level.NORMAL)
    def test_file_operations(self, driver):
        """
        测试文件操作相关功能，包括：
        1. PDF下载
        """
        try:
            with allure.step("1. 下载PDF文件"):
                logger.info("测试PDF下载功能")
                self.judgment_utils.download_pdf()
                time.sleep(2)

        except Exception as e:
            logger.error(f"文件操作测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("判决书模块")
    @allure.story("卷宗预览功能测试")
    @allure.title("测试卷宗预览和相关操作")
    def test_document_preview_operations(self, driver):
        """
        测试卷宗预览相关功能，包括：
        1. 文档树操作
        2. 页面导航
        3. 视图切换
        4. OCR操作
        """
        try:

            # with allure.step("1. 点击进入判决书"):
            #     logger.info("点击进入判决书")
            #     self.judgment_utils.enter_judgment()
            #     time.sleep(2)

            with allure.step("1. 预览判决书文档"):
                logger.info("开始预览判决书文档")
                time.sleep(1)
                self.judgment_utils.preview_judgment_document()

            with allure.step("2. 操作卷宗侧边栏和页面导航"):
                logger.info("打开卷宗侧边栏")
                self.judgment_utils.toggle_preview_sidebar()
                time.sleep(1)

                logger.info("关闭卷宗侧边栏")
                self.judgment_utils.toggle_preview_sidebar()
                time.sleep(1)

            # with allure.step("3. 切换视图和缩放操作"):
            #     logger.info("切换到书籍视图")
            #     self.judgment_utils.switch_to_book_view()

            with allure.step("4. OCR相关操作"):
                logger.info("执行OCR操作")
                self.judgment_utils.handle_ocr_operations()

        except Exception as e:
            logger.error(f"卷宗预览功能测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("判决书模块")
    @allure.story("判决书导入导出功能")
    @allure.title("测试判决书的导入导出操作")
    def test_judgment_import_export(self, driver):
        """
        测试判决书导入导出功能，包括：
        1. 选择指定判决书
        2. 导出判决书
        3. 导入新的判决书
        """
        try:


            with allure.step("1. 选择指定判决书"):
                logger.info("开始选择判决书")
                self.judgment_utils.select_judgment_by_date()

            with allure.step("2. 导出判决书"):
                logger.info("开始导出判决书")
                self.judgment_utils.export_judgment()

            with allure.step("3. 导入判决书"):
                logger.info("开始导入判决书")
                self.judgment_utils.import_judgment()

        except Exception as e:
            logger.error(f"判决书导入导出测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("判决书模块")
    @allure.story("判决书对比功能")
    @allure.title("测试判决书版本对比")
    def test_judgment_comparison(self, driver):
        """
        测试判决书对比功能，包括：
        1. 选择新旧版本进行对比
        2. 测试窗口切换功能
        3. 验证对比结果
        """
        try:
            # 执行判决书对比操作

            with allure.step("1. 点击进入判决书"):
                logger.info("点击进入判决书")
                self.judgment_utils.enter_judgment()
                time.sleep(2)

            with allure.step("执行判决书对比操作"):
                logger.info("开始导出判决书")
                self.judgment_utils.compare_judgments()

        except Exception as e:
            logger.error(f"判决书对比测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "测试失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("判决书模块")
    @allure.story("辅助阅卷功能")
    @allure.title("测试辅助阅卷功能")
    def test_assist_reading(self, driver):
        """
        测试辅助阅卷功能，包括：
        1. 打开辅助阅卷
        2. 浏览文档
        3. 搜索操作
        4. 视图调整
        """
        try:

            with allure.step("1. 点击进入判决书"):
                logger.info("点击进入判决书")
                self.judgment_utils.enter_judgment()
                time.sleep(2)

            # 执行辅助阅卷操作
            with allure.step("执行辅助阅卷操作"):
                result = self.judgment_utils.assist_reading_operations()
                assert result, "辅助阅卷操作失败"


        except Exception as e:
            logger.error(f"辅助阅卷测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "测试失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("判决书模块")
    @allure.story("法条检索功能")
    @allure.title("测试法条检索功能")
    def test_law_search(self, driver):
        """
        测试法条检索功能，包括：
        1. 搜索法条
        2. 预览法条
        3. 在预览中搜索
        4. 翻页操作
        """
        try:
            with allure.step("1. 点击进入判决书"):
                logger.info("点击进入判决书")
                self.judgment_utils.enter_judgment()
                time.sleep(2)

            # 执行法条检索操作
            with allure.step("执行法条检索操作"):
                result = self.judgment_utils.law_search_operations()
                assert result, "法条检索操作失败"

        except Exception as e:
            logger.error(f"法条检索测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "测试失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("判决书模块")
    @allure.story("卷宗检索功能")
    @allure.title("测试卷宗检索功能")
    def test_dossier_search(self, driver):
        """
        测试卷宗检索功能，包括：
        1. 搜索卷宗
        2. 文件名显示切换
        3. 预览庭审笔录
        """
        try:

            with allure.step("1. 点击进入判决书"):
                logger.info("点击进入判决书")
                self.judgment_utils.enter_judgment()
                time.sleep(2)

            # 执行卷宗检索操作
            with allure.step("执行卷宗检索操作"):
                result = self.judgment_utils.dossier_search_operations()
                assert result, "卷宗检索操作失败"


        except Exception as e:
            logger.error(f"卷宗检索测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "测试失败截图",
                allure.attachment_type.PNG
            )
            raise

    @allure.feature("判决书模块")
    @allure.story("智能问答功能")
    @allure.title("测试智能问答功能")
    def test_smart_qa(self, driver):
        """
        测试智能问答功能，包括：
        1. 查看争议焦点
        2. 提问并获取回答
        3. 验证问答响应
        """
        try:

            with allure.step("1. 点击进入判决书"):
                logger.info("点击进入判决书")
                self.judgment_utils.enter_judgment()
                time.sleep(2)

            # 执行智能问答操作
            with allure.step("执行智能问答操作"):
                result = self.judgment_utils.smart_qa_operations()
                assert result, "智能问答操作失败"

        except Exception as e:
            logger.error(f"智能问答测试失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "测试失败截图",
                allure.attachment_type.PNG
            )
            raise




