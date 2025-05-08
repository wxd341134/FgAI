
from utils.logger import Logger

logger = Logger().get_logger()

import pytest
import os
import shutil

def run_tests():
    try:
        # 清理并创建结果目录
        results_dir = os.path.join(os.path.dirname(__file__), 'allure-results')
        if os.path.exists(results_dir):
            shutil.rmtree(results_dir)
        os.makedirs(results_dir)

        # 运行测试
        pytest.main([
            # f'tests/test_login.py',
            # f'tests/test_usercenter.py',
            # f'tests/test_case.py',
            # f'tests/test_DossierUp.py',
            # f'tests/test_assisted_read.py',
            # f'tests/test_case_search.py',
            # f'tests/test_read_notes.py',
            # f'tests/test_annotations.py',
            # f'tests/test_statute_search.py',
            # f'tests/test_archives_search.py',
            # f'tests/test_search_annotations.py',
              f'tests/test_case_analysis.py',


            '-v',
            '--alluredir', results_dir
        ])

        # 生成报告
        report_dir = os.path.join(os.path.dirname(__file__), 'allure-report')
        os.system(f'allure generate {results_dir} -o {report_dir} --clean')
        #os.system(f'allure open {report_dir}')  #自动打开报告

    except Exception as e:
        logger.error(f"测试执行失败: {e}")
        raise

if __name__ == '__main__':
    # 选择要运行的测试文件
    run_tests()