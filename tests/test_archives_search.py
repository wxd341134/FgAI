import os

import allure
import pytest
from common.archives_search_utils import ArchivesSearchUtils
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("辅助阅卷")
@allure.feature("卷宗检索模块")
@pytest.mark.usefixtures("setup_class")  # 使用 conftest.py 中的类级 fixture
class TestArchivesSearch:
    """卷宗检索测试类，适配 conftest.py 的 fixture 管理方式"""

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """
        测试用例级别的设置和清理
        使用 conftest.py 提供的 self.driver
        """
        logger.info("开始测试前置操作...")
        try:
            # 初始化工具类
            self.archives_search = ArchivesSearchUtils(self.driver)
            logger.info("卷宗检索工具类初始化完成")

            yield

            logger.info("测试后置操作完成")

        except Exception as e:
            logger.error(f"测试前置/后置操作失败: {str(e)}")
            self.archives_search.take_screenshot("设置/清理失败截图") #调用 CommonUtils 的截图方法

            raise

    @allure.story("卷宗检索功能")
    @allure.title("测试卷宗检索基本流程")
    @allure.severity(allure.severity_level.NORMAL)
    def test_basic_archives_search(self):
        """
        测试卷宗检索基本流程：
        1. 点击卷宗检索
        2. 输入搜索内容
        3. 点击搜索
        4. 预览卷宗
        5. 关闭预览
        6. 勾选仅显示文件名
        7. 关闭搜索
        """
        try:
            with allure.step("执行卷宗检索基本流程"):
                self.archives_search.perform_archives_search("判决")
                self.archives_search.take_screenshot("基本流程完成")  #调用 CommonUtils 的截图方法

        except Exception as e:
            logger.error(f"卷宗检索测试失败: {str(e)}")
            self.archives_search.take_screenshot("基本流程失败")
            raise

# if __name__ == "__main__":
#     print("🚀 开始运行测试...")
#     # 获取当前文件所在目录
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     results_dir = os.path.join(current_dir, "allure-results")
#     print(f"💡 当前文件: {__file__}")
#     print(f"📁 allure-results 将生成在: {results_dir}")
#
#
#     pytest.main([
#         "-v",
#         f"--alluredir={results_dir}",
#         "--clean-alluredir"
#     ])