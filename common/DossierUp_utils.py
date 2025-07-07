import os
import time
import allure

from utils.common import get_project_root
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

    # @staticmethod
    # @allure.step("上传单个文件")
    # def upload_single_file(dossier_page, docx_file_path):
    #     """上传单个文件流程"""
    #     try:
    #         if docx_file_path and os.path.exists(docx_file_path):
    #             result = dossier_page.upload_single_file(docx_file_path)
    #             if result:
    #                 logger.info("单个文件上传成功")
    #                 allure.attach(
    #                     dossier_page.driver.get_screenshot_as_png(),
    #                     name="single_file_upload_success",
    #                     attachment_type=allure.attachment_type.PNG
    #                 )
    #                 return True
    #         else:
    #             logger.warning("未找到可用的DOCX文件")
    #             allure.attach(
    #                 "未找到可用的DOCX文件",
    #                 name="docx_file_missing",
    #                 attachment_type=allure.attachment_type.TEXT
    #             )
    #         return False
    #     except Exception as e:
    #         logger.error(f"单个文件上传流程失败: {str(e)}")
    #         return False

    @staticmethod
    @allure.step("上传指定文件: 法官AI助手安装文档.docx")
    def upload_single_file(dossier_page, test_data_dir):
        """
        在指定目录中查找并上传 '法官AI助手安装文档.docx' 文件
        :param dossier_page: 页面对象，用于调用上传方法
        :param test_data_dir: 测试数据目录路径
        :return: 成功返回 True，失败返回 False
        """
        # 构造完整文件路径
        target_file = "法官AI助手安装文档.docx"
        # file_path = os.path.join(test_data_dir, target_file)
        # 构建文件路径
        file_path = os.path.join(
            get_project_root(),
            "test_data",
            "法官AI助手安装文档.docx"
        )
        logger.info(f"上传文件路径: {file_path}")

        try:
            # 检查文件是否存在
            if os.path.isfile(file_path):
                logger.info(f"开始上传指定文件: {target_file}")

                # 调用页面上传方法
                result = dossier_page.upload_single_file(file_path)

                if result:
                    logger.info("指定文件上传成功")
                    allure.attach(
                        dossier_page.driver.get_screenshot_as_png(),
                        name="designated_file_upload_success",
                        attachment_type=allure.attachment_type.PNG
                    )
                    return True
                else:
                    logger.error("指定文件上传失败")
                    allure.attach(
                        "指定文件上传失败",
                        name="designated_file_upload_failed",
                        attachment_type=allure.attachment_type.TEXT
                    )
                    return False
            else:
                logger.warning(f"未找到指定文件: {target_file}")
                allure.attach(
                    f"未找到指定文件: {target_file}",
                    name="designated_file_missing",
                    attachment_type=allure.attachment_type.TEXT
                )
                return False

        except Exception as e:
            logger.error(f"上传指定文件时发生异常: {str(e)}", exc_info=True)
            allure.attach(
                str(e),
                name="exception_details",
                attachment_type=allure.attachment_type.TEXT
            )
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