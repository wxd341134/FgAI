import time
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


class TextSelectionUtils:
    """文本选择工具类"""

    @staticmethod
    def get_selection_script():
        """获取选择文本的JavaScript脚本"""
        return """
        function selectText(searchText) {
            try {
                const walker = document.createTreeWalker(
                    document.body,
                    NodeFilter.SHOW_TEXT,
                    null,
                    false
                );

                let node;
                while (node = walker.nextNode()) {
                    const index = node.textContent.indexOf(searchText);
                    if (index >= 0) {
                        // 创建范围
                        const range = document.createRange();
                        range.setStart(node, index);
                        range.setEnd(node, index + searchText.length);

                        // 选择文本
                        const selection = window.getSelection();
                        selection.removeAllRanges();
                        selection.addRange(range);

                        // 获取位置信息
                        const rect = range.getBoundingClientRect();

                        // 返回必要的信息
                        return {
                            x: rect.left + (rect.width / 2),
                            y: rect.top + (rect.height / 2),
                            text: searchText,
                            textContent: node.textContent,
                            startOffset: index,
                            endOffset: index + searchText.length
                        };
                    }
                }
                return null;
            } catch (error) {
                console.error('Error in selectText:', error);
                return null;
            }
        }
        return selectText(arguments[0]);
        """

    @staticmethod
    def get_context_menu_script():
        """获取右键菜单的JavaScript脚本"""
        return """
        function triggerContextMenu() {
            try {
                const selection = window.getSelection();
                if (!selection.rangeCount) return false;

                const range = selection.getRangeAt(0);
                const rect = range.getBoundingClientRect();

                const contextEvent = new MouseEvent('contextmenu', {
                    bubbles: true,
                    cancelable: true,
                    view: window,
                    button: 2,
                    buttons: 2,
                    clientX: rect.left + (rect.width / 2),
                    clientY: rect.top + (rect.height / 2)
                });

                range.startContainer.parentElement.dispatchEvent(contextEvent);
                return true;
            } catch (error) {
                console.error('Error in triggerContextMenu:', error);
                return false;
            }
        }
        return triggerContextMenu();
        """

    @staticmethod
    def switch_to_frame_and_select_text(driver, frame_locator, text_to_select, wait_time=10):
        """
        切换到iframe并选中文本
        Args:
            driver: WebDriver实例
            frame_locator: iframe的定位器
            text_to_select: 要选择的文本
            wait_time: 等待时间
        Returns:
            dict: 包含选中文本的位置和内容信息
        """
        try:
            logger.info(f"开始切换iframe并选择文本: {text_to_select}")

            # 切换到默认内容
            driver.switch_to.default_content()
            time.sleep(0.5)

            # 等待并切换到iframe
            wait = WebDriverWait(driver, wait_time)
            iframe = wait.until(EC.presence_of_element_located(frame_locator))
            driver.switch_to.frame(iframe)
            time.sleep(0.5)

            # 执行文本选择
            selection_info = driver.execute_script(
                TextSelectionUtils.get_selection_script(),
                text_to_select
            )

            if not selection_info:
                raise Exception(f"未找到文本: {text_to_select}")

            time.sleep(1)  # 等待选择效果
            logger.info("文本选择成功")

            return selection_info

        except Exception as e:
            logger.error(f"切换iframe和选择文本失败: {str(e)}")
            raise

    @staticmethod
    def trigger_context_menu_and_keep_selection(driver):
        """
        触发右键菜单并保持选择状态
        Args:
            driver: WebDriver实例
        """
        try:
            logger.info("开始触发右键菜单")

            result = driver.execute_script(TextSelectionUtils.get_context_menu_script())

            if not result:
                raise Exception("右键菜单触发失败")

            time.sleep(1)  # 等待菜单显示
            logger.info("右键菜单触发成功")

        except Exception as e:
            logger.error(f"触发右键菜单失败: {str(e)}")
            raise

    @staticmethod
    def reselect_text_in_frame(driver, text_to_select):
        """
        在当前frame中重新选择文本
        Args:
            driver: WebDriver实例
            text_to_select: 要选择的文本
        """
        try:
            logger.info(f"开始重新选择文本: {text_to_select}")

            selection_info = driver.execute_script(
                TextSelectionUtils.get_selection_script(),
                text_to_select
            )

            if not selection_info:
                raise Exception(f"重新选择文本失败: {text_to_select}")

            time.sleep(0.5)
            logger.info("文本重新选择成功")

            return selection_info

        except Exception as e:
            logger.error(f"重新选择文本失败: {str(e)}")
            raise

