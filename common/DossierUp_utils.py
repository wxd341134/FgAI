import os
import time
import allure
from utils.logger import Logger

logger = Logger().get_logger()

class DossierUpUtils:
    """卷宗上传工具类"""

    @staticmethod
    def check_test_files(test_data_dir):
        """检查测试文件"""
        try:
            # 确保test_data目录存在
            if not os.path.exists(test_data_dir):
                logger.warning(f"test_data目录不存在，创建目录: {test_data_dir}")
                os.makedirs(test_data_dir)

            # 查找ZIP文件
            zip_file_path = None
            for file in os.listdir(test_data_dir):
                if file.endswith('.zip'):
                    zip_file_path = os.path.join(test_data_dir, file)
                    logger.info(f"找到ZIP文件: {file}")
                    break

            # 查找DOCX文件
            docx_file_path = None
            for file in os.listdir(test_data_dir):
                if file.endswith('.docx'):
                    docx_file_path = os.path.join(test_data_dir, file)
                    logger.info(f"找到DOCX文件: {file}")
                    break

            return zip_file_path, docx_file_path
        except Exception as e:
            logger.error(f"检查测试文件失败: {str(e)}")
            return None, None

    @staticmethod
    @allure.step("上传ZIP文件")
    def upload_zip_file(dossier_page, zip_file_path):
        """上传ZIP文件流程"""
        try:
            if zip_file_path and os.path.exists(zip_file_path):
                result = dossier_page.upload_zip_file(zip_file_path)
                if result:
                    logger.info("ZIP文件上传成功")
                    allure.attach(
                        dossier_page.driver.get_screenshot_as_png(),
                        name="zip_upload_success",
                        attachment_type=allure.attachment_type.PNG
                    )
                    return True
            else:
                logger.warning("未找到可用的ZIP文件")
                allure.attach(
                    "未找到可用的ZIP文件",
                    name="zip_file_missing",
                    attachment_type=allure.attachment_type.TEXT
                )
            return False
        except Exception as e:
            logger.error(f"ZIP文件上传流程失败: {str(e)}")
            return False

    @staticmethod
    @allure.step("上传单个文件")
    def upload_single_file(dossier_page, docx_file_path):
        """上传单个文件流程"""
        try:
            if docx_file_path and os.path.exists(docx_file_path):
                result = dossier_page.upload_single_file(docx_file_path)
                if result:
                    logger.info("单个文件上传成功")
                    allure.attach(
                        dossier_page.driver.get_screenshot_as_png(),
                        name="single_file_upload_success",
                        attachment_type=allure.attachment_type.PNG
                    )
                    return True
            else:
                logger.warning("未找到可用的DOCX文件")
                allure.attach(
                    "未找到可用的DOCX文件",
                    name="docx_file_missing",
                    attachment_type=allure.attachment_type.TEXT
                )
            return False
        except Exception as e:
            logger.error(f"单个文件上传流程失败: {str(e)}")
            return False

    @staticmethod
    @allure.step("执行完整的卷宗上传流程")
    def execute_upload_workflow(dossier_page, test_data_dir):
        """执行完整的卷宗上传流程"""
        try:
            # 检查测试文件
            zip_file_path, docx_file_path = DossierUpUtils.check_test_files(test_data_dir)

            # 点击上传卷宗按钮
            with allure.step("点击上传卷宗按钮"):
                if not dossier_page.click_upload_button():
                    raise Exception("点击上传卷宗按钮失败")

            # 上传ZIP文件
            with allure.step("上传ZIP文件"):
                DossierUpUtils.upload_zip_file(dossier_page, zip_file_path)

            # 上传单个文件
            with allure.step("上传单个文件"):
                DossierUpUtils.upload_single_file(dossier_page, docx_file_path)

            # 刷新并展开文件列表
            with allure.step("刷新并展开文件列表"):
                dossier_page.refresh_and_expand_file_list()

            # 关闭上传窗口
            with allure.step("关闭上传窗口"):
                dossier_page.close_upload_window()

            logger.info("卷宗上传流程执行完成")
            return True
        except Exception as e:
            logger.error(f"卷宗上传流程执行失败: {str(e)}")
            return False 