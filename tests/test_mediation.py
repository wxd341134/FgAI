import pytest
import allure
from common.Mediation_utils import MediationUtils
from utils.logger import Logger

logger = Logger().get_logger()


@allure.epic("调节模块功能测试")
@pytest.mark.usefixtures("setup_class")  # ✅ 使用 conftest.py 中定义的类级 fixture
class TestMediation:
    """调节模块功能测试用例"""

    @pytest.fixture(autouse=True)
    def setup_mediation(self):
        """
        测试前后处理
        前置：初始化MediationUtils对象
        后置：记录日志
        """
        logger.info("开始测试前置操作...")
        try:
            self.mediation_utils = MediationUtils(self.driver)
            yield
            logger.info("测试后置操作完成")
        except Exception as e:
            logger.error(f"测试前置/后置操作失败: {str(e)}")
            self.mediation_utils.take_screenshot("设置/清理失败截图")  # 调用 CommonUtils 的截图方法
            raise

    @allure.feature("调节功能")
    @allure.story("基本调节操作")
    @allure.title("测试调节基本功能")
    def test_mediation_basic(self):
        """
        测试调节基本功能，包括：
        1. 打开调节界面
        2. 卷宗预览
        3. 保存和导出
        4. 查找替换功能（包括单次替换和全部替换）
        """
        try:
            # 执行调节操作
            with allure.step("执行调节操作"):
                self.mediation_utils.perform_mediation_operations()

        except Exception as e:
            logger.error(f"调节测试失败: {str(e)}")
            self.mediation_utils.take_screenshot("调解功能失败截图")
            raise

