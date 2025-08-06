import allure
import pytest
from common.statute_search_utils import StatuteSearchUtils
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("辅助阅卷")
@allure.feature("法条检索模块")
@pytest.mark.usefixtures("setup_class")  # ✅ 使用 conftest.py 中定义的类级 fixture,应用到整个类
class TestStatuteSearch():
    """法条检索测试类"""

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """
        测试用例级别的设置和清理
        使用基类的driver fixture
        """
        logger.info("开始测试前置操作...")
        try:
            # 初始化法条检索工具类
            self.statute_search = StatuteSearchUtils(self.driver)
            logger.info("法条检索工具类初始化完成")

            # 执行测试
            yield

            logger.info("测试后置操作完成")

        except Exception as e:
            logger.error(f"测试前置/后置操作失败: {str(e)}")
            self.statute_search.take_screenshot("设置/清理失败截图")  # 调用 CommonUtils 的截图方法
            raise


    @allure.story("法条检索")
    @allure.title("测试法条检索基本流程")
    @allure.severity(allure.severity_level.NORMAL)
    def test_basic_statute_search(self):
        """
        测试法条检索基本流程：
        1. 点击辅助阅卷
        2. 点击法条检索
        3. 输入搜索内容
        4. 点击搜索
        5. 预览法条
        6. 关闭预览
        7. 关闭搜索
        """
        try:
            with allure.step("执行法条检索基本流程"):
                self.statute_search.perform_statute_search("身份证")
                self.statute_search.take_screenshot("基本流程完成")

        except Exception as e:
            logger.error(f"法条检索测试失败: {str(e)}")
            self.statute_search.take_screenshot("基本流程失败")

            raise